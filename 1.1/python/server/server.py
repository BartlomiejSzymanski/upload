import socket
import sys

# default values
HOST = "172.21.13.2"
BUFSIZE = 1024

def run_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((host, port))

        while True:
            data, address = sock.recvfrom(BUFSIZE)
            print(f"Received message: {data.decode('utf-8')} ({len(data)} bytes) from client: {address}")
            sock.sendto(data, address)
            print("Sent echo of datagram")

if __name__ == "__main__":
    run_server(host=HOST, port=int(sys.argv[1]))
