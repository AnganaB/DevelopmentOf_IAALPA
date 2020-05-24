Note: Please do not disrupt the directory structure while executing the codes.

Requirements:

<!-- 

		Requried libraries

 -->



1. Finding the AAIs for each network

<!-- instructions to execute code -->

2. Finding optimal AAIs using decision tree

<!-- instructions to execute code -->

3. Finding complementary AAIs using SVM

	(a) Go to "3 Finding complementary AAIs with SVM\output\"

	(b) Run "1 GenerateDataFrame.py" and provide the path to the edgelist (prepared in CSV format) as the command-line argument.

	(c) Run "2 prepare_test_sample_for_svm.py" and provide as the command-line arguments the path to the dataset produced as the output of (b) and the optimal AAI index (starting from 0) for this network obtained from the results of the Decision Tree.

	(d) Run "3 find_comp_aais.py" providing the CSV, produced as a result of step (c), as the command-line input.
	
	After the completion of step (d), we get pairs of AAI and a value 1 or -1 alongside them representing whether they are complementary or not respectively.

	The training dataset for the SVM is located in "3 Finding complementary AAIs with SVM\svm_train\". The training has been carried out in the notebook "svm.ipynb". To retrain the model, replace "svm_train.csv" with your own training set and execute all the cells of the IPython Notebook "svm.ipynb". The model after exeution will be saved as "svm.pkl".

	The proof of execution has been provided inside both the folders.

4. Finding composite AAI