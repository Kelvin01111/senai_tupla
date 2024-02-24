
#  3. Crie uma tupla com os meses do ano e uma tupla com os meses do verão
#  e outra com os meses da primavera. Imprima os meses que não são
#  considerados meses nem de verão e nem de primavera.


def meses_inverno_outono():
    m_ano = ("janeiro","fevereiro","março","abril","maio","junho","julho","agosto","setembro","outubro","novembro","dezembro")
    m_verao = ("dezembro","janeiro","fevereiro")
    m_primavera = ("setembro", "outubro", "novembro")

    tupla_final = set(m_ano) - set(m_verao) - set(m_primavera)
    return tupla_final


def main():
    tupla = meses_inverno_outono() 
    print("Meses de Inverno e Outono",tupla)



if __name__=="__main__":
    main()
