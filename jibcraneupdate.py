from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import time
import csv

import math
import turtle



global tree
global s_no



class HoverButton(Button):
    def __init__(self, master, **kw):
        Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.defaultForeground = self["foreground"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']
        self['foreground'] = self['activeforeground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground
        self['foreground'] = self.defaultForeground


def alpha(c,a,b):
    arg=((b**2+c**2-a**2)/(2*b*c))
    A=math.acos(arg)
    A=math.degrees(A)
    return A
def beta(c,a,b):
    arg=((a**2+b**2-c**2)/(2*a*b))
    B=math.acos(arg)
    B=math.degrees(B)
    return B
def gamma(c,a,b):
    arg=((a**2+c**2-b**2)/(2*a*c))
    C=math.acos(arg)
    C=math.degrees(C)
    return C
def turtle_diagram():
    turtle.Screen().bgcolor("#C4DFE6")
    turtle.speed(100000)
    turtle.hideturtle()
    turtle.left(90)
    turtle.penup()
    turtle.forward(100)
    turtle.left(180)
    turtle.pendown()
    turtle.color("#4B0082")
    turtle.write("C")
    turtle.forward((BC * 5) / 2)
    turtle.penup()
    turtle.right(90)
    turtle.forward(50)
    turtle.pendown()
    turtle.write("BC:  "+str(BC))
    turtle.penup()
    turtle.right(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.pendown()
    turtle.forward((BC * 5) / 2)
    turtle.left(180 - gamma(AB, BC, AC))
    turtle.write("B")
    turtle.color("#B8255F")
    turtle.forward((AB * 5) / 2)
    turtle.penup()
    turtle.right(90)
    turtle.forward(50)
    turtle.pendown()
    turtle.write("AB:  "+str(AB))
    turtle.penup()
    turtle.right(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.pendown()
    turtle.forward((AB * 5) / 2)
    turtle.write("A")
    turtle.left(180 - alpha(AB, BC, AC))
    turtle.color("#4073FF")
    turtle.forward((AC * 5) / 2)
    turtle.penup()
    turtle.right(90)
    turtle.forward(50)
    turtle.pendown()
    turtle.write("AC:  "+str(AC))
    turtle.penup()
    turtle.right(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.pendown()
    turtle.forward((AC * 5) / 2)
    turtle.left(180 - beta(AB, BC, AC))
    turtle.penup()
    turtle.forward(400)
    turtle.pendown()
    turtle.color("#000000")
    angle="ANGLES: ???BAC:"+str(round(alpha(AB, BC, AC), 3))+"??   ||   "+"???ACB:"+str(round(beta(AB, BC, AC), 3))+"??   ||   "+"???CBA:"+str(round(gamma(AB, BC, AC), 3))+"??   ||   "
    turtle.write("SPACE DIAGRAM")
    turtle.penup()
    turtle.forward(15)
    turtle.pendown()
    turtle.write(angle)
    turtle.done()
    turtle.bye()
    turtle.mainloop()

def calc():


    try:
        global AB
        global AC
        global BC


        BC = float(post.get())
        AB = float(len_AB.get())
        AC = float(len_AC.get())

        a = alpha(AB, BC, AC)
        b = beta(AB, BC, AC)
        c = gamma(AB, BC, AC)

        Weight = float(weight.get())

        ze_t = float(ze_tension.get())
        ze_c = float(ze_compression.get())

        tie_obs = float(final_tie_reading.get()) - ze_t
        jib_obs = float(final_jib_reading.get()) - ze_c

        global Comp_Trunc, Ten_Trunc, perc_tie, perc_jib

        Compression=(Weight*math.sin(math.radians(b)))/(math.sin(math.radians(a)))
        Comp_Trunc = round(Compression, 3)
        Tension=(Weight*math.sin(math.radians(c)))/(math.sin(math.radians(a)))
        Ten_Trunc = round(Tension, 3)

        perc_tie = ((tie_obs - Ten_Trunc) / Ten_Trunc) * 100
        perc_jib = ((jib_obs - Comp_Trunc) / Comp_Trunc) * 100

        perc_tie = round(perc_tie,3)
        perc_jib = round(perc_jib, 3)

        if abs(perc_tie) < 5:
            perc_error_tie.configure(fg='green')
        elif abs(perc_tie) < 10:
            perc_error_tie.configure(fg='#F06000')
        else:
            perc_error_tie.configure(fg='red')

        if abs(perc_jib) < 5:
            perc_error_jib.configure(fg='green')
        elif abs(perc_jib) < 10:
            perc_error_jib.configure(fg='#F06000')
        else:
            perc_error_jib.configure(fg='red')




        perc_error_jib.configure(text=(f"Percentage Error Jib: {perc_jib}%"))
        perc_error_tie.configure(text=(f"Percentage Error Tie: {perc_tie}%" ))

        compr_calc.configure(text=("Compression calculated: " + str(Comp_Trunc)))
        tens_calc.configure(text=("Tension calculated: " + str(Ten_Trunc)))
        #
        # print(gamma(AB, BC, AC))
        # print(alpha(AB, BC, AC))
        # print(beta(AB, BC, AC))
        # print("")
        # print(Comp_Trunc)
        # print(Ten_Trunc)
        # print(perc_tie)
        # print(perc_jib)

        turtle_diagram()
        # time.sleep(3)
        turtle.bye()
        turtle.mainloop()
    except turtle.Terminator:
        pass



def clear():
    final_tie_reading.delete(0, END)
    final_jib_reading.delete(0, END)
    len_AB.delete(0, END)
    len_AC.delete(0, END)
    weight.delete(0, END)
    compr_calc.configure(text="Compression calculated: ")
    tens_calc.configure(text="Tension calculated: ")
    perc_error_tie.configure(text="Percentage Error Tie: ")
    perc_error_jib.configure(text="Percentage Error Jib: ")

def reset():
    clear()
    initial_tie.delete(0, END)
    global s_no
    f = open("obs.csv", "w", newline='') # clearing observation table
    writer = csv.writer(f)
    f.close()
    s_no=0
    for item in tree.get_children():
        tree.delete(item)
    initial_jib.delete(0, END)
    post.delete(0, END)
    ze_tension.delete(0, END)
    ze_compression.delete(0, END)
    weight.delete(0, END)

def view_table():

    global tree


    # obs_table.title('Observation Table')
    # obs_table.geometry("988x266")
    # obs_table.configure(background='white')
    #
    # obs_heading = Label(obs_table, text="Observation Table", font=('Helvatical bold',20), background='white', foreground='blue', anchor=CENTER)
    # obs_heading.grid(row=0, column=0)
    #
    #

    f = open("obs.csv", "r")
    reader = csv.reader(f)
    data = list(reader)

    if not data:

        tree.heading('S.No', text='S.No')
        tree.column("S.No", minwidth=0, width=35, stretch=NO)

        tree.heading('Weight', text='Weight')
        tree.column("Weight", minwidth=0, width=50, stretch=NO)

        tree.heading('Initial Tie Length', text='Initial Tie Length')
        tree.column("Initial Tie Length", minwidth=0, width=100, stretch=NO)

        tree.heading('Initial Jib Length', text='Initial Jib Length')
        tree.column("Initial Jib Length", minwidth=0, width=100, stretch=NO)

        tree.heading('Post Length', text='Post Length')
        tree.column("Post Length", minwidth=0, width=100, stretch=NO)

        tree.heading('Final Jib Length', text='Final Jib Length')
        tree.column("Final Jib Length", minwidth=0, width=100, stretch=NO)

        tree.heading('Final Tie Length', text='Final Tie Length')
        tree.column("Final Tie Length", minwidth=0, width=100, stretch=NO)

        tree.heading('Calculated Tie Length', text='Calc. Tie Length')
        tree.column("Calculated Tie Length", minwidth=0, width=100, stretch=NO)

        tree.heading('Calculated Jib Length', text='Calc. Jib Length')
        tree.column("Calculated Jib Length", minwidth=0, width=100, stretch=NO)

        tree.heading('Percentage Error Jib', text='% Error Jib')
        tree.column("Percentage Error Jib", minwidth=0, width=100, stretch=NO)

        tree.heading('Percentage Error Tie', text='% Error Tie')
        tree.column("Percentage Error Tie", minwidth=0, width=100, stretch=NO)

        tree.grid(row=1, column=0, sticky='nsew')
        scrollbar = ttk.Scrollbar(main_win, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky='ns')

    else:
        tree.heading('S.No', text='S.No')
        tree.column("S.No", minwidth=0, width=35, stretch=NO)

        tree.heading('Weight', text='Weight')
        tree.column("Weight", minwidth=0, width=50, stretch=NO)

        tree.heading('Initial Tie Length', text='Initial Tie Length')
        tree.column("Initial Tie Length", minwidth=0, width=100, stretch=NO)

        tree.heading('Initial Jib Length', text='Initial Jib Length')
        tree.column("Initial Jib Length", minwidth=0, width=100, stretch=NO)

        tree.heading('Post Length', text='Post Length')
        tree.column("Post Length", minwidth=0, width=100, stretch=NO)

        tree.heading('Final Jib Length', text='Final Jib Length')
        tree.column("Final Jib Length", minwidth=0, width=100, stretch=NO)

        tree.heading('Final Tie Length', text='Final Tie Length')
        tree.column("Final Tie Length", minwidth=0, width=100, stretch=NO)

        tree.heading('Calculated Tie Length', text='Calc. Tie Length')
        tree.column("Calculated Tie Length", minwidth=0, width=100, stretch=NO)

        tree.heading('Calculated Jib Length', text='Calc. Jib Length')
        tree.column("Calculated Jib Length", minwidth=0, width=100, stretch=NO)

        tree.heading('Percentage Error Jib', text='% Error Jib')
        tree.column("Percentage Error Jib", minwidth=0, width=100, stretch=NO)

        tree.heading('Percentage Error Tie', text='% Error Tie')
        tree.column("Percentage Error Tie", minwidth=0, width=100, stretch=NO)

        for item in data:
            tree.insert('', END, values=item)

        tree.grid(row=1, column=0, sticky='nsew')
        scrollbar = ttk.Scrollbar(main_win, orient=VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky='ns')

    # contacts = []
    # for n in range(1, 100):
    #     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))
    #
    # for contact in contacts:
    #     tree.insert('', END, values=contact)


    obs_table.mainloop()

def add_to_table():


    global s_no, Comp_Trunc, Ten_Trunc, perc_jib, perc_tie
    f = open("obs.csv", "a", newline='')
    writer = csv.writer(f)
    s_no += 1
    data = [s_no, weight.get(), initial_tie.get(), initial_jib.get(), post.get(), final_jib_reading.get(), final_tie_reading.get(), Comp_Trunc, Ten_Trunc, perc_jib, perc_tie]
    writer.writerow(data)
    tree.insert('', END, values = data)

    f.close()

main_win = Tk()
main_win.geometry("1024x768")
main_win.title('Jib Crane Experiment')
main_win.configure(background='white')

global Comp_Trunc, Ten_Trunc, perc_tie, perc_jib
Comp_Trunc, Ten_Trunc, perc_tie, perc_jib = -1,-1,-1,-1


#main_frame = ttk.Frame(main_win, padding=10)
main_heading = ttk.Label(main_win, text="Jib Crane Experiment", )
main_heading.configure( font=('Helvatical bold',30), padding=0)

jib_crane_img = Canvas(main_win, height=600, width=500)
img = ImageTk.PhotoImage(Image.open('jib_crane.jpg'))
jib_crane_img.create_image(10, 10, anchor=NW, image=img)

#btn = tkinter.Button(main_frame, text="Quit", command=main_win.destroy)

#main_heading.grid(row=0)
#jib_crane_img.grid(row=1)
#btn.grid(row=1)
#btn.config(background='white', font='30', padx=10, pady=10)

ze_tension = Entry(main_win, selectbackground="red", font='30', width=8)
ze_tension_label = ttk.Label(main_win, text="Zero error of tension spring balance", font=('Helvatical bold',13))

ze_compression = Entry(main_win, selectbackground="red", font='30', width=8)
ze_compression_label = ttk.Label(main_win, text="Zero error of compression spring balance", font=('Helvatical bold',13))

initial_tie = Entry(main_win, selectbackground="red", font='30', width=8)
initial_tie_label = ttk.Label(main_win, text="Initial length of tie (cm)",  font=('Helvatical bold',13))

initial_jib = Entry(main_win, selectbackground="red",  font=('Helvatical bold',13), width=8)
initial_jib_label = ttk.Label(main_win, text="Initial length of jib (cm)",  font=('Helvatical bold',13))

post = Entry(main_win, selectbackground="red",  font=('Helvatical bold',13), width=8)
post_label = ttk.Label(main_win, text="Length of post (cm)",  font=('Helvatical bold',13))

ze_compression = Entry(main_win, selectbackground="red",  font=('Helvatical bold',13), width=8)
ze_compression_label = ttk.Label(main_win, text="Zero error of compression spring balance",  font=('Helvatical bold',13))

weight = Entry(main_win, selectbackground="red",  font=('Helvatical bold',13), width=8, background='white')
weight_label = Label(main_win, text="Weight", background='white')

len_AB = Entry(main_win, selectbackground="red", background="white",  font=('Helvatical bold',13), width=8)
len_AB_label = Label(main_win, text="Final Jib Length", background='white')

len_AC = Entry(main_win, selectbackground="red", font="30", width=8, background="white")
len_AC_label = Label(main_win, text="Final Tie Length", background='white')

perc_error_tie = Label(main_win, text="Percentage Error Tie: ",  font=('Helvatical bold',13))
perc_error_jib = Label(main_win, text="Percentage Error Jib: ",  font=('Helvatical bold',13))

compr_calc = Label(main_win, text="Compression calculated: ",  font=('Helvatical bold',13))
tens_calc = Label(main_win, text="Tension calculated: ",  font=('Helvatical bold',13))

final_tie_reading_label = Label(main_win, text="Final reading of tie(kgf)",  font=('Helvatical bold',13))
final_tie_reading = Entry(main_win,selectbackground='red',  font=('Helvatical bold',13), width=8)

final_jib_reading_label = Label(main_win, text="Final reading of jib(kgf)",  font=('Helvatical bold',13))
final_jib_reading = Entry(main_win, selectbackground='red',  font=('Helvatical bold',13), width=8)

calculate_button = HoverButton(main_win, padx=10, pady=10,  font=('Helvatical bold',13), background='white', foreground='#1EC600', text='Calculate', command=calc, activeforeground='white', activebackground='#1EC600')
clear_button = HoverButton(main_win, padx=10, pady=10, font=('Helvatical bold',13), background='white', foreground='red', text='Clear', command=clear, activeforeground='white', activebackground='red')
reset_button = HoverButton(main_win, padx=10, pady=10, font=('Helvatical bold',13), background='white', foreground='red', text="reset", command=reset, activeforeground='white', activebackground='red')

view_table = HoverButton(main_win, padx=10, pady=10, font=('Helvatical bold', 13), background='white', foreground='#F06000', text="View Table", command=view_table, activeforeground='white', activebackground='#F06000')
add_table = HoverButton(main_win, padx=10, pady=10, font=('Helvatical bold', 13), background='white', foreground='#F06000', text="Add to table", command=add_to_table, activeforeground='white', activebackground='#F06000')



#ze_tension_label.grid(row=2, column=0)
#ze_tension.grid(row=1, column=1)

main_heading.configure(background='white')

jib_crane_img.configure(background='white', borderwidth=0, highlightthickness=0)

ze_tension.configure(background='white')
ze_tension_label.configure(background='white', foreground='blue')

ze_compression.configure(background='white')
ze_compression_label.configure(background='white', foreground='blue')

initial_tie.configure(background='white')
initial_tie_label.configure(background='white', foreground='blue')

initial_jib.configure(background='white')
initial_jib_label.configure(background='white', foreground='blue')

post.configure(background='white')
post_label.configure(background='white', foreground='blue')

perc_error_jib.configure(background='white', foreground='blue')
perc_error_tie.configure(background='white', foreground='blue')

tens_calc.configure(background='white', foreground='blue')
compr_calc.configure(background='white', foreground='blue')

final_tie_reading.configure(background='white', foreground='blue')
final_tie_reading_label.configure(background='white', foreground='blue')

final_jib_reading.configure(background='white', foreground='blue')
final_jib_reading_label.configure(background='white', foreground='blue')

'''Placing elements'''
main_heading.place(x=350, y=50)
jib_crane_img.place(x=270, y=100)

ze_tension.place(x=310, y=500)
ze_tension_label.place(x=30, y=500)

ze_compression_label.place(x=30, y=530)
ze_compression.place(x=340, y=530)

initial_tie.place(x=210, y=560)
initial_tie_label.place(x=30, y=560)

initial_jib.place(x=210, y=590)
initial_jib_label.place(x=30, y=590)
#
# initial_tie.place(x=200, y=560)
# initial_tie_label.place(x=30, y=560)

post.place(x=210, y=620)
post_label.place(x=30, y=620)

weight.place(x=670, y=350)
weight_label.place(x=668, y=325)

len_AB.place(x=535, y=270)
len_AB_label.place(x=530, y=250)

len_AC.place(x=460, y=150)
len_AC_label.place(x=455, y=130)



final_tie_reading_label.place(x=30, y=650)
final_tie_reading.place(x=210, y=650)

final_jib_reading_label.place(x=30, y=680)
final_jib_reading.place(x=210, y=680)


perc_error_tie.place(x=590, y = 550)
perc_error_jib.place(x=590, y = 580)

compr_calc.place(x=590, y = 490)
tens_calc.place(x=590, y = 520)

calculate_button.place(x=590,y=620)
clear_button.place(x=700, y=620)
reset_button.place(x=780, y=620)
#view_table.place(x=560, y = 705)
add_table.place(x=675, y=675)

#main_heading.pack()
#main_frame.pack()


f = open("obs.csv", "w", newline='')  # clearing observation table
writer = csv.writer(f)
f.close()

global obs_table, tree
s_no = 0
columns = ("S.No", 'Weight', 'Initial Tie Length', 'Initial Jib Length', 'Post Length', 'Final Jib Length', 'Final Tie Length',
            'Calculated Tie Length', 'Calculated Jib Length', 'Percentage Error Jib', "Percentage Error Tie")

obs_table = Tk()

global tree

obs_table.title('Observation Table')
obs_table.geometry("988x266")
obs_table.configure(background='white')

tree = ttk.Treeview(obs_table, columns=columns, show='headings')

obs_heading = Label(obs_table, text="Observation Table", font=('Helvatical bold', 20), background='white',
                    foreground='blue', anchor=CENTER)
obs_heading.grid(row=0, column=0)

f = open("obs.csv", "r")
reader = csv.reader(f)
data = list(reader)

if not data:

    tree.heading('S.No', text='S.No')
    tree.column("S.No", minwidth=0, width=35, stretch=NO)

    tree.heading('Weight', text='Weight')
    tree.column("Weight", minwidth=0, width=50, stretch=NO)

    tree.heading('Initial Tie Length', text='Initial Tie Length')
    tree.column("Initial Tie Length", minwidth=0, width=100, stretch=NO)

    tree.heading('Initial Jib Length', text='Initial Jib Length')
    tree.column("Initial Jib Length", minwidth=0, width=100, stretch=NO)

    tree.heading('Post Length', text='Post Length')
    tree.column("Post Length", minwidth=0, width=100, stretch=NO)

    tree.heading('Final Jib Length', text='Final Jib Length')
    tree.column("Final Jib Length", minwidth=0, width=100, stretch=NO)

    tree.heading('Final Tie Length', text='Final Tie Length')
    tree.column("Final Tie Length", minwidth=0, width=100, stretch=NO)

    tree.heading('Calculated Tie Length', text='Calc. Tie Length')
    tree.column("Calculated Tie Length", minwidth=0, width=100, stretch=NO)

    tree.heading('Calculated Jib Length', text='Calc. Jib Length')
    tree.column("Calculated Jib Length", minwidth=0, width=100, stretch=NO)

    tree.heading('Percentage Error Jib', text='% Error Jib')
    tree.column("Percentage Error Jib", minwidth=0, width=100, stretch=NO)

    tree.heading('Percentage Error Tie', text='% Error Tie')
    tree.column("Percentage Error Tie", minwidth=0, width=100, stretch=NO)

    tree.grid(row=1, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(obs_table, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky='ns')

else:
    tree.heading('S.No', text='S.No')
    tree.column("S.No", minwidth=0, width=35, stretch=NO)

    tree.heading('Weight', text='Weight')
    tree.column("Weight", minwidth=0, width=50, stretch=NO)

    tree.heading('Initial Tie Length', text='Initial Tie Length')
    tree.column("Initial Tie Length", minwidth=0, width=100, stretch=NO)

    tree.heading('Initial Jib Length', text='Initial Jib Length')
    tree.column("Initial Jib Length", minwidth=0, width=100, stretch=NO)

    tree.heading('Post Length', text='Post Length')
    tree.column("Post Length", minwidth=0, width=100, stretch=NO)

    tree.heading('Final Jib Length', text='Final Jib Length')
    tree.column("Final Jib Length", minwidth=0, width=100, stretch=NO)

    tree.heading('Final Tie Length', text='Final Tie Length')
    tree.column("Final Tie Length", minwidth=0, width=100, stretch=NO)

    tree.heading('Calculated Tie Length', text='Calc. Tie Length')
    tree.column("Calculated Tie Length", minwidth=0, width=100, stretch=NO)

    tree.heading('Calculated Jib Length', text='Calc. Jib Length')
    tree.column("Calculated Jib Length", minwidth=0, width=100, stretch=NO)

    tree.heading('Percentage Error Jib', text='% Error Jib')
    tree.column("Percentage Error Jib", minwidth=0, width=100, stretch=NO)

    tree.heading('Percentage Error Tie', text='% Error Tie')
    tree.column("Percentage Error Tie", minwidth=0, width=100, stretch=NO)

    for item in data:
        tree.insert('', END, values=item)

    tree.grid(row=1, column=0, sticky='nsew')
    scrollbar = ttk.Scrollbar(main_win, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=1, column=1, sticky='ns')

# contacts = []
# for n in range(1, 100):
#     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))
#
# for contact in contacts:
#     tree.insert('', END, values=contact)



obs_table.mainloop()

main_win.mainloop()
