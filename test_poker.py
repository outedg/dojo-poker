import pytest
from collections import Counter

'''  
Correção dos testes listados abaixo, eles não estão passando:

- test_nao_eh_trinca  
- test_par_de_5_ganha_par_de_8
- test_trinca_ganha_de_par
'''

def extract_method(cartas,repeticoes):
    quantidade_de_repeticoes = 0
    numeros_de_cartas_suja = []

    for carta in cartas:
        numeros_de_cartas_suja.append(carta[0])

    for chave in Counter(numeros_de_cartas_suja).keys():
        if numeros_de_cartas_suja.count(chave) == repeticoes:
            quantidade_de_repeticoes = quantidade_de_repeticoes + 1

    return quantidade_de_repeticoes


def contar_quantidades_de_repeticoes_de_um_numero(cartas,repeticoes,numero):
    quantidade_de_repeticoes = 0

    if cartas.count(numero) == repeticoes:
        quantidade_de_repeticoes = quantidade_de_repeticoes + 1

    return quantidade_de_repeticoes 

def eh_trinca(cartas):
    return extract_method(cartas,3) == 1

def contar_quantidade_de_pares(cartas):
    return extract_method(cartas,2)

def eh_apenas_um_par(cartas):
    return contar_quantidade_de_pares(cartas) == 1

def par_de_cinco_ganha_par_de_8(cartas_mao_um,cartas_mao_dois):
    quantidade_de_cartas_mao_1 = []
    quantidade_de_cartas_mao_2 = []

    for carta_mao_um in cartas_mao_um:
        quantidade_de_cartas_mao_1.append(carta_mao_um[0])
    
    for carta_mao_dois in cartas_mao_dois:
        quantidade_de_cartas_mao_2.append(carta_mao_dois[0])



def jogar(mao_1, mao_2):

    if eh_trinca(mao_1) and eh_apenas_um_par(mao_2):
        return mao_1
    if eh_apenas_um_par(mao_1) and extract_method(mao_2,2) == 2:
        return mao_2
    if eh_apenas_um_par(mao_1) and eh_apenas_um_par(mao_2):
        if contar_quantidades_de_repeticoes_de_um_numero(mao_1, 2, '5') == 1 :
            return mao_1
        return mao_2

    return mao_1


def test_2_pares_ganham_de_par():
    mao_par = ['5C', '5E', 'AO', '2C', '3E']
    mao_2_pares = ['5C', '5E', 'AO', 'AC', '2E']

    vencedor = jogar(mao_par, mao_2_pares)
    
    assert vencedor == mao_2_pares

def test_eh_trinca():
    cartas = ['AC', 'AP','AO','5E','JC']
    
    assert eh_trinca(cartas)

def test_nao_eh_trinca():
    cartas = ['AC' ,'5P' ,'AO' ,'5E' ,'JC']
    
    assert eh_trinca(cartas)
    
def test_dois_pares_tem_que_ter_dois_pares():
    mao_2_pares = ['5C', '5E', 'AO', 'AC', '2E']
    resultado_esperado = 2
    quantidade_de_pares = contar_quantidade_de_pares(mao_2_pares)

    assert quantidade_de_pares == resultado_esperado

def test_par_de_5_ganha_par_de_8():
    par_de_5 = ['5C', '5E', 'AO', 'AC', 'AE']
    par_de_8 = ['8C', '8E', 'AO', 'AC', 'AE']

    vencedor = jogar(par_de_5,par_de_8)

    assert vencedor == par_de_8

def test_trinca_ganha_de_par():
    par = ['8C', '8E', '2O', 'AC', 'AE']
    trinca = ['8C', '8E', 'AO', 'AC', 'AE']

    vencedor = jogar(trinca,par)

    assert vencedor == trinca

def test_eh_apenas_um_par():
    cartas = ['5C', '5E', 'AO', '2C', '3E']

    assert eh_apenas_um_par(cartas)

def test_nao_eh_apenas_um_par():
    cartas = ['5C','2E','4O','8C','JP']

    assert eh_apenas_um_par(cartas) == False