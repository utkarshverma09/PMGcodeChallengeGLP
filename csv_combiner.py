'''
Coding challenge for the Graduate Leadership Program at PMG Digital Agency
Submission by: Utkarsh Verma
Date: 03/31/2022
'''
#importing all the necessary and required libraries
import pandas as pd
import sys
import os
#checking if the given arguements in the command line are valid or not
def validateArgs(argsList):
    #incase no csv file names given then the function would return False
    if len(argsList)<=1:
        print("Not enough arguements given")
        return False
    else:
        for file in argsList[1:]:
            #will check if there exist a file in the given directory
            if os.path.exists(file):
                #will check if the file is of csv format
                if file[-4:]!=".csv":
                    print("Given file is not of csv format")
                    return False
                #will check if the File has data in it otherwise return False
                if os.stat(file).st_size==0:
                    print(" Given File is empty!")
                    return False
            else:
                print("Incorrect File name entered!")
                return False
        #return True if it satisfies all the condition
        return True

def combine_csv(argsList):
    
    #iterating over all the args but the first one which is supposed to be the py file itself
    for fNum in range(1,len(argsList)):
        #reading data in chunks to avoid any memory error in case file size is too large
        for chunk in pd.read_csv(argsList[fNum],chunksize=10**6):
            #supplying data to the new column which is named filename that consist the name of the file from which data is extracted
            chunk['filename']=argsList[fNum][11:]
            #printing the data to directly to the csv file; only putting the header for the first iteration 
            print (chunk.to_csv(index = False, line_terminator='\n', header = True if fNum == 1 else False), end = '')
    
def main():
    #storing all the arguments in the argsList
    argsList=sys.argv
    #if the arguements are valid then it will call the combine_csv function else it will print the error message
    if validateArgs(argsList):
        combine_csv(argsList)
    else:
        print("Try running the code using command: csv_combiner.py ./fixtures/name1.csv ./fixtures/name2.csv > output.csv")

if __name__=="__main__":
    main()