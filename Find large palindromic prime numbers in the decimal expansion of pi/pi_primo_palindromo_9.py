""" 

Desafio: [1º primo palíndromo de 9 digitos na expansão do π].com
Premio: R$ 10.000,00

"""
import time
import math
import numpy as np
import decimal
from decimal import Decimal
import requests
import sys

#%%
primo_palindromo = False
batch_digits = 1000             # Lote máximo permitido pelo π delivery
n_digits = 9
n = 0
t_loop = time.time()

print('Desafio: [1º primo palíndromo de 9 digitos na expansão do π].com')
print('Premio: R$ 10.000,00')

while False == primo_palindromo:
    # d_0 = 128992
    d_0 = 1
    if n == 0:
        d_start = d_0 + n*batch_digits
    else:
        d_start = d_0 + n*batch_digits - n_digits
    print(50 * '#')
    print(f'Tempo decorrido do loop, com lote de {batch_digits} dígitos: {round((time.time() - t_loop),1)}s')
    print(f'N-ésimo dígito, primeiro do {n+1}º lote: {d_start}')
    print((50 * '#'),'\n')
    # Pegar os dígitos da expansão de π (https://pi.delivery/#apipi_get) - 100 trilhões de dígitos:
    url = f'https://api.pi.delivery/v1/pi?start={d_start}&numberOfDigits={batch_digits}'
    resposta = requests.get(url)
    print(50 * '#')
    
    # Verifica se a solicitação da url foi bem-sucedida:
    if resposta.status_code == 200:
        print('Análise do lote...')
        
        for i in range(batch_digits - n_digits + 1):
            print("\r[{0}{1}] {2}%".format('#' * int(i/(batch_digits - n_digits)*50), 
                                            ' ' * (50 - int(i/(batch_digits - n_digits)*50)), 
                                            round(i/(batch_digits - n_digits)*100,1)), end='')
            conteudo = resposta.json()
            lote_digits = conteudo['content']
            pi_9 = str(lote_digits)[i:n_digits + i]
            pi_9_reversed = pi_9[::-1]
            ti_palin = time.time()
            
            # Verificar se o número é um palíndromo e possível primo:
            if pi_9 == pi_9_reversed and pi_9[-1] in ['1', '3', '7', '9']:
                print(f"\nOs 9 dígitos {pi_9} da expansão de π é um palíndromo e possível primo")
                print('Verificando se é número primo... ')
                
                for x in range(3, int(np.sqrt(int(pi_9))) + 1):
                    if (int(pi_9) % x) == 0:
                        print(f"O número {pi_9} não é primo")
                        break
                        
                else:
                    print(f"O número {pi_9} é primo")
                    pi_9_primo_palindromo = pi_9
                    primo_palindromo = True
                    tf_palin = time.time()
                    temp_palin = np.array(round((tf_palin - ti_palin),2))
                    print(f'O tempo de verificação do palíndromo primo de {n_digits} dígitos foi de {temp_palin}s', end='')
                    break
            else:
                pass
            
    else:
        print('Não foi possível acessar a página:', resposta.status_code)
        
    n += 1
    print('\n', end='')
    print((50 * '#'),'\n')
    
print(50 * '#')
print(f"O número {pi_9} é o 1º primo palíndromo de {n_digits} dígitos da expansão de π")
print((50 * '#'),'\n')






#%%
# formula = int(input("Escolha a fórmula de calcular o Pi:\n1 - Leibniz;\n2 - Nilakantha;\n3 - Machin;\n4 - Chudnovsky.\n")) #;\n5 - Bailey-Borwein-Plouffe.\n"))


# ###################################################################
# """
# fórmula de Leibniz: 
# que é uma série infinita alternada que converge para Pi
# """
# def Leibniz_pi(n):
#     pi = 0
#     for i in range(n):
#         pi += ((-1)**i) / (2*i+1)
#     return 4*pi

# """ 
# Fórmula de Nilakantha:
# A fórmula de Nilakantha é uma série infinita que converge rapidamente para Pi. É dada por:
# """
# def Nilakantha_pi(n):
#     pi = 3.0
#     sinal = 1.0
#     j = 2.0
#     for i in range(n):
#         pi += sinal * 4.0 / (j * (j+1) * (j+2))
#         sinal *= -1.0
#         j += 2.0
#     return pi

# """ 
# Fórmula de Machin:
# A fórmula de Machin é uma fórmula que usa funções trigonométricas para calcular Pi. É dada por:
# pi = 4 * (4*arctan(1/5) - arctan(1/239))
# """
# def Machin_pi():
#     arctan_1_5 = math.atan(1.0/5.0)
#     arctan_1_239 = math.atan(1.0/239.0)
#     pi = 4.0 * (4.0*arctan_1_5 - arctan_1_239)
#     return pi

# """ 
# In 1989, the Chudnovsky brothers computed π to over 1 billion decimal places on the supercomputer IBM 3090
# using the following variation of Ramanujan's infinite series of π:
# Pi = 1 / ( 12 * SUM[k=0 to infinity]( ((-1)^k(6*k)!(13591409 + 545140134*k)) / ((3*k)!(k!)^3(640320)^(3*k+3/2)) ) 
# """
# def Chudnovsky_pi(num_termos):
#     decimal.getcontext().prec = num_termos // 14 + 2
    
#     somatorio = Decimal(0)
#     k = 0
#     for k in range(num_termos):
#         numerador = Decimal((-1)**k) * Decimal(math.factorial(6*k)) * Decimal((13591409 + 545140134*k))
#         denominador = Decimal(math.factorial(3*k)) * Decimal(math.factorial(k)**3) * Decimal(640320**(3*k))
#         somatorio += numerador / denominador
    
#     constante = Decimal(426880*Decimal(10005).sqrt())
#     resultado = constante / somatorio
#     return resultado

# """ 
# Fórmula de Bailey-Borwein-Plouffe:
# A fórmula de Bailey-Borwein-Plouffe é uma fórmula que
# permite calcular qualquer dígito de Pi sem precisar
# calcular os dígitos anteriores. É dada por:
# pi = SUM[ k=0 até infinito ] (1/16^k) * { 4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6) }
# """
# def pi_digit(n):
#     pi = 0.0
#     k = 0
#     while True:
#         termo = 1.0 / 16**k * (4.0/(8*k+1) - 2.0/(8*k+4) - 1.0/(8*k+5) - 1.0/(8*k+6))
#         pi += termo
#         if abs(termo) < 1e-15:
#             break
#         k += 1
#     return int(pi * 16**n) % 16

# ###################################################################




# if formula == 1:
#     n = int(input("Insira o número de termos da série:\n"))
#     label_formula = "Leibniz"
#     ti = time.time()
#     Pi_calc = Leibniz_pi(n)
#     tf = time.time()
# elif formula == 2:
#     n = int(input("Insira o número de termos da série:\n"))
#     label_formula = "Nilakantha"
#     ti = time.time()
#     Pi_calc = Nilakantha_pi(n)
#     tf = time.time()
# elif formula == 3:
#     label_formula = "Machin"
#     ti = time.time()
#     Pi_calc = Machin_pi()
#     tf = time.time()
# elif formula == 4:
#     n = int(input("Insira o número de termos da série:\n"))
#     label_formula = "Chudnovsky"
#     ti = time.time()
#     Pi_calc = Chudnovsky_pi(n)
#     tf = time.time()
# elif formula == 5:
#     n_digit = int(input("Escolha o n-ésimo dígito de Pi:\n"))
#     label_formula = "Bailey-Borwein-Plouffe"
#     ti = time.time()
#     Pi_calc = pi_digit(n_digit)
#     tf = time.time()
    
# temp_cal = np.array(round((tf - ti),2))

# print(50 * '-')
# print(f'Pi com 15 casas decimais do pacote \'math\' é {math.pi}')
# print(f"Pi pela fórmula de {label_formula} é {Pi_calc}. \nNúmero de casas decimais: {len(str(Pi_calc))-2}")
# print(f"O tempo gasto foi de {temp_cal}s.")
# print(f"O erro em relação ao Pi de 1000 digitos é {abs((Decimal(Pi_calc))-Decimal(math.pi))}.")
# print((50 * '-'),'\n')
