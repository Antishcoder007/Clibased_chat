import socket as s # importing some libraries socket
import os  # os library
import datetime as dt # importing datetime


a = s.socket(s.AF_INET,s.SOCK_DGRAM) 
ip_add ="127.0.0.1"
port_no=2525

address = (ip_add,port_no)

a.bind(address)

print("Receiver is Ready to Receive Messages ")
print("Message ==> ip address ==> Date ==> Time")
while True :
    data,addr = a.recvfrom(100) # receive message as data and its address because the message have to parts one is message and one is address part
    message = data.decode() # the data part is decode
    ip_add = addr[0] # seprated ip address store in ip_add
    current_date = dt.datetime.now().strftime('%d-%m-%y') #taking  out date 
    current_time = dt.datetime.now().strftime('%H-%M-%S') #taking out time
    print(f'{message} ==> {ip_add} ==> {current_date} ==> {current_time}') #it will print all the details like message, ip, address date and time 
    
    with open('Data.txt',"a") as file:  # here we are storing messages with their Ip address and daytime in a data.txt file
        file.write(f"\n{message} ==> {ip_add} ==> {current_date} ==> {current_time}")
