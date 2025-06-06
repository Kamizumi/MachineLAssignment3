#-------------------------------------------------------------------------
# AUTHOR: Timothy Tsang
# FILENAME: Assignment 3
# SPECIFICATION: Train single layer Perceptron and Multi-Layer Perceptron to classify optically recognized handwritten digits
# FOR: CS 4210- Assignment #3
# TIME SPENT: 2 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: YOU HAVE TO WORK WITH THE PYTHON LIBRARIES numpy AND pandas to complete this code.

#importing some Python libraries
from sklearn.linear_model import Perceptron
from sklearn.neural_network import MLPClassifier #pip install scikit-learn==0.18.rc2 if needed
import numpy as np
import pandas as pd

n = [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.05, 0.1, 0.5, 1.0]
r = [True, False]
used_algorithms = ["Perceptron", "MLP"]

df = pd.read_csv('optdigits.tra', sep=',', header=None) #reading the data by using Pandas library

X_training = np.array(df.values)[:,:64] #getting the first 64 fields to form the feature data for training
y_training = np.array(df.values)[:,-1]  #getting the last field to form the class label for training

df = pd.read_csv('optdigits.tes', sep=',', header=None) #reading the data by using Pandas library

X_test = np.array(df.values)[:,:64]    #getting the first 64 fields to form the feature data for test
y_test = np.array(df.values)[:,-1]     #getting the last field to form the class label for test

greatest_perceptron_acc = 0
greatest_mlp_acc = 0
perceptron_lrate = 0
mlp_lrate = 0
perceptron_shuffle = ""
mlp_shuffle = ""


for learning_rate in n : #iterates over n

    for shuffle in r: #iterates over r

        #iterates over both algorithms
        #-->add your Pyhton code here
        for algorithm in used_algorithms:

            #Create a Neural Network classifier
            #if Perceptron then
            if algorithm == "Perceptron":
                #   clf = Perceptron()    #use those hyperparameters: eta0 = learning rate, shuffle = shuffle the training data, max_iter=1000
                clf = Perceptron(eta0 = learning_rate, shuffle = shuffle, max_iter = 1000)
                #   clf = MLPClassifier() #use those hyperparameters: activation='logistic', learning_rate_init = learning rate,
                #                          hidden_layer_sizes = number of neurons in the ith hidden layer - use 1 hidden layer with 25 neurons,
                #                          shuffle = shuffle the training data, max_iter=1000
                # -->add your Pyhton code here
            else:
                clf = MLPClassifier(activation = 'logistic', learning_rate_init = learning_rate,
                                    hidden_layer_sizes = (25), shuffle = shuffle, max_iter = 1000)



            #Fit the Neural Network to the training data
            clf.fit(X_training, y_training)

            #make the classifier prediction for each test sample and start computing its accuracy
            #hint: to iterate over two collections simultaneously with zip() Example:
            #for (x_testSample, y_testSample) in zip(X_test, y_test):
            #to make a prediction do: clf.predict([x_testSample])
            #--> add your Python code here
            correct_predictions = 0
            for(x_testSample, y_testSample) in zip(X_test, y_test):
                prediction  = clf.predict([x_testSample])
                if prediction == y_testSample:
                    correct_predictions += 1
            tot_acc =  correct_predictions / len(y_test)


            #check if the calculated accuracy is higher than the previously one calculated for each classifier. If so, update the highest accuracy
            #and print it together with the network hyperparameters
            #Example: "Highest Perceptron accuracy so far: 0.88, Parameters: learning rate=0.01, shuffle=True"
            #Example: "Highest MLP accuracy so far: 0.90, Parameters: learning rate=0.02, shuffle=False"
            #--> add your Python code here
            if algorithm == "Perceptron":
                if tot_acc > greatest_perceptron_acc:
                    greatest_perceptron_acc = tot_acc
                    perceptron_lrate = learning_rate
                    perceptron_shuffle = shuffle
                    print(f"Highest Perceptron Accuracy, currently, is : {tot_acc:.4f}, Parameters: learning rate = {learning_rate}, shuffle = {shuffle}")
            else:
                if tot_acc > greatest_mlp_acc:
                    greatest_mlp_acc = tot_acc
                    mlp_lrate = learning_rate
                    mlp_shuffle = shuffle
                    print(f"Highest MLP Accuracy, currently, is : {tot_acc:.4f}, Parameters: learning rate = {learning_rate}, shuffle = {shuffle}")
print("---------------------------------------------------------------")
print(f"Best Perceptron Accuracy: {greatest_perceptron_acc:.4f}, Parameters: learning rate = {perceptron_lrate}, shuffle = {perceptron_shuffle}")
print(f"Best MLP Accuracy: {greatest_mlp_acc:.4f}, Parameters: learning_rate = {mlp_lrate}, shuffle = {mlp_shuffle}")













