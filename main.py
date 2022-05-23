# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

palavras_reservadas = ["if", "int", "else", "return", ]
simbolos = ["<", "=", ">", "*", "/", "-", "+", "(", ")", ";", "{", "}"]

def consome_caracter():
    global count
    global string
    i = count
    count += 1
    if(count >= len(string)):
        return -1
    return string[i]

def transforma_em_string(arq):
    texto = arq.read()
    return list(texto)

def identifica_tokens():


arq = open("programa.txt", "r")
count = 0
string = transforma_em_string(arq)
x = consome_caracter()

while(x != -1):
    if()
    x = consome_caracter()
