import tkinter as tk
from tkinter import *

dic = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}
                    
def encrpt():
    a=input1.get()
    b=a.upper()
    ciper=""
    for i in b:
        if i != ' ':
            ciper=ciper+dic[i]+' '
        else:
            ciper+=' '
        var.set(ciper)

def decrpt():
    a1=input2.get()
    a1+=" "
    decp=''
    ctext=''
    for j in a1:
        if j!=' ':
            k=0
            ctext+=j
        else:
            k+=1
            if k==2:
                decp+=' '
            else:
                decp+=list(dic.keys())[list(dic.values()).index(ctext)]
                ctext=''
        var1.set(decp)

app=tk.Tk()
app.geometry("500x500")
app.title("MORSE_CODE TRANSLATOR USING tkinter")

var= StringVar()
var1=StringVar()

head1=tk.Label(app,text='MORSE_DECRPYT_AND_ENCRYPT')
head1.pack()

head2=tk.Label(app,text='ENCRYPTER: ')
head2.place(x=40,y=24)

input1=tk.Entry(app)
input1.place(x=160,y=100)

B1=tk.Button(app, text ="CLICK TO ENCRYPT",command=encrpt)
B1.place(x=160,y=125)

output1=tk.Label(app,text='',textvariable=var)
output1.place(x=160,y=160)

LINEE=tk.Label(app,text='___________________________________________________________________________________')
LINEE.place(x=40,y=200)

head3=tk.Label(app,text='DECRYPTER: ')
head3.place(x=40,y=260)

input2=tk.Entry(app)
input2.place(x=160,y=300)

B2=tk.Button(app, text ="CLICK TO DECRYPT",command = decrpt)
B2.place(x=160,y=330)

output2=tk.Label(app,text='dsfd',textvariable=var1)
output2.place(x=160,y=357)

LINEE=tk.Label(app,text='___________________________________________________________________________________')
LINEE.place(x=40,y=450)

tk.mainloop()
