import os,urllib.request
from PIL import Image
import matplotlib.pyplot as plt
import io

def open_image(url):
    img = urllib.request.urlopen(url).read()
    tmpIm =io.BytesIO(img)
    im = Image.open(tmpIm)
    im.show()
    

def open_image3(file):
    img=Image.open(file)
    plt.figure("验证码")
    plt.imshow(img)
    plt.show()
    #img.save("")
    
def downs(url,strrange):
    path = "x:\\Download"
    os.chdir(path)
    os.getcwd()
    urllib.request.urlretrieve(url, "x:\\Download\\"+str(strrange)+".jpg")
    print('Pic Saved!')
if __name__=="__main__":
    file="C:\\Users\\zhang\\Pictures\\验证码\CheckCode.gif"
    url= "http://210.44.176.43/CheckCode.aspx?"
    #open_image(url)
    open_image3(file)
