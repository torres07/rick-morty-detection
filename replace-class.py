# -*- coding: utf-8 -*-
# @Author: pedrotorres
# @Date:   2019-02-16 19:33:22
# @Last Modified by:   pedrotorres
# @Last Modified time: 2019-02-17 14:19:21

from os import listdir
from os.path import join

path = '/home/pedrotorres/Documents/rick-morty/rick-morty-1'

for f in listdir(path):
	with open(join(path, f), 'r') as txt:
		if '.txt' in f and 'morty-yolo' in f:
			data = txt.readline().split(' ') 
			data[0] = 1
			with open(join(path, 'new_' + f), 'w') as txt_:
				txt_.write('{} {} {} {}'.format(data[0], data[1], data[2], data[3]))