import socket
import time
import threading
import tkinter 

root=Tk()
root.config(bg="white")
root.geometry("300*400")
def func():
    t = threading.Thread(target=recv)
    t.start()
  
  
def recv():
    listensocket = socket.socket()
    port=3050
    maxconnection=99
    ip=socket.gethostename()
  
    
    listensocket.blind('',port)
    listensocket.listen(maxconnection)
    (clintsocket,address)=listensocket.accept()
    
    while True:
        sendermessage=clintsocket.recv(1024).decode()
        if not sendermessage=="":
            time.sleep(5)
            lstbx.insert(0,"clint: ",sendmessage)
            
r=0

def sendmsg():
    global r
    if r==0:
       r=socket.socket()
       hostname='LAPTOP-99CROPBF'
       port=4050
       r.connect((hostname,port))
       msg=messagebox.get()
       lstbx.insert(0,"you :"+msg)
       r.send(msg,encode())
       r=r+1
       
    else:
        msg=messagebox.get()
        lstbx.insert(0,"you :"+msg)
        r.send(msg,encode())
        

def threadsending():
    th=threading.Thread(target=sendmsg)
    th.start()
    

startchatimage=photo(file="start.png")

button=button(root,image=startchatimags,command=func,borderwith=2)
button.place(x=90,y=10)

message=stringvar()
messagebox=entry(root,textvariable=message,font=('calibre',10,'normal'),border=2,width=32)
messagebox.place(x=10,y=444)

sendmessageing=photoimage(file='seng.png')

sendmessagebutton=button(root,image=sendmessageing,command=threadsending,borderwidth=0)
sendmessagebutton.place(x=260,y=440)

lstbx=listbox(root,height=20,width=43)
lstbx.place(x=15,y=80)





