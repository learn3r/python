import os.path
import cv2
import itertools

DATA_PATH1 = "data1"
DATA_PATH2 = "data2"

def main():
	curr_path = os.getcwd()

	data_path1 = os.path.join(curr_path, DATA_PATH1)
	data_path2 = os.path.join(curr_path, DATA_PATH2)
	data_list1 = os.listdir(data_path1)
	data_list2 = os.listdir(data_path2)
	
	for file1, file2 in zip(data_list1, data_list2):
		file_name1 = os.path.splitext(file1)[0]
		file_name2 = os.path.splitext(file2)[0]
		ext1 = os.path.splitext(file1)[1]
		ext2 = os.path.splitext(file2)[1]
		
		file_size1 = os.path.getsize(data_path1 + "/" + file1)
		file_size2 = os.path.getsize(data_path2 + "/" + file2)
		
		if file_size1 == file_size2:
			print("These two images' size are the same: " + file_name1 + " and " + file_name2)
		
		input_path1 = os.path.join(data_path1, file1)
		image1 = cv2.imread(cv2.samples.findFile(input_path1))
		
		input_path2 = os.path.join(data_path2, file2)
		image2 = cv2.imread(cv2.samples.findFile(input_path2))
		
		image_shape1 = image1.shape[:2]
		image_shape2 = image2.shape[:2]
		
		if image_shape1 == image_shape2:
			difference = cv2.subtract(image1, image2)
			b, g, r = cv2.split(difference)
			
			if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
				print("These two images' colors are equal: " + file_name1 + " and " + file_name2)
			else:
				print("These two images' colors are different: " + file_name1 + " and " + file_name2)

	return

if __name__ == '__main__':
	main()