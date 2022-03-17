import GUI
from PIL import Image
import AES
import matplotlib.pyplot as plt


if __name__ == "__main__":
	the_path_is_valid = True
	while(True):
		GUI.load_window(the_path_is_valid)
		if GUI.image_path_is_set==False:
			break 
		try:
			im = Image.open(GUI.image_path)
			print("image was loaded successully")
			break
		except Exception as e:
			the_path_is_valid = False
	if GUI.image_path_is_set :
		GUI.AES_window(GUI.image_path)
		if GUI.action :
			result = AES.encrypt(im,GUI.key)
		else :
			result = AES.decrypt(im,GUI.key)


	plt.imshow(result)
	plt.draw()
	plt.pause(5)
	result.save('result.png')
