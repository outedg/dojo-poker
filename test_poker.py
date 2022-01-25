import pytest
from collections import Counter


def eh_trinca(cartas):
    quantidade_maxima = 0
    # cartas = 'AC AP AO AE JC'
    for carta in cartas: 
        quantidade = cartas.count(list(carta)[0])
        if quantidade > quantidade_maxima:
            quantidade_maxima = cartas.count(list(carta)[0])
        
    return quantidade_maxima >= 3

def eh_par(cartas):
    return True

def jogar(mao_1, mao_2):
    if eh_trinca(mao_2) and eh_par(mao_1):
        return mao_2
    
    return mao_1

def test_eh_trinta():
    cartas = 'AC AP AO 5E JC'
    
    assert eh_trinca(cartas)

def test_nao_eh_trinta():
    cartas = 'AC 5P AO 5E JC'
    
    assert eh_trinca(cartas)

def test_par_de_5_e_par_de_8_ganha_par_de_8():
    par_de_5 = ['5C', '5E', 'AO', 'AC', 'AE']
    par_de_8 = ['8C', '8E', 'AO', 'AC', 'AE']

    vencedor = jogar(par_de_8, par_de_5)

    assert vencedor == par_de_8

def test_trinca_ganha_de_par():
    par = ['8C', '8E', '2O', 'AC', 'AE']
    trinca = ['8C', '8E', 'AO', 'AC', 'AE']

    vencedor = jogar(par, trinca)

    assert vencedor == trinca