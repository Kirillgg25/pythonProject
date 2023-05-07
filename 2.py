from tkinter import*
vikno_1 = Tk()
vikno_1.title("Home")
vikno_1.geometry('1920x1080')
vikno_1['bg'] = 'yellow'
knp_1 = Button(text="Quit", fg = 'red', bg = 'blue')
knp_1.pack()
knp_1.place(x = '1890', y = '0')
vikno_1.mainloop()