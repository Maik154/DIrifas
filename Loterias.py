import random

'''
Codificamos las funciones
'''

def menu():
    print("1. Primitiva\n")
    print("2. Euromillones\n")
    print("3. Fútbol\n")
    print("4. Lotería nacional\n")
    print("5. Salir\n")
    op = int(input('Elija una opción\n'))
    return op

def primitiva():
    s = ""
    for i in range(6):
        s += str(random.randint(1,49))
    complementario = random.randint(1,9)
    print("lotería: ", s, "\ncomplementario: ", complementario)

def nacional():
    x = random.randint(0,99999)
    print("El número ganaador es: ", x)




op = menu()
if(op == 1):
    primitiva()
elif(op == 2):
    euromillones()
elif(op == 3):
    quiniela()
elif(op == 4):
    nacional()
else:
    exit()