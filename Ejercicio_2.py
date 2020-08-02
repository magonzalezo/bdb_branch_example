'''
Ejercicio 2: Se desea crear un arbol tan alto como los niveles que indique el usuario.
'''

num = int(input("Que tan alto sera el arbol?: "))

print(" ")

for i in range(0,num):
    for j in range(0,num-i-1):
        print(' ',end='')
    for j in range(0,i+1):
        print("*",end='')
    for j in range(1,i+1):
        print("*",end='')
    print()

print((" "*(num-1))+"|\n")