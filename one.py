# 1 - Problem: Caesar Cipher encoding and decoding

ALPHABETS = "abcdefghijklmnopqrstuvwxyz"


def main():
    option = int(input("Encode(1) OR Decode(2): "))
    if option != 1 and option != 2:  # if user inputs anything other than 1 or 2
        return
    key = int(input("Enter Cypher Key: "))  # to get the cypher key
    msg = input("Enter Your Message: ")
    msg = msg.lower()  # to make the message case insensitive
    res = ""
    if option == 1:
        for letter in msg:
            # take nth letter to the right
            res += ALPHABETS[(ALPHABETS.index(letter) + key) % 26]
        print("Your Encrypted message is", res)
    else:
        for letter in msg:
            # take nth letter to the left
            res += ALPHABETS[(ALPHABETS.index(letter) - key) % 26]
        print("Your Decrypted message is:", res)


main()
