import cv2
import numpy as np
import webcolors
import urllib.request
import time

url='http://192.168.1.55/cam-lo.jpg'

cv2.namedWindow("Input")

def detect_color(image):
    # Resize the image to a smaller size for faster processing
    pixels = cv2.resize(image, (100, 100))

    # Reshape the image to a list of pixels
    #pixels = pixels.reshape(-1, 30)

    # Convert the pixels from BGR to HSV
    pixels = cv2.cvtColor(pixels, cv2.COLOR_BGR2HSV)
    #print(pixels[0][0])

    # Convert the RGB pixel values to web colors
    web_colors = []
    for row in pixels:
        for pixel in row:
            h, s, v = pixel[0], pixel[1], pixel[2]
            h = (h/255)*360-20
            #print(h)
            #web_color = webcolors.rgb_to_name((h, s, v), spec=u'html4')
            #web_colors.append(web_color)
            if h>=0 and h<20:
                web_color = "red"
                web_colors.append(web_color)
            elif h>=20 and h<40:
                web_color = "orange"
                web_colors.append(web_color)
            elif h>=40 and h<70:
                web_color = "yellow"
                web_colors.append(web_color)
            elif h>=70 and h<155:
                web_color = "green"
                web_colors.append(web_color)
            elif h>=155 and h<210:
                web_color = "blue"
                web_colors.append(web_color)
            elif h>=210 and h<260:
                web_color = "dark blue"
                web_colors.append(web_color)
            elif h>=260 and h<285:
                web_color = "violet"
                web_colors.append(web_color)
            elif h>=285 and h<330:
                web_color = "pink"
                web_colors.append(web_color)
            elif h>=330 and h<360:
                web_color = "red"
                web_colors.append(web_color)
            else:
                pass

    # Count the occurrences of each color
    color_counts = {}
    for color in web_colors:
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1

    # Get the dominant color
    dominant_color = max(color_counts, key=color_counts.get)

    return dominant_color
while True:
    
    # Load the image
    img_resp=urllib.request.urlopen(url)
    imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
    frame=cv2.imdecode(imgnp,-1)

    # Detect the dominant color
    dominant_color = detect_color(frame)
    cv2.imshow("Input", frame)
    
    print("Dominant color:", dominant_color)
    key=cv2.waitKey(5)
    if key==ord('q'):
        break
cv2.destroyAllWindows()
    
