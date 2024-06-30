import socket as s #importing socket

a = s.socket(s.AF_INET,s.SOCK_DGRAM) # making Connection
target_id ="127.0.0.1" # target adderss where we want to send message
port_no = 2525  # it a port number

target_add = (target_id,port_no) # establishing Connection between send er and receiver
print("If You Want To EXIT Form Chat Send Empty Message")

quite = True
while quite: # making infinite foop for sending as much as messages we want to send
    message = input("Enter Your Message : ")

    if message == '': # we want to check if the message is empty or not if its empty the chatapp is exit
        print("Exit Sucessfully !!")
        quite = False
    else:  # it not empty then 
        mess_encript = message.encode('ascii') # the message is encripted
        a.sendto(mess_encript,target_add) # And the message is sent to its destination ()sender side
