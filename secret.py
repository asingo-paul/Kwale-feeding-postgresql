import os
import secrets

print("Generating secret key...")

print(secrets.token_hex(32))

print("Key generation done successfully.")