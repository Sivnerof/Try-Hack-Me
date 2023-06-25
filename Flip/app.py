import socketserver 
import socket, os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
from binascii import unhexlify

flag = open('flag','r').read().strip()

def encrypt_data(data,key,iv):
    padded = pad(data.encode(),16,style='pkcs7')
    cipher = AES.new(key, AES.MODE_CBC,iv)
    enc = cipher.encrypt(padded)
    return enc.hex()

def decrypt_data(encryptedParams,key,iv):
    cipher = AES.new(key, AES.MODE_CBC,iv)
    paddedParams = cipher.decrypt( unhexlify(encryptedParams))
    if b'admin&password=sUp3rPaSs1' in unpad(paddedParams,16,style='pkcs7'):
        return 1
    else:
        return 0

def send_message(server, message):
    enc = message.encode()
    server.send(enc)

def setup(server,username,password,key,iv):
        message = 'access_username=' + username +'&password=' + password
        send_message(server, "Leaked ciphertext: " + encrypt_data(message,key,iv)+'\n')
        send_message(server,"enter ciphertext: ")

        enc_message = server.recv(4096).decode().strip()

        try:
                check = decrypt_data(enc_message,key,iv)
        except Exception as e:
                send_message(server, str(e) + '\n')
                server.close()

        if check:
                send_message(server, 'No way! You got it!\nA nice flag for you: '+ flag)
                server.close()
        else:
                send_message(server, 'Flip off!')
                server.close()

def start(server):
        key = get_random_bytes(16)
        iv = get_random_bytes(16)
        send_message(server, 'Welcome! Please login as the admin!\n')
        send_message(server, 'username: ')
        username = server.recv(4096).decode().strip()

        send_message(server, username +"'s password: ")
        password = server.recv(4096).decode().strip()

        message = 'access_username=' + username +'&password=' + password

        if "admin&password=sUp3rPaSs1" in message:
            send_message(server, 'Not that easy :)\nGoodbye!\n')
        else:
            setup(server,username,password,key,iv)

class RequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        start(self.request)

if __name__ == '__main__':
    socketserver.ThreadingTCPServer.allow_reuse_address = True
    server = socketserver.ThreadingTCPServer(('0.0.0.0', 1337), RequestHandler)
    server.serve_forever()
