from tkinter import *
from PIL import ImageTk, Image
import random
import vlc

count = 0
current_agent = "astra"
current_path = "sounds/astra_dirt_1.mp3"
current_sound = vlc.MediaPlayer(current_path)

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

# Omen DONE
# Phoenix DONE
# Raze DONE
# Reyna DONE
# Sage DONE
# Skye DONE
# Sova DONE
# Viper
# Yoru


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

## Import sounds




def play_sound():
    #Plays the current sound
    global current_sound
    global current_path
    current_sound.stop()
    current_sound.play()
    pass

def set_actual_agent(agent):
    if agent == "astra":
        actual_agent.config(image=astra)
    elif agent == "breach":
        actual_agent.config(image=breach)
    elif agent == "brim":
        actual_agent.config(image=brim)
    elif agent == "chamber":
        actual_agent.config(image=chamber)
    elif agent == "cypher":
        actual_agent.config(image=cypher)
    elif agent == "fade":
        actual_agent.config(image=fade)
    elif agent == "jett":
        actual_agent.config(image=jett)
    elif agent == "kayo":
        actual_agent.config(image=kayo)
    elif agent == "killjoy":
        actual_agent.config(image=killjoy)
    elif agent == "neon":
        actual_agent.config(image=neon)
    elif agent == "omen":
        actual_agent.config(image=omen)
    elif agent == "phoenix":
        actual_agent.config(image=phoenix)
    elif agent == "raze":
        actual_agent.config(image=raze)
    elif agent == "reyna":
        actual_agent.config(image=reyna)
    elif agent == "sage":
        actual_agent.config(image=sage)
    elif agent == "skye":
        actual_agent.config(image=skye)
    elif agent == "sova":
        actual_agent.config(image=sova)
    elif agent == "viper":
        actual_agent.config(image=viper)
    elif agent == "yoru":
        actual_agent.config(image=yoru)


def guess(agent):
    # Set stuff based on correct/incorrect and then set the next sound and agent
    global current_agent
    global current_sound
    global current_path
    agents = ["astra", "breach", "brim", "chamber", "cypher", "fade", "jett", "kayo", "killjoy", "neon", "omen", "phoenix", "raze", "reyna", "sage", "skye", "sova", "viper", "yoru"]
    environments = ["normal", "grass", "dirt", "metal", "wood"]
    numbers = ["1", "2"]
    if agent == current_agent:
        click()
        set_actual_agent(current_agent)
        correct_incorrect_text.config(text="Correct", bg='#00ff00')
        pass
    else:
        set_actual_agent(current_agent)
        newstr = "Incorrect"
        correct_incorrect_text.config(text=newstr, bg='#ff6200')
        pass
    # Reset sound and agent
    new_agent = random.choice(agents)
    new_environment = random.choice(environments)
    new_number = random.choice(numbers)
    current_agent = new_agent
    new_path = "sounds/" + new_agent + "_" + new_environment + "_" + new_number + ".mp3"
    current_path = new_path
    current_sound = vlc.MediaPlayer(new_path)

correct_incorrect_text = Label(window,text='Correct')
correct_incorrect_text.config(font=('Monospace',25))
correct_incorrect_text.config(bg='#ff6200')

actual_agent = Label(window,image=astra)

# Configuration commands
correct_incorrect_text.grid(row=0, column=2)
actual_agent.grid(row=0, column=3)

play_button.config(command=lambda : play_sound())
play_button.grid(row=0, column=1)
astra_button.config(command=lambda : guess("astra"))
astra_button.grid(row=1, column=0)
breach_button.config(command=lambda : guess("breach"))
breach_button.grid(row=1, column=1)
brim_button.config(command=lambda : guess("brim"))
brim_button.grid(row=1, column=2)
chamber_button.config(command=lambda : guess("chamber"))
chamber_button.grid(row=1, column=3)
cypher_button.config(command=lambda : guess("cypher"))
cypher_button.grid(row=1, column=4)
fade_button.config(command=lambda : guess("fade"))
fade_button.grid(row=1, column=5)
jett_button.config(command=lambda : guess("jett"))
jett_button.grid(row=1, column=6)
kayo_button.config(command=lambda : guess("kayo"))
kayo_button.grid(row=1, column=7)
killjoy_button.config(command=lambda : guess("killjoy"))
killjoy_button.grid(row=1, column=8)
neon_button.config(command=lambda : guess("neon"))
neon_button.grid(row=1, column=9)
omen_button.config(command=lambda : guess("omen"))
omen_button.grid(row=2, column=0)
phoenix_button.config(command=lambda : guess("phoenix"))
phoenix_button.grid(row=2, column=1)
raze_button.config(command=lambda : guess("raze"))
raze_button.grid(row=2, column=2)
reyna_button.config(command=lambda : guess("reyna"))
reyna_button.grid(row=2, column=3)
sage_button.config(command=lambda : guess("sage"))
sage_button.grid(row=2, column=4)
skye_button.config(command=lambda : guess("skye"))
skye_button.grid(row=2, column=5)
sova_button.config(command=lambda : guess("sova"))
sova_button.grid(row=2, column=6)
viper_button.config(command=lambda : guess("viper"))
viper_button.grid(row=2, column=7)
yoru_button.config(command=lambda : guess("yoru"))
yoru_button.grid(row=2, column=8)

# Display everything in the window

#label.pack()

#astra_button.pack()
#jett_button.pack()


#label2 = Label(window,image=image)

window.mainloop()