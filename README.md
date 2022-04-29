___
# Diffie–Hellman key exchange
There is client-server application that exchange key by Diffie-Hellman algorithm. 
___
## Client side
The client generates a random secret exponent x and sends the value a^x to the server. 
The system parameters are also transmitted: generator a, module p. Thus, three parameters 
are passed to the server (a^x, a, p). asn1 message format:
```
SEQUENCE {- header
  SET { - set of keys, 1 enabled
    SEQUENCE {- first key
      OCTET STRING - algorithm identifier (Diffie-Hellman protocol)
        00 21
      UTF8String 'dh' - may not be involved or used to identify a future set key
      SEQUENCE { } – public key value, not used
      SEQUENCE {- cryptosystem parameters
        INTEGER - prime number p
           PP PP … PP
        INTEGER - generator a
           AA AA … AA
        }
      SEQUENCE {- ciphertext, exponent a^x
        INTEGER - number c
          CC CC … CC
        }
      }
    }
  SEQUENCE {} – file parameters, not used
```
___
## Server side
On an incoming connection, the server accepts the triple (a^x,a,p), 
generates a random y score, and sends the value of a^y to the client.
The a^xy value is also calculated. The client receives a message in 
the following format:
```
SEQUENCE {- header
  SET { - set of keys, 1 enabled
    SEQUENCE {- first key
      OCTET STRING - algorithm identifier (Diffie-Hellman protocol)
        00 21
      UTF8String 'dh' - may not be involved or used to identify a future set key
      SEQUENCE { } – public key value, not used
      SEQUENCE { } – cryptosystem parameters
      SEQUENCE {- ciphertext
        INTEGER - a^xy value
          CC CC … CC
        }
      }
    }
  SEQUENCE {} – file parameters, not used
}
```
