README PREPARED BY NICHOLAS NEO 2021-04-18

The codes are executed in both platforms
1. Jupyter Notebook  
2. Google Colaboratory  

The notebooks are placed in one of these two folders.  

If the notebook is in jupyter_notebook => code executed using Jupyter Notebook  
If the notebook is in google_colaboratory => code executed using Google Colaboratory  

./jupyter_notebook/4041-dog-breed-classification/ &  
./google_colaboratory/4041-dog-breed-classification/  
are directories that the source codes are placed  

NOTEBOOK DEPENDENCIES (PYTHON LIBRARIES USED):  

PRE-PROCESSING (JUPYTER NOTEBOOK):  
	- numpy   
	- pandas  
	- glob  
	- h5py  
	- os  
	- math  
	- time  
	- matplotlib  
	- tensorflow  
	- tqdm  

TRAINING (IN GOOGLE COLABORATORY):  
	- gc  
	- os  
	- copy  
	- tqdm  
	- numpy  
	- pandas  
	- random  
	- time  
	- shutil  
	- csv  
	- tensorflow   
	- math  
	- matplotlib  
	- sklearn  
	- seaborn  

./jupyter_notebook/4041-dog-breed-classification/  
	Datasets/data.txt  
		- A list of data filenames that were used in this project  
		- A link to direct to the actual files in Google Drive  
		
	data-preprocess-imgs-128-float64.ipynb   
		- generate .npz compressed file containing all the train images   
		- scaled image size of 128x128   
		- dtype of each pixel is of 64bits float   

	data-preprocess-imgs-192-float16.ipynb
		- generate .npz compressed file containing all the train images  
		- scaled image size of 192x192   
		- dtype of each pixel is of 16bits float  
		
	data-preprocess-imgs-224-uint8.ipynb  
		- generate .npz compressed file containing all the train images  
		- scaled image size of 224x224  
		- dtype of each pixel is of 8bits integer  
		
	data-preprocess-imgs-299-uint8.ipynb  
		- generate .npz compressed file containing all the train images  
		- scaled image size of 299x299   
		- dtype of each pixel is of 8bits integer
		
	get-test-filename.ipynb
		- a notebook to generate the filenames of the test set without extension '.jpg' and save it in a .csv file
		- .csv used in the model evaluation part in the training-feature-extraction-299.ipynb notebook
		
./google_colaboratory/4041-dog-breed-classification/
	Datasets/data.txt
		- A list of data filenames that were used in this project
		- A link to direct to the actual files in Google Drive

	models/models.txt
		- A list of model filenames that were used in this project
		- A link to direct to the actual files in Google Drive		

	training-feature-extraction-299.ipynb
		- notebook to train the ensemble model used in Phase 3 of the report
	
	training-general-128.ipynb
		- notebook to train the pre-trained model used in Phase 1 of the report
	
	training-general-192.ipynb
		- notebook to train the pre-trained model used in Phase 2 of the report
	
	training-general-224.ipynb
		- notebook to train the pre-trained model used in Phase 2 of the report