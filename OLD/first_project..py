import random
import time
import os
import tkinter as tk
import sys
import matplotlib.pyplot as plt
import numpy as np
p=0
k=20
high=0
ti=0
flag=True#loop
flag2=True#epiloges loop
flag3=True#epilogh high score
try:
    f=open("high_score.txt",
           "xt")
    f.write("ONOMA   SCORE")
    f.close()
    f.open("high_score.txt",
            "rt")
except:
    f=open("high_score.txt",
           "rt")
def high_score():
    global high
    high=int(dysk*p/(ti/typos/1000))
    return high
on=str(input("dwse onoma:"))
while on.isalpha==False or (len(on)<=15)==False:
    print("-------------------------------------------------------------------\nto onoma prepei na einai latinikoi xarakthres kai mexri 15 grammata\ndwse onoma\n-------------------------------------------------------------------")
    on=str(input())
on=on.upper()
fi=str(f.read())
if fi!=None and on not in fi:
    f.close()
    f=open("high_score.txt",
           "at")
    f.write("\n")
    f.write(on)
    f.write(" 0")
    f.close()
try:
    while flag:
        print("\nepiloges:")
        print("1.addition\n2.multiplication\n3.division\n4.high score\n5.telos paixnidiou")
        while flag2==True:
            try:
                typos=int(input("typos paixnidiou:"))
                flag2=False
            except ValueError:
                print("---------------------------------\nprepei na einai arithmos arithmos\n---------------------------------")
        flag2=True
        if typos>=1 and typos<=4:
            if typos==4:
                while flag3==True:
                    try:
                        out=str(input("text/graph:"))
                        flag3=False
                    except ValueError or (out!="text" and out!="graph"):
                        print("prepei na einai text h graph")
                flag3=True
#elegxei an exoun dw8ei arithmoi h kapoia la8os epilogh sto out kai to empodizei
                if out=="graph":
                    n=-1
                    z=np.array([])
                    u=np.array([])
                    v=np.array([])
                    f=open("high_score.txt","rt")
                    fi=str(f.read())
                    f.close()
                    fi=fi[14:]
                    filist=fi.splitlines()
                    for i in filist:
                        fisub=fi.rsplit()
                        fisubit=iter(fisub)
                        n+=1
                        z=np.append(z,
                                    [str(fisub[n])])
                        n+=1
                        u=np.append(u,
                                    [int(fisub[n])])
                        n+=1
                        v=np.append(v,
                                    [str(fisub[n])])
                    n=-1
                    plt.title("Score")
                    plt.bar(z,u,
                            color="#33cc33")
                    plt.show()
                elif out=="text":
                    print(fi)
                plt.close()
                out=None
            else:
                print("\ndyskolia paixnidiou")
                dysk=int(input("(1-9):"))
                turn=int(input("arithmos prajewn:"))
                start_time=time.time()
                p=0
                for r in range(turn):
                    if typos==1:
                        x=dysk*(random.randrange(-20,20))
                        y=dysk*(random.randrange(-20,20))
                        time.sleep(0.4)
                        if y>=0:
                            print(x,"+",y,":")
                        else:
                            print(x,y,":")
                        z=int(input())
                        if z==(x+y):
                            print("swsto")
                            p+=1
                        else:
                            print("lathos")
                            print("H swsth apanthsh einai",x+y)
                            p-=1
                    elif typos==2:
                        x=dysk*(random.randrange(-40,40))
                        y=dysk*(random.randrange(-40,40))
                        time.sleep(0.4)
                        if y>=0:
                            print(x,"*",y,":")
                        else:
                            print(x,"*","(",y,")",":")
                        z=int(input())
                        if z==(x*y):
                            print('swsto')
                            p+=1
                        else:
                            print("lathos")
                            print("H swsth apanthsh einai",x*y)
                            p-=1
                    elif typos==3:
                        x=dysk*(random.randrange(-20,20))
                        y=dysk*(random.randrange(-15,15))
                        while y==0:
                            y=dysk*(random.randrange(-15,15))
                        x=x*y
                        time.sleep(0.4)
                        if y>=0:
                            print(x,"/",y,":")
                        else:
                            print(x,"/","(",y,")",":")
                        z=int(input())
                        if z==(x/y):
                            print('swsto')
                            p+=1
                        else:
                            print("lathos")
                            print("H swsth apanthsh einai",x/y)
                            p-=1               
                else:
                    print("Oi pontoi sou einai",(p))
                    print("O xronos sou htan","--- %s seconds ---" % (int(time. time() - start_time - 0.4*turn)))
                    ti=int(time. time() - start_time - 0.4*turn)
                    if ti==0:
                        ti=1
                    f=open("high_score.txt",
                           "rt")
                    fi=str(f.read())
                    position=fi.find(on)
                    f.close()
                    
                    le2=len(on)#mege8os onomatos
                    fi1=fi[:position-1]#mexri to score
                    fi2=fi[position:position+le2]#onoma
                    fi3=fi[position+le2+1:position+le2+1+k]
                    while fi3.isdigit()==False:
                        k-=1
                        fi3=fi[position+le2+1:position+le2+k]#score
                    h=int(float(fi[position+le2+1:position+le2+k]))
                    le3=len(fi3)
                    fi4=fi[le2+le3+position+2:]#meta score
                    high_score()
                    if h<high:
                        fi3=fi3.replace(fi3,str(high))
                    fi=fi1+"\n"+fi2+" "+fi3+"\n"+fi4
                    
                    open("high_score.txt","wt")
                    f=open("high_score.txt","wt")
                    f.write(fi)
                    f.close()
                    time.sleep(1)               
        elif typos==5:
            epil=str(input("eisai sigouros:\n----\nnai.\n----\noxi.\n----"))
            if epil=="nai":
                f.close()
                flag=False
        else:
            print("--------------\nlathos epilogh\n--------------")
        time.sleep(0.4)

except KeyboardInterrupt:
    f.close()
    sys.exit()
