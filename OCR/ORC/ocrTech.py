# 图文识字
import pytesseract
import re
from PIL import Image
from googletrans import Translator


def translator(txt):
    # 设置Google翻译服务地址
    translator = Translator(service_urls=[
        'translate.google.cn'
    ])

    translation = translator.translate(txt, dest='zh-CN')
    return translation.text


def imageToStr(image_url, lang):
    im = Image.open(image_url)
    im = im.convert('L')
    im_str = pytesseract.image_to_string(im, lang=lang)
    return im_str


img_url = r'P.jpg'

# img_str = imageToStr(img_url, 'eng')
# print('识别到的英文', img_str)
result = []
print('识别到的中文')
cn_img_str = imageToStr(img_url, 'chi_sim')
cn_img_str = re.sub('[\u4e00-\u9fa5]', '', cn_img_str)  # 去除字符串之中的中文

cn_img_str = re.sub(r'[0-9]+', '', cn_img_str)
cn_img_str = re.sub(r'[-]+', '', cn_img_str)
result.append(cn_img_str)
print(result)
# print(translator(cn_img_str))
str = result[0]
str = re.sub(r'[\n]+', ',', str)
print(str)
my_list = str.split(",")
print(my_list)
my_list = [i for i in my_list if i != ""]

for i in range(len(my_list)):
    print(translator(my_list[i]))
    my_list[i] = my_list[i] + '-' + translator(my_list[i])
print(my_list)
print(len(my_list))
