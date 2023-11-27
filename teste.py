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

# status_personagem = 2
# dificuldade_mapa = 50

# resultado = realizar_atividade_facil(status_personagem, dificuldade_mapa)
# print("Resultado:", resultado)

# resultado = realizar_atividade_media(status_personagem, dificuldade_mapa)
# print("Resultado:", resultado)

# resultado = realizar_atividade_dificil(status_personagem, dificuldade_mapa)
# print("Resultado:", resultado)

# resultado = realizar_atividade_extrema(status_personagem, dificuldade_mapa)
# print("Resultado:", resultado)

import curses
import time
import textwrap

def func_janela_texto_com_valor(texto):
    # Inicializa a janela
    stdscr = curses.initscr()

    # Desativa o modo de caractere de eco para que a entrada do usuário não seja exibida na tela
    curses.noecho()

    # Obtém as dimensões da janela
    height, width = stdscr.getmaxyx()

    # Divide o texto em linhas
    lines = textwrap.wrap(texto, width - 20)

    # Calcula a linha inicial para centralizar o texto verticalmente
    start_line = (height - len(lines)) // 2

    # Limpa a janela
    stdscr.clear()

    # Imprime cada linha do texto
    for i, line in enumerate(lines):
        # Calcula a coluna inicial para centralizar o texto horizontalmente
        start_col = (width - len(line)) // 2

        # Imprime a linha na posição calculada
        stdscr.addstr(start_line + i, start_col, line)

    # Obtém a entrada do usuário
    instrucao = "Digite um valor e pressione Enter:"
    start_col_instrucao = (width - len(instrucao)) // 2
    stdscr.addstr(start_line + len(lines) + 1, start_col_instrucao, instrucao)
    curses.echo()
    valor_digitado = stdscr.getstr(start_line + len(lines) + 2, start_col_instrucao).decode('utf-8')
    curses.noecho()


    # Finaliza a janela
    curses.endwin()

    return valor_digitado

import os
from main import func_janela_ASCII, func_janela_texto



questoes = {
    "Fabrica": {
        "pergunta": "O que é, o que é: Detenho capital, domino os meios de produção, acumulo riqueza, controlo os setores comerciais e industriais, e exerço influência na política. Quem sou eu? ",
        "resposta": "burguesia"
    },
    "Loja": {
        "pergunta": "O que é, o que é, que representa a luta diária pela sobrevivência através do trabalho árduo e, no contexto social, é a força impulsionadora da classe que vende sua mão de obra? ",
        "resposta": "proletariado"
    },
    "Escritorio": {
        "pergunta": "Sou um sistema ideal, onde a propriedade é coletiva, e a distribuição é baseada nas necessidades individuais. O que sou? ",
        "resposta": "comunismo"
    },
    "Gerencia": {
        "pergunta": "O que é, refere-se a um fenômeno social de tensão ou antagonismo que existe entre pessoas ou grupos de diferentes classes sociais? ",
        "resposta": "Luta de classes"
    },
    "Alta Cúpula da Empresa": {
        "pergunta": "Minha presença é evidente na especialização de funções e tarefas na sociedade, frequentemente levando à alienação e desigualdades. O que sou? ",
        "resposta": "Divisão do Trabalho"
    },
    "greve": [
        {
            "pergunta": "O que é o que é? Foi concebida por Marx, refere-se à separação ou distanciamento dos trabalhadores em relação ao produto do seu trabalho, ao processo de trabalho e até mesmo em relação a sua própria humanidade. É um fenômeno que ocorre nas sociedades capitalistas.",
            "resposta": "Alienação"
        },
        {
            "pergunta": "Sou o valor extra extraído do trabalho dos operários, representando a exploração inerente ao sistema econômico. O que sou? ",
            "resposta": "Mais-Valia"
        },
        {
            "pergunta": "O que é, sou um processo de transformação social e política que busca estabelecer uma sociedade baseada nos princípios do socialismo.",
            "resposta": "Revolução Socialista"
        }
    ]
}

def jogo_adivinhacao(questao):
    
    func_janela_texto("Para adentrar a este mapa você deve passar em teste de conceito.", "AGUARDAR_TECLA")
    
    selected_question = questoes[questao]
    resposta_correta_mostrar = selected_question["resposta"]
    resposta_correta = selected_question["resposta"].lower().replace(" ", "")
    tentativas = 3
    while True:
        
        os.system('cls')
        
        if tentativas <= 0:
            func_janela_ASCII("Voce falhou!",True,5,1)
            func_janela_ASCII("GAME OVER",True,10,"epic")
            return False
        
        resposta_usuario = func_janela_texto_com_valor(selected_question["pergunta"])
        resposta_usuario_tratada = resposta_usuario.lower().replace(" ", "")
        
        
        if not resposta_usuario_tratada.isalpha():
            pass
        elif resposta_usuario_tratada.find(resposta_correta) != -1:
            func_janela_texto(f"Parabéns pelo acerto! Agora está na hora de continuar sua jornada.", "AGUARDAR_TECLA")
            return True
        else:
            tentativas-=1
            plural = "s" if tentativas > 1 else ""
            func_janela_texto(f"Poxa, a resposta não é '{resposta_usuario}', continue tentando!", "AGUARDAR_TECLA")
            func_janela_texto(f"Você possui mais {tentativas} tentativa{plural}.", "AGUARDAR_TECLA")
        

for key in questoes.keys():
    
    if key != "greve":    
        jogo_adivinhacao(key)




