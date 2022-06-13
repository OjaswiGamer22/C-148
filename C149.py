from tkinter import *
import random
root=Tk()
root.title("LUCKY FRIEND")
root.geometry("500x500")
friend_list=["ajay","akshay","tanmay","adityavardhan","dharmani"]
def luckyfriend():
    random_number=random.randint(0,4)
    lf=friend_list[random_number]
    print("Your lucky friend is: "+lf)
button1=Button(root, text="who is your lucky friend",command=luckyfriend)
button1.place(relx=0.5,rely=0.4,anchor=CENTER)
root.mainloop()


