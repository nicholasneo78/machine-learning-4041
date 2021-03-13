import matplotlib.pyplot as plt
import numpy as np
import h5py
import cv2
import os
import math

def time_convert(seconds):
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    if h>0:
        return "%dh %dm %ds" % (h, m, s)
    elif m>0:
        return "%dm %ds" % (m, s)
    else:
        return "%ds" % (s) 
    
def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    i = int(math.floor(math.log(size_bytes, 1024)))
    p = math.pow(1024, i)
    s = round(size_bytes / p, 2)
    return "%s %s" % (s, size_name[i])

def nparray_info(header, nparr):
    print(header)
    print("-  shape\t", nparr.shape)
    print("-  dtype\t", nparr.dtype)
    print("- nbytes\t", f"{nparr.nbytes} ({convert_size(nparr.nbytes)})")
    

def generate_h5_data(data, labels, saving_path="./Datasets/data.h5"):
    assert(type(saving_path) is str)
    assert(len(data) == len(labels))
    
    os.makedirs(os.path.dirname(saving_path), exist_ok=True)
    try:
        with h5py.File(saving_path, 'w') as h5:
            #h5.create_dataset('image', data= data, compression="gzip", compression_opts=9)
            h5.create_dataset('image', data= data)
            h5.create_dataset('label', data= labels)
    except Exception as e:
        print(e)
    

def load_h5_data(saving_path="./Datasets/data.h5"):
    try:
        with h5py.File(saving_path, "r") as h5:
            #print("h5.keys", h5.keys())
            data = np.array(h5['image'][:])
            labels = np.array(h5['label'][:])
    except Exception as e:
        print(e)
    return data, labels
        

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
    ax.set_ylim([0,1.2]) # fix y-range for eazy comparison 
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

