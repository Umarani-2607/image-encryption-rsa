from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from PIL import Image
import os


def generate_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    with open("private.pem", "wb") as f:
        f.write(private_key)

    with open("public.pem", "wb") as f:
        f.write(public_key)


def encrypt_image(image_path):
    with open("public.pem", "rb") as f:
        public_key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(public_key)

    with open(image_path, "rb") as img:
        data = img.read()

    encrypted_data = cipher.encrypt(data[:190])  # RSA size limit demo

    with open("encrypted.bin", "wb") as f:
        f.write(encrypted_data)


def decrypt_image(output_path):
    with open("private.pem", "rb") as f:
        private_key = RSA.import_key(f.read())

    cipher = PKCS1_OAEP.new(private_key)

    with open("encrypted.bin", "rb") as f:
        encrypted_data = f.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    with open(output_path, "wb") as f:
        f.write(decrypted_data)


if __name__ == "__main__":
    generate_keys()
    encrypt_image("sample.jpg")
    decrypt_image("decrypted_sample.jpg")
    print("Encryption and decryption complete.")
