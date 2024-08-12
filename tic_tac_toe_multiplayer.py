from tkinter import *
from tkinter import messagebox as m

def ticTacToe():
    global clicked
    rt  = Toplevel()
    rt.title('TIC-TAC-TOE')
    rt.geometry('1005x729+350+5')
    rt['bg'] = 'lightblue'
    rt.resizable(0,0)

    bg=PhotoImage(file='t2.png')
    img=Label(rt,image=bg)
    img.place(x=0,y=0)

    clicked = True
    count = 0
    def disable_buttons():
        l=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
        for i in l:
            i.config(state=DISABLED)
    def won():
        if b1['text'] == b2['text'] == b3['text'] != ' ':
            b1.config(bg = 'red')
            b2.config(bg = 'red')
            b3.config(bg = 'red')
            xwin() if b1['text'] == b2['text'] == b3['text'] == 'X' else owin()
        elif b4['text'] == b5['text'] == b6['text'] != ' ':
            b4.config(bg = 'red')
            b5.config(bg = 'red')
            b6.config(bg = 'red')
            xwin() if b4['text'] == b5['text'] == b6['text'] == 'X' else owin()
        elif b7['text'] == b8['text'] == b9['text'] != ' ':
            b7.config(bg = 'red')
            b8.config(bg = 'red')
            b9.config(bg = 'red')
            xwin() if b7['text'] == b8['text'] == b9['text'] == 'X' else owin()
        elif b1['text'] == b4['text'] == b7['text'] != ' ':
            b1.config(bg = 'red')
            b4.config(bg = 'red')
            b7.config(bg = 'red')
            xwin() if b1['text'] == b4['text'] == b7['text'] == 'X' else owin()
        elif b2['text'] == b5['text'] == b8['text'] != ' ':
            b2.config(bg = 'red')
            b5.config(bg = 'red')
            b8.config(bg = 'red')
            xwin() if b2['text'] == b5['text'] == b8['text'] == 'X' else owin()
        elif b3['text'] == b6['text'] == b9['text'] != ' ':
            b3.config(bg = 'red')
            b6.config(bg = 'red')
            b9.config(bg = 'red')
            xwin() if b3['text'] == b6['text'] == b9['text'] == 'X' else owin()
        elif b1['text'] == b5['text'] == b9['text'] != ' ':
            b1.config(bg = 'red')
            b5.config(bg = 'red')
            b9.config(bg = 'red')
            xwin() if b1['text'] == b5['text'] == b9['text'] == 'X' else owin()
        elif b3['text'] == b5['text'] == b7['text'] != ' ':
            b3.config(bg = 'red')
            b5.config(bg = 'red')
            b7.config(bg = 'red')
            xwin() if b3['text'] == b5['text'] == b7['text'] == 'X' else owin()
        elif count == 9:
            m.showinfo('Oops!!','It\'s a TIE')
            refresh()
    def owin():
        c_inp = lblo.cget('text')
        op = int(c_inp)+1
        lblo.config(text=str(op))
        o_name = lbl2.cget('text')
        winner(o_name,op,'O')
        if op != 3: m.showinfo('info',f'{o_name} SCORE 1 POINT')
        refresh()
    def xwin():
        c_inp = lblx.cget('text')
        op = int(c_inp)+1
        lblx.config(text=str(op))
        x_name = lbl1.cget('text')
        winner(x_name,op,'X')
        if op != 3: m.showinfo('info',f'{x_name} SCORE 1 POINT')
        refresh()
    def winner(name,op,id):
        if op == 3:
            rt.config(bg="lightgreen")
            if id=='X':
                lblx.config(bg='green',fg='white')
                lbl1.config(bg='green')
                lblo.config(bg='red',fg='white')
                lbl2.config(bg='red')
            else:
                lblx.config(bg='red',fg='white')
                lbl1.config(bg='red')
                lblo.config(bg='green',fg='white')
                lbl2.config(bg='green')
            m.showinfo('GAME OVER !!!',f' {name} is the winner!!!')
            newGame()
    def b_click(b):
        global clicked,count
        if b['text'] == ' ' and clicked == True:
            b['text'] = 'X'
            clicked = False
            count += 1
            won()
        elif b['text'] == ' ' and clicked == False:
            b['text'] = 'O'
            clicked = True
            count += 1
            won()
        else:
            m.showerror('tic-tac-toe','Its not empty !!!!')
    def refresh():
        global count
        count = 0
        b=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
        for i in b:
            i.config(text=' ')
            i.config(state=ACTIVE)
            i.config(fg='black')
            i.config(bg='SystemButtonFace')
    def newGame():
        refresh()
        lbl1.config(bg='lightgreen')
        lbl2.config(bg='lightgreen')
        lblo.config(text='0',bg='lightgreen',fg='red')
        lblx.config(text='0',bg='lightgreen',fg='red')
        rt.config(bg="lightblue")
    
        y = m.askyesno('NEW GAME',"Woul\'d You Like To Play Again ???")
        if y == 1:
            ask_to_change_name()
        else:
            rt.withdraw()
        
    def ask_to_change_name():
        x = m.askyesno('player_name','woul\'d you like to change the Name of Players')
        if x == 1:
            change_name()
    
    def change_name():
        def save_name():
            new_x = p_entry1.get()
            new_o = p_entry2.get()
            lbl1.config(text = new_x.upper()+' (X):')
            lbl2.config(text = new_o.upper()+' (O):')
            t.withdraw()
        global p_entry1,p_entry2
        t=Tk()
        t.geometry('690x150+550+200')
        t.title('Change Player_Names')
        top1 = Frame(t,bg = 'lightgreen',bd=20)
        top1.pack(side=TOP)
        player1 = Label(top1,text="player 'X'  :",font=('aria',20,'bold'),width=20)
        player2 = Label(top1,text="player 'O'  :",font=('aria',20,'bold'),width=20)
        p_entry1 = Entry(top1,font=('aria',20,'bold'),width=20)
        p_entry2 = Entry(top1,font=('aria',20,'bold'),width=20)
        btn = Button(top1,text='SAVE',command = save_name,font=('aria',10,'bold'),width=10,relief=SUNKEN,bg='red',fg='white')
        player1.grid(row=1,column=1)
        player2.grid(row=2,column=1)
        p_entry1.grid(row=1,column=2)
        p_entry2.grid(row=2,column=2)
        btn.grid(row=3,column=2)
        t.mainloop()
        
    top = Frame(rt,bg="black",width=800,height=50,relief=SUNKEN,bd=5)
    top.place(x=50,y=35)
    player = Frame(rt,bg="brown",width=500,height=500,bd=20)
    player.place(x=500,y=350)
    newgame_btn = Frame(rt,bg="white",width=500,height=500,relief=SUNKEN,bd=5)
    newgame_btn.place(x=500,y=310)
    game = Frame(rt,bg="red",width=500,height=500,bd=20,relief=SUNKEN)
    game.place(x=100,y=200)
    refresh_btn = Frame(rt,bg="white",width=500,height=500,relief=SUNKEN,bd=5)
    refresh_btn.place(x=100,y=160)

    reset_btn = Button(newgame_btn,text = 'New Game',command = lambda :newGame(),width=60,bg='black',fg='white')
    reset_btn.grid(row=5,column=0)
    reset_btn = Button(refresh_btn,text = 'Refresh',command = lambda :refresh(),width=49,bg='black',fg='white')
    reset_btn.grid(row=5,column=1)

    lbl_max= Label(player,text="Max_Score",font=('aria',20,'bold'),fg='green',width=20,bd=10)
    lbl_max_score = Label(player,text='3',font=('aria',20,'bold'),fg= 'green',bd=10)
    lbl1 = Label(player,text="player 'X'  : ",font=('aria',20,'bold'),width=20,bd=10,bg='lightgreen')
    lblx = Label(player,text='0',font=('aria',20,'bold'),fg= 'red',bd=10,bg='lightgreen')
    lbl2 = Label(player,text="player 'O'  : ",font=('aria',20,'bold'),width=20,bd=10,bg='lightgreen')
    lblo = Label(player,text='0',font=('aria',20,'bold'),fg= 'red',bd=10,bg='lightgreen')
    lbl_max.grid(row=1,column=0)
    lbl_max_score.grid(row=1,column=1)
    lbl1.grid(row=2,column=0)
    lbl2.grid(row=3,column=0)
    lblx.grid(row=2,column=1)
    lblo.grid(row=3,column=1)

    head=Label(top,font=('aria',30,'bold'),text="                          TIC _ TAC _ TOE                          ")
    head.grid(row=2,column=0)

    b1=Button(game,text=" ",font=("Helvetica",20),height=3,width=6,bg='SystemButtonFace', command =lambda : b_click(b1))
    b2=Button(game,text=" ",font=("Helvetica",20),height=3,width=6,bg='SystemButtonFace', command =lambda : b_click(b2))
    b3=Button(game,text=" ",font=("Helvetica",20),height=3,width=6,bg='SystemButtonFace', command =lambda : b_click(b3))

    b4=Button(game,text=" ",font=("Helvetica",20),height=3,width=6,bg='SystemButtonFace', command =lambda : b_click(b4))
    b5=Button(game,text=" ",font=("Helvetica",20),height=3,width=6,bg='SystemButtonFace', command =lambda : b_click(b5))
    b6=Button(game,text=" ",font=("Helvetica",20),height=3,width=6,bg='SystemButtonFace', command =lambda : b_click(b6))

    b7=Button(game,text=" ",font=("Helvetica",20),height=3,width=6,bg='SystemButtonFace', command =lambda : b_click(b7))
    b8=Button(game,text=" ",font=("Helvetica",20),height=3,width=6,bg='SystemButtonFace', command =lambda : b_click(b8))
    b9=Button(game,text=" ",font=("Helvetica",20),height=3,width=6,bg='SystemButtonFace', command =lambda : b_click(b9))

    b1.grid(row=1,column=0)
    b2.grid(row=1,column=1)
    b3.grid(row=1,column=2)

    b4.grid(row=2,column=0)
    b5.grid(row=2,column=1)
    b6.grid(row=2,column=2)

    b7.grid(row=3,column=0)
    b8.grid(row=3,column=1)
    b9.grid(row=3,column=2)
    refresh()
    ask_to_change_name()
    rt.mainloop()
# ticTacToe()