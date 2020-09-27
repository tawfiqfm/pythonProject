import string
def encrypt(s):
    # this function returns the encrypted form of s
    key = int(s[0:2])
    k = s.index('/')
    time = s[0:k]
    plaintext = s[ k +1:]
    result = ""
    for c in plaintext:


        if c == ' ':
            code = -',' + '_'

        else:
            code = str((('abcdefghijklmnopqrstuvwxyz'.index(c ) +key) % 26)) + ','




















        result = result + code

    return (time + '/') + result





def decrypt(s):
    key = int(s[0:2])
    k = s.index('/')
    time = s[0:k]
    plaintext = s[k + 1:]
    result = ""

    for c in plaintext:
        if c == '_':
            code = ' '
        else:
            code = str((()))



def main ():
  # s = "14:00/the ships are in position"
  # s = "21:30/17,25_21,12,25_12,25,21,24,19_14,9_21,14,14,21,23,5"
    while True:
        s = input("\nEnter e plain-text or d coded-text or q: ")
        if s[0] == "e":
            print("Encrypted text is: " + encrypt(s[2:]))
        elif s[0] == "d":
            print("Decrypted text is: " + decrypt(s[2:]))
        elif s[0] == "q":
            break
        else:
            print("Invalid choice")


main()
