from DiffieHellman.diffie_hellman import DiffieHellmanAlg
import socket


def main():
    DH = DiffieHellmanAlg(n=256)

    x, client_key = DH.get_key_parth()
    print(f"x: {x}")
    print(f"a^x / client_key: {client_key}")
    message = DH.create_client_message(client_key)

    ip = input('Server ip:')
    port = int(input('Port:'))

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((ip, port))
        s.sendall(message)
        file = open("client_message.asn1", "wb")
        file.write(message)
        file.close()
        server_message = s.recv(1024)

    server_key = DH.read_key_from_server_message(server_message)

    key = DH.calculate_key_from_server_key(server_key, x)

    print(f"Client calculate key: {key}")


if __name__ == '__main__':
    main()