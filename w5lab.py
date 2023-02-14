'''
Author  : Chaiyapon Sowanna
STD ID  : 1650702473
Week    : 5
Label   : Lab of Week 5
Desc    : To create a creativity calculator by using Lambda Function and Eval()
Date    : 2023-02-07
'''

from tkinter import *

rosewater = '#E8B4B8'
dustyrose = '#EED6D3'
rosequart = '#FADCD9'
cream = '#F9F1F0'
coral = '#F79489'
coffee = '#67595E'
pot = '#A49393'
lilac = '#D3BBDD'
dusty= '#CEC5C5'

def mainscreen():
    root = Tk()
    root.title("My calculator by Chaiyapon Sowanna")
    root.geometry("400x380")
    root.configure(bg="light green")
    root.rowconfigure((1,2,3,4,5),weight=1)
    root.rowconfigure(0,weight=2)
    root.columnconfigure((0,1,2,3),weight=1)
    return(root)

def framecalculator():

    frame_top = Frame(root,bg='#5DADE2')
    frame_top.grid_propagate(0)
    frame_top.grid(row=0,column=0,columnspan=4,sticky='NEWS')

    frame_left = Frame(root,bg=rosequart)
    frame_left.grid_propagate(0)
    frame_left.grid(row=1,column=0,columnspan=2,rowspan=5,sticky='news')

    frame_right = Frame(root,bg=lilac)
    frame_right.grid_propagate(0)
    frame_right.grid(row=1,column=2,columnspan=2,rowspan=5,sticky='news')

    return(root,frame_top,frame_left,frame_right)

def top_widget(top):
    Label(top, textvariable=input,fg='#fff', font="koharu 40 bold",anchor=CENTER,bg='#5DADE2').grid(row=0,column=0,sticky='news',padx=150,pady=50)


def left_widget(left):
    Button(left,text='AC',bd=2,fg='#fff', bg='#EC1B1B',width=10,height=3,command=lambda:allclear()).grid(row=0,column=0,ipadx=10,sticky=W)
    Button(left,text='Clear',bd=2, fg='#fff', bg='#EC1B1B',width=10,height=3,command=lambda:allclear()).grid(row=0,column=1,ipadx=10,sticky=W)
    Button(left,text='7',bd=2,bg=rosewater,width=10,height=3,command=lambda:buttonsCal('7')).grid(row=1,column=0,ipadx=10,sticky=W)
    Button(left,text='4',bd=2,bg=rosewater,width=10,height=3,command=lambda:buttonsCal('4')).grid(row=2,column=0,ipadx=10,sticky=W)
    Button(left,text='1',bd=2,bg=rosewater,width=10,height=3,command=lambda:buttonsCal('1')).grid(row=3,column=0,ipadx=10,sticky=W)
    Button(left,text='8',bd=2,bg=rosewater,width=10,height=3,command=lambda:buttonsCal('8')).grid(row=1,column=1,ipadx=10,sticky=W)
    Button(left,text='5',bd=2,bg=rosewater,width=10,height=3,command=lambda:buttonsCal('5')).grid(row=2,column=1,ipadx=10,sticky=W)
    Button(left,text='2',bd=2,bg=rosewater,width=10,height=3,command=lambda:buttonsCal('2')).grid(row=3,column=1,ipadx=10,sticky=W)
    Button(left,text='0',width=10,height=3, fg='#fff', bg='#229954',command=lambda:buttonsCal('0')).grid(row=5,column=0,columnspan=2,sticky='news')

def right_widget(right):

    Button(right,text='%',bd=2,bg=rosequart,width=10,height=3, command=lambda:buttonsCal('%')).grid(row=0,column=2,ipadx=10,sticky=E)
    Button(right,text='9',bd=2,bg=rosewater,width=10,height=3, command=lambda:buttonsCal('9')).grid(row=1,column=2,ipadx=10,sticky=E)
    Button(right,text='6',bd=2,bg=rosewater,width=10,height=3, command=lambda:buttonsCal('6')).grid(row=2,column=2,ipadx=10,sticky=E)
    Button(right,text='3',bd=2,bg=rosewater,width=10,height=3, command=lambda:buttonsCal('3')).grid(row=3,column=2,ipadx=10,sticky=E)


    Button(right,text='.',bd=2,bg=rosequart,width=10,height=3,command=lambda:buttonsCal('.')).grid(row=4,column=2,ipadx=10,sticky=E)


    Button(right,text='/',bd=2,bg=rosequart,width=10,height=3,command=lambda:buttonsCal('/')).grid(row=0,column=3,ipadx=10,sticky=E)
    Button(right,text='X',bd=2,bg=rosequart,width=10,height=3,command=lambda:buttonsCal('*')).grid(row=1,column=3,ipadx=10,sticky=E)
    Button(right,text='-',bd=2,bg=rosequart,width=10,height=3,command=lambda:buttonsCal('-')).grid(row=2,column=3,ipadx=10,sticky=E)
    Button(right,text='+',bd=2,bg=rosequart,width=10,height=3,command=lambda:buttonsCal('+')).grid(row=3,column=3,ipadx=10,sticky=E)

    Button(right,text='=',width=10,height=3,fg='#fff', bg='#7D3C98',command=lambda:equal()).grid(row=4,column=3,sticky='news')


def buttonsCal(value):
    global output
    output = output + str(value)
    input.set(output)

    

def allclear():
    global output
    output = ""
    input.set("0.0")

def equal():
    global output
    result=str(eval(output))
    input.set(result)


root = mainscreen()
root,frame_top,frame_left,frame_right = framecalculator()
#spy
input = StringVar()
input.set(0.0)
output = ""


top_widget(frame_top)
left_widget(frame_left)
right_widget(frame_right)

root.mainloop()