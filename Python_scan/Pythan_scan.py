import socket
def run(start_port, end_port,target):
    for port in range(int(start_port), int(end_port) + 1):
        scanning(port, target)
def scanning(port, target):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(.05)      
        result = sock.connect_ex((target, port))               
        if result == 0:
            print(f"Port{port}:open")
        sock.close
    except:
        pass

    #192.168.0.149