from Crypto.Util.number import getPrime, getRandomRange, isPrime
from asn1Handler.asn1_handler import ASN1


class DiffieHellmanAlg:

    def __init__(self, n=None, p=None, a=None):

        if n is not None:
            self.p = getPrime(n)
            self.a = getRandomRange(2, self.p - 1)
            while not isPrime(self.a):
                self.a = getRandomRange(2, self.p - 1)

            print(f"p: {self.p}")
            print(f"a: {self.a}")

        elif n is None and p is not None and a is not None:
            self.p = p
            self.a = a
        else:
            print('Error!')
            exit(-1)

    def get_key_parth(self):
        x = getRandomRange(2, self.p)
        key_parth = pow(self.a, x, self.p)

        return x, key_parth

    def create_client_message(self, client_key):
        return ASN1.client_message(self.p, self.a, client_key)

    @staticmethod
    def create_server_message(server_key):
        return ASN1.server_message(server_key)

    @staticmethod
    def read_key_from_server_message(message):
        return ASN1.server_message_decode(message)

    @staticmethod
    def read_info_from_client_message(message):
        return ASN1.client_message_decode(message)

    def calculate_key_from_server_key(self, server_key, x):
        return pow(server_key, x, self.p)

    def calculate_key_from_client_key(self, client_key, y):
        return pow(client_key, y, self.p)