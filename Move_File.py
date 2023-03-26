import os
import shutil

source='C:/Users/bmohi/Downloads'
destination='C:/Users/bmohi/OneDrive/Documents/docs_file'

list_of_files = os.listdir(source)
print(list_of_files)

for i in list_of_files:
  os.path.splitext(list_of_files)