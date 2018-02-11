import itchat
import PIL.Image as image
import math
import os

current_path = (os.path.dirname(os.path.abspath(__file__)))
if not os.path.exists(current_path+'/images'):
    os.makedirs(current_path+'/images')
itchat.auto_login(hotReload=True)
friends = itchat.get_friends(update=True)
i = 0
for friend in friends:
    img = itchat.get_head_img(userName=friend['UserName'])
    with open('./images/' + str(i) + ".jpg", "wb") as img_file:
        img_file.write(img)
        i += 1



# number of pics in one side
num_in_side = int(math.sqrt(i))
# total number of pics
total_num = num_in_side ** 2
# small images side length
each_side_length = int(float(1200 / num_in_side))

to_image = image.new('RGB', (1200, 1200))
x = 0
y = 0
for j in range(i):
    if total_num == i:
        break
    if j == total_num:
        break
    try:
        img = image.open('./images/' + str(j) + '.jpg')
    except IOError:
        print(IOError)
        total_num += 1
    else:
        # resize pics
        img = img.resize((each_side_length, each_side_length), image.ANTIALIAS)
        to_image.paste(img, (x * each_side_length, y * each_side_length))
        x += 1
        if x == num_in_side:
            x = 0
            y += 1

to_image.save("profile_combination.jpg")
itchat.send_image("profile_combination.jpg", "filehelper")

