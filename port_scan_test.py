import socket

ip = ["136.243.154.86"]
ports = [22, 445, 80, 443, 3389]
s = socket.socket()

for address in ip:
    for port in ports:
        try:
            print("[+] Connecting to " + address + ":" + str(port))
            s.connect((address, port))
            banner = s.recv(1024)
            if banner:
                print("[+] Port " + str(port) + " open: " + banner)
            s.close()
        except: pass
