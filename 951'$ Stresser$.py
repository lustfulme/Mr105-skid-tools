import time
import subprocess
import os
from datetime import datetime

print("\033[30m")
print("\033[34m")
print("951'$ STRESEER'$ 🛰️")

# Prompt for IP and Port
target_ip = input("🌐 Enter IP to ping (ENTER IP): ")
target_port = input("🔒 Enter Port to Hit (Port Here): ")

# Validate input
if not target_ip:
    print("❌ No IP entered. Exiting.")
    input("Press Enter to exit...")
    exit()

# Log filename (Generic without showing full path)
log = f"FloodLog_{target_ip}_{datetime.now().strftime('%Y-%m-%d')}.txt"
print(f"🔄 Logging to: {log}")
print("=======================================================")
time.sleep(2)

# Start test
count = 0
print(f"🛰️ Starting 951'$ $tressor... {target_ip} ...")
print("Press Ctrl+C to stop.")
print()

# Fast ping loop with minimized ping parameters
while count < 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000:
    count += 1
    try:
        response = subprocess.check_output(['ping', '-n', '1', '-w', '1', target_ip], stderr=subprocess.STDOUT, universal_newlines=True)
        if "TTL=" in response:
            print(f"[{count}] {response.strip()} TTL=50000")
            with open(log, 'a') as log_file:
                log_file.write(f"[{count}] {response.strip()} TTL=25000\n")
    except subprocess.CalledProcessError:
        continue

# Wrap up
print()
print(f"✅ Test finished after {count} pings.")
print(f"📁 Log saved as: {log}")
input("Press Enter to exit...")