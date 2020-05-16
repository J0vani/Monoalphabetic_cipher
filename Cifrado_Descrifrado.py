import sys
from io import open
import matplotlib.pyplot as plt


def mono_encryption():
    txtFile = open('File.txt', 'r', encoding="utf8")
    fileContent = txtFile.readlines()
    txtFile.close()

    plain_text = ""
    for fc in fileContent:
        plain_text += fc.replace("\n", " ").upper()

    # Print the plaint text
    print(plain_text)

    alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789'
    A = 0;
    B = 0;
    C = 0;
    D = 0;
    E = 0;
    F = 0;
    G = 0;
    H = 0;
    I = 0;
    J = 0;
    K = 0;
    L = 0;
    M = 0;
    N = 0;
    Ñ = 0;
    O = 0;
    P = 0;
    Q = 0;
    R = 0;
    S = 0;
    T = 0;
    U = 0;
    V = 0;
    W = 0;
    X = 0;
    Y = 0;
    Z = 0
    one = 0;
    two = 0;
    three = 0;
    four = 0;
    five = 0;
    six = 0;
    seven = 0;
    eigth = 0;
    nine = 0;
    ten = 0

    message = plain_text.upper()
    clave = str(input("\nClave : ")).upper()
    cifrado = ''

    # Encrypted text
    if checkKey(alphabet, clave):
        for i in range(len(message)):
            if message[i] in alphabet:
                letter = message[i]

                # data for histogram
                indxAlpha = alphabet.find(letter)  # int
                cifrado += clave[indxAlpha]
            else:
                if message[i] == " ":
                    cifrado += " "
                else:
                    cifrado += ""

        # Create output file
        outputFile = open('FileC.txt', 'w')
        outputFile.write(cifrado)
        outputFile.close()

        print("Texto Cifrado: ", cifrado, "\n\n")

        encrypted_text = cifrado

    for i in range(len(encrypted_text)):
        if encrypted_text[i] in alphabet:
            letter = encrypted_text[i]

            # data for histogram
            if letter == 'A': A += 1
            if letter == 'B': B += 1
            if letter == 'C': C += 1
            if letter == 'D': D += 1
            if letter == 'E': E += 1
            if letter == 'F': F += 1
            if letter == 'G': G += 1
            if letter == 'H': H += 1
            if letter == 'I': I += 1
            if letter == 'J': J += 1
            if letter == 'K': K += 1
            if letter == 'L': L += 1
            if letter == 'M': M += 1
            if letter == 'N': N += 1
            if letter == 'Ñ': Ñ += 1
            if letter == 'O': O += 1
            if letter == 'P': P += 1
            if letter == 'Q': Q += 1
            if letter == 'R': R += 1
            if letter == 'S': S += 1
            if letter == 'T': T += 1
            if letter == 'U': U += 1
            if letter == 'V': V += 1
            if letter == 'W': W += 1
            if letter == 'X': X += 1
            if letter == 'Y': Y += 1
            if letter == 'Z': Z += 1
            if letter == '0': one += 1
            if letter == '1': two += 1
            if letter == '2': three += 1
            if letter == '3': four += 1
            if letter == '4': five += 1
            if letter == '5': six += 1
            if letter == '6': seven += 1
            if letter == '7': eigth += 1
            if letter == '8': nine += 1
            if letter == '9': ten += 1

            indxAlpha = alphabet.find(letter)  # int
            cifrado += clave[indxAlpha]
        # Plot Histogram
    fig = plt.figure(u'Histograma')

    ax = fig.add_subplot(111)


    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T',
               'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    num = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, Ñ, O, P, Q, R, S, T, U, V, W, X, Y, Z, one, two, three, four,
               five, six, seven, eigth, nine, ten]
    xx = range(len(num))



    ax.bar(xx, num, width=0.8, align='center')
    print(xx)
    ax.set_xticks(xx)
    ax.set_xticklabels(abc)

    plt.show()

#DCBAEFGHIJKLMNÑOPQRSTUVWXYZ0123456789


def checkKey(alphabet, key):
    if (len(alphabet) != len(key)):
        print('\n\n La llave debe ser igual al alfabeto [A-Z] - [0-9] (37 CHARACTERS)')
        return False

    i = 0
    for a in alphabet:
        if not a in key:
            i += 1

    if i > 0:
        print('\n Falta una letra en la clave')
        return False
    else:
        return True


def main():
    mono_encryption()


if __name__ == "__main__":
    main()