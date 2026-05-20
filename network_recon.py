import socket

# ask for the target IP
target = input("Enter the IP address to scan (e.g., 127.0.0.1): ")

# list of critical ports to scan
ports_to_scan = [21, 22, 80, 443, 3389]

print("-" * 50)
print(f"Starting scan on target: {target}")
print("-" * 50)

# loop through each port
for port in ports_to_scan:
    
    # Configure the socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1) 
    
    # Attempt to connect to the port
    result = s.connect_ex((target, port))
    
    if result == 0:
        if result == 0:
            # Core logic for identifying services
            if port == 22:
                print("[OPEN] Port 22 (SSH)")
            elif port == 80:
                print("[OPEN] Port 80 (HTTP)")
            elif port == 3389:
                print("[CRITICAL] Port 3389 (RDP) exposed!")
            else:
                # Fallback for any other open port on the list
                print(f"[OPEN] Port: {port}")
            
    s.close()

print("-" * 50)
print("Scan completed.")