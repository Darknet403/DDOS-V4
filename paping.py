import socket
import time
import sys

def tcp_ping(target_ip, target_port, interval=0.5): 
    while True:
        try:
            start_time = time.time()
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.settimeout(5)
            client_socket.connect((target_ip, target_port))
            client_socket.close()
            end_time = time.time()
            response_time = (end_time - start_time) * 1000
            print(f"\033[97mConnected to \033[92m{target_ip}\033[97m: \033[97mtime=\033[92m{response_time:.2f}ms \033[97mprotocol=\033[92mTCP \033[97mport=\033[92m{target_port}")
        except Exception as e:
            print("\033[91mConnection timed out")

        time.sleep(interval)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 paping.py ip port")
        sys.exit(1)

    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    interval = 0.4
    tcp_ping(target_ip, target_port, interval)