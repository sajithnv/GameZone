import random
from tkinter import *
from tkinter import messagebox as m

def rockPaperScissors():
    rt  = Toplevel()
    rt.title('ROCK_PAPER_SCISSORS')
    rt.geometry('1005x729+350+5')
    rt['bg'] = 'lightblue'
    rt.resizable(0,0)

    bg=PhotoImage(file='r1.png')
    img=Label(rt,image=bg)
    img.place(x=0,y=0)

    p_score = 0
    m_score = 0
    n = 1

    top = Frame(rt,bg="black",width=800,height=50,relief=SUNKEN,bd=5)
    top.place(x=50,y=35)
    head=Label(top,font=('aria',30,'bold'),text="                 ROCK_PAPER_SCISSORS                 ")
    head.grid(row=2,column=0)
    #player
    player = Frame(rt,bg="gray",width=350,height=150,bd=9)
    player.place(x=110,y=150)
    head1=Label(player,font=('aria',15,'bold'),text="                     PLAYER                     ")
    head1.grid(row=1,column=0)
    game1 = Frame(rt,bg="red",width=350,height=150,bd=10,relief=SUNKEN)
    game1.place(x=110,y=210)
    pb1=Button(game1,text="    ROCK   ",font=("Helvetica",10),height=3,width=13,bg='SystemButtonFace', command =lambda : bClick('r'))
    pb2=Button(game1,text="   PAPER   ",font=("Helvetica",10),height=3,width=12,bg='SystemButtonFace', command =lambda : bClick('p'))
    pb3=Button(game1,text="  SCISSORS ",font=("Helvetica",10),height=3,width=13,bg='SystemButtonFace', command =lambda : bClick('s'))
    pb1.grid(row=2,column=0)
    pb2.grid(row=2,column=1)
    pb3.grid(row=2,column=2)
    #computer
    comp = Frame(rt,bg="gray",width=350,height=150,bd=9)
    comp.place(x=520,y=150)
    head2=Label(comp,font=('aria',15,'bold'),text="                  COMPUTER                  ")
    head2.grid(row=1,column=0)
    game2 = Frame(rt,bg="red",width=350,height=150,bd=10,relief=SUNKEN)
    game2.place(x=520,y=210)
    cb1=Button(game2,text="    ROCK   ",font=("Helvetica",10),height=3,width=13,bg='SystemButtonFace', command =lambda : bClick('r'),state=DISABLED)
    cb2=Button(game2,text="   PAPER   ",font=("Helvetica",10),height=3,width=12,bg='SystemButtonFace', command =lambda : bClick('p'),state=DISABLED)
    cb3=Button(game2,text="  SCISSORS ",font=("Helvetica",10),height=3,width=13,bg='SystemButtonFace', command =lambda : bClick('s'),state=DISABLED)
    cb1.grid(row=2,column=0)
    cb2.grid(row=2,column=1)
    cb3.grid(row=2,column=2)
    #score_board
    score_board = Frame(rt,bg="black",width=350,height=150,bd=9)
    score_board.place(x=140,y=380)
    head=Label(score_board,font=('aria',15,'bold'),text="                                      LIVE_SCORE_BOARD                                      ")
    head.grid(row=1,column=0)
    score_frame = Frame(rt,bg="lightgray",width=680,height=150,bd=10,relief=SUNKEN)
    score_frame.place(x=140,y=440)
    p_score=Label(score_frame,font=('aria',15,'bold'),text="             PLAYER_SCORE            |",bg='lightgray')
    p_score.grid(row=1,column=0)
    p_score_value=Label(score_frame,font=('aria',15,'bold'),text="0",fg='red',bg='lightgray')
    p_score_value.grid(row=2,column=0)
    c_score=Label(score_frame,font=('aria',15,'bold'),text="|            COMPUTER_SCORE           ",bg='lightgray')
    c_score.grid(row=1,column=1)
    c_score_value=Label(score_frame,font=('aria',15,'bold'),text="0",fg='red',bg='lightgray')
    c_score_value.grid(row=2,column=1)

    newgame = Frame(rt,bg="white",width=500,height=500,relief=SUNKEN,bd=5)
    newgame.place(x=270,y=600)
    reset_btn = Button(newgame,text = 'New Game',command = lambda :refresh(),width=60,bg='black',fg='white')
    reset_btn.grid(row=5,column=0)
    if __name__ == '__main__':
        None if m.askyesno("TIC TAC TOE"," THE MAXIMUM SCORE TO WIN THIS GAME IS # 3\n WOULD YOU LIKE TO CONTINUE ?") else rt.withdraw()
    def bClick(p_choice):
        c_choice = random.choice(['r','p','s'])
        colorMe(p_choice,c_choice) ##color the selected boxes
        if p_choice==c_choice:
            m.showinfo("IT'S A TIE !!!",'Both computer and You choose the SAME OPTION !!!')
        else:
            score(p_choice,c_choice)
        unColorMe(p_choice,c_choice)
    def colorMe(p1,c1):
        if p1=='r':
            pb1.config(bg='lightgreen')
        if p1=='p':
            pb2.config(bg='lightgreen')
        if p1=='s':
            pb3.config(bg='lightgreen')
        if c1=='r':
            cb1.config(bg='lightgreen')
        if c1=='p':
            cb2.config(bg='lightgreen')
        if c1=='s':
            cb3.config(bg='lightgreen')
    def unColorMe(p1,c1):
        if p1=='r':
            pb1.config(bg='SystemButtonFace')
        if p1=='p':
            pb2.config(bg='SystemButtonFace')
        if p1=='s':
            pb3.config(bg='SystemButtonFace')
        if c1=='r':
            cb1.config(bg='SystemButtonFace')
        if c1=='p':
            cb2.config(bg='SystemButtonFace')
        if c1=='s':
            cb3.config(bg='SystemButtonFace')
    def refresh():
        p_score_value.config(text="0")
        c_score_value.config(text="0")
        head1.config(bg="lightblue")
        head2.config(bg="lightblue")
    def newGame():
        y = m.askyesno('NEW GAME',"Woul\'d You Like To Play Again ???")
        if y == 1:
            refresh()
        else:
            rt.withdraw()
    def score(p,c):
        p_score = p_score_value.cget('text')
        c_score = c_score_value.cget('text')
        # r<p and p<s and s<r #player will score
        if (p == 'p' and c == 'r') or (p == 's' and c == 'p') or (p == 'r' and c == 's'):
            # player++
            p_incr = int(p_score)+1
            p_score_value.config(text=str(p_incr))
            if p_incr == 3:
                head1.config(bg="green")
                head2.config(bg="red")
                m.showinfo('CONGRATS !!!','***     YOU WON THE GAME     ***')
                newGame()
            else:
                m.showinfo('SCORE_UPDATED !!!',' You Score ONE POINT :(')
            return 1
        else:
            # computer++
            c_incr = int(c_score)+1
            c_score_value.config(text=str(c_incr))
            if c_incr == 3:
                head1.config(bg="red")
                head2.config(bg="green")
                m.showinfo('GAME OVER !!!',' YOU LOOSE IT !! BETTER LUCK NEXT TIME')
                newGame()
            else:
                m.showinfo('SCORE_UPDATED !!!',' I Score ONE POINT :)')
            return 0
    rt.mainloop()
# rockPaperScissors()