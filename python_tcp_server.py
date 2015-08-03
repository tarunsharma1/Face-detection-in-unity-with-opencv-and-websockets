import socket
import sys
import cv2
from base64 import decodestring
import numpy as np
import base64

HOST = 'localhost'   # Symbolic name, meaning all available interfaces
PORT =1234 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
conn, addr = s.accept()
print 'Connected with ' + addr[0] + ':' + str(addr[1]) 
#now keep talking with the client

# fourcc = cv2.cv.CV_FOURCC(*'DIVX')
# out = cv2.VideoWriter('output.avi',-1, 20.0, (640,480))



while 1:
    #wait to accept a connection - blocking call
    print 'top'
    
    #Receiving from client

    length=conn.recv(1024)
    length=int(length)
    #print 'length',length


    k=int(length/1024)
    j=length%1024

    maindata=''
    i=0
    while i<k:
        i=i+1
        data = conn.recv(1024)
        maindata=maindata+data

    if j!=0:    
        data=conn.recv(j)
        maindata=maindata+data

  

    # g = open("out.png", "wb")
    # g.write(maindata.decode('base64'))
    # g.close()


    
    a=maindata.decode('base64')
    nparr = np.fromstring(a, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.CV_LOAD_IMAGE_COLOR)

    gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

    print gray.shape

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if len(faces)>0:
        print 'FFFFFAAAAAAAAAACCCCCCCCCCCCCCEEEEEEEEEEEEEEEEE!!!!!!!!'
        conn.sendall("face")
    # cv2.imshow('frame',img_np)
    # cv2.waitKey(5)
    #out.write(img_np)

    # reply = data
    # print reply
    # if not data: 
    #     break
     
    # conn.sendall(reply)
    # break
s.close()