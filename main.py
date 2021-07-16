import os
import time
import numpy as np
from tkinter import *
import datetime
import tkinter.messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
from cryptography.fernet import Fernet
from steganogan.models import SteganoGAN
from steganogan.loader import DataLoader
from steganogan.critics import BasicCritic
from steganogan.decoders import BasicDecoder, DenseDecoder
from steganogan.encoders import BasicEncoder, DenseEncoder, ResidualEncoder
from second_window import Sub_window

class Window(Frame):

    def __init__(self, master):
        Frame.__init__(self, master, bg='#b3b3b3')
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("Data Hiden Using GANs")
        self.inputfileimage = StringVar()
        self.inputfilemodel = StringVar()
        self.timeprocess = StringVar()
        self.accuracy_show = StringVar()
        self.reedsolomom_show = StringVar()
        self.psnr_show = StringVar()
        self.ssim_show = StringVar()
        self.message_encode = StringVar()
        self.message_decode = StringVar()
        self.txt_in = StringVar()
        self.txt_out = StringVar()
        self.mode_var = StringVar()
        self.status_file = False
        self.status_key = False
        self.have_key = False
        self.hidden_image = False
        
        # Tao folder can thiet cho GUI
        if not os.path.exists("image_decode"):
            os.makedirs(os.path.join(fullpath_work, "image_decode"), exist_ok=True)
        if not os.path.exists("text_decode"):
            os.makedirs(os.path.join(fullpath_work, "text_decode"), exist_ok=True)
        if not os.path.exists("key"):
            os.makedirs(os.path.join(fullpath_work, "key"), exist_ok=True)
        if not os.path.exists("message"):
            os.makedirs(os.path.join(fullpath_work, "message"), exist_ok=True)
        if not os.path.exists("result"):
            os.makedirs(os.path.join(fullpath_work, "result"), exist_ok=True)
            if not os.path.exists("result/_"):
                os.makedirs(os.path.join(os.path.join(fullpath_work,"result"),  "_"), exist_ok=True)
        
        # Tao logo
        logo = Image.open(os.path.join(os.path.join(fullpath_work, "images"), "logo.png"))
        self.photo_logo = ImageTk.PhotoImage(logo)
        self.lab_logo = Label(image= self.photo_logo)
        self.lab_logo.place(x= 1120, y= 38)

        # Ten truong
        city_name = Label(window, text='Ho Chi Minh City', fg ="black", \
                    bg= None, relief= None, font =("arial", 10, "bold"))
        city_name.place(x= 1100, y=150)
        school_name = Label(window, text='University of Technology', fg ="black", \
                    bg= None, relief= None, font =("arial", 10, "bold"))
        school_name.place(x= 1100, y=170)

        # Chen thong tin ca nhan
        name = Label(window, text='Name: DO DUY', fg ="black", \
                    bg= None, relief= None, font =("arial", 12, "bold"))
        name.place(x= 1100, y=190)
        id_student = Label(window, text='ID: 1710772', fg ="black", \
                    bg= None, relief= None, font =("arial", 12, "bold"))
        id_student.place(x= 1100, y=210)
        year = Label(window, text='K2017', fg ="black", \
                    bg= None, relief= None, font =("arial", 12, "bold"))
        year.place(x= 1100, y=230)

        # Tao cho nhap message
        mess_encode = Label(window, text='Message encode', fg ="black", \
                    bg= None, relief= None, font =("arial", 12, "bold"))
        mess_encode.place(x= 1100, y=270)
        self.location_mess_encode = Entry(window, textvariable= self.message_encode)
        self.location_mess_encode.place(x= 1100, y= 290, width= 160, height= 30)

        # Tao cho xuat message
        mess_decode = Label(window, text='Message decode', fg ="black", \
                    bg= None, relief= None, font =("arial", 12, "bold"))
        mess_decode.place(x= 1100, y=320)
        self.location_mess_decode = Entry(window, textvariable= self.message_decode)
        self.location_mess_decode.place(x= 1100, y= 340, width= 160, height= 30)

        # Tao nut clear message
        clear_mess_button = Button(window, text= "Clear message", fg ="black", \
                    bg="white", relief=RAISED, font =("arial", 12, "bold"),\
                    command= self.clear_mess)
        clear_mess_button.place(x= 1100, y= 380)

        # Tao nut load file txt
        load_txt = Button(window, text= "Open file", fg ="black", \
                    bg="white", relief=RAISED, font =("arial", 12, "bold"),\
                    command= self.Load_file)
        load_txt.place(x= 1100, y= 440)

        # Tao cho xuat file in
        location_file_in = Entry(window, textvariable= self.txt_in)
        location_file_in.place(x= 1100, y= 480, width= 160, height= 30)

         # Tao cho xuat file out
        location_file_out = Entry(window, textvariable= self.txt_out)
        location_file_out.place(x= 1100, y= 530, width= 160, height= 30)
        
        # Chen chu tren anh input 
        label_input_image = Label(window, text='Cover Image', fg ="red", \
                    bg="yellow", relief="solid", font =("arial", 12, "bold"))
        label_input_image.place(x= 206, y=10)

        # Chen chu tren anh output
        label_output_image = Label(window, text='Steganographic', fg ="red", \
                    bg="yellow", relief="solid", font =("arial", 12, "bold"))
        label_output_image.place(x= 748, y=10)

        # Tao cho de show image input
        location_image_input = Entry(window, state= DISABLED)
        location_image_input.place(x= 10, y= 30, width= 530, height= 530)

        # Tao cho de show image output
        location_image_input = Entry(window, state= DISABLED)
        location_image_input.place(x= 552, y= 30, width= 530, height= 530)

        # Tao nut nhan load image
        load_image = Button(window, text= "Load image cover", fg ="black", \
                    bg="white", relief=RAISED, font =("arial", 12, "bold"),\
                    command= self.Load_image_encoder)
        load_image.place(x= 10, y= 570)

        # Hien thi duong dan load image
        show_path_image = Entry(window, textvariable= self.inputfileimage)
        show_path_image.place(x= 200, y= 570, width= 580, height= 30)

        # Tao nut nhan load model
        load_model = Button(window, text= "Load model", fg ="black", \
                    bg="white", relief=RAISED, font =("arial", 12, "bold"),\
                    command= self.Load_model)
        load_model.place(x= 10, y= 600)

        # Hien thi duong dan load model
        show_path_model = Entry(window, textvariable= self.inputfilemodel)
        show_path_model.place(x= 200, y= 600, width= 580, height= 30)

        # Tao nut nhan Encoder
        encoder_button = Button(window, text= "Encoder", fg ="black", \
                    bg="white", relief=RAISED, font =("arial", 16, "bold"),\
                    command= self.Encoder_Button)
        encoder_button.place(x= 100, y= 640)

        # Tao nut nhan Decoder
        decoder_button = Button(window, text= "Decoder", fg ="black", \
                    bg="white", relief=RAISED, font =("arial", 16, "bold"),\
                    command= self.Decoder_Button)
        decoder_button.place(x= 300, y= 640)

        # Tao nut nhan Evaluate
        evaluate_button = Button(window, text= "Evaluate", fg ="black", \
                    bg="white", relief=RAISED, font =("arial", 16, "bold"),\
                    command= self.Evaluate_Button)
        evaluate_button.place(x= 500, y= 640)

        # Hien thi time xu ly
        time_process = Label(window, text='Time processing', fg ="black", \
                    bg="white", relief="solid", font =("arial", 12, "bold"))
        time_process.place(x= 10, y= 690)

        # Tao nut get key
        key_button = Button(window, text= "Get Key", fg ="black", \
                    bg="white", relief=RAISED, font =("arial", 16, "bold"),\
                    command= self.Key_Button)
        key_button.place(x= 370, y= 680)

        # Tao nut enter key
        enter_key_button = Button(window, text= "Enter Key", fg ="black", \
                    bg="white", relief=RAISED, font =("arial", 16, "bold"),\
                    command= self.Enter_Key_Button)
        enter_key_button.place(x= 550, y= 680)

        # Tao cho de show time
        location_time = Entry(window, textvariable= self.timeprocess)
        location_time.place(x= 170, y= 680, width= 100, height= 30)

        # Hien thi don vi
        unit_seconds = Label(window, text='seconds', fg ="black", \
                    bg="white", relief="solid", font =("arial", 12, "bold"))
        unit_seconds.place(x= 275, y= 690)

        # Tao Accuracy
        acc_button = Label(window, text= "Accuracy", fg ="black", \
                    bg=None, relief=None, font =("arial", 16, "bold"))
        acc_button.place(x= 790, y= 570)

        # Tao reedsolomom bbp
        rsbbp_button = Label(window, text= "RS-BPP", fg ="black", \
                    bg=None, relief=None, font =("arial", 16, "bold"))
        rsbbp_button.place(x= 790, y= 605)

        # Tao psnr
        psnr_button = Label(window, text= "PSNR", fg ="black", \
                    bg=None, relief=None, font =("arial", 16, "bold"))
        psnr_button.place(x= 790, y= 640)

        # Tao ssim
        ssim_button = Label(window, text= "SSIM", fg ="black", \
                    bg=None, relief=None, font =("arial", 16, "bold"))
        ssim_button.place(x= 790, y= 675)

        # Tao cho hien thi acc
        location_acc = Entry(window, textvariable= self.accuracy_show)
        location_acc.place(x= 900, y= 570, width= 100, height= 30)

        # Tao cho hien thi rsbbp
        location_rsbbp = Entry(window, textvariable= self.reedsolomom_show)
        location_rsbbp.place(x= 900, y= 605, width= 100, height= 30)

        # Tao cho hien thi psnr
        location_psnr = Entry(window, textvariable= self.psnr_show)
        location_psnr.place(x= 900, y= 640, width= 100, height= 30)

        # Tao cho hien thi ssim
        location_ssim = Entry(window, textvariable= self.ssim_show)
        location_ssim.place(x= 900, y= 675, width= 100, height= 30)

        # Chon mode
        mode_hidden = Label(window, text='Mode to hidden:', fg ="black", \
                    bg= None, relief= None, font =("arial", 12, "bold"))
        mode_hidden.place(x= 1100, y=570)

        # Check model text
        text_button = Radiobutton(window, text="Text", variable=self.mode_var, value= "Text")
        text_button.place(x= 1095, y= 600)

        # Check model image
        image_button = Radiobutton(window, text="Image", variable=self.mode_var, value= "Image")
        image_button.place(x= 1180, y= 600)

        # Tao nut load image for hidden
        img_hidden_button = Button(window, text= "Open image", fg ="black", \
                    bg="white", relief=RAISED, font =("arial", 16, "bold"),\
                    command= self.open_image)
        img_hidden_button.place(x= 1100, y= 620)

        # Tao nut Exit thoat GUI
        exit_button = Button(window, text= "Quit", fg ="black", \
                    bg="red", relief=RAISED, font =("arial", 20, "bold"),\
                    command= self.close_window)
        exit_button.place(x= 1175, y= 670)

    def Load_file(self):

        txt_selected = filedialog.askopenfilename(title= 'Choose file ',initialdir=fullpath_work, filetypes= (("All","*.txt"),("TXT files","*.txt")))

        try:

            if os.path.exists(txt_selected):
                self.txt_in.set(os.path.basename(txt_selected))
                with open(txt_selected, 'r') as m:
                    self.mess = m.read()
                    self.status_file = True
                m.close()

        except Exception as e:

            print(e)
            tkinter.messagebox.showwarning("Notification", "Can not open file")

    def Load_image_encoder(self):

        try:

            self.image_selected = filedialog.askopenfilename(title= 'Choose image encoder',initialdir=fullpath_work, filetypes= (("All","*.png"),("PNG files","*.png")))
            self.inputfileimage.set(self.image_selected)
            # Hien thi hinh anh input

            image_input = Image.open(self.image_selected)
            image_resize = image_input.resize((512, 512))
            self.photo_input = ImageTk.PhotoImage(image_resize)
            self.lab_input = Label(image= self.photo_input)
            self.lab_input.place(x= 18, y= 38)

        except Exception as e:

            print(e)
            tkinter.messagebox.showerror("Error", "Can not open image")

    def Load_model(self):

        models_selected = filedialog.askopenfilename(title= 'Choose model',initialdir=fullpath_work, filetypes= (("All","*.steg"),("Models files","*.steg")))
        self.inputfilemodel.set(models_selected)
        try:
            self.steganogan = SteganoGAN.load(path = models_selected, cuda=False, verbose=True)
            tkinter.messagebox.showinfo("Notification", "Load model success")
        except Exception as e:
            print(e)
            tkinter.messagebox.showerror("Error", "Can not load model")


    def Encoder_Button(self):
        
        self.name_save =  str(datetime.datetime.now()).replace(" ", "@") + ".png"
        #self.name_save = self.name_save.replace(":", "#") Using this comment if you run in window OS

        self.path_img_out = os.path.join(fullpath_work, os.path.join("result/_", self.name_save))

        try:

            if len(self.mode_var.get()) == 0:
                tkinter.messagebox.showwarning("Warning", "Must select the mode using")
            
            if self.mode_var.get() == "Text":
                if not self.status_file:
                    message_encode_get = self.message_encode.get()
                else:
                    message_encode_get = self.mess
                self.len_message = len(message_encode_get)
                if self.status_key:
                    f = Fernet(self.key)
                    token = f.encrypt(message_encode_get.encode("utf-8"))
                    message_encode_get = token.decode("utf-8")
                else:
                    pass
                if self.len_message == 0:
                    tkinter.messagebox.showwarning("Warning", "Enter message")

                else:
                    start_time = time.time()
                    self.steganogan.encode(self.image_selected, self.path_img_out , message_encode_get)
                    end_time = time.time()
                    self.timeprocess.set(end_time - start_time)
                    tkinter.messagebox.showinfo("Notification", "Encoding success")
                    image_output = Image.open(self.path_img_out)
                    image_resize = image_output.resize((512, 512))
                    self.photo_output = ImageTk.PhotoImage(image_resize)
                    self.lab_output = Label(image= self.photo_output)
                    self.lab_output.place(x= 560, y= 38)

            elif self.mode_var.get() == "Image":

                if self.hidden_image:
                    name_file_out = self.client_win.get_name_txt_file()
                    with open(name_file_out, 'r') as m:
                        mess_from_img = m.read()
                    m.close()
                    print(len(mess_from_img))
                if self.status_key:
                    f = Fernet(self.key)
                    token = f.encrypt(mess_from_img.encode("utf-8"))
                    message_encode_get = token.decode("utf-8")
                else:
                    message_encode_get = mess_from_img
                start_time = time.time()
                self.steganogan.encode(self.image_selected, self.path_img_out , message_encode_get)
                end_time = time.time()
                self.timeprocess.set(end_time - start_time)
                tkinter.messagebox.showinfo("Notification", "Encoding success")
                image_output = Image.open(self.path_img_out)
                image_resize = image_output.resize((512, 512))
                self.photo_output = ImageTk.PhotoImage(image_resize)
                self.lab_output = Label(image= self.photo_output)
                self.lab_output.place(x= 560, y= 38)

            else:
                print("You do not choose hidden mode")

        except Exception as e:

            print(e)
            tkinter.messagebox.showerror("Error", "Can not encode")

    def Decoder_Button(self):

        try:
            start_time = time.time()
            message = self.steganogan.decode(self.path_img_out)
            end_time = time.time()
            if self.have_key:
          
                f = Fernet(self.get_key.encode("utf-8"))
                token = message.encode("utf-8")
                temp = f.decrypt(token)
                message = temp.decode("utf-8")
            else:
                pass

            self.timeprocess.set(end_time - start_time)

            if not self.status_file:
                self.message_decode.set(message)

            else:
                if self.hidden_image:
                    name_file_out = os.path.join("text_decode", self.name_save + ".txt")
             
                else:
                    name_file_out = os.path.join("message", self.name_save + ".txt")
                    self.txt_out.set(self.name_save + ".txt")

                with open(name_file_out, 'w') as f:
                    f.write(message)
                f.close()
            tkinter.messagebox.showinfo("Notification", "Decoding success")
        except Exception as e:
            print(e)
            tkinter.messagebox.showerror("Error", "Can not decode")

    def Evaluate_Button(self):

        METRIC_FIELDS = [
            'val.encoder_mse',
            'val.decoder_loss',
            'val.decoder_acc',
            'val.cover_score',
            'val.generated_score',
            'val.ssim',
            'val.psnr',
            'val.bpp',
            'train.encoder_mse',
            'train.decoder_loss',
            'train.decoder_acc',
            'train.cover_score',
            'train.generated_score',
            ]
        metrics = {field: list() for field in METRIC_FIELDS}
        start_time = time.time()
        validation = DataLoader(os.path.join(fullpath_work, 'result'), limit=np.inf, shuffle=True, batch_size=1)
        self.steganogan._validate(validation, metrics)
        end_time = time.time()
        self.timeprocess.set(end_time - start_time)
        acc = sum(metrics['val.decoder_acc'])/len(metrics['val.decoder_acc'])
        bpp = sum(metrics['val.bpp'])/len(metrics['val.bpp'])
        psnr = sum(metrics['val.psnr'])/len(metrics['val.psnr'])
        ssim = sum(metrics['val.ssim'])/len(metrics['val.ssim'])

        self.accuracy_show.set(acc)
        self.reedsolomom_show.set(bpp)
        self.psnr_show.set(psnr)
        self.ssim_show.set(ssim)

    def Key_Button(self):

        try:

            self.key = Fernet.generate_key()
            print("Your key: ", self.key)
            key_file_out = os.path.join("key", str(datetime.datetime.now()).replace(" ", "@") + ".txt")
            with open(key_file_out, 'w') as f:
                f.write(self.key.decode("utf-8"))
            f.close()
            tkinter.messagebox.showinfo("Notification", "Key creation was successful")
            self.status_key = True

        except Exception as e:
            print(e)

    def Enter_Key_Button(self):
        
        key_selected = filedialog.askopenfilename(title= 'Choose key',initialdir=fullpath_work, filetypes= (("All","*.txt"),("Key files","*.txt")))
        try:
            if os.path.exists(key_selected):
                with open(key_selected, 'r') as m:
                    self.get_key = m.read()
                    self.have_key = True
                m.close()
            tkinter.messagebox.showinfo("Notification", "Load key was successful")
        except Exception as e:
            print(e)
            tkinter.messagebox.showwarning("Notification", "Can not open file")

    def open_image(self):

        # Tao cua so sub GUI, init 
        subwindow = Toplevel()
        subwindow.geometry("550x660")
        self.client_win = Sub_window(subwindow)
        self.hidden_image = True

    def clear_mess(self):

        self.location_mess_encode.delete(first=0, last=self.len_message)
        self.location_mess_decode.delete(first=0, last=self.len_message)
        

    def close_window(self):
        
        window.destroy()


if __name__ == "__main__":

    fullpath_work = os.getcwd()

    # Tao cua so GUI
    window = Tk()
    window.geometry("1280x720")
    Window(window)
    window.mainloop()
    
