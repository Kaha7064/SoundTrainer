from tkinter import *
from PIL import ImageTk, Image

count = 0

def click():
    global count
    count+=1
    label.config(text=count)
    #label2.pack()

window = Tk()
#window.grid_columnconfigure(0, weight=1, uniform="fred")

#image = PhotoImage(file='images/jett.jpg')
play = ImageTk.PhotoImage(Image.open("images/play.png").resize((100, 100), Image.ANTIALIAS))
astra = ImageTk.PhotoImage(Image.open("images/astra.jpg").resize((100, 100), Image.ANTIALIAS))
breach = ImageTk.PhotoImage(Image.open("images/breach.jpg").resize((100, 100), Image.ANTIALIAS))
brim = ImageTk.PhotoImage(Image.open("images/brim.jpg").resize((100, 100), Image.ANTIALIAS))
chamber = ImageTk.PhotoImage(Image.open("images/chamber.jpg").resize((100, 100), Image.ANTIALIAS))
cypher = ImageTk.PhotoImage(Image.open("images/cypher.jpg").resize((100, 100), Image.ANTIALIAS))
fade = ImageTk.PhotoImage(Image.open("images/fade.jpg").resize((100, 100), Image.ANTIALIAS))
jett = ImageTk.PhotoImage(Image.open("images/jett.jpg").resize((100, 100), Image.ANTIALIAS))
kayo = ImageTk.PhotoImage(Image.open("images/kayo.jpg").resize((100, 100), Image.ANTIALIAS))
killjoy = ImageTk.PhotoImage(Image.open("images/killjoy.jpg").resize((100, 100), Image.ANTIALIAS))
neon = ImageTk.PhotoImage(Image.open("images/neon.jpg").resize((100, 100), Image.ANTIALIAS))
omen = ImageTk.PhotoImage(Image.open("images/omen.jpg").resize((100, 100), Image.ANTIALIAS))
phoenix = ImageTk.PhotoImage(Image.open("images/phoenix.jpg").resize((100, 100), Image.ANTIALIAS))
raze = ImageTk.PhotoImage(Image.open("images/raze.jpg").resize((100, 100), Image.ANTIALIAS))
reyna = ImageTk.PhotoImage(Image.open("images/reyna.jpg").resize((100, 100), Image.ANTIALIAS))
sage = ImageTk.PhotoImage(Image.open("images/sage.jpg").resize((100, 100), Image.ANTIALIAS))
skye = ImageTk.PhotoImage(Image.open("images/skye.jpg").resize((100, 100), Image.ANTIALIAS))
sova = ImageTk.PhotoImage(Image.open("images/sova.jpg").resize((100, 100), Image.ANTIALIAS))
viper = ImageTk.PhotoImage(Image.open("images/viper.jpg").resize((100, 100), Image.ANTIALIAS))
yoru = ImageTk.PhotoImage(Image.open("images/yoru.jpg").resize((100, 100), Image.ANTIALIAS))

#button = Button(window,text='Click me!!!')
play_button = Button(window,image=play)

astra_button = Button(window,image=astra)
breach_button = Button(window,image=breach)
brim_button = Button(window,image=brim)
chamber_button = Button(window,image=chamber)
cypher_button = Button(window,image=cypher)
fade_button = Button(window,image=fade)
jett_button = Button(window,image=jett)
kayo_button = Button(window,image=kayo)
killjoy_button = Button(window,image=killjoy)
neon_button = Button(window,image=neon)
omen_button = Button(window,image=omen)
phoenix_button = Button(window,image=phoenix)
raze_button = Button(window,image=raze)
reyna_button = Button(window,image=reyna)
sage_button = Button(window,image=sage)
skye_button = Button(window,image=skye)
sova_button = Button(window,image=sova)
viper_button = Button(window,image=viper)
yoru_button = Button(window,image=yoru)

correct_incorrect_text = Label(window,text='Correct')
correct_incorrect_text.config(font=('Monospace',25))
correct_incorrect_text.config(bg='#ff6200')

actual_agent = Label(window,image=astra)

# Configuration commands
correct_incorrect_text.grid(row=0, column=2)
actual_agent.grid(row=0, column=3)

play_button.config(command=lambda : click()) #performs call back of function
play_button.grid(row=0, column=1)
astra_button.config(command=click) #performs call back of function
astra_button.grid(row=1, column=0)
jett_button.config(command=click) #performs call back of function
jett_button.grid(row=1, column=1)
#button.config(font=('Ink Free',50,'bold'))
#button.config(bg='#ff6200')
#button.config(fg='#fffb1f')
#button.config(activebackground='#FF0000')
#button.config(activeforeground='#fffb1f')

#button.config(image=image)
#button.config(compound='bottom')
#button.config(state=DISABLED) #disabled button (ACTIVE/DISABLED)
label = Label(window,text=count)
label.config(font=('Monospace',50))
label.grid(row=0, column=0)


# Display everything in the window

#label.pack()

#astra_button.pack()
#jett_button.pack()


#label2 = Label(window,image=image)

window.mainloop()