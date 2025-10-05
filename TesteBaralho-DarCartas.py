# Crie um código que simula um baralho de cartas.
# O código deve conter as seguintes funções:

# gerar_baralho -> retorna um baralho novo. Parâmetros da função
# definem quantas cópias retornar (1 baralho, 2 baralhos, ...),
# se o baralho deve conter coringas, e se deve ser embaralhado
# antes de ser retornado.

# mostrar_baralho -> exibe a quantidade de cartas no baralho e
# mostra quais são.

# dar_as_cartas -> distribui as cartas do baralho entre X
# jogadores, de forma que cada jogador recebe Y cartas.

# mostrar_jogadores -> exibe a quantidade de cartas na mão de
# cada jogador e mostra quais são.

# A partir dessas funções, o código deve:
# - gerar o baralho e exibi-lo
# - dar as cartas para os jogadores
# - exibir o baralho após as cartas terem sido distribuídas
# - exibir a mão de cada jogador

# DICA: utilize os símbolos ♠ ♥ ♦ ♣ para representar os naipes.
# DICA: utilize a função random.shuffle (módulo random) para embaralhar.

import random
import time

# ----------------------------------------------------
# criação de um baralho apenas:
baralho_montar = []
um_baralho = []
numero_cartas = list(range(2, 11))
letras_cartas = ["J", "Q", "K", "A"]
naipe_cartas = ["♠", "♥", "♦", "♣"]
baralho_montar = numero_cartas + letras_cartas
for cartas in baralho_montar:
    for naipe in naipe_cartas:
        um_baralho.append(str(cartas) + naipe)
print(f"Um baralho sozinho possui {len(um_baralho)} cartas.\n")
# -----------------------------------------------------
# Escolha de quantos baralhos são:
while True:
    numero_de_baralhos = int(
        input("Então com quantos baralhos deseja jogar?(de 1 a 4)  ")
    )
    if numero_de_baralhos in [1, 2, 3, 4]:
        break
baralhos_existentes = 0
baralhos_prontos = []
while baralhos_existentes < numero_de_baralhos:
    baralhos_prontos.extend(um_baralho)
    baralhos_existentes += 1

time.sleep(0.5)
print(f"\nO baralho de jogo será então de {len(baralhos_prontos)} cartas!\n")
# -------------------------------------------------------
# Escolha de coringas:
while True:
    try:
        coringas = int(input(f"Devem haver quantos coringas? Digite um nº de 0 até {baralhos_existentes}:     ")
        )
        if coringas <= baralhos_existentes and coringas > -1:
            break
        else:
            print("\nDeve ser e de zero a {baralhos_existentes} apenas! (que é o nº de baralhos)\n")
    except:
        print(f"Digite um numero inteiro! Deve ser de zero a {baralhos_existentes} apenas. (que é o nº de baralhos)\n")

if coringas > 0:
    coringas_no_baralho = 0
    while coringas > coringas_no_baralho:
        baralhos_prontos.append("JOCKER " + str(coringas_no_baralho + 1))
        coringas_no_baralho += 1

time.sleep(0.5)
print(
    f"\nO baralho de jogo será então de {len(baralhos_prontos)} cartas! Sendo {coringas} coringa(s).\n"
)
# --------------------------------------------------------
# Embaralhar ou não
while True:
    embaralhar = str.lower(input("Deseja embaralhar as cartas? (s/n)    "))
    if embaralhar in ["s", "n"]:
        break
    else:
        print("\nResponda com s ou n\n")
if embaralhar == "s":
    random.shuffle(baralhos_prontos)
    print("\nEmbaralhando...\n")
    time.sleep(2)
else:
    print("\nPreparando as cartas...\n")
    time.sleep(2)
# --------------------------------------------------------
# mostrar  o baralho

print("Pronto, o baralho completo está a baixo:\n")
print(baralhos_prontos)

# --------------------------------------------------------
# escolher quantos jogadores
while True:
    try:
        numero_de_jogadores = int(input(f"\nQuantas pessoas vão jogar? Mínimo 2 e máximo de {(baralhos_existentes * 4)} no caso:     ")
        )
        if numero_de_jogadores <= (baralhos_existentes * 4) and numero_de_jogadores >= 2:
            break
        else:
            print(f"\nDeve ser mínimo duas pessoas e no máximo de {(baralhos_existentes * 4)} no caso.\n")
    except:
        print("\nDigite um numero inteiro! Mínimo duas pessoas e máximo de quatro pessoas por baralho.\n")

time.sleep(0.5)

print(f"\nTeremos então {numero_de_jogadores} jogadores\n")
# --------------------------------------------------------
# Escolher quantas cartas pra cada e distribuir

def distribuir_cartas(baralhos_prontos, cartas_por_jogador, numero_de_jogadores):
    cartas_dos_jogadores = []
    jogadores_com_carta = 0
    while jogadores_com_carta < numero_de_jogadores:
        numero_de_cartas = 0
        jogador = []
        while numero_de_cartas < cartas_por_jogador:
            carta = baralhos_prontos.pop()
            jogador.append(carta)
            numero_de_cartas += 1
        cartas_dos_jogadores.append(jogador)
        jogadores_com_carta += 1
    return cartas_dos_jogadores


while True:
    try:
        cartas_por_jogador = int(input(f"Quantas cartas para cada jogador? Mínimo de 4 e máximo de {(baralhos_existentes * 5)} no caso: ")
        )
        if cartas_por_jogador <= (baralhos_existentes * 5) and cartas_por_jogador >= 4:
            cartas_dos_jogadores = distribuir_cartas(baralhos_prontos, cartas_por_jogador, numero_de_jogadores)
            break
        else:
            print(f"\nDeve ser mínimo 4 cartas e no máximo de {(baralhos_existentes * 5)} no caso\n")
    except:
        print(f"\nDigite um numero inteiro! Mínimo 4 cartas e máximo de {(baralhos_existentes * 5)} no caso.\n")

# --------------------------------------------------------
# mostrar o baralho que sobrou a as cartas de cada jogador

time.sleep(1)
print(f'\nTerminamos de montar o jogo! Sendo assim, o baralho que sobrou está a baixo ({len(baralhos_prontos)} cartas):\n')

print("Mostrando as cartas...\n")

{time.sleep(3)}

print(f'{baralhos_prontos}\n\nE as cartas que estão com os jogadores são as seguintes:\n')
print("\nDistribuindo as cartas...\n")

time.sleep(3)

i = 1
for _ in cartas_dos_jogadores:
    print(f'Mão do jogador {i}:\n\n{_}\n')
    i += 1

print('Terminamos de montar e distribuir as cartas! Pronto pra jogar!\n')
print('---------FIM------------')