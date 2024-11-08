import os
from cryptography.fernet import Fernet

def load_key():
    return open("secret.key", "rb").read()

def decrypt_file(file_name):
    key = load_key()
    f = Fernet(key)
    with open(file_name, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)

    original_file_path = file_name.replace(".enc", "")
    with open(original_file_path, "wb") as file:
        file.write(decrypted_data)

    os.remove(file_name)

def decrypt_folder(folder_path):
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            if file_path.endswith(".enc"):
                print(f"Decrypting: {file_path}")
                decrypt_file(file_path)


decrypt_folder(r"E:\project\Malware\MWS\test")
