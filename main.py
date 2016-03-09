# -*- coding: utf-8 -*-
'''
File Name: main.py
Author: JackeyGao
mail: junqi.gao@shuyun.com
Created Time: 二  3/ 8 13:36:53 2016
'''
import sys, commands

try:
    from PIL import Image,ImageDraw,ImageFont
except ImportError:
    sys.stdout.write('错误: 没有安装Pillow,使用pip install Pillow安装\n')
    sys.exit(255)

def group_list(list,block):
    size = len(list)
    return [ list[i:i+block] for i in range(0,size,block) ]

def usage(error_code=1):
    sys.stderr.write('Usage: \n\tpython {0} $text'
        '\nExample: \n\tpython {0} "哈哈"\n'.format(sys.argv[0]))
    sys.exit(error_code)
    

if __name__ == '__main__':
    try:
        string = sys.argv[1]
        string = string.decode('utf-8')
    except IndexError as e:
        usage()
    except Exception as e:
        usage(error_code=255)

    # set var
    font_size = 100
    raw_f_number = 8
    draw_x = font_size * raw_f_number + 20
    draw_y = font_size * raw_f_number + 20

    # building a draw
    font = ImageFont.truetype('simsun.ttc', font_size)
    img = Image.new('RGB', (draw_x, draw_y), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    groups = group_list(list(string), raw_f_number)

    # insert text to draw and save to jpg.
    if len(groups) == 1:
        s = groups[0]
        x, y = len(s) * font_size, font_size + 10
        draw.text((10,0), ''.join(s),(0,0,0),font=font)
    else:
        x, y = draw_x, 0
        for s in groups:
            draw.text((10,y), ''.join(s),(0,0,0),font=font)
            y += 110

    crop = (0, 0, x, y)
    img = img.crop(crop)
    img.save('text.jpg', 'JPEG')

    # copy to clipboard
    commands.getstatusoutput('./impbpaste text.jpg')
    print("已复制到剪切板.")
