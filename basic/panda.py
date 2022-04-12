  
import numpy as np
import pandas as pd

def header(msg):
	print('-' * 50)
	print('[ ' + msg + ' ]')

# 1. load hard-coded data into a dataframe
header("1. load hard-coded data into a df")
filename  = 'topost.pdf'
df = pd.read_csv(filename)
print(df)
#print(df.head(2))    #first two lines of data
#print(df.tail(2))      # last two lines of data