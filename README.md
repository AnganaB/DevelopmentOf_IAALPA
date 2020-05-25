Note: Please do not disrupt the directory structure while executing the codes.

For a clearer view of this README file go to https://github.com/manjitborah2710/DevelopmentOf_IAALPA

Requirements:

<!-- 

		Requried libraries

 -->



# 1. Finding the AAIs for each network

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
>
>```python
>def s22(pair,graph):
>   s = rwa(pair,graph,1,1,1,4,1)
>   return s
>```

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
 

# 2. Finding optimal AAIs using decision tree

<!-- instructions to execute code -->

# 3. Finding complementary AAIs using SVM

Go to **"3 Finding complementary AAIs with SVM\output\"** and carry out the following operations:

	(a) Run "1 GenerateDataFrame.py" and provide the path to the edgelist (prepared in CSV format) as the command-line argument. This generated a file "Dataset.csv".

	(b) Run "2 prepare_test_sample_for_svm.py" and provide as the command-line arguments the path to the dataset produced as the output of (a) (Dataset.csv) and the optimal AAI index (starting from 0) for this network obtained from the results of the Decision Tree. This generates a file "test_sample.csv".

	(c) Run "3 find_comp_aais.py" providing the CSV, produced as a result of step (b) (test_sample.csv), as the command-line input.

**Note: The edgelist used in step (a) should correspond to the network for which we are finding the optimal and complementary AAIs.**

After the completion of step (c), we get pairs of AAI and a value 1 or -1 alongside them representing whether they are complementary or not respectively.

The training dataset for the SVM is located in **"3 Finding complementary AAIs with SVM\svm_train\"**. The training has been carried out in the notebook **svm.ipynb**. To retrain the model, replace **svm_train.csv** with your own training set and execute all the cells of the IPython Notebook **svm.ipynb**. The model after exeution will be saved as **svm.pkl**.

The code for preparing the training dataset is placed inside **"3 Finding complementary AAIs with SVM\dataset_preparation\"**. There are two files:

**auc_new.py** - This is a slight alteration of the code **auc.py** mentioned in section _1. Finding the AAIs for each network_. This file is imported in the next code.

**prepare_train_data_for_svm.py** - This is the main code that will generate a training sample for the SVM given a network. This preparation is done based on random sampling from the node pairs of the network edgelist provided in .csv format. To specify the network from which the training sample is to be prepared, before running the code, replace the path to the csv edgelist in the following line of this file:

>```python
> res=auc_new.main("sample.csv")
>```

Please note that the **auc_new.py** file must be in the same directory as **prepare_train_data_for_svm.py**. There is no need to run **auc_new.py**, this file is imported in **prepare_train_data_for_svm.py** as a module and acts as a helper code for its successful execution.

The proof of execution has been provided inside folders **output** and **svm_train**. Since the **dataset_preparation** folder consists only of helper code and won't generate any console I/O, the execution of the files is not shown.

**Important**
The index for the different AAIs are mentioned in the following table:
| AAI | Index|
| --- | ---|
| S1  | 0  |
| S2  | 1  |
| .   | .  |
| .   | .  |
| S25 | 24 |
Please refer to the literature followed for this project to have a full understanding of the algorithms **S1,S2,S3...,S25**. Also please note that the edgelist in csv format must contain only 2 columns the **Source** and **Target** respectively.

# 4. Finding composite AAI
