#---------------------------------------
# Arduino-Python Ethernet Communication
#---------------------------------------
from os import *; system('cls')
from tkinter import *
#--------------------------------------------------------
from socket import *
address = ('192.168.1.177', 8888)
s = socket(AF_INET, SOCK_DGRAM)
s.settimeout(1)
#--------------------------------------------------------
def TxArduino():
    outMsg.delete('1.0', END)
    msgWR = inMsg.get()
    s.sendto(bytes(msgWR, 'utf-8'), address)
    try:
        msgRD, addr = s.recvfrom(2048)
        outMsg.insert(END, msgRD)
    except:
        outMsg.insert(END, 'TRANSMISSION ERROR')
#--------------------------------------------------------
def clrDisp():
    inMsg.delete('0', END)
    outMsg.delete('1.0', END)
#------------------------------------------------------------------------------------
win = Tk();
win.title('Arduino-Python Ethernet Comm');
win.minsize(350, 160)

label = Label(text='Transmitted message to Arduino', font='calibri')
label.pack()

inMsg = Entry(width=25, font='calibri 12 bold', fg='red')
inMsg.pack()

btn = Button(text=' Transmit ', font='calibri 12 bold', bg='#FF6666', command=TxArduino)
btn.pack()

label = Label(text='Received message from Arduino', font='calibri')
label.pack()

outMsg = Text(width=25, height=1, font='calibri 12 bold', fg='blue')
outMsg.pack()

clrBtn = Button(text=' Clear ', bg='#ADD8E6', command=clrDisp)
clrBtn.pack()

win.mainloop()