#tutorial from codemy.com
from tkinter import *
from random import  randint

root=Tk()
root.title("Ogedmund.com - Strong Password Generator")
root.iconbitmap("c:/Users/hp/Desktop/Cyber_projects")
root.geometry("500x300")


#random strong password
def new_rand():
    #Clear the entry box
    pw_entry.delete(0,END)
    #Get Pw Length and convert to integer
    pw_length = int(my_entry.get())
    #create a variable to hold the password length
    my_password=""
    #Loop through password length
    for x in range(pw_length):
        my_password += chr(randint(33,126))#33 to 126 is the range of ASCII characters used.. check asci website
    #output password to the screen
    pw_entry.insert(0, my_password)

#Copy to clipboard
def clipper():
    #clear the clipboard
    root.clipboard_clear()
    #copy the clipboard
    root.clipboard_append(pw_entry.get())


#Label Frame
lf= LabelFrame(root, text="How many characters?")
lf.pack(pady=20)

#Create Entry Box To Designate Number of Characters
my_entry = Entry(lf, font=("Helvetica", 24))
my_entry.pack(pady=20, padx=20)

#Create Entry Box For Our Returned Password
pw_entry = Entry(root, text = "", font=("Helvitica", 24), bd=0, bg="systembuttonface")
pw_entry.pack(pady=20)

#Create a frame for our Buttons
my_frame = Frame(root)
my_frame.pack(pady=20)

#Create a button
my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=10)

clip_button= Button(my_frame, text="Copy to CLipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)


root.mainloop()