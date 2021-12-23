from tkinter import *
from tkinter import messagebox
import pytube

window = Tk()

# define size screen 
widht = 500
height = 300

# define title 
window.title('Youtube Downloader')

# get resolution of screen 
widht_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()

# where put label in center
pos_x = widht_screen/2 - widht
pos_y = height_screen/2 - height

window.geometry("%dx%d+%d+%d" % (widht, height, pos_x, pos_y))

# define title 
label_title = Label(window, text="Insira o link do video:", font="serif 20 bold")
label_title.pack(pady=20)

# get youtube link
get_link = Entry(window, width=40)
get_link.pack()

# function that make download of link  
def Download_video():
    link = get_link.get()
    if link == "": 
        messagebox.showinfo("Link invalido", "Por favor digite um link valido!")
    else:
        youtube = pytube.YouTube(link)
        video = youtube.streams.first()
        video = youtube.streams.get_highest_resolution()
        video.download()


# Download button
download_btn = Button(window, bd=5, relief="raised", text="Download", command=lambda: Download_video(), width=20, pady=5)
download_btn.pack(pady=50)




window.mainloop()