import cv2
import numpy as np
import webcolors
import urllib.request
import time

url='http://192.168.1.55/cam-lo.jpg'

cv2.namedWindow("Config")
cv2.namedWindow("Changed")

def store_color(image):
    # Resize the image to a smaller size for faster processing
    pixels = cv2.resize(image, (320, 240))

    # Convert the pixels from BGR to HSV
    pixels = cv2.cvtColor(pixels, cv2.COLOR_BGR2HSV)
    #print(pixels[0][0])

    return pixels

def dominant_color(image):
    changedPixels = []
    threshold = 10
    for i in range(len(config_color)):
        for j in range(len(config_color[i])):
            if change_color[i][j][0] > config_color[i][j][0] + threshold or change_color[i][j][0] < config_color[i][j][0] - threshold:
                changedPixels.append(change_color[i][j])
            if len(changedPixels) > 200:
                web_colors = []
                for pixel in changedPixels:
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

                    color_counts = {}
                    for color in web_colors:
                        if color in color_counts:
                            color_counts[color] += 1
                        else:
                            color_counts[color] = 1

                    # Get the dominant color
                    dominant_color = max(color_counts, key=color_counts.get)
                    return dominant_color

# Load the image
img_resp=urllib.request.urlopen(url)
imgnp=np.array(bytearray(img_resp.read()),dtype=np.uint8)
frame=cv2.imdecode(imgnp,-1)
cv2.imshow("Config", frame)
while True:
    user_input = input("Do you want to configure the frame now? (y/n): ")
    if user_input == "y":
        # Configure the color
        config_color = store_color(frame)
        user_input2 = input("Do you want to check for changes? (y/n) [Enter x to configure again]: ")
        if user_input2 == "y":
            # Check for changes
            change_color = store_color(frame)
            cv2.imshow("Changed", frame)
            domColor = dominant_color(config_color)
            cont = input("Do you want to continue? (y/n): ")
            if cont == "y":
                continue
            else:
                break
        elif user_input2 == "x" or user_input2 == "n":
            continue
    elif user_input == "n":
        continue

cv2.destroyAllWindows()
    
