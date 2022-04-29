from DiffieHellman.diffie_hellman import DiffieHellmanAlg
import socket


def main():
    host = "127.0.0.1"
    port = 8080

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                message = conn.recv(1024)
                if not message:
                    break

                p, a, client_key = DiffieHellmanAlg.read_info_from_client_message(message)
                DH = DiffieHellmanAlg(p=p, a=a)
                y, server_key = DH.get_key_parth()
                print(f"y: {y}")
                print(f"a^y / server_key: {server_key}")
                key = DH.calculate_key_from_client_key(client_key, y)
                print(f"Server calculate key: {key}")

                message = DH.create_server_message(server_key)
                file = open("server_message.asn1", "wb")
                file.write(message)
                file.close()
                conn.sendall(message)


if __name__ == '__main__':
    main()
