'''
Author  : Chaiyapon Sowanna
STD ID  : 1650702473
Week    : 5
Label   : Class Activity
Desc    : Creating widgets using loop and event handling.
Date    : 2023-02-07
'''

from tkinter import *

def mainwindow() :
    root = Tk()
    root.title("GUI5: Class Activity of Week5")
    root.geometry("600x400")
    root.configure(bg='lightgreen')
    root.rowconfigure((0,2),weight=1)
    root.rowconfigure(1,weight=4)
    root.columnconfigure(0,weight=1)
    root.columnconfigure(1,weight=1)
    return(root)

def createframe(root) :
    top = Frame(root,bg='#694E4E')
    left = Frame(root,bg='#F3C5C5')
    left.rowconfigure((0,1,2,3,4,5),weight=1)
    left.columnconfigure((0,1),weight=1)
    right = Frame(root,bg='#886F6F')
    right.rowconfigure((0,1,2,3,4,5),weight=1)
    right.columnconfigure((0,1),weight=1)
    bottom = Frame(root,bg='#694E4E')
    bottom.rowconfigure(0,weight=1)
    bottom.columnconfigure((0,1),weight=1)
    top.grid(row=0,columnspan=2,sticky='news')
    left.grid(row=1,column=0,sticky='news')
    right.grid(row=1,column=1,sticky='news')
    bottom.grid(row=2,columnspan=2,sticky='news')
    return(root,top,left,right,bottom)

def widgettop(top) : 
    Label(top,text="Little Dream House Cafe by 1650702473",fg='white',font=("Helvetica", "20"),bg="#694E4E",pady=10).pack()

def widgetleft(left) :
    cakemenu = ["Stawberry Cake\n125 B.","Cheese Cake\n110 B.","Babybloom Cake\n140 B.","Chocolate Cake\n100 B."]

    # TODO: 1 To create widgets by cakemenu.
    #  Hint! YOUR CODE
    #  1. ใช้ for loop ในการสร้าง Label สำหรับแสดงรูป และ Checkbox สำหรับเลือกรายการ โดยทั้งสองจัดวาง widget ด้วย grid()
    for i in range(len(cakelist)):
        lbl_profile = Label(left, image=cakelist[i], height=80, bg="#F3C5C5")
        lbl_profile.grid(row=i, column=0)
    #  2. สร้าง widget ในแต่ละแถว โดยเริ่มจากแถวที่ 0 (แถวบน)
    #  3. widget แต่ละตัว เมื่อถูกคลิก จะต้องเรียกฟังก์ชัน find_summary() เพื่อคำนวณ พร้อมแสดงผลลัพธ์
    
    c1 = [IntVar() for i in cakemenu]
    for i in range(len(cakemenu)):
        Checkbutton(left, text=cakemenu[i], variable=c1[i],bg="#F3C5C5", command=find_summary).grid(row=i,column=1,sticky='W')
    # 
    #  YOUR CODE
    # 
    return(c1)

def widgetright(right) :
    coffeemenu = ["Hot Latte\n80 B.","Hot Cappuccino\n70 B.","Hot Caramel Latte\n100 B.","Hot Chocolate\n90 B."]

    for i in range(len(coffeelist)):
        lbl_profile = Label(right, image=coffeelist[i], height=80, bg="#886F6F")
        lbl_profile.grid(row=i, column=0)
    # TODO 2: To create widgets by coffeemenu
    #  Hint! YOUR CODE
    #  ใช้ for loop ในการสร้าง Label สำหรับแสดงรูป และ Checkbox สำหรับเลือกรายการ โดยจัดวาง widget ด้วย grid()
    #  สร้าง widget ในแต่ละแถว โดยเริ่มจากแถวที่ 0 (แถวบน)
    #  widget แต่ละตัว เมื่อถูกคลิก จะต้องเรียกฟังก์ชัน find_summary() เพื่อคำนวณ พร้อมแสดงผลลัพธ์

    c2 = [IntVar() for i in coffeemenu]
    for i in range(len(coffeemenu)):
        Checkbutton(right, text=coffeemenu[i], variable=c2[i],bg="#886F6F", command=find_summary).grid(row=i,column=1,sticky='W')
    return(c2)

def widgetbottom(bottom) :
    showcake = Label(bottom,textvariable=cakespy,bg='#694E4E',font=("Helvetica", "12","bold"))
    showcake.grid(row=0,column=0,ipady=5,pady=5)
    showcoff = Label(bottom,textvariable=coffspy,bg='#694E4E',font=("Helvetica", "12","bold"))
    showcoff.grid(row=0,column=1,ipady=5,pady=5)
    return(showcake,showcoff)

def find_summary() :
    global c1net
    global c2net
    c1net = 0
    c2net = 0
    cakeprice = [125,110,140,100]
    coffprice = [80,70,100,90]

    # TODO 3 : ใช้ for loop เพื่อคำนวณค่าใช้จ่าย โดยใช้ cakelist ในการวนหา ผลรวมของ cake และ coffee
    # YOUR CODE
    
    for i in range(len(cakeprice)):
        # print()
        if c1[i].get():
            c1net += cakeprice[i]
        if c2[i].get():
            c2net += coffprice[i]


    # TODO 4 : 
    # กำหนดสีพื้นหลัง และสีตัวอักษรให้สวยงาม
    # นำผลลัพธ์ c1net และ c2net ไปใช้ในการจัด string format ให้กับ spy ทั้งสอง


    showcake["bg"] = "#694E4E"
    showcake["fg"] = "#FFFF00"
    cakespy.set("Cake Total Amount = %0.2f Bahts."%(c1net))

    showcoff["bg"] = "#694E4E"
    showcoff["fg"] = "#FFFF00"
    coffspy.set("Coffee Total Amount = %0.2f Bahts."%(c2net))


root = mainwindow()


cake1 = PhotoImage(file='image/cake1.png')
cake2 = PhotoImage(file='image/cake2.png')
cake3 = PhotoImage(file="image/cake3.png")
cake4 = PhotoImage(file="image/cake4.png")
coffee1 = PhotoImage(file="image/coffee1.png")
coffee2 = PhotoImage(file="image/coffee2.png")
coffee3 = PhotoImage(file="image/coffee3.png")
coffee4 = PhotoImage(file="image/coffee4.png")

cakelist = [cake1,cake2,cake3,cake4]

coffeelist = [coffee1,coffee2,coffee3,coffee4]
root,top,left,right,bottom = createframe(root)
widgettop(top)
c1 = widgetleft(left)
c2 = widgetright(right)
cakespy,coffspy = StringVar(),StringVar()
showcake,showcoff = widgetbottom(bottom)


root.mainloop()