# 5) Escreva um programa que inverta os caracteres de um string. 

# IMPORTANTE: 
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; 
# b) Evite usar funções prontas, como, por exemplo, reverse;

def reverse_string(string):
    reversed_string = ""
    for i in range(len(string)-1, -1, -1):
        reversed_string += string[i]
    return reversed_string

string = input("Digite uma string: ")
print(reverse_string(string))