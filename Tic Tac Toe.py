from turtle import *
class game:
    check={'y':[False,None],'u':[False,None],'i':[False,None],'h':[False,None],'j':[False,None],'k':[False,None],'n':[False,None],'m':[False,None],',':[False,None]}
    def check_plots(self):
        g=True
        p=u=0
        for q in self.check:
            if self.check[q]==[g,'user']:
                u=u+1
            elif self.check[q]==[g,'pc']:
                p=p+1
        return (u,p)
    def lock(self,l,person):
        for i in self.check:
            if i==l:
                self.check[i][0]=True
                self.check[i][1]=person
                break
    def check_avail(self,l):
        if self.check[l][0]==False:
            return True
        else:
            return False
    def putin(self,l):
        if l=='y':
            penup()
            goto(50,30)
            pendown()
            circle(25)
            return True
        elif l=='u':
            penup()
            goto(115,30)
            pendown()
            circle(25)
            return True
        elif l=='i':
            penup()
            goto(175,30)
            pendown()
            circle(25)
            return True
        elif l=='h':
            penup()
            goto(50,-30)
            pendown()
            circle(25)
            return True
        elif l=='j':
            penup()
            goto(115,-30)
            pendown()
            circle(25)
            return True
        elif l=='k':
            penup()
            goto(175,-30)
            pendown()
            circle(25)
            return True
        elif l=='n':
            penup()
            goto(50,-90)
            pendown()
            circle(25)
            return True
        elif l=='m':
            penup()
            goto(115,-90)
            pendown()
            circle(25)
            return True
        elif l==',':
            penup()
            goto(175,-90)
            pendown()
            circle(25)
            return True
    def draw(self,i,person):
        if self.check_avail(i):
            self.lock(i,person)
            return self.putin(i)
    def cons(self,a,b,c,v):
        if self.check[a]==v and self.check[b]==v:
            return self.draw(c,'pc')
    def res(self,per):
        c=[True,per]
        if self.check['y']==c and self.check['h']==c and self.check['n']==c:
            penup()
            goto(30,60)
            pendown()
            goto(30,-120)
            return False
        elif self.check['y']==c and self.check['u']==c and self.check['i']==c:
            penup()
            goto(0,30)
            pendown()
            goto(180,30)
            return False
        elif self.check['y']==c and self.check['j']==c and self.check[',']==c:
            penup()
            goto(0,60)
            pendown()
            goto(180,-120)
            return False
        elif self.check['i']==c and self.check['j']==c and self.check['n']==c:
            penup()
            goto(180,60)
            pendown()
            goto(0,-120)
            return False
        elif self.check['i']==c and self.check['k']==c and self.check[',']==c:
            penup()
            goto(120,60)
            pendown()
            goto(120,-120)
            return False
        elif self.check['n']==c and self.check['m']==c and self.check[',']==c:
            penup()
            goto(0,-90)
            pendown()
            goto(180,-90)
            return False
        elif self.check['h']==c and self.check['j']==c and self.check['k']==c:
            penup()
            goto(0,-30)
            pendown()
            goto(180,-30)
            return False
        elif self.check['u']==c and self.check['j']==c and self.check['m']==c:
            penup()
            goto(90,60)
            pendown()
            goto(90,-120)
            return False
        else:
            return True
    def win(self):
        v=[True,'pc']
        begin_fill()
        fillcolor('black')
        if self.cons('y','i','u',v):
            end_fill()
            return True
        elif self.cons('y','n','h',v):
            end_fill()
            return True
        elif self.cons('y',',','j',v):
            end_fill()
            return True
        elif self.cons('n',',','m',v):
            end_fill()
            return True
        elif self.cons('i',',','k',v):
            end_fill()
            return True
        elif self.cons('i','n','j',v):
            end_fill()
            return True
        elif self.cons('h','k','j',v):
            end_fill()
            return True
        elif self.cons('u','m','j',v):
            end_fill()
            return True
        elif self.cons('y','u','i',v):
            end_fill()
            return True
        elif self.cons('u','i','y',v):
            end_fill()
            return True
        elif self.cons('i','k',',',v):
            end_fill()
            return True
        elif self.cons('k',',','i',v):
            end_fill()
            return True
        elif self.cons('m',',','n',v):
            end_fill()
            return True
        elif self.cons('n','m',',',v):
            end_fill()
            return True
        elif self.cons('n','h','y',v):
            end_fill()
            return True
        elif self.cons('y','h','n',v):
            end_fill()
            return True
        elif self.cons('y','j',',',v):
            end_fill()
            return True
        elif self.cons('j',',','y',v):
            end_fill()
            return True
        elif self.cons('i','j','n',v):
            end_fill()
            return True
        elif self.cons('j','n','i',v):
            end_fill()
            return True
        elif self.cons('h','j','k',v):
            end_fill()
            return True
        elif self.cons('j','k','h',v):
            end_fill()
            return True
        elif self.cons('u','j','m',v):
            end_fill()
            return True
        elif self.cons('j','m','u',v):
            end_fill()
            return True
        else:
            end_fill()
            return False
    def defend(self):
        v=[True,'user']
        begin_fill()
        fillcolor('black')
        if self.cons('y','i','u',v):
            end_fill()
            return True
        elif self.cons('y','n','h',v):
            end_fill()
            return True
        elif self.cons('y',',','j',v):
            end_fill()
            return True
        elif self.cons('n',',','m',v):
            end_fill()
            return True
        elif self.cons('i',',','k',v):
            end_fill()
            return True
        elif self.cons('i','n','j',v):
            end_fill()
            return True
        elif self.cons('h','k','j',v):
            end_fill()
            return True
        elif self.cons('u','m','j',v):
            end_fill()
            return True
        elif self.cons('h','m','n',v):
            end_fill()
            return True
        elif self.cons('m','k',',',v):
            end_fill()
            return True
        elif self.cons('u','k','i',v):
            end_fill()
            return True
        elif self.cons('h','u','y',v):
            end_fill()
            return True
        elif self.cons('y','u','i',v):
            end_fill()
            return True
        elif self.cons('u','i','y',v):
            end_fill()
            return True
        elif self.cons('i','k',',',v):
            end_fill()
            return True
        elif self.cons('k',',','i',v):
            end_fill()
            return True
        elif self.cons('m',',','n',v):
            end_fill()
            return True
        elif self.cons('n','m',',',v):
            end_fill()
            return True
        elif self.cons('n','h','y',v):
            end_fill()
            return True
        elif self.cons('y','h','n',v):
            end_fill()
            return True
        elif self.cons('y','j',',',v):
            end_fill()
            return True
        elif self.cons('j',',','y',v):
            end_fill()
            return True
        elif self.cons('i','j','n',v):
            end_fill()
            return True
        elif self.cons('j','n','i',v):
            end_fill()
            return True
        elif self.cons('h','j','k',v):
            end_fill()
            return True
        elif self.cons('j','k','h',v):
            end_fill()
            return True
        elif self.cons('u','j','m',v):
            end_fill()
            return True
        elif self.cons('j','m','u',v):
            end_fill()
            return True
        else:
            end_fill()
            return False
    def sys(self):
        begin_fill()
        fillcolor('black')
        if self.check['j']==[False,None]:
            if self.draw('j','pc')==True:
                end_fill()
                return True
        elif True:
            a,b=self.check_plots()
            if self.check['n']==[False,None] and a+b==1:
                if self.draw('n','pc')==True:
                    end_fill()
                    return True
            elif True:
                if a+b>=3 and a+b<=7:
                    if self.draw('i','pc')==True:
                        end_fill()
                        return True
                    elif self.draw(',','pc')==True:
                        end_fill()
                        return True
                    elif self.draw('n','pc')==True:
                        end_fill()
                        return True
                    elif self.draw('y','pc')==True:
                        end_fill()
                        return True
def play():
    hey=True
    w=False
    p=game()
    while hey:
        try:
            ins=input("Your Turn: ").lower()
        except:
            pass
        else:
            if (ins=='y' or ins=='u' or ins=='i' or ins=='h' or ins=='j' or ins=='k' or ins=='n' or ins=='m' or ins==',') and p.check_avail(ins):
                p.draw(ins,'user')
                if p.win()==True:
                    pass
                elif p.defend()==True:
                    pass
                elif p.sys()==True:
                    pass
                p1=p.res('user')
                p2=p.res('pc')
                hey=p1 and p2
                x,y=p.check_plots()
                if x+y==9 and (p1 and p2):
                    w=True
                    break
                else:
                    pass
            else:
                pass
    state="User" if p1==False else "It's a Draw" if w==True else "Computer"
    print('Winner is',state) if p1==True and w==False else print('Its a Draw')
    penup()
    goto(-290,130)
    write('Winner',font=('Lao UI',12,'normal'))
    goto(-290,105)
    write(state,font=('Times New Roman',18,'normal'))
    goto(-320,-160)
    write('Created by,',font=('Arial',14,'normal'))
    goto(-320,-167)
    write('                                                           ___',font=('FrankRuehl',20,'normal'))
    goto(-320,-195)
    write('           J Maria Irudaya Regilan ., B.E (CS)',font=('FrankRuehl',20,'normal'))
    goto(-320,-215)
    write('                 Follow him @ www.regilanj.wordpress.com',font=('Footlight MT Light',12,'normal'))
    print("\nCoded by, J. Maria Irudaya Regilan ., B.E (CS)")
    print("Get him @ www.regilanj.wordpress.com")
    ch=input("Enter any key to close...")
def plate():
    penup()
    goto(175,-260)
    write('Version RS01',font=('Lucida Calligraphy',14,'normal'))
    penup()
    goto(-335,-265)
    pendown()
    goto(-335,275)
    goto(320,275)
    goto(320,-265)
    goto(-335,-265)
    penup()
    bgcolor('lightcyan')
    goto(0,0)
    pendown()
    forward(180)
    backward(60)
    left(90)
    forward(60)
    backward(180)
    forward(120)
    backward(60)
    right(90)
    forward(60)
    backward(180)
    forward(60)
    left(90)
    forward(120)
    backward(180)
    penup()
    goto(-150,220)
    write('Tic Tac Toe',font=('Arial',30,'normal'))
    goto(-180,200)
    write('Place your choice in the manner  Y    U    I')
    goto(-180,185)
    write('                                                      H    J    K')
    goto(-180,170)
    write('                                                      N    M    ,')
    play()
print("TIC TAC TOE Input Panel\nVersion RS01")
print("\nYour input to draw --> \n\t\t\t\tY     U     I\n\t\t\t\tH     J     K\n\t\t\t\tN     M     ,")
print("\nPress the key and give 'enter' to draw when your turn comes")
print("Don't forget!! You are going to play against the computer.")
print("\nPost your Experience at www.facebook.com/jrtinst/\n")
plate()