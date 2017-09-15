from select_friend import select_friend
from steganography.steganography import Steganography

def read_message():
    # choose friend from the list
    sender=select_friend()

    encypted_image=input("Provide encrypted image  :")
    secret_message=Steganography.decode(encypted_image)
    print("secret_message")
