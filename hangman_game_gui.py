import random
from tkinter import *
from tkinter import messagebox as m
from word_list import word_list1 as word
from word_list import a_z

def hangman():
    rt  = Toplevel()
    rt.title('HANGMAN GAME')
    rt.geometry('1005x729+350+5')
    rt['bg'] = 'lightblue'
    rt.resizable(0,0)

    bg=PhotoImage(file='h2.png')
    img=Label(rt,image=bg)
    img.place(x=0,y=0)

    top = Frame(rt,bg="black",width=800,height=50,relief=SUNKEN,bd=5)
    top.place(x=80,y=35)
    head=Label(top,font=('aria',30,'bold'),text="                      HANGMAN GAME                      ",bg='lightgray')
    head.grid(row=2,column=0)

    #Guess A Letter
    guess = Frame(rt,bg="lightblue",width=350,height=150,bd=9)
    guess.place(x=120,y=150)
    head2=Label(guess,font=('aria',15,'bold'),text="             GUESS A LETTER             ")
    head2.grid(row=1,column=0)
    screen = Frame(rt,bg="lightgray",width=350,height=100,bd=10,relief=SUNKEN)
    screen.place(x=120,y=210)

    screen_in = Entry(screen,width=22,font=('aria',20,'bold'))
    screen_in.pack()
    submit_btn = Button(screen,text = 'SUBMIT',command = lambda :sub(),width=10,bg='brown',fg='white')
    submit_btn.pack()
    #Pattern
    pattern1 = Frame(rt,bg="lightblue",width=350,height=150,bd=9)
    pattern1.place(x=120,y=350)
    head1=Label(pattern1,font=('aria',15,'bold'),text="                    PATTERN                   ")
    head1.grid(row=1,column=0)
    dis1 = Frame(rt,bg="lightgray",width=350,height=100,bd=10,relief=SUNKEN)
    dis1.place(x=120,y=405)
    lbl1=Label(dis1,font=('aria',15,'bold'),text="",fg='red',width=27,height=3)
    lbl1.grid(row=1,column=0)
    #Chances Remaining
    chances1 = Frame(rt,bg="lightblue",width=350,height=150,bd=9)
    chances1.place(x=520,y=150)
    head2=Label(chances1,font=('aria',15,'bold'),text="          REMAINING CHANCES         ")
    head2.grid(row=1,column=0)
    dis2 = Frame(rt,bg="lightgray",width=350,height=100,bd=10,relief=SUNKEN)
    dis2.place(x=520,y=200)
    lbl2=Label(dis2,font=('aria',15,'bold'),text="0",fg='red',width=27,height=1)
    lbl2.grid(row=1,column=0)

    #Trash/usedletters
    trash1 = Frame(rt,bg="lightblue",width=350,height=150,bd=9)
    trash1.place(x=520,y=275)
    head3=Label(trash1,font=('aria',15,'bold'),text="               USED LETTERS              ")
    head3.grid(row=1,column=0)
    dis3 = Frame(rt,bg="lightgray",width=350,height=100,bd=10,relief=SUNKEN)
    dis3.place(x=520,y=325)
    lbl3=Label(dis3,font=('aria',15,'bold'),text="",fg='red',width=27,height=1)
    lbl3.grid(row=1,column=0)
    #Options
    trash1 = Frame(rt,bg="lightblue",width=350,height=150,bd=9)
    trash1.place(x=520,y=455)
    head3=Label(trash1,font=('aria',15,'bold'),text="                    OPTIONS                   ")
    head3.grid(row=1,column=0)
    dis4 = Frame(rt,bg="lightgray",width=350,height=100,bd=10,relief=SUNKEN)
    dis4.place(x=420,y=515)
    lbl4=Label(dis4,font=('aria',15,'bold'),text="",fg='red',width=45,height=1)
    lbl4.grid(row=1,column=0)

    newgame = Frame(rt,bg="white",width=500,height=500,relief=SUNKEN,bd=5)
    newgame.place(x=270,y=600)
    reset_btn = Button(newgame,text = 'New Game',command = lambda :newGame(),width=60,bg='black',fg='white')
    reset_btn.grid(row=5,column=0)
    #functions
    def newGame():
        head.config(bg='lightgray',fg='black')
        global chances,pattern,trash,new_word,new_word_prs
        new_word = random.choice(word).upper()
        new_word_prs = list(new_word)
        chances = len(new_word)
        pattern = list(chances*'_')
        trash = ''
        opt = new_word
        for _ in range(chances):
            opt += random.choice(a_z).upper()
        options = set(opt)
        lbl2.config(text=str(chances))
        lbl1.config(text=str(' '.join(pattern)))
        lbl4.config(text=str(options))
        lbl3.config(text=str(trash))
        screen_in.delete(0,END)
    def askToPlayAgain():
        y = m.askyesno('NEW GAME',"Woul\'d You Like To Play Again ???")
        if y == 1:
            newGame()
            return 1
        else:
            rt.withdraw()
    def trashF():
        global chances,pattern,trash,new_word,new_word_prs
        char = screen_in.get().upper()
        if len(char)!=1:
            char='!'
        trash+=char
        trash+=' '
        lbl3.config(text=str(trash))#trash updating
        screen_in.delete(0,END)
        chances-=1
        lbl2.config(text=str(chances))
    def sub():
            global chances,pattern,trash,new_word,new_word_prs
            
            char = screen_in.get().upper()
            if len(char) > 1 and char != new_word:
                trashF()
            if char == new_word :
                        lbl1.config(text=str(' '.join(list(new_word))))#pattern updatting
                        head.config(bg='green',fg='white')
                        m.showinfo('** G O T C H A **','YOU WON, \n YOU SAVED HIM ##')
                        askToPlayAgain()
            elif char.isalpha():
                if len(char)==1 :
                    if char in new_word_prs:
                        ind = new_word_prs.index(char)
                        pattern[ind]=char
                        new_word_prs[ind] = '_'
                        screen_in.delete(0,END)
                        lbl1.config(text=str(' '.join(pattern)))#pattern updatting
                    else:
                        trashF()
                else:
                    screen_in.delete(0,END)
                    m.askretrycancel("CHAR COUNT","You Have To Enter A SINGLE CHARACTER !!")
            else:
                m.askretrycancel("NOT AN ALPHABET","You Have To Enter An ALPHABET !!")
            if chances < 1:
                head.config(bg='red',fg='white')
                m.showerror('G A M E  O V E R !!',' Out Of Chances,\n YOU KILLED HIM !!!')
                askToPlayAgain()
            if '_' not in pattern:
                head.config(bg='green',fg='white')
                m.showinfo('** G O T C H A **','YOU WON, \n YOU SAVED HIM ##')
                askToPlayAgain()
    
    newGame()
    rt.mainloop()
# hangman()