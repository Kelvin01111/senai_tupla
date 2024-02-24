
#   5. Dada uma lista de palavras (informadas pelo usuário), crie uma tupla com
#   as palavras que têm mais de quatro letras.



def mais_de_quatro_letras(tupla):
    TAM_MAXIMO = 4
    tupla_final = ()

    for item_tupla in tupla:
        tam = len(item_tupla)
        if(tam >= TAM_MAXIMO):
           tupla_final = tupla_final + (item_tupla,)
    return tupla_final


def gerar_tupla(tam_tupla):
    tupla = ()

    for i in range(tam_tupla):
        item = input(f"Informe o item: ")
        tupla = tupla + (item,)




def main():
    tam_tupla = input("Insira uma lista de palavras: ")
    tupla1 = gerar_tupla(tam_tupla)
    tupla_final = mais_de_quatro_letras(tam_tupla)



if __name__=="__main__":
    main()