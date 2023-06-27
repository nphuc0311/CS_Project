#Tkinter Color GUI Button Click & Exit

from tkinter import * #imports all of the tkinter module


window = Tk() #call tkinter function to create a tkinter window // create GUI window // window is the named given to the GUI: name is needed for attributes
window.title("App") #Title of the Message Window // Will appear on the Top // title widget
window.geometry('475x75') #Defines the width, height and coordinates of the top left corner of the frame as below in pixels | (width x height + XPOS + YPOS) //geometry widget
window.configure(bg='#000000', highlightbackground='#000000') #Defines bg=background | highlightbackground=Defines background of the whole window //configuration widget


button_1 = Button(window, text='Goku - SuperSaiyan', command=window.destroy, fg='black', bg='yellow', height=3, width=20, padx=5, pady=5).pack(side=LEFT) #create a button 
button_2 = Button(window, text='ANBU', command=window.destroy, fg='black', bg='white', height=3, width=20, padx=5, pady=5).pack(side=LEFT) #create a button
button_3 = Button(window, text='Sharingan', command=window.destroy, fg='black', bg='red', height=3, width=20, padx=5, pady=5).pack(side=LEFT) #create a button


window.mainloop() #event listening loop // it waits for other events such as radio buttons et al // will close on x // main loop widget // needed for the GUI to pop-up
