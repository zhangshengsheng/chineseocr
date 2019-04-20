# -*- coding: utf-8 -*-

def saveimage(partImg,text,newW,newH):
    partImg.save("/media/zs/CAE6A962E6A9500D/trainimage/" + str(text).replace("/","") + str(int(newW)) + str(int(newH)) + ".jpg")
    with open("/media/zs/CAE6A962E6A9500D/trainimage/" + str(text).replace("/","") + str(int(newW)) + str(int(newH)) + ".txt", "w",
              encoding='utf-8') as f:
        f.write(str(text))