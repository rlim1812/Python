import socket

#create a socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connect to host "www.pythonlearn.com's" port #80
mysock.connect(("www.pythonlearn.com", 80))
message = "GET http://www.pythonlearn.com/code/intro-short.txt HTTP/1.0\n\n"
mysock.sendto(message.encode("utf-8"), ("www.pythonlearn.com", 80))

#retrieve the data and print it out
while True:
    data = mysock.recv(512)
    if ( len(data) < 1 ) :
        break
    decoded_data = data.decode("utf-8")
    print(decoded_data)

mysock.close()