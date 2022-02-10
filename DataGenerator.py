##****************************************************************************************************************************
##                                          Data Generator for Inverse Methods
##                                 
## Author: Omkar Junnarkar, Semester-3 MSc. Computational Material Science
## Matriculation Nr.: 66157	Email: omkar.junnarkar@student.tu-freiberg.de
## IDE : Visual Studio Code 

## os : To access a directory from system
## numpy : To perform certain matrix operations
## pandas : To write csv files
## matplotlib.pyplot : To enable plotting IF REQUIRED

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

## Changing directory to write files to a specific folder

os.chdir(r"E:\Documents\TU Freiberg CMS\3.Sem-Study Material\PPP\Working_Directory\Gradient_Descent_Algorithm")

## Defining function y=f(x)

def f(x):
    #y=0.745*x**3 + 1e-8*x**2*np.cos(2*x)
    ##//y=0.745*x**3 + 4*x**2*np.cos(2*x)
    y=0.745*x**3 + 8.24*x**2 - 0.08*x + 9.4*np.exp(1*x - 4)
    
    #y=6.89*x**4 - 2.17*np.exp(1.97*x)
    return y

## Opening file in write mode

outf=open("ActualParameterData.txt","w")
outf.write("Equation and Parameters for generated Dataset are as follows:\n")
outf.write(" y=0.745*x**3 + 8.24*x**2 - 0.08*x + 9.4*np.exp(1*x - 4)")
outf.close();

## Listing Input Values

x=np.linspace(-1,4,num=100)
# z=np.linspace(-2,5,num=100)
# p=np.linspace(-1,2,num=100)

## Obtaining Output Values

y=f(x)
print(y)

## Creating Data Frame and writing csv file for i/o data

dfx =pd.DataFrame(x)
dfx.to_csv("xdata.csv",index=False,index_label=False)

dfy =pd.DataFrame(y)
dfy.to_csv("y_measured.csv",index=False,index_label=False)



