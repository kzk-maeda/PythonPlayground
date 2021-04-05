from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

def generate_key(bytes: int) -> bytes:
  key = get_random_bytes(bytes)
  return key


class Crypto:
  def __init__(self, key: bytes):
    self.key = key
  
  def AES(self, text: str) -> bytes:
    iv = b'0000000000000000'
    cipher = AES.new(self.key, AES.MODE_CBC, iv=iv)
    byte_text = text.encode('utf-8')
    ciphertext = cipher.encrypt(pad(byte_text, AES.block_size))
    return ciphertext


if __name__ == '__main__':
  # key = generate_key(16)
  key = b"\x0f0oj'\xfc\x14h\xf0L\x99\xd9\xaf=\xdd\xfb"
  crypto = Crypto(key)
  crypted_text = crypto.AES('this is sample text')
  print(f'key: {key}, crypted_text: {crypted_text}')