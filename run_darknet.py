# -*- coding: utf-8 -*-
# @Author: Pedro Torres
# @Date:   2019-02-16 11:01:56
# @Last Modified by:   Pedro Torres
# @Last Modified time: 2019-02-17 10:36:45

from os import system
from os import listdir
from os.path import join

path = '/home/pedrotorres/Documents/darknet/data/rick-morty/E01S01'
# add data info at the end
config = './darknet detector test cfg/rick-morty.data cfg/rick-morty-yolov3-tiny.cfg backup/yolov3-tiny-rick_5000.weights'
output_dir = 'output_predictions'


for f in listdir(path):
	system('{} {} -out {}'.format(config, join(path, f), join(output_dir, f)))