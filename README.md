Note: Please do not disrupt the directory structure while executing the codes.

Requirements:

<!-- 

		Requried libraries

 -->



#1. Finding the AAIs for each network

Included in this folder are a series of **helper codes** for construction of training and testing datasets for both the Decision Tree 
as well as the Support Vector Machine Models. The scripts are not intended to function as standalone units, rather they are meant 
to be used in other driver functions. 


**computeAAI.py**

This contains the fuctions that compute the 8 different microstructure-based indices and 4 different macrostructure-based indices.
Each function takes in a _node pair_ and a _**networkx** graph_ as mandatory inputs.

>wa2 additionally takes as input the constant values _rho_ and _phi_
>rwa additionally takes as input the constant values _a_,_b_,_c_,_rho_,_phi_

All the inputs are entered in the order of mention


**getAAI.py**

The functions in this script are used to call the functions in *computeAAI.py* to generate the indices mentioned in the theory by 
passing the appropriate parameter values. For eg, 

>Index S22 is defined as _rwa_ with _a=1, b=1, c=1, rho=4, phi=1_ 
>This is computed by 
>`def s22(pair,graph):
    s = rwa(pair,graph,1,1,1,4,1)
    return s`

All the functions in this file take a _node pair_ and a _**networkx** graph_ as mandatory inputs.


**auc.py**

This is the script that uses the above scripts to compute the AUC values used by the Decision Tree and the SVM. There are 3 primary
functions in the file with several other helper functions. 

>_getNetworkAUC(csvfile)_ takes in a CSV file _(.csv format)_ and returns a list of 25 AUC for 25 differrent AAI values.
>_getBestAUC(csvfile)_ takes in a CSV file _(.csv format)_ and returns the index of the best AAI based on the best AUC value.
>_getComplementaryAAI(csvfile)_ takes in a CSV file _(.csv format)_ and the _index of the best AAI_ and returns a list of 
the complementary AAIs based on the best AAI.

The file has comments that describe in detail what all the other functions do.


Apart from these scripts, there are two *IPYNB* files and a *Dataset* folder. _demo.ipynb_ demonstrates the working of the scripts and the above mentioned 
functionalities. _avg_auc_plot.ipynb_ has the plot of the avgerage AUC values and also the list of values. _Dataset_ has the datasets used
in these two IPYNB files. These files can be treated as the proof of execution. 
 

#2. Finding optimal AAIs using decision tree

<!-- instructions to execute code -->

#3. Finding complementary AAIs using SVM

	(a) Go to "3 Finding complementary AAIs with SVM\output\"

	(b) Run "1 GenerateDataFrame.py" and provide the path to the edgelist (prepared in CSV format) as the command-line argument.

	(c) Run "2 prepare_test_sample_for_svm.py" and provide as the command-line arguments the path to the dataset produced as the output of (b) and the optimal AAI index (starting from 0) for this network obtained from the results of the Decision Tree.

	(d) Run "3 find_comp_aais.py" providing the CSV, produced as a result of step (c), as the command-line input.
	
	After the completion of step (d), we get pairs of AAI and a value 1 or -1 alongside them representing whether they are complementary or not respectively.

	The training dataset for the SVM is located in "3 Finding complementary AAIs with SVM\svm_train\". The training has been carried out in the notebook "svm.ipynb". To retrain the model, replace "svm_train.csv" with your own training set and execute all the cells of the IPython Notebook "svm.ipynb". The model after exeution will be saved as "svm.pkl".

	The proof of execution has been provided inside both the folders.

#4. Finding composite AAI