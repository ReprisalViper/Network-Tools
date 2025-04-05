import socket

def port_scanner(ip, port_range):
    print(f"Scanning {ip} for open ports...")
    for port in port_range:
        try:
            sock = socket.socket()
            sock.settimeout(0.5)
            sock.connect((ip, port))
            print(f"[+] Port {port} is open.")
        except:
            pass
        finally:
            sock.close()

# Example usage
if __name__ == "__main__":
    target_ip = "127.0.0.1"
    ports = range(20, 1025)
    port_scanner(target_ip, ports)
