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
    label_t1.config(text=f'{box_1.get()}x 1 = {int(box_1.get())*1}', font=30)
    label_t2.config(text=f'{box_1.get()}x 2 = {int(box_1.get())*2}', font=30)
    label_t2.config(text=f'{box_1.get()}x 3 = {int(box_1.get())*3}', font=30)
    label_t3.config(text=f'{box_1.get()}x 4 = {int(box_1.get())*4}', font=30)
    label_t4.config(text=f'{box_1.get()}x 5 = {int(box_1.get())*5}', font=30)
    label_t5.config(text=f'{box_1.get()}x 6 = {int(box_1.get())*6}', font=30)
    label_t6.config(text=f'{box_1.get()}x 7 = {int(box_1.get())*7}', font=30)
    label_t7.config(text=f'{box_1.get()}x 8 = {int(box_1.get())*8}', font=30)
    label_t8.config(text=f'{box_1.get()}x 9 = {int(box_1.get())*9}', font=30)
    label_t9.config(text=f'{box_1.get()}x 10 = {int(box_1.get())*10}', font=30)
    label_t10.config(text=f'{box_1.get()}x 11 = {int(box_1.get())*11}', font=30)
    label_t11.config(text=f'{box_1.get()}x 12 = {int(box_1.get())*12}', font=30)
    label_t12.config(text=f'{box_1.get()}x 13 = {int(box_1.get())*13}', font=30)

    box_1.delete(0,'end')


label_t1 = Label(w2)
label_t1.pack(side=TOP,anchor=NW,padx=15,pady=15)
label_t2 = Label(w2)
label_t2.pack(side=TOP,anchor=NW,padx=15,pady=15)
label_t3 = Label(w2)
label_t3.pack(side=TOP,anchor=NW,padx=15,pady=15)
label_t4 = Label(w2)
label_t4.pack(side=TOP,anchor=NW,padx=15,pady=15)
label_t5 = Label(w2)
label_t5.pack(side=TOP,anchor=NW,padx=15,pady=15)
label_t6 = Label(w2)
label_t6.pack(side=TOP,anchor=NW,padx=15,pady=15)
label_t7 = Label(w2)
label_t7.pack(side=TOP,anchor=NW,padx=15,pady=15)
label_t8 = Label(w2)
label_t8.pack(side=TOP,anchor=NW,padx=15,pady=15)
label_t9 = Label(w2)
label_t9.pack(side=TOP,anchor=NW,padx=15,pady=15)
label_t10 = Label(w2)
label_t10.pack(side=TOP,anchor=NW,padx=15,pady=15)
label_t11 = Label(w2)
label_t11.pack(side=TOP,anchor=NW,padx=15,pady=15)
label_t12 = Label(w2)
label_t12.pack(side=TOP,anchor=NW,padx=15,pady=15)

btn_1 = Button(w1,text= 'AGGREGETE',command=multiplication_tabel)
btn_1.pack(side=LEFT,padx=10,pady=10,fill='both',expand='yes')






cal_muliti.overrideredirect(1)
cal_muliti.title('multiplication_table')
cal_muliti.geometry('850x850')
cal_muliti.mainloop()
