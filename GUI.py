import tkinter as tk
from PIL import ImageTk, Image


image_path = ''
image_path_is_set = False #when the path for the image is set it beccomes true
action = False # encrypt = false , decrypt = true
key = '' # enccryption key

def load_window(valid_path = True):
	global image_path_is_set
	image_path_is_set = False
	window = tk.Tk()
	window.title('image AES')
	window.geometry("500x500")
	window.resizable(0,0)

	def take_input():
		global image_path
		global image_path_is_set
		input = T.get("1.0","end-1c")
		image_path = input
		image_path_is_set = True
		window.destroy()

	
	photo = tk.PhotoImage(file = r'photos/drive.png')
	tk.Label(window ,font=('Verdana',15), text = 'first step : load the image\nplease enter the image path to be loaded').pack(side = tk.TOP , pady = 10)
	tk.Label(window ,image = photo).pack(side = tk.TOP)
	T = tk.Text(window,height = 1 , width = 52, bg = "light yellow")
	T.pack()

	if not valid_path :
		tk.Label(window ,font=('Verdana',10), text = 'please enter the correct path',fg = 'red').pack(side = tk.TOP)

	tk.Button(window ,font=('Verdana',15), text = 'LOAD',command = lambda:take_input()).pack(side = tk.BOTTOM,pady = 10)
	window.mainloop()

	return image_path 

def AES_window(targit_path):

	window = tk.Tk()
	window.title('image AES')

	def enc_button():
		global action
		global key
		action = False
		key = T.get("1.0","end-1c")
		window.destroy()

	def dec_button():
		global action
		global key
		action= True
		key = T.get("1.0","end-1c")
		window.destroy()

	
	photo = ImageTk.PhotoImage(Image.open(targit_path))
	tk.Label(window ,font=('Verdana',15), text = 'second step : encrypt or decrypt the image').pack(side = tk.TOP , pady = 10)
	tk.Label(window ,image = photo).pack(side = tk.TOP)
	T = tk.Text(window,height = 1 , width = 52, bg = "light yellow")
	T.pack()
	tk.Button(window ,font=('Verdana',15), text = 'Encrypt',command = lambda:enc_button()).pack(pady = 10)
	tk.Button(window ,font=('Verdana',15), text = 'Decrypt',command = lambda:dec_button()).pack(pady = 10)
	window.mainloop()

	return key , action 
