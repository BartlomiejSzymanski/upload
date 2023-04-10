import socket
import sys

# default values
BUFSIZE = 1024
MESSAGE = "abcde".encode("utf-8")
N_OF_MESSAGES = 5

def client_send(message, host, port, how_many):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        for _ in range(how_many):
            bytes_sent = sock.sendto(message, (host, port))
            print(f"Sent {bytes_sent} bytes to {host}:{port}")
            print(f"Received message: {sock.recv(BUFSIZE)}")
    print("Client finished.")

if __name__ == "__main__":
    host = sys.argv[1]
    port = sys.argv[2]
    client_send(MESSAGE, host=sys.argv[1], port=int(sys.argv[2]), how_many=N_OF_MESSAGES)
