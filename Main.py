import cv2
import os
import PIL
from PIL import ImageTk
import PIL.Image
import tkinter as tk

ActivityScreen = tk.Tk()
ActivityScreen.title('ASL')
figure_x, figure_y = 64, 64
# Add image file
figure = tk.PhotoImage(file="backg_img.png")
label = tk.Label(
    ActivityScreen,
    image=figure
)
label.place(x=0, y=0)


def check_word(i, file_map):
    for item in file_map:
        for word in file_map[item]:
            if i == word:
                return 1, item
    return -1, ""


# set your path
open_filtered = "C:\\Users\\dell\\PycharmProjects\\Dialog 5 and 6\\gifs\\"
alpha_destination = "C:\\Users\\dell\\PycharmProjects\\Dialog 5 and 6\\letters\\"

directory_open = os.listdir(open_filtered)
update_data = []
for item in directory_open:
    if ".webp" in item:
        update_data.append(item)

file_map = {}
for i in update_data:
    tmp = i.replace(".webp", "")
    # print(tmp)
    tmp = tmp.split()
    file_map[i] = tmp


def word_split_func(a):
    all_frames = []
    final = PIL.Image.new('RGB', (380, 260))
    print("answer : ",a)
    words = a.split()
    for i in words:
        flag, word = check_word(i, file_map)
        if flag == -1:
            for j in i:
                if j == '?' or j == ',' or j == '.' or j == "'" or j == '!' or j == '’' or j == '(' or j == ')'or j=='…':
                    continue
                print(j)
                im = PIL.Image.open(alpha_destination + str(j).lower() + ".gif")
                frameCnt = im.n_frames
                for frame_cnt in range(frameCnt):
                    im.seek(frame_cnt)
                    im.save("temporary.png")
                    figure = cv2.imread("temporary.png")
                    figure = cv2.cvtColor(figure, cv2.COLOR_BGR2RGB)
                    figure = cv2.resize(figure, (380, 260))
                    im_arr = PIL.Image.fromarray(figure)
                    for itr in range(15):
                        all_frames.append(im_arr)
        else:
            print(word)
            im = PIL.Image.open(open_filtered + word)
            im.info.pop('background', None)
            im.save('temporary.gif', 'gif', save_all=True)
            im = PIL.Image.open("temporary.gif")
            frameCnt = im.n_frames
            for frame_cnt in range(frameCnt):
                im.seek(frame_cnt)
                im.save("temporary.png")
                figure = cv2.imread("temporary.png")
                figure = cv2.cvtColor(figure, cv2.COLOR_BGR2RGB)
                figure = cv2.resize(figure, (380, 260))
                im_arr = PIL.Image.fromarray(figure)
                all_frames.append(im_arr)
    final.save("def.gif", save_all=True, append_images=all_frames, duration=100, loop=0)
    return all_frames


figure_counter = 0
figure_text = ''

cnt = 0
gif_frames = []
input_user = None
tk.Frame()

gif_box = tk.Label(ActivityScreen)


def gif_stream():
    global cnt
    global gif_frames
    if cnt == len(gif_frames):
        return
    figure = gif_frames[cnt]
    cnt += 1
    figuretk = ImageTk.PhotoImage(image=figure)
    gif_box.figuretk = figuretk
    gif_box.configure(image=figuretk)
    gif_box.after(50, gif_stream)


def Take_input():
    INPUT = input_user.get("1.0", "end-1c")
    print(INPUT)
    global gif_frames
    x=0

    if INPUT == "What time is it?":
        answer= "It’s a quarter to five."
    elif INPUT == "Aren’t we supposed to be at Jim’s house by five o’clock?":
        answer ="Five or fivethirty. He said it didn’t make any difference."
    elif INPUT == "Then maybe we could pick your suit up at the cleaners.":
        answer = "Sure, we have plenty of time."
    elif INPUT == "Hello.":
        answer = "Hello . May I speak to Alice Weaver, please?"
    elif INPUT == "Just a minute… Alice, it’s for you.":
        answer = "Hello."
    elif INPUT == "Hi, Alice. This is Fred. Would you like to go to a movie tonight?":
        answer = "Thanks, I’d love to. I haven’t been to a movie for a long time."
    elif INPUT == "Good. I’ll pick you up around seventhirty, then. The movie starts at eight.":
        answer = "Fine, I’ll be ready."
    else:
        x=1
        gif_frames =word_split_func(INPUT)
    if(x!=1):
        gif_frames = word_split_func(answer)
    global cnt
    cnt = 0
    gif_stream()
    gif_box.place(x=450, y=240)


l = tk.Label(ActivityScreen, text="Enter Sentence :", bg='#325C7F', width=40)
input_user = tk.Text(ActivityScreen, height=7, width=35)
l.place(x=30, y=40)
input_user.place(x=30, y=60)

convert_btn = tk.PhotoImage(file="convert.png")
img = tk.Button(ActivityScreen, image=convert_btn ,width=120,height=120, command=lambda: Take_input(), borderwidth=0)
img.place(x=430, y=40)

ActivityScreen.resizable(False, False)
ActivityScreen.geometry("800x530")
ActivityScreen.mainloop()
