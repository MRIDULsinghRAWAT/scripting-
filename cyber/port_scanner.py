import socket 
ip = input("ip:")
for port in [21,22,23,25,53,80,110,135,139,443]:
    s=socket.socket()
    s.settimeout(0.5)
    if s.connect_ex((ip,port))==0:
        print("port",port,"open")
        s.close()