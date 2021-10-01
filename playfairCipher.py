# this is your encrypt matrix
PFmatrix1 = [['M', 'O', 'N', 'A', 'R'],
 ['C', 'H', 'Y', 'B', 'D'],
 ['E', 'F', 'G', 'I', 'K'],
 ['L', 'P', 'Q', 'S', 'T'],
 ['U', 'V', 'W', 'X', 'Z']]


def encryptByPF(plaintext):
#     input data pre-processing
    plaintext = plaintext.upper()
    i = 0 
    for s in range(0, len(plaintext)+1, 2):
        if s< len(plaintext) - 1: 
            if plaintext[s] == plaintext[s+1]:
                plaintext = plaintext[:s+1] + 'X' + plaintext[s+1:]
            elif len(plaintext) % 2 !=0:
                plaintext = plaintext[:] + 'X'
    print("The prepared plaintext is:", plaintext)
    return plaintext
#   example
plaintextX = encryptByPF("meetprimeministerafterdinner")
print(plaintextX)

  # a function to find the exact position in encrypt matrix of a letter
def find_position(keyMatrix, letter):
    x=y=0
    for i in range(5):
        for j in range(5):
            if keyMatrix[i][j] == letter:
                x=i
                y=j
    return x,y

def PFencrypt(PFmatrix,plaintextX):
    plaintext_spilited = [plaintextX[i:i+2] for i in range(len(plaintextX)) if i % 2 == 0]
    cipher=[]
    for i in plaintext_spilited:
        x1,y1 = find_position(PFmatrix,i[0])
        x2,y2 = find_position(PFmatrix,i[1])
        if x1 == x2:
            if y1 == 4:
                y1 = -1
            if y2 == 4:
                y2 = -1
            cipher.append(PFmatrix[x1][y1+1])
            cipher.append(PFmatrix[x1][y2+1])
        elif y1 == y2:
            if x1 == 4:
                x1 = -1;
            if y2 == 4:
                y2 = -1;
            cipher.append(PFmatrix[x1+1][y1])
            cipher.append(PFmatrix[x2+1][y2])
        else:
            cipher.append(PFmatrix[x1][y2])
            cipher.append(PFmatrix[x2][y1])
    return cipher

def showEncryptedText(cipher):
    print("The encrypted text: ",end="")
    for x in cipher:
        print(x,end='')
        
plaintextX1 = encryptByPF("classicalcryptography")
print("")
print(PFencrypt(PFmatrix1,plaintextX1))
print("")
showEncryptedText(PFencrypt(PFmatrix1,plaintextX1))
