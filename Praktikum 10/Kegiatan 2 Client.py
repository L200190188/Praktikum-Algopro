import socket

hostname = "localhost"
pesan = ""
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("",50007))
s.listen(5)
print "Program Komunikasi Tentang Server"
while pesan.lower() !="quit":
    pesan = raw_input("Command: ")
    s.send(pesan)
    if pesan.lower() == "quit":
        s.close
        break
    elif pesan.lower() != "quit":
        reponse = s.recv(1024)
        print "Response :", response
s.close()
                      
