from audioop import reverse
from genericpath import exists
from operator import itemgetter
from signal import raise_signal
from tkinter import *
import tkinter

if exists("CoinCount.txt")== False:
    file = open("CoinCount.txt", "w")
    file.write('{"bags": 0, "total": 0}\n[{"name":"admin","accuracy":0,"correct_bags":0,"bags":0}]')
else:
    pass
            
# Main Root
root = Tk()
root.title("Coin bag Checker")

# logic #

# searvhes for the users name in the data base
def coin_count():
    found = False
    name = name_inp.get("1.0",tkinter.END)
    value = check_bag()
    if value[0] == ("correct"):
        accuracy = 1
    else:
        accuracy = 0

    for i in range(len(voulnteers)):
        location=i
        if name == voulnteers[i]["name"]:
            found = (True)
            break    
    if found == (True):
        pass
    else:
        location += 1
        voulnteers.append({"name":name,'correct_bags':0,"accuracy":0,"bags":0})
    if accuracy == 1:
        voulnteers[location]["correct_bags"] += 1
        voulnteers[location]["bags"] += 1
        totals["bags"] += 1
        totals["total"] += value[1]
    else:
        add_reminder.configure(text="{}".format(value))
        voulnteers[location]["bags"] += 1
        totals["bags"] += 1
        total_bags_lbl.configure(text="ammount of bags = {}".format(totals["bags"]))

    voulnteers[location]["accuracy"] = (float(voulnteers[location]["correct_bags"])/float(voulnteers[location]["bags"]))*100
    voulnteers[location]["accuracy"] = round(voulnteers[location]["accuracy"],2)
    total_bags_lbl.configure(text="ammount of bags = {}".format(totals["bags"]))
    total_value_lbl.configure(text="total value = £{}".format(totals["total"]))


    
# checks bag for correct weight
def check_bag():

    coin_type = var.get()
    weight = weight_inp.get("1.0",tkinter.END)

    current_target_weight = bag_target_weights[coin_type]
    current_coin_weight = coin_weight[coin_type]
    target_bag_value = bag_value[coin_type]

    coins = ((float(current_target_weight) - float(weight))/float(current_coin_weight))
    coins=round(coins)
    coins = str(coins)
    if float(weight) > float(current_target_weight):
        coins =coins[1:len(coins)]
        return("remove {} coins").format(str(coins))
    elif float(weight) < float(current_target_weight):
        return("add {} coins").format(coins)
    else:
        return["correct",target_bag_value]

# defining txt file dicts
file = open("CoinCount.txt", "r")
totals = eval(file.readline())
voulnteers = eval(file.readline())
voulnteers = sorted(voulnteers,key=itemgetter('accuracy'),reverse=True)

# setting up dicts for the math
bag_target_weights = {"£2":"120","£1":"175","50p":"160","20p":"250","10p":"325","5p":"235","2p":"356","1p":"365"}
coin_weight = {"£2":"12","£1":"8.75","50p":"8","20p":"5","10p":"6.5","5p":"2.35","2p":"7.12","1p":"3.65"}
bag_value = {"£2":20,"£1":10,"50p":10,"20p":5,"10p":5,"5p":5,"2p":1,"1p":1}

# menu bar functions

def raise_frame(frame):
    frame.tkraise()

def save_and_quit():
    data =("{}\n{}").format(totals,voulnteers)
    file  = open("CoinCount.txt", "w")
    file.write(data)
    exit()

# menu bar
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
menu= tkinter.Menu(menu_bar,tearoff=False)
menu.add_command(label="save and quit", command=save_and_quit)
menu.add_command(label="home", command=lambda:raise_frame(frame1))
menu.add_command(label="totals", command=lambda:raise_frame(frame2))
menu.add_command(label="volunteers", command=lambda:raise_frame(frame3))
menu_bar.add_cascade(label="options",menu=menu)

frame3 = tkinter.Frame()
frame2 = tkinter.Frame()
frame1 = tkinter.Frame()

for frame in (frame1, frame2, frame3):
    frame.grid(row=0, column=0, sticky='news')

####################### main window

#name = lable
name_lbl = tkinter.Label(frame1,text="name = ")
name_lbl.grid(column=1,row=1)
# name text box creation
name_inp = tkinter.Text(frame1,height=1,width=15)
name_inp.grid(column=2,row=1)
        # weight lable creation
weight_lbl = tkinter.Label(frame1,text="weight (G) = ")
weight_lbl.grid(column=1,row=2)
# weight text box creation
weight_inp = tkinter.Text(frame1,height=1,width=15)
weight_inp.grid(column=2,row=2)

#
add_reminder = tkinter.Label(frame1,text="")
add_reminder.grid(column=2,row=3)

# coin_type lable creation
coin_lbl = tkinter.Label(frame1,text="coin type =")
coin_lbl.grid(column=1,row=4)

# list of coin options
options = ["£2","£1","50p","20p","10p","5p","2p","1p"]
var=tkinter.StringVar(frame1)
var.set("£2")

# coin_type menu creation
coin_menu = tkinter.OptionMenu(frame1,var,"£2","£1","50p","20p","10p","5p","2p","1p")  
coin_menu.grid(column=2,row=4)

# confirm information button creation
confirm_but = tkinter.Button(frame1,text="confirm",command=coin_count)
confirm_but.grid(column=2,row=5)


########################### totals windows
total_bags_lbl = tkinter.Label(frame2,font=("tkinterdefaltfont",14),text="ammount of bags = {}".format(totals["bags"]))
total_bags_lbl.grid(row=1)
total_value_lbl = tkinter.Label(frame2,font=("tkinterdefaltfont",14),text="total value = {}".format(totals["total"]))
total_value_lbl.grid(row=2)

########################### voulnteer window
voulnteer_text = tkinter.Label(frame3,font=("Bold",10),text = "Name")
voulnteer_text.grid(row=1,column=1)
voulnteer_text = tkinter.Label(frame3,font=("Bold",10),text = "Accuracy")
voulnteer_text.grid(row=1,column=2)
voulnteer_text = tkinter.Label(frame3,font=("Bold",10),text = "Bags")
voulnteer_text.grid(row=1,column=3)
for i in range(len(voulnteers)):
    name=voulnteers[i]["name"]
    score=voulnteers[i]["accuracy"]
    row = i+2
    voulnteer_name_lbl = tkinter.Label(frame3,font=("tkinterdefaltfont",10),text = name)
    voulnteer_name_lbl.grid(row=row,column=1)
    voulnteer_accuracy_lbl = tkinter.Label(frame3,font=("tkinterdefaltfont",10),text = score)
    voulnteer_accuracy_lbl.grid(row=row,column=2)
    voulnteer_accuracy_lbl = tkinter.Label(frame3,font=("tkinterdefaltfont",10),text = voulnteers[i]["bags"])
    voulnteer_accuracy_lbl.grid(row=row,column=3)

root.mainloop() 