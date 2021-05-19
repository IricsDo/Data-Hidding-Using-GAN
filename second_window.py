import os
import time
import cv2
import numpy as np
from tkinter import *
import datetime
import tkinter.messagebox
from tkinter import filedialog
from PIL import Image, ImageTk  

class Sub_window(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg='#b3b3b3')
        self.sub_master = master
        self.init_sub_window()

    def init_sub_window(self):

        self.fullpath_work_secon = os.getcwd()
        self.subwindow = self.sub_master
        self.master.title("Image Hidden Mode")
        self.subfileimage = StringVar()
        self.subfiletxt = StringVar()
        self.sizeOfimg = StringVar()
        
        # Tao folder can thiet cho GUI
        if not os.path.exists("image_decode"):
            os.makedirs(os.path.join(self.fullpath_work_secon, "image_decode"), exist_ok=True)
        if not os.path.exists("text_decode"):
            os.makedirs(os.path.join(self.fullpath_work_secon, "text_decode"), exist_ok=True)

        # Tao cho de show image
        location_image = Entry(self.subwindow, state= DISABLED)
        location_image.place(x= 10, y= 10, width= 530, height= 530)

        # Hien thi duong dan load image
        show_path_sub_image = Entry(self.subwindow, textvariable= self.subfileimage)
        show_path_sub_image.place(x= 150, y= 560, width= 390, height= 30)

        # Hien thi duong dan load txt
        show_path_sub_image = Entry(self.subwindow, textvariable= self.subfiletxt)
        show_path_sub_image.place(x= 150, y= 590, width= 390, height= 30)

        # shape of image orginal
        shape_img = Label(self.subwindow, text='Shape Of Image:', fg ="black", \
                    bg= None, relief= None, font =("arial", 11, "bold"))
        shape_img.place(x= 10, y=630)

        # Hien thi shape of image orginal
        shape_image_hidden = Entry(self.subwindow, textvariable= self.sizeOfimg)
        shape_image_hidden.place(x= 150, y= 620, width= 100, height= 35)

        # Tao nut load image
        load_sub_image = Button(self.subwindow, text= "Open image", fg ="black", \
                    bg="white", relief=RAISED, font =("arial", 12, "bold"),\
                    command= self.Load_sub_image)
        load_sub_image.place(x= 10, y= 560)

        # Tao nut load text
        load_sub_txt = Button(self.subwindow, text= "Open text", fg ="black", \
                    bg="white", relief=RAISED, font =("arial", 12, "bold"),\
                    command= self.Load_sub_txt)
        load_sub_txt.place(x= 10, y= 590)

        # Tao nut convert image to text
        i2t_button = Button(self.subwindow, text= "Im2Tex", fg ="black", \
                    bg="white", relief=RAISED, font =("arial", 16, "bold"),\
                    command= self.images_to_text)
        i2t_button.place(x= 250, y= 620)

        # Tao nut convert text to image
        t2i_button = Button(self.subwindow, text= "Tex2Im", fg ="black", \
                    bg="white", relief=RAISED, font =("arial", 16, "bold"),\
                    command= self.text_to_images)
        t2i_button.place(x= 355, y= 620)

        # Tao nut Exit thoat GUI
        exit_sub_button = Button(self.subwindow, text= "Quit", fg ="black", \
                    bg="red", relief=RAISED, font =("arial", 16, "bold"),\
                    command= self.close_sub_window)
        exit_sub_button.place(x= 460, y= 620)

    def Load_sub_image(self):

        try:
            self.image_sub_selected = filedialog.askopenfilename(title= 'Choose image ',initialdir=self.fullpath_work_secon, filetypes= (("All","*.png"),("PNG files","*.png")))
            self.subfileimage.set(self.image_sub_selected)

            # Hien thi hinh anh
            image_input = Image.open(self.image_sub_selected)
            image_resize = image_input.resize((512, 512))
            self.photo_sub_input = ImageTk.PhotoImage(image_resize)
            self.lab_sub = Label(self.subwindow, image= self.photo_sub_input)
            self.lab_sub.place(x= 18, y= 18)
            tkinter.messagebox.showinfo("Notification", "Open image successful")

        except Exception as e:
            print(e)
            tkinter.messagebox.showerror("Error", "Can not open image")

    def Load_sub_txt(self):

        try:
            self.txt_sub_selected = filedialog.askopenfilename(title= 'Choose file ',initialdir=self.fullpath_work_secon, filetypes= (("All","*.txt"),("TXT files","*.txt")))
            self.subfiletxt.set(self.txt_sub_selected)

            if os.path.exists(self.txt_sub_selected):
                with open(self.txt_sub_selected, 'r') as m:
                    self.get_txt = m.read()
                m.close()

                tkinter.messagebox.showinfo("Notification", "Load file was successful")

        except Exception as e:
            print(e)
            tkinter.messagebox.showerror("Error", "Can not open txt file")

    def images_to_text(self):
        
        try:
            listOfCharacter = []

            image = cv2.imread(self.image_sub_selected, 0)
            self.shapeOrgi = image.shape
            self.sizeOfimg.set('w:' + str(self.shapeOrgi[1]) + ' ' + 'h:' + str(self.shapeOrgi[0]))

            flatten_image = image.flatten()
            for value in flatten_image:
                listOfCharacter.append(chr(value))
            
            listToStr = ' '.join(map(str, listOfCharacter))
            self.imageToString = listToStr.replace(" ", "")

            self.txt_file_out = os.path.join("text_decode", str(datetime.datetime.now()).replace(" ", "@") + ".txt")

            with open(self.txt_file_out, 'w') as f:
                f.write(self.imageToString)
            f.close()
            print("Number of character after convert image to text: ", len(self.imageToString))

            tkinter.messagebox.showinfo("Notification", "Convert Image to Text successful")

        except Exception as e:
            print(e)
            tkinter.messagebox.showwarning("Notification", "Can not convert Image to Text")
        
    def text_to_images(self):

        try:
            if self.sizeOfimg == 0:
                tkinter.messagebox.showwarning("Notification", "Must enter size of image")

            else:
                shapeOrgi = self.sizeOfimg.get()
                listOfshape = shapeOrgi.split(" ")

                w = listOfshape[0][2::]
                h = listOfshape[1][2::]

                listOfVal = []
                strToList = list(self.get_txt)
                for value in strToList:
                    listOfVal.append(ord(value))

                arrayOfVal = np.array(listOfVal)
                image_found = arrayOfVal.reshape(int(h), int(w))
                img_file_out = os.path.join("image_decode", str(datetime.datetime.now()).replace(" ", "@") + ".png")
                cv2.imwrite(img_file_out, image_found)

                tkinter.messagebox.showinfo("Notification", "Convert Text to Image successful")
        except Exception as e:
            print(e)
            tkinter.messagebox.showwarning("Notification", "Can not convert Text to Image")

    def close_sub_window(self):
            
        self.sub_master.destroy()

    def get_name_txt_file(self):

        return self.txt_file_out
