#Does not work for nested folders

import os
import zipfile
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename

def encrypt_file(key, filename, out_filename):
    chunk_size = 64 * 1024
    iv = get_random_bytes(16)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
       
    with open(filename, 'rb') as file:
        with open(out_filename, 'wb') as out_file:
            out_file.write(iv)
            
            while True:
                chunk = file.read(chunk_size)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)
                    
                out_file.write(encryptor.encrypt(chunk))

def archive_and_encrypt_folder(folder_path, zip_path, key):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, folder_path)
                encrypted_path = os.path.join(os.path.dirname(file_path), 'encrypted_' + file)
                
                encrypt_file(key, file_path, encrypted_path)
                zip_file.write(encrypted_path, relative_path)
                
                os.remove(encrypted_path)



def decrypt_file(key, filename, out_filename):
    chunk_size = 64 * 1024
    
    with open(filename, 'rb') as file:
        with open(out_filename, 'wb') as out_file:
            iv = file.read(16)
            decryptor = AES.new(key, AES.MODE_CBC, iv)
            
            while True:
                chunk = file.read(chunk_size)
                if len(chunk) == 0:
                    break
                
                out_file.write(decryptor.decrypt(chunk))
                
def extract_and_decrypt_folder(zip_path, output_folder, key):
    with zipfile.ZipFile(zip_path, 'r') as zip_file:
        for file_info in zip_file.infolist():
            if file_info.filename.startswith('__MACOSX/'):
                continue
            
            encrypted_file_path = os.path.join(output_folder, file_info.filename)
            decrypted_file_path = os.path.join(output_folder, 'decrypted_' + os.path.basename(file_info.filename))
            
            zip_file.extract(file_info, output_folder)
            decrypt_file(key, encrypted_file_path, decrypted_file_path)
            
            os.remove(encrypted_file_path)


root = Tk()
root.withdraw()

while True:
    os.system('cls')
    print("1 - Encrypt folder 🔐")
    print("2 - Decrypt file 🔓")
    print("0 - END")
    choice = input("Choice: ")

    match choice:
        case "1":
            print("Select the folder you want to encrypt.")
            print("[INFO] The default path of the encrypted folder is the same as the selected folder.")

            folder_path = askdirectory()
            if folder_path:
                print("Selected folder: ", folder_path)
                key  = get_random_bytes(16)
                print("KEY = ["+key.hex() +"]")
                encrypted_folder_path = folder_path + ".zip"
                archive_and_encrypt_folder(folder_path, encrypted_folder_path, key)
            else:
                print("No folder has been selected.")

            _ = input("Press ENTER to continue")


        case "2":
            print("Select the file you want to decrypt.")
            print("[INFO] The default path of the decrypted file is the same as the selected file.")

            zippedFolder_path = askopenfilename()
            if zippedFolder_path:
                print("Selected file: ", zippedFolder_path)
                key = input("Enter key: ")
                output_file = os.path.splitext(zippedFolder_path)[0]
                extract_and_decrypt_folder(zippedFolder_path, output_file, bytes.fromhex(key))
            else:
                print("No file has been selected.")

            _ = input("Press ENTER to continue")

        case "0":
            break
