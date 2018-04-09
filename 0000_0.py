from PIL import Image, ImageDraw, ImageFont
import os

class Draw_num():
    def __init__(self, pic_path, num):
        self.pic_path = pic_path
        self.pic = Image.open(pic_path)
        self.num = num

    def draw(self):
        w, h = self.pic.size
        draw = ImageDraw.Draw(self.pic)
        font = ImageFont.truetype('arial.ttf', min(w // 6, h // 6))
        fillColor = "#ff0000"
        draw.text((w*0.75, h*0.075), str(self.num), font=font, fill=fillColor)
        
        basename = os.path.basename(self.pic_path)
        newname = basename.split('.')[0] + '_' + str(self.num) +'.'+ basename.split('.')[1]
        new_path = os.path.join(os.path.dirname(self.pic_path), newname)
        print(new_path)
        
        self.pic.save(new_path)
        print('Save to new path {}'.format(new_path))

if __name__ == '__main__':
    d = Draw_num('E:/cx.jpg',6)
    d.draw()