from tkinter import *
from tkinter import ttk

#ปรกาศตัวแปรสำหรับ TKinter
cal_muliti = Tk()
tab_1=ttk.Notebook(cal_muliti)
tab_1.pack(fill='both',expand='yes')
#สร้าง เฟรม สำหรับแบ่งหน้าจอ
Frame_1 = Frame(tab_1)
Frame_1.pack(fill='both', expand='yes')
Frame_2 = Frame(tab_1)
Frame_2.pack(fill='both',expand='yes')
#กำหนด LabelFrame
w1 = LabelFrame(Frame_1, text='Input Number')
w1.pack(fill='both', expand='NO', padx=10, pady=10)
w2 = LabelFrame(Frame_2,text='แม่สูตรคูณ',font=20)
w2.pack(fill='both',expand ='yes',padx=10,pady=10)

#คอนโทรลดาด้า
label_t1 = Label(w1, text="Input Number : ")
label_t1.pack(side = LEFT,padx=10,pady=10,anchor=NW)
box_1 = Entry(w1)
box_1.pack(side=LEFT,padx=10,pady=10)


#ฟังก์ชันแม่สูตรคูณ
global count
count = 1
def multiplication_tabel():
    global count
    for x in range(1,12):
        x_1= int(box_1.get()) * count
        print(f'{box_1.get()}x{count} = {x_1}')
        count+=1

label_t1 = Label(w2)
label_t1.pack(side=LEFT,anchor=NW)
label_t2 = Label(w2)
label_t2.pack(side=LEFT,anchor=NW)
label_t3 = Label(w2)
label_t3.pack(side=LEFT,anchor=NW)
label_t4 = Label(w2)
label_t4.pack(side=LEFT,anchor=NW)
label_t5 = Label(w2)
label_t5.pack(side=LEFT,anchor=NW)
label_t6 = Label(w2)
label_t6.pack(side=LEFT,anchor=NW)
label_t7 = Label(w2)
label_t7.pack(side=LEFT,anchor=NW)
label_t8 = Label(w2)
label_t8.pack(side=LEFT,anchor=NW)
label_t9 = Label(w2)
label_t9.pack(side=LEFT,anchor=NW)
label_t10 = Label(w2)
label_t10.pack(side=LEFT,anchor=NW)
label_t11 = Label(w2)
label_t11.pack(side=LEFT,anchor=NW)
label_t12 = Label(w2)
label_t12.pack(side=LEFT,anchor=NW)

btn_1 = Button(w1,text= 'AGGREGETE',command=multiplication_tabel)
btn_1.pack(side=LEFT,padx=10,pady=10,fill='both',expand='yes')







cal_muliti.title('multiplication_table')
cal_muliti.geometry('850x850')
cal_muliti.mainloop()
