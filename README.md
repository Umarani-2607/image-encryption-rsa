# Image Encryption and Decryption using RSA

A project demonstrating how RSA public-key cryptography
can be applied to image data to understand secure data handling.

---

## What This Project Demonstrates

- RSA key pair generation
- Encrypting image data using a public key
- Decrypting encrypted data using a private key
- Understanding cryptographic size limitations
- Practical security considerations

---

## How It Works

1. An RSA key pair is generated (public and private keys)
2. A small portion of image binary data is encrypted using the public key
3. The encrypted data is stored in a binary file
4. The encrypted data is decrypted using the private key

> Note: RSA is not designed to encrypt large files directly.
> This project intentionally encrypts a limited portion of image data
> to demonstrate why hybrid encryption is used in real systems.

---

## Tech Stack

- Python
- PyCryptodome
- Pillow

## Security Considerations

This project focuses on understanding cryptographic concepts and limitations.
It intentionally avoids committing sensitive keys and explains why hybrid
encryption is used in real-world systems.
