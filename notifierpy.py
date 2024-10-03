from tkinter import *
from plyer import notification
from tkinter import messagebox
from PIL import Image, ImageTk # type: ignore
import time

t = Tk()
t.title('Remainder')
t.geometry("500x300")
img = Image.open("logo.png")
tkimage = ImageTk.PhotoImage(img)

# get details
def get_details():
    get_title = title.get()
    get_msg = msg.get()
    get_time = time1.get()
    get_time2 = time2.get()

    if get_time == '':
        get_time = 0
    else :
        if get_time2 == '':
            get_time2 = 0
    if get_title == "" or get_msg == "" or get_time2== "":
        messagebox.showerror("Alert", "All fields are required!")
    else:
        int_time = int(get_time)
        int_time2 = int(get_time2)
        min_to_sec = int_time * 60
        secoo = int_time2 + min_to_sec
        t.destroy()
        time.sleep(secoo)

        notification.notify(title=get_title,
                            message=get_msg,
                            app_name="Remainder",
                            app_icon="ico.ico",
                            toast=True,
                            timeout=10)

img_label = Label(t, image=tkimage).grid()

# Label - Title
t_label = Label(t, text="Title",font=("poppins", 10))
t_label.place(x=12, y=70)

# ENTRY - Title
title = Entry(t, width="25",font=("poppins", 13))
title.place(x=123, y=70)

# Label - Message
m_label = Label(t, text="Enter Message", font=("poppins", 10))
m_label.place(x=12, y=120)

# ENTRY - Message
msg = Entry(t, width="40", font=("poppins", 13))
msg.place(x=123,height=30, y=120)

# Label - Time
time_label = Label(t, text="Time To Remind In", font=("poppins", 10))
time_label.place(x=12, y=175)

# ENTRY - Time
time1 = Entry(t, width="5", font=("poppins", 13))
time1.place(x=130, y=175)

# Label - min
time_min_label = Label(t, text="min", font=("poppins", 10))
time_min_label.place(x=180, y=175) 

# ENTRY - Time
time2 = Entry(t, width="5", font=("poppins", 13))
time2.place(x=210, y=175)

# Label - min
time_sec_label = Label(t, text="sec", font=("poppins", 10))
time_sec_label.place(x=260, y=175) 

# Button
but = Button(t, text="Remind", font=("times new roman", 14, "bold"), fg="#ffffff", bg="#528DFF", width=20,
             relief="raised",
             command=
             get_details)
but.place(x=170, y=220)

t.resizable(0,0)
t.mainloop()

