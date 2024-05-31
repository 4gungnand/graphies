from math import cos, sin, pi
from PIL import Image, ImageDraw

# Definisikan window dan viewport
xwmin = -3
xwmax = 3
ywmin = 0
ywmax = 7.5
xvmin = 0
xvmax = 500
yvmin = 0
yvmax = 625

# Definisikan parameter transformasi
alpa = 10
beta = -50
gamma = 40

# Definisikan jumlah iterasi
numit = 10

# Definisikan matriks transformasi
a,b,c,d,e,f = [0]*5,[0]*5,[0]*5,[0]*5,[0]*5,[0]*5

# ranting bawah
a[1]=1
b[1]=0
c[1]=0
d[1]=1
e[1]=0
f[1]=0

# ranting atas
a[2]=0.65*cos(alpa*pi/180)
b[2]=-0.65*sin(alpa*pi/180)
c[2]=0.65*sin(alpa*pi/180)
d[2]=0.65*cos(alpa*pi/180)
e[2]=0.85
f[2]=0.2

# ranting kiri
a[3]=0.5*cos(beta*pi/180)
b[3]=-0.5*sin(beta*pi/180)
c[3]=0.5*sin(beta*pi/180)
d[3]=0.5*cos(beta*pi/180)
e[3]=-2.9
f[3]=2.8

# ranting kanan
a[4]=0.5*cos(gamma*pi/180)
b[4]=-0.5*sin(gamma*pi/180)
c[4]=0.5*sin(gamma*pi/180)
d[4]=0.5*cos(gamma*pi/180)
e[4]=2.4
f[4]=2.7


# Definisikan fungsi untuk transformasi window ke viewport

def Vw(xv, yv):
    xw = xwmin + (xv - xvmin) * (xwmax - xwmin) / (xvmax - xvmin)
    yw = ywmin + (yv - yvmin) * (ywmax - ywmin) / (yvmax - yvmin)
    return xw, yw

def Wv(xw, yw):
    xv = xvmin + round((xw - xwmin) * (xvmax - xvmin) / (xwmax - xwmin))
    yv = yvmin + round((yw - ywmin) * (yvmax - yvmin) / (ywmax - ywmin))
    return xv, yv


# Definisikan image dan image draw
img = Image.new("RGB", (xvmax - xvmin, yvmax - yvmin), "white")
img_draw = ImageDraw.Draw(img)

# Gambar bentuk pohon mula-mula
img_draw.polygon([(xvmax // 2 - 7, yvmax - 2), (xvmax // 2 - 5, 415),
                 (xvmax // 2 + 5, 415), (xvmax // 2 + 7, yvmax - 2)], fill=(90, 39, 41))

# Lakukan transformasi fractal terhadap pohon
for i in range(numit):
    new_img = Image.new("RGB", (xvmax - xvmin, yvmax - yvmin), "white")
    new_draw = ImageDraw.Draw(new_img)
    for xv in range(xvmin, xvmax):
        for yv in range(yvmin, yvmax):
            if img.getpixel((xv, yv)) != (255, 255, 255):
                xw, yw = Vw(xv, yv)        

                # ranting bawah
                xp, yp = ((a[1]*xw + b[1]*yw + e[1]),
                        (c[1]*xw + d[1]*yw + f[1]))
                new_xv, new_yv = Wv(xp, yp)
                new_draw.point((new_xv, new_yv), fill=(90, 39, 41))
            
                # ranting atas
                xp, yp = ((a[2]*xw + b[2]*yw + e[2]),
                        (c[2]*xw + d[2]*yw + f[2]))
                new_xv, new_yv = Wv(xp, yp)
                new_draw.point((new_xv, new_yv), fill=(255, 183, 197))

                # ranting kiri
                xp, yp = ((a[3]*xw + b[3]*yw + e[3]),
                        (c[3]*xw + d[3]*yw + f[3]))
                new_xv, new_yv = Wv(xp, yp)
                new_draw.point((new_xv, new_yv), fill=(255, 183, 197))

                # ranting kanan
                xp, yp = ((a[4]*xw + b[4]*yw + e[4]),
                        (c[4]*xw + d[4]*yw + f[4]))
                new_xv, new_yv = Wv(xp, yp)
                new_draw.point((new_xv, new_yv), fill=(255, 183, 197))

    img = new_img

# Program akan menghasilkan gambar PNG berupa pohon fractal
img.show()
