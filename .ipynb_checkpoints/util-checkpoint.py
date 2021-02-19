import matplotlib.pyplot as plt
import numpy as np
import h5py
import cv2
import os

def time_convert(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    if h>0:
        return "%dh %dm %ds" % (h, m, s)
    elif m>0:
        return "%dm %ds" % (m, s)
    else:
        return "%ds" % (s) 

def generate_h5_data(data,labels,filename):
    assert(type(filename) is str)
    assert(len(data) == len(labels)) 
    try:
        filepath= f'./{filename}.h5'
        h5data = h5py.File(filepath, 'w')
        h5data.create_dataset('image',data= data)
        h5data['label'] = labels

    finally:
        h5data.close()

#NO NEED FOR THIS EXERCISE
def load_h5_data(h5filepath):
    h5file = h5py.File(h5filepath, "r")
    try:
        x_fieldname,y_fieldname, = h5file.keys()   #this order is Gfriend files
        print("The keys are: ", h5file.keys())
        data = np.array(h5file['image'][:]) # your test set features
        labels = np.array(h5file['label'][:]) # your test set labels
        print("The shape of x_field",data.shape)
        print("The shape of y_field",labels.shape)
    finally:
        h5file.close()
    return data, labels



def show_20_images(df, img_array, label_array, offset=0):
    assert(len(img_array)==len(label_array))
    
    datalen = len(img_array)
    numOfIter = min(datalen,20)
    
    if numOfIter < 20:
        offset = 0  #if numOfIter < 20, it means it equals datalen, which is less than 20 fed in. So no need offset
        
    numOfRow = numOfIter//4 + (numOfIter%4 != 0)   #a ceiling function
    
    plt.rcParams['figure.figsize'] = (60.0, 100.0) 
    print(img_array.shape)
    num_px = img_array.shape[1] #shape is (m, num_px,num_px,3)
    for i in range(numOfIter):
        plt.subplot(5,4,i+1)  #plot 5 by 4 grid
        #plt.imshow(img_array[i+offset])
        img_preview = img_array[i+offset].reshape(num_px,num_px,3)
        img_preview = np.float32(img_preview)
        img_preview = cv2.cvtColor(img_preview, cv2.COLOR_BGR2RGB)
        plt.imshow(img_preview, interpolation='nearest')  #take only the num_px
        plt.axis('off')
        #print(f'IMG {i+1} is labelled {label_array[i+offset]}')
        _class = df['breed'][int(label_array[i+offset])]
        plt.title("Class: " + _class,fontsize = 50)
        

def plot_model_history( history, folder="plots/", saving_name="model_loss_accuracy"):
    plt.style.use("ggplot")
    plt.figure(figsize=(16, 6))

    # plot for loss
    ax = plt.subplot(1, 2, 1)
    # ensure ploting never plot beyond 10
    #y_max = (max(history.history["loss"]), max(history.history["val_loss"]))
    #y_max = min(10.0, max(y_max))
    #ax.set_ylim(ymax=y_max)
    plt.plot( history.history["loss"], label="train_loss")
    plt.plot( history.history["val_loss"], label="val_loss")
    plt.title("Model Loss")
    plt.xlabel("Epoch #")
    plt.ylabel("Loss")
    plt.legend(loc="upper right")

    # plot for accuracy
    ax = plt.subplot(1, 2, 2)
    ax.set_ylim([0,1]) # fix y-range for eazy comparison 
    plt.plot(history.history["accuracy"], label="train_acc")
    plt.plot(history.history["val_accuracy"], label="val_acc")

    plt.title("Model Accuracy")
    plt.xlabel("Epoch #")
    plt.ylabel("Accuracy")
    plt.legend(loc="upper left")

    # save plot to disk
    os.makedirs(os.path.dirname(folder), exist_ok=True)
    plt.savefig(folder+saving_name)
    plt.show()

def plot_learning_rate( history, folder="plots/", saving_name="model_learn_rate"):
    # history only contain lr when lrScheduler used 
    #assert('lr' in history.history.keys()), "model history does not contain lr, ensure lr related callback is used"
    
    # the learning rate schedule
    plt.style.use("ggplot")
    plt.figure(figsize=(8, 6))
    plt.plot( history.history["lr"], label="learn rate")
    plt.title("Learning Rate")
    plt.xlabel("Epoch #")
    plt.ylabel("Learning Rate")
    # save plot to disk
    os.makedirs(os.path.dirname(folder), exist_ok=True)
    plt.savefig(folder+saving_name)
    plt.show()

