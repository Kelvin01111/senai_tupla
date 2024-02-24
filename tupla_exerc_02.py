
# 2. Escreva um programa que receba duas tuplas de números (informadas
# pelo usuário) e crie um conjunto com os elementos que são únicos a ambas
# as tuplas.


def conjunto_tupla(tuplas):
    tupla = ()

    for i in range(tuplas):
        item = input(f"Informe o item {i}: ")
        tupla = tupla + (item,)


    return tupla


def criar_conjunto_unico(tupla1,tupla2):
    tupla_final = ()
    conjunto1 = set(tupla1)
    conjunto2 = set(tupla2)

    conjunto_unico = conjunto1.intersection(conjunto2)
    tupla_final = (conjunto_unico)

    return tupla_final


def main():
    tupla_01 = int(input("Insira números na primeira tupla: "))
    tupla_02 = int(input("Insira números na segunda tupla: "))
    
    print("Elemento da tupla 1: ")
    tupla1 = conjunto_tupla(tupla_01)
    print("Elementos da tupla 2: ")
    tupla2 = conjunto_tupla(tupla_02)

    tuplra_resultante = criar_conjunto_unico(tupla1,tupla2)

    print(tuplra_resultante)


if __name__=="__main__":
    main()