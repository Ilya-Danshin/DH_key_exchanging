from asn1 import Encoder, Decoder, Numbers


class ASN1:
    @staticmethod
    def client_message(p, a, client_key):
        encoder = Encoder()
        encoder.start()

        encoder.enter(Numbers.Sequence)
        encoder.enter(Numbers.Set)
        encoder.enter(Numbers.Sequence)
        encoder.write('\x00\x21', Numbers.OctetString)
        encoder.write('dh', Numbers.UTF8String)

        encoder.enter(Numbers.Sequence)
        encoder.leave()

        encoder.enter(Numbers.Sequence)
        encoder.write(p, Numbers.Integer)
        encoder.write(a, Numbers.Integer)
        encoder.leave()

        encoder.enter(Numbers.Sequence)
        encoder.write(client_key, Numbers.Integer)
        encoder.leave()

        encoder.leave()
        encoder.leave()

        encoder.enter(Numbers.Sequence)
        encoder.leave()

        encoder.leave()

        return encoder.output()

    @staticmethod
    def client_message_decode(message):
        decoder = Decoder()
        decoder.start(message)

        decoder.enter()
        decoder.enter()
        decoder.enter()
        decoder.read()
        decoder.read()

        decoder.enter()
        decoder.leave()

        decoder.enter()
        p = decoder.read()[1]
        a = decoder.read()[1]
        decoder.leave()

        decoder.enter()
        client_key = decoder.read()[1]
        decoder.leave()

        decoder.leave()
        decoder.leave()

        decoder.enter()
        decoder.leave()

        decoder.leave()

        return p, a, client_key

    @staticmethod
    def server_message(server_key):
        encoder = Encoder()
        encoder.start()

        encoder.enter(Numbers.Sequence)
        encoder.enter(Numbers.Set)

        encoder.enter(Numbers.Sequence)
        encoder.write('\x00\x21', Numbers.OctetString)
        encoder.write('dh', Numbers.UTF8String)

        encoder.enter(Numbers.Sequence)
        encoder.leave()

        encoder.enter(Numbers.Sequence)
        encoder.leave()

        encoder.enter(Numbers.Sequence)
        encoder.write(server_key, Numbers.Integer)
        encoder.leave()

        encoder.leave()
        encoder.leave()

        encoder.enter(Numbers.Sequence)
        encoder.leave()

        encoder.leave()

        return encoder.output()

    @staticmethod
    def server_message_decode(message):
        decoder = Decoder()
        decoder.start(message)

        decoder.enter()
        decoder.enter()

        decoder.enter()
        decoder.read()
        decoder.read()

        decoder.enter()
        decoder.leave()

        decoder.enter()
        decoder.leave()

        decoder.enter()
        server_key = decoder.read()[1]
        decoder.leave()

        decoder.leave()
        decoder.leave()

        decoder.enter()
        decoder.leave()

        decoder.leave()

        return server_key
