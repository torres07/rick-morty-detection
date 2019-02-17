# -*- coding: utf-8 -*-
# @Author: pedrotorres
# @Date:   2019-02-15 15:40:01
# @Last Modified by:   pedrotorres
# @Last Modified time: 2019-02-16 15:59:33

import glob, os

# Current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
current_dir = current_dir + '/rick-morty-1'

print(current_dir)

# Directory where the data will reside, relative to 'darknet.exe'
#path_data = './NFPAdataset/'

# Percentage of images to be used for the test set
percentage_test = 20;

# Create and/or truncate train.txt and test.txt
file_train = open('train.txt', 'w')
file_test = open('test.txt', 'w')

# Populate train.txt and test.txt
counter = 1
index_test = round(100 / percentage_test)
for pathAndFilename in glob.iglob(os.path.join(current_dir, "*.jpg")):
    title, ext = os.path.splitext(os.path.basename(pathAndFilename))

    if counter == index_test:
        counter = 1
        file_test.write(current_dir + "/" + title + '.jpg' + "\n")
    else:
        file_train.write(current_dir + "/" + title + '.jpg' + "\n")
        counter = counter + 1