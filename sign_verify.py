from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.exceptions import InvalidSignature


def is_valid(public_key, signature, data):
    try:
        public_key.verify(signature, data)
    except InvalidSignature:
        return False
    return True


message = "Send 100kr to Malmö"
data = message.encode()
private_key = Ed25519PrivateKey.generate()
public_key = private_key.public_key()
signature = private_key.sign(data)

tampered = "Send 100kr to Malmo".encode()

print(is_valid(public_key, signature, data))
print(is_valid(public_key, signature, tampered))