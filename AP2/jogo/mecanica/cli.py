from jogo.ativos import itens, mapa, tesouro
from jogo.Personagens import Player, Monstros

def interagir_item(p, pocoes):
    mochila = [ pocoes ]
    
    """
    - lista os itens da mochila
    - pede para o jogador escolher o item
    - usa o item caso exista, ou diz que não achou aquele item na mochila
    """
    pass

def movimentar(p1, move):
    """
    - movimenta o aventureiro
    - se ele andou, seleciona uma das opções: nada, item ou monstro
    - se sorteou monstro, inicializa um monstro e começa um combate
    - se sorteou item, inicializa um item
    - retorna False se o aventureiro morrer, e True nos outros casos
    """


def jogo():
    nome = input("Deseja buscar um tesouro? Primeiro, informe seu nome: ")
    p1 = Player.p1(nome)
    print(f"Saudações, {nome}! Boa sorte!")
    tes = tesouro.Tesouro()
    mapa.map(p1, tes)

    while True:
        op = input("Insira o seu comando: ").upper()
        if op == "Q":
            print("Já correndo?")
            break

        if op == "T":
            p1.ver_atributos()
        elif op == "I":
            interagir_item(p1)
        elif op in ["W", "A", "S", "D"]:
            if movimentar(p1, op):
                mapa.map(p1, tes)
            else:
                print("Game Over...")
                break
        else:
            print(f"{p1.nome}, não conheço essa! Tente novamente!")

        if p1.posicao == tes.posicao:
            print(f"Parabéns, {p1.nome}! Você encontrou o tesouro!")
            break