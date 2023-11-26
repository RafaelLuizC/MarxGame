import random

def realizar_atividade_facil(status_personagem, dificuldade_mapa):
    valor = random.randint(0, 100 - status_personagem * 5)  # Ajuste na chance com base no status_personagem
    print("Valor gerado:", valor)
    
    if valor >= dificuldade_mapa:
        print("Um camarada a mais")
        return 1  # Ganha um camarada
    else:
        print("Aumentou o detector")
        return 0  # Não ganha camaradas, aumenta o detector

def realizar_atividade_media(status_personagem, dificuldade_mapa):
    valor = random.randint(0, 100)
    print("Valor gerado:", valor)
    
    chance_camaradas = 70 - status_personagem * 5  # Ajuste na chance com base no status_personagem
    if valor >= dificuldade_mapa - chance_camaradas:
        print("Um camarada a mais")
        return 1  # Ganha um camarada
    else:
        print("Aumentou o detector")
        return 0  # Não ganha camaradas, aumenta o detector

def realizar_atividade_dificil(status_personagem, dificuldade_mapa):
    valor = random.randint(0, 100 + status_personagem * 5)  # Ajuste na chance com base no status_personagem
    print("Valor gerado:", valor)
    
    if valor >= dificuldade_mapa + 10:
        print("Um camarada a mais")
        return 1  # Ganha um camarada
    else:
        print("Aumentou o detector")
        return 0  # Não ganha camaradas, aumenta o detector

def realizar_atividade_extrema(status_personagem, dificuldade_mapa):
    valor = random.randint(0, 100 - status_personagem * 5)  # Ajuste na chance com base no status_personagem
    print("Valor gerado:", valor)
    
    chance_camaradas = 50 - status_personagem * 5  # Ajuste na chance com base no status_personagem
    if valor >= dificuldade_mapa - chance_camaradas:
        print("Um camarada a mais")
        return 1  # Ganha um camarada
    else:
        print("Aumentou o detector")
        return 0  # Não ganha camaradas, aumenta o detector

status_personagem = 2
dificuldade_mapa = 50

resultado = realizar_atividade_facil(status_personagem, dificuldade_mapa)
print("Resultado:", resultado)

resultado = realizar_atividade_media(status_personagem, dificuldade_mapa)
print("Resultado:", resultado)

resultado = realizar_atividade_dificil(status_personagem, dificuldade_mapa)
print("Resultado:", resultado)

resultado = realizar_atividade_extrema(status_personagem, dificuldade_mapa)
print("Resultado:", resultado)
