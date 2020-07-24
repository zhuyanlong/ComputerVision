import cv2

class dHash:
	def __init__(self,path):
		self.path=path

	def difference(self):
		#opencv读取照片
		image=cv2.imread(self.path)
		resize_width = 9
		resize_height = 8
		#按9X8缩放
		smaller_image = cv2.resize(image,(resize_width, resize_height),interpolation=cv2.INTER_CUBIC)
		#灰度化
		grayscale_image = cv2.cvtColor(smaller_image,cv2.COLOR_BGR2GRAY)
		cv2.imwrite(self.path,grayscale_image)
		# 3. 比较相邻像素
		# pixels = list(grayscale_image.getdata())
		# difference = []
		# for row in range(resize_height):
		# 	row_start_index = row * resize_width
		# 	for col in range(resize_width - 1):
		# 		left_pixel_index = row_start_index + col
		# 		difference.append(pixels[left_pixel_index] > pixels[left_pixel_index + 1])
		# return difference

def main():
	dhash=dHash("contrast2.jpg")
	dhash.difference()

main()