# -*- coding: utf-8 -*-
# @Author: pedrotorres
# @Date:   2019-02-17 11:27:05
# @Last Modified by:   pedrotorres
# @Last Modified time: 2019-02-17 13:01:34

import cv2

result_path = '/home/pedrotorres/Documents/darknet-master/result.txt'

dic = {}

if __name__ == "__main__":
	with open(result_path, 'r') as f:
		last_path = ''
		for line in f:
			if "Image Path" in line:
				img_path = line.split()[3][:-1]
				dic[img_path] = []
				last_path = img_path
				# dic[]
			if "morty: " in line:
				dic[last_path].append(line)

	final_dic = {}

	for key in dic:
		if len(dic[key]) != 0:
			final_dic[key] = dic[key]

	for key in final_dic:
		i = 1
		for data in final_dic[key]:
			data = data.split()
			x = int(data[3])
			y = int(data[5])
			w = int(data[7])
			h = int(data[9][:-1])
			
			print('cords: {}'.format((x,y,w,h)))

			if x < 0: x = 0
			if y < 0: y = 0

			img = cv2.imread(key)
			print(img.shape)


			crop_img = img[y:y+h, x:x+w]
			filename = key.split('/')[-1]
			cv2.imwrite('bbox_out/{}_{}'.format(i, filename), crop_img)

			with open('bbox_out/{}_{}.txt'.format(i, filename), 'w') as txt:
				# first param class number
				# <class_number> (<absolute_x> / <image_width>) (<absolute_y> / <image_height>) (<absolute_width> / <image_width>) (<absolute_height> / <image_height>)
				txt.write('{} {} {} {} {}'.format(0, (.1 * x) / img.shape[0] , (.1 * y) / img.shape[1], (.1 * w) / img.shape[0], (.1 * h) / img.shape[1]))			
			
			i = i + 1


	# crop_img = img[y:y+h, x:x+w]
	# cv2.imshow("cropped", crop_img)
	# cv2.waitKey(0)
