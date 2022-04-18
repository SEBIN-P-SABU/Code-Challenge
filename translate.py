import copy
import csv
import sys
import fileinput
import os
import re
from tkinter.filedialog import askopenfilename
from googletrans import Translator
import pandas as pd  
      


with open("french_dictionary.csv") as csv_file: 
      
    csv_reader = csv.reader(csv_file, delimiter=',')  # read the csv file
       
    df = pd.DataFrame([csv_reader], index=None)
    df.head()
      

# iterating 
for val in list(df[2]):
    print(val[0])      #value of first column
    print(val[1])      #value of second column              


with open('t8.shakespeare.txt') as f:
    lines = f.readlines()
    # f1 = open(str(lines),'rt')

    f = (str(lines),'wt')
    for lines in f:

     for word in lines.split():      # reading each word                                
      print(word)     # displaying the words line by line

# have to fetch each words in find_words text file ("val[0]") and check those with each lines in t8.shakespeare file ("word") 
# and if equals ("val[0]==word"), then replace it by val[i]
