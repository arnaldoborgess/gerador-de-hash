import hashlib
#Este módulo implementa uma interface comum para muitos algoritmos de hash e digestão de mensagens seguros.

string = input("Digite o texto a ser gerado a hash: ")

menu = int(input('''#### MENU - ESCOLHA O TIPO DE HASH ####
             1) MD5
             2) SHA1
             3) SHA256
             4)SHA512
             Digite o número do hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(string.encode('utf-8')) # b' converte a string em bits
    print("A hash MD5 da string: ", string, " é: ", resultado.hexdigest())
elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print("A hash SHA1 da string: ", string, " é: ", resultado.hexdigest())
elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print("A hash SH256 da string: ", string, " é: ", resultado.hexdigest())
elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print("A hash SH512 da string: ", string, " é: ", resultado.hexdigest())
else:
    print("Algo de errado não deu certo! :O, você precisa escolher uma opção no menu!")
