from PIL import Image, ImageFont, ImageDraw
import numpy as np
import matplotlib.pyplot as plt

'''打开图片'''
img_path = 'e:/cx.jpg'
img = Image.open(img_path)
# img.show()

# plt.figure('cx')
# plt.figure(num=1, figsize=(8,5))
# plt.title('cxxxx')
# plt.axis('off')
# plt.imshow(img)
# plt.show()

# '''属性'''
# print('size    :' ,img.size )
# print('mode    :', img.mode)
# print('format  :', img.format)
# print('pixel   :', img.getpixel((0,0))[0])
# '''
# size    : (1229, 1683)
# mode    : RGB
# format  : JPEG
# '''

# '''灰度图'''
# img_gray = img.convert('L')
# plt.imshow(img_gray, cmap='gray')
# plt.show()
# '''
# 使用函数convert()来进行转换，它是图像实例对象的一个方法，接受一个 mode 参数，
# 用以指定一种色彩模式，mode 的取值可以是如下几种：
# · 1 (1-bit pixels, black and white, stored with one pixel per byte)
# · L (8-bit pixels, black and white)
# · P (8-bit pixels, mapped to any other mode using a colour palette)
# · RGB (3x8-bit pixels, true colour)
# · RGBA (4x8-bit pixels, true colour with transparency mask)
# · CMYK (4x8-bit pixels, colour separation)
# · YCbCr (3x8-bit pixels, colour video format)
# · I (32-bit signed integer pixels)
# · F (32-bit floating point pixels)
# '''


# '''裁剪roi（感兴趣区域)'''
# w, h = img.size
# box = (w*0.2, h*0.2, w*0.8, h*0.8)
# roi = img.crop(box)
# plt.imshow(roi)
# plt.show()


# '''缩放'''

# sf_img = img.resize((int(w*0.75), int(h*0.75)))
# plt.imshow(sf_img)
# plt.show()


# '''旋转'''
# rot_img = img.rotate(45)
# plt.imshow(rot_img)
# plt.show()

# '''变换'''
# trans1 = img.transpose(Image.FLIP_LEFT_RIGHT)
# trans2 = img.transpose(Image.FLIP_TOP_BOTTOM)
# trans3 = img.transpose(Image.ROTATE_90)
# plt.subplot(131)
# plt.imshow(trans1)
# plt.subplot(132)
# plt.imshow(trans2)
# plt.subplot(133)
# plt.imshow(trans3)
# plt.show()

# '''层叠图片'''
# Image.blend(img1, img2, alpha)  
# composite可以使用另外一个图片作为蒙板(mask)，
# 所有的这三张图片必须具备相同的尺寸，
# mask图片的模式可以为“1”，“L”，“RGBA”
# Image.composite(img1, img2, mask) 

'''添加文字水印'''
im = img.convert('RGBA')
txt = Image.new('RGBA',im.size,(0,0,0,0))
font = ImageFont.truetype('arial.ttf', 40)
draw = ImageDraw.Draw(txt)
draw.text((txt.size[0]-300,txt.size[1]-50), "cnBlogs",
    font=font, fill=(255,255,255,255))
out = Image.alpha_composite(im, txt)
# out.show()

'''添加图片水印'''
mark = Image.open('E:/PHOTO/Snipaste_2018-04-07_20-21-22.png')
mark = mark.resize((200, 200))
layer=Image.new('RGBA', img.size, (0,0,0,0))
layer.paste(mark, (img.size[0]-250,50))
out = Image.composite(layer, img, layer)
# out.show()


'''IMG转numpy'''
im_array = np.array(img)
print(im_array.shape)
print(im_array.dtype)
im = Image.fromarray(np.uint8(im_array))
im.show()
