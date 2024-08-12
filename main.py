from tkinter import *
from hangman_game_gui import *
from rock_paper_scissors_gui import *
from tic_tac_toe_multiplayer import *

t=Tk()
t.title('Game Zone')
t.geometry('350x729+0+5')
t.resizable(0,0)
t.wm_iconbitmap('life.ico')
t['bg']='steelblue4'

bg=PhotoImage(file='img1.png')
img=Label(t,image=bg)
img.place(x=0,y=0)

b1=Button(t,text="ROCK PAPER SCISSORS",command=rockPaperScissors,width=200,height=1,font=('ariel',15,'bold'),relief=SUNKEN,bd=10,fg='white',bg='black')
b1.pack(padx=40,pady=80)
# b1.place(x=150,y=530)
b2=Button(t,text="TIC TAC TOE",command=ticTacToe,width=200,height=1,font=('ariel',15,'bold'),relief=SUNKEN,bd=10,fg='white',bg='black')
b2.pack(padx=40,pady=0)
# b2.place(x=550,y=530)
b3=Button(t,text="HANGMAN",command=hangman,width=200,height=1,font=('ariel',15,'bold'),relief=SUNKEN,bd=10,fg='white',bg='black')
b3.pack(padx=40,pady=80)
# b3.place(x=950,y=530)
t.mainloop()