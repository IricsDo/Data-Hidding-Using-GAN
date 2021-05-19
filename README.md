# ***DATA HIDDING USING GAN***
*Note: My English is bab, so if i using some wrong word or wrong grammar, please ignore.*

This is my graduation essay.
I have two document guide for this. One in *README.md* (this file you are reading) writing by English and *Vietnamese.md* writing by Vietnamese. 

This project base on [paper](https://arxiv.org/pdf/1901.03892.pdf) and [source code](https://github.com/DAI-Lab/SteganoGAN). All copy need to follow above quote!

# I. SUMMARY

After reviewing the [source code](https://github.com/DAI-Lab/SteganoGAN), I decided to build an interface for users to manipulate more intuitively.

*The whole project is doing on linux operating system - Ubuntu 18.04, hardware configuration is Intel i5 8th Gen CPU, 12G RAM. GeForce MX 130 GPU, 2G RAM.*

# II. GUIDE TO USE INTERFACE

The interface is written by the Tkinter library.

## 1. Set up environment

The environment use in the project was created by Anaconda. You can download and install it at the link [anaconda](https://www.anaconda.com/products/individual)

	$ cd Data-Hidding-Using-GAN/
	$ conda create -n myenv python=3.6
	$ conda activate myenv
	$ pip install -r requirement.txt

## 2. Change working path

~~In file main.py at line 471 replace path to SteganoGAN ( fullpath_work ) by the path where you download my project.~~

~~In file second_window.py at line 19 relace path to SteganoGAN ( fullpath_work ) by the path where you download my project.~~

***New update !!*** Not need do that. 

## 3. How to use the interface

Run the following command in the downloaded folder

    $ python3 main.py

You will see the interface like this

![This is the main window you see](/images/2.png)

The interface includes the following function buttons and how it work:

+ Load image cover: Select the image you want to hide information on it. The direct path of the image will be displayed next to.

	- Images will be saved by default in folder path **../Data-Hidding-Using-GAN/research/**

	- Images will be display under text: *Cover Image*
	
+ Load model: Select the model you want use for hide. The direct path of the image will be displayed next to.

	- Default all my pre-train model will be save in folder path **../Data-Hidding-Using-GAN/models/**

+ Encoder: Doing hide with selected images and models.

	- The images after embedding information will display under text: *Steganographic*

	- And will be save in folder path **../Data-Hidding-Using-GAN/result/-/**

+ Evalute: Doing evalution with images was emdedded. The parameter include:

	- Accuracy - This is accuracy of the model you use.
	
	- RS-BPP   - This is number of bit you can hide in one pixel
	
	- PSNR     - This is signal divided noise 

	- SSIM     - The structural similarity index measure

+ Get Key: This is an optional mode, when pressed the information will be encrypted before hiding.

+ Enter Key: This button is required if the user has pressed Get Key above, the user will have to select the generated key through the Get Key button, enter the key, the information after decryption will be correct, otherwise the information can not readable.

	- The key file will be save in folder path **../Data-Hidding-Using-GAN/key/**

Below Message encode is place to enter the information to be hidden (text).
Below Message decode is where the decoded information will be displayed.
+ Clear message: When pressing all text below Message encode and Message decode will be deleted.
+ Open file: Doing hide a file with format txt

	- The first empty place below is where the path to the txt file you want to hide is displayed.

	- The second empty place will be the place to display the path to the decoded txt file.

	- The txt file will save default in folder path **../Data-Hidding-Using-GAN/message/**

There are two options for hiding information for users: Hiding information as text or hiding information as images. Click to select the user mode you want to use.

Select hide text mode to use keyboard input functions or open from a txt file.

When selecting image hiding mode, before pressing the Encoder button, you need to:

Click Open image: A second interface like the following appears

![This is the second window you see](/images/1.png)

In this interface there are the following buttons:
+ Open image: Select the image you want to hide. The direct path of the image will be displayed next to.
+ Open text: Make a selection of the txt file, that is the image in text format. The direct path of the image will be displayed next to.
+ Im2Tex: Doing convert image to text format.

	- File text after converting from images will be saved in a folder with path **../Data-Hidding-Using-GAN/text_decode/**

+ Tex2Im: Doing convert text to images format.

	- The image after converting from text file will be saved in a folder with path **../Data-Hidding-Using-GAN/image_decode/**

If the user accidentally presses exit this second window, before the user do the text-to-image conversion, the user needs to enter the size of the image to be restored with the following format:
> w:{width} h:{height}
> 
> Note: In the middle is a space, example w:12 h:12 or w:128 h:128
> 
then press the Tex2Im button.

# III. RESTRICTION

According to the article, the model that gives the best results is Dense Encoder. However, because my hardware is not ***"strong"***, I can only run Basic Encoder models so some of the results of the Enconder images I gave you are not good quality.

The pre-train models you see in the models folder are because I used Google Colab Pro to train. But most of them only train with a few iterations, so the model is not optimal. You can not use these models of mine, but train other models better yourself. You can see how to train at the [original source] (https://github.com/DAI-Lab/SteganoGAN).

Or you can use the pre-train models that the author provides, including 3 types: Basic, Dense and Residual. Trained with data_deep = 6 (The theoretical number of bits per pixel).

**Citing SteganoGAN**

If you use SteganoGAN for your research, please consider citing the following work:

Zhang, Kevin Alex and Cuesta-Infante, Alfredo and Veeramachaneni, Kalyan. SteganoGAN: High Capacity Image Steganography with GANs. MIT EECS, January 2019. ([PDF](https://arxiv.org/pdf/1901.03892.pdf))

> @article{zhang2019steganogan,
> 
> title={SteganoGAN: High Capacity Image Steganography with GANs},
> 
> author={Zhang, Kevin Alex and Cuesta-Infante, Alfredo and Veeramachaneni, Kalyan},
> 
> journal={arXiv preprint arXiv:1901.03892},
> 
> year={2019},
> 
> url={ https://arxiv.org/abs/1901.03892 }
> 
> }
> 
