# -*- coding: utf-8 -*-
"""
Created on Fri May  4 00:35:14 2018

@author: Nikhil Patel
"""

global answer


import tkinter as tk
from tkinter import ttk

def seven():
    s = v.get()
    v.set(s+'7')
    
def eight():
    s = v.get()
    v.set(s+'8')
    
def nine():
    s = v.get()
    v.set(s+'9')
    
def zero():
    s = v.get()
    v.set(s+'0')
    
def one():
    s = v.get()
    v.set(s+'1')
    
def two():
    s = v.get()
    v.set(s+'2')
    
def three():
    s = v.get()
    v.set(s+'3')
    
def four():
    s = v.get()
    v.set(s+'4')
    
def five():
    s = v.get()
    v.set(s+'5')
    

def six():
    s = v.get()
    v.set(s+'6')
    
    
def clear():
    v.set('')
    
def enter():
    # calc here
    temp=''
    comp=''
    op=''
    line = v.get()
    for i in line:
        if(i in '~0123456789.'):
            temp+=i
        if(i in '+-/*'):
            comp+=temp
            temp=''
            op+=i
    
    #if(comp == ''):
        
    first= float(comp) 
    second = float(temp)
    
    #if(first == 2 and second == 2 )
    
    if(op == '+'):
        answer = first+second
    if(op == '-'):
        answer = first-second
    if(op == '/'):
        answer = first/second
    if(op == '*'):
        answer = first*second
    
    if(answer==3):
        v.set("Quick maths")
    else:
    #output
        v.set(answer)
        
        
def dot():
    s = v.get()
    v.set(s+'.')
    
def plus():
    s = v.get()
    v.set(s+'+')
    
def minus():
    s = v.get()
    v.set(s+'-')
    
def multiple():
    s = v.get()
    v.set(s+'*')
    
def divide():
    s = v.get()
    v.set(s+'/')
    
def negative():
    s = v.get()
    v.set(s+'~')
    
def backspace():
    s = v.get()
    v.set(s[:-1])

win = tk.Tk()

ttk.Label(win, text= 'Meme Calculator:').grid(column=0, row=0)
ttk.Label(win, text= '').grid(column=0, row=1)

v = tk.StringVar()
e = tk.Entry(win, textvariable=v).grid(column=1, row=2)

ttk.Label(win, text= ' ').grid(column=0, row=3)
ttk.Label(win, text= ' ').grid(column=0, row=4)

# layout
ttk.Button(win, text = "7", command = lambda:seven()).grid(column=0, row=6)
ttk.Button(win, text = "8", command = lambda:eight()).grid(column=1, row=6)
ttk.Button(win, text = "9", command = lambda:nine()).grid(column=2, row=6)
ttk.Button(win, text = "1", command = lambda:one()).grid(column=0, row=8)
ttk.Button(win, text = "2", command = lambda:two()).grid(column=1, row=8)
ttk.Button(win, text = "3", command = lambda:three()).grid(column=2, row=8)
ttk.Button(win, text = "4", command = lambda:four()).grid(column=0, row=7)
ttk.Button(win, text = "5", command = lambda:five()).grid(column=1, row=7)
ttk.Button(win, text = "6", command = lambda:six()).grid(column=2, row=7)
ttk.Button(win, text = "0", command = lambda:zero()).grid(column=1, row=9)
#clear
ttk.Button(win, text = "Clear", command = lambda:clear()).grid(column=0, row=5)
#enter
ttk.Button(win, text = "=", command = lambda:enter()).grid(column=4, row=9)
# . 
ttk.Button(win, text = ".", command = lambda:dot()).grid(column=2, row=9)
# +
ttk.Button(win, text = "+", command = lambda:plus()).grid(column=4, row=8)
# -
ttk.Button(win, text = "-", command = lambda:minus()).grid(column=4, row=7)
# /
ttk.Button(win, text = "/", command = lambda:divide()).grid(column=4, row=5)
# x
ttk.Button(win, text = "x", command = lambda:multiple()).grid(column=4, row=6)
# - 
ttk.Button(win, text = "-", command = lambda:negative()).grid(column=0, row=9)
# backspace
ttk.Button(win, text = "<x|", command = lambda:backspace()).grid(column=2, row=5)
#bs
ttk.Button(win, text = "C", command = lambda:clear()).grid(column=1, row=5)
          
v.set("")



win.title("Calculator")
win.geometry('{}x{}'.format(400, 250))
win.mainloop()
