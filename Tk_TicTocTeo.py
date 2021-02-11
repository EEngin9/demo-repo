from tkinter import *
import tkinter.messagebox
import random
# import pkg_resources.py2_warn


ttt_matrix = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
number_list = []

tk = Tk()
tk.title("Ercan- Tic Tac Teo")
tk.iconbitmap('./Td.ico')
weather_color = 'LightBlue'   # Variable is define window default background color.
tk.configure(background=weather_color)

pa = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()
p2.set("Computer")

player1_name = Entry(tk, textvariable=p1, bd=5)
player1_name.grid(row=1, column=1, columnspan=8)

player2_name = Entry(tk, textvariable=p2, bd=5)
player2_name.grid(row=2, column=1, columnspan=8)

bclick = True
flag = 0


def clearButton():
    button1 = Button(tk, text=" ", font='Times 20 bold', bg=weather_color, fg='black', height=4, width=8,
                     command=lambda: btnClick(button1))
    button1.grid(row=3, column=0)

    button2 = Button(tk, text=' ', font='Times 20 bold', bg=weather_color, fg='black', height=4, width=8,
                     command=lambda: btnClick(button2))
    button2.grid(row=3, column=1)

    button3 = Button(tk, text=' ', font='Times 20 bold', bg=weather_color, fg='black', height=4, width=8,
                     command=lambda: btnClick(button3))
    button3.grid(row=3, column=2)

    button4 = Button(tk, text=' ', font='Times 20 bold', bg=weather_color, fg='black', height=4, width=8,
                     command=lambda: btnClick(button4))
    button4.grid(row=4, column=0)

    button5 = Button(tk, text=' ', font='Times 20 bold', bg=weather_color, fg='black', height=4, width=8,
                     command=lambda: btnClick(button5))
    button5.grid(row=4, column=1)

    button6 = Button(tk, text=' ', font='Times 20 bold', bg=weather_color, fg='black', height=4, width=8,
                     command=lambda: btnClick(button6))
    button6.grid(row=4, column=2)

    button7 = Button(tk, text=' ', font='Times 20 bold', bg=weather_color, fg='black', height=4, width=8,
                     command=lambda: btnClick(button7))
    button7.grid(row=5, column=0)

    button8 = Button(tk, text=' ', font='Times 20 bold', bg=weather_color, fg='black', height=4, width=8,
                     command=lambda: btnClick(button8))
    button8.grid(row=5, column=1)

    button9 = Button(tk, text=' ', font='Times 20 bold', bg=weather_color, fg='black', height=4, width=8,
                     command=lambda: btnClick(button9))
    button9.grid(row=5, column=2)


def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


def btnClick(buttons):
    global bclick, flag, player2_name, player1_name, playerb, pa, value
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        if buttons == button1:
            value = 1
        elif buttons == button2:
            value = 2
        elif buttons == button3:
            value = 3
        elif buttons == button4:
            value = 4
        elif buttons == button5:
            value = 5
        elif buttons == button6:
            value = 6
        elif buttons == button7:
            value = 7
        elif buttons == button8:
            value = 8
        elif buttons == button9:
            value = 9
        bclick = False
        playerb = p2.get() + " Wins!"
        pa = p1.get() + " Wins!"
        checkForWin()
        flag += 1
        # Than computer choose empty buttons
        number_list.append(value)
        choose_button()

    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1

    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")


def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
        button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
        button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
        button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
        button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
        button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
        button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
        button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", pa)

    elif (flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif (button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button4['text'] == 'O' and button5['text'] == 'O' and button6['text'] == 'O' or
          button7['text'] == 'O' and button8['text'] == 'O' and button9['text'] == 'O' or
          button1['text'] == 'O' and button5['text'] == 'O' and button9['text'] == 'O' or
          button3['text'] == 'O' and button5['text'] == 'O' and button7['text'] == 'O' or
          button1['text'] == 'O' and button2['text'] == 'O' and button3['text'] == 'O' or
          button1['text'] == 'O' and button4['text'] == 'O' and button7['text'] == 'O' or
          button2['text'] == 'O' and button5['text'] == 'O' and button8['text'] == 'O' or
          button7['text'] == 'O' and button6['text'] == 'O' and button9['text'] == 'O'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)


# computer choose empty number of button in table and put "O"
def choose_button():
    while True:
        choose = random.randint(1, 9)
        if choose not in number_list:
            number_list.append(choose)
            if choose == 1:
                btnClick(button1)
            elif choose == 2:
                btnClick(button2)
            elif choose == 3:
                btnClick(button3)
            elif choose == 4:
                btnClick(button4)
            elif choose == 5:
                btnClick(button5)
            elif choose == 6:
                btnClick(button6)
            elif choose == 7:
                btnClick(button7)
            elif choose == 8:
                btnClick(button8)
            elif choose == 9:
                btnClick(button9)
#            buttons["text"] = "O"
            break
    return choose


buttons = StringVar()

label = Label(tk, text="Player 1:", font='Times 20 bold', bg='black', fg='white',
              height=1, width=8)
label.grid(row=1, column=0)

label = Label(tk, text="Player 2:", font='Times 20 bold', bg='black', fg='white',
              height=1, width=8)
label.grid(row=2, column=0)

button1 = Button(tk, text=" ", font='Times 20 bold', bg=weather_color, fg='black', height=4, width=8,
                 command=lambda: btnClick(button1))
button1.grid(row=3, column=0)

button2 = Button(tk, text=' ', font='Times 20 bold', bg=weather_color, fg='black', height=4, width=8,
                 command=lambda: btnClick(button2))
button2.grid(row=3, column=1)

button3 = Button(tk, text=' ', font='Times 20 bold', bg=weather_color, fg='black', height=4, width=8,
                 command=lambda: btnClick(button3))
button3.grid(row=3, column=2)

button4 = Button(tk, text=' ', font='Times 20 bold', bg=weather_color, fg='black', height=4, width=8,
                 command=lambda: btnClick(button4))
button4.grid(row=4, column=0)

button5 = Button(tk, text=' ', font='Times 20 bold', bg=weather_color, fg='black', height=4, width=8,
                 command=lambda: btnClick(button5))
button5.grid(row=4, column=1)

button6 = Button(tk, text=' ', font='Times 20 bold', bg=weather_color, fg='black', height=4, width=8,
                 command=lambda: btnClick(button6))
button6.grid(row=4, column=2)

button7 = Button(tk, text=' ', font='Times 20 bold', bg=weather_color, fg='black', height=4, width=8,
                 command=lambda: btnClick(button7))
button7.grid(row=5, column=0)

button8 = Button(tk, text=' ', font='Times 20 bold', bg=weather_color, fg='black', height=4, width=8,
                 command=lambda: btnClick(button8))
button8.grid(row=5, column=1)

button9 = Button(tk, text=' ', font='Times 20 bold', bg=weather_color, fg='black', height=4, width=8,
                 command=lambda: btnClick(button9))
button9.grid(row=5, column=2)


# button_exit = Button(tk, text="Reset ", height=2, width=4, command=clearButton)
# button_exit.grid(row=6, column=0, padx=5, pady=10, stick=W+E+N+S)

button_exit = Button(tk, text="Exit ", height=2, width=4, command=tk.destroy)
button_exit.grid(row=6, column=1, padx=5, pady=10, stick=W+E+N+S)

tk.mainloop()
