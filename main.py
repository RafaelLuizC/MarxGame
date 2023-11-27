import keyboard
import time
import os
import random
import pyfiglet
import curses
import textwrap

class Mapa():
    
    def __init__(self,nome_mapa,camaradas_totais,valor_dificuldade,lista_mapa,mensagem_acoes):
        
        self.lista_mapa = lista_mapa
        self.nome_mapa = nome_mapa
        self.camaradas_totais = int(camaradas_totais)
        self.camaradas_conquistados = int(0)
        self.valor_dificuldade = valor_dificuldade
        self.detec_comunista = int(0)
        self.mensagem_acoes = mensagem_acoes

    def get_lista_mapa(self):
        return self.lista_mapa 

    def get_nome_mapa(self):
        return self.nome_mapa

    def get_camaradas_totais(self):
        return self.camaradas_totais

    def get_porcentagem_concluida(self):
        return round(self.camaradas_conquistados / self.camaradas_totais *100,2)

    def get_detec_comunista(self):
        return self.detec_comunista
    
    def get_mensagem_acoes(self,numero_acao):
        return self.mensagem_acoes[numero_acao]

    def set_camaradas(self,soma_valor):
        self.camaradas_conquistados = (self.camaradas_conquistados + soma_valor)
        if self.camaradas_conquistados < 0:
            self.camaradas_conquistados = 0

    def set_detec_comunista(self,novo_valor):
        #caso o valor seja negativo, ele vai subtrair, caso seja positivo, vai somar.
        self.detec_comunista = (self.detec_comunista + novo_valor)
        if self.detec_comunista < 0:
            self.detec_comunista = 0


class Jogador():
    def __init__(self,nome,carisma,forca,agilidade,sorte):
        self.nome = nome
        self.carisma = carisma
        self.forca = forca
        self.agilidade = agilidade
        self.sorte = sorte

    def get_nome(self):
        return self.nome
    
    def get_carisma(self):
        return self.carisma
    
    def get_forca(self):
        return self.forca

    def get_agilidade(self):
        return self.agilidade
    
    def get_sorte(self):
        return self.sorte
    
    def set_agilidade(self, agilidade):
        self.agilidade += agilidade

    def set_carisma(self, carisma):
        self.carisma += carisma
    
    def set_forca(self, forca):
        self.forca += forca
###################


def func_janela_texto(text,tempo_sleep):
    # Inicializa a janela
    stdscr = curses.initscr()
    
    # Obtém as dimensões da janela
    height, width = stdscr.getmaxyx()

    # Divide o texto em linhas
    lines = text.split('\n')

    lines = textwrap.wrap(text, width - 20)
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

    #Imprime um botão para continuar

    # Atualiza a janela para mostrar o texto
    stdscr.refresh()


    # Aguarda o usuário pressionar uma tecla para sair
    if type(tempo_sleep) == str:
        time.sleep(1)
        stdscr.addstr(start_line + 8, (width - len("Pressione qualquer tecla para continuar")) // 2, " >> Pressione qualquer tecla para continuar")
        stdscr.refresh()
        keyboard.wait('enter')
    else:
        time.sleep(tempo_sleep)

    # Finaliza a janela
    curses.endwin()

def func_janela_ASCII(text,gerar_ascii,tempo_sleep,fonte):
    # Inicializa a janela
    stdscr = curses.initscr()

    if gerar_ascii == True: #Função que serve para gerar um ascii, caso venha True na Variavel gerar_ascii, ele formata para art.
        if type(fonte) == str:
            ascii_font = pyfiglet.figlet_format(text,font = fonte)
            text = ascii_font
        else:
            ascii_font = pyfiglet.figlet_format(text)
            text = ascii_font
    
    # Obtém as dimensões da janela
    height, width = stdscr.getmaxyx()

    # Divide o texto em linhas
    lines = text.split('\n')

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

    # Atualiza a janela para mostrar o texto
    stdscr.refresh()

    # Aguarda o usuário pressionar uma tecla para sair
    if type(tempo_sleep) == str:
        stdscr.getch()
    else:
        time.sleep(tempo_sleep)

    # Finaliza a janela
    curses.endwin()

def checador_de_conclusao(objeto_mapa):
    if (objeto_mapa.get_porcentagem_concluida()) >= 100:
        return True
    else:
        return False

def print_hud(objeto_mapa,jogador):
    print("-" * 130)
    print ("\n\n\n")

    print (f'   Local: {objeto_mapa.get_nome_mapa()}')
    print (f'   Experiencia: {objeto_mapa.get_camaradas_totais()}')
    print (f'   Porcentagem Camarada: {objeto_mapa.get_porcentagem_concluida()}.% {"/"} 100.%')
    print (f'   Detector de Comunistas: {objeto_mapa.get_detec_comunista()} [{"x"*(objeto_mapa.get_detec_comunista()//10)+" "*((100-objeto_mapa.get_detec_comunista())//10)}]')
    print("-" * 130)
    print (f'   Pontos de Carisma: {jogador.get_carisma()}')
    print (f'   Pontos de Força: {jogador.get_forca()}')
    print (f'   Pontos de Agilidade: {jogador.get_agilidade()}')
    print (f'   Pontos de Sorte: {jogador.get_sorte()}')
    
    print ("\n")
    print("-" * 130)
    print ("\n\n")
    
## Objeto Jogador Teste
jogador = Jogador("Fulano", carisma=5, forca=5, agilidade=5, sorte=5)
### Ações possiveis no jogo


def trabalhar_duro(jogador, mapa):
    aleatoriedade = random.randint(1, 10)
    mapa.set_camaradas(-aleatoriedade)
    mapa.set_detec_comunista(-(jogador.get_forca())*2)
    func_janela_texto("A produção sobe consideravelmente graças ao seu empenho, mas as pausas para conversas amigáveis ficam escassas. Os colegas notam a mudança.", "AGUARDAR_TECLA")

def sabotagem(jogador, mapa):  
    sorte = jogador.get_sorte() / 10
    agilidade = jogador.get_agilidade()
    
    status = ( (agilidade * 4 ) + ( sorte * 6 ) ) / 10
    aleatoriedade = random.randint(1, 10)
    
    if aleatoriedade <= status:
        mapa.set_camaradas(aleatoriedade*4)
        func_janela_texto("Ninguem viu sua sabotagem, somente os camaradas!Você ganhou pontos com eles, bom trabalho!", "AGUARDAR_TECLA")
    else:
        mapa.set_camaradas(aleatoriedade*3)
        mapa.set_detec_comunista(aleatoriedade*3)
        func_janela_texto("Você foi pego durante a sabotagem... Os camaradas ficaram mais desmotivados em seguir você.", "AGUARDAR_TECLA")
    jogador.set_agilidade(1)
        
def discurso(jogador, mapa):
    carisma = jogador.get_carisma()
    sorte = jogador.get_sorte()
    
    status = ( (carisma * 4 ) + ( sorte * 6 ) ) / 10
    aleatoriedade = random.randint(1, 10)
    
    if aleatoriedade <= status: 
        mapa.set_camaradas(status*4)
        func_janela_texto("Ótimo discurso! Os camaradas se sentiram mais motivados em seguir suas ideias.", "AGUARDAR_TECLA")
    else:
        mapa.set_detec_comunista(aleatoriedade*3) 
        mapa.set_camaradas(aleatoriedade)
        func_janela_texto("Péssimo discurso...\n\nVocê se perdeu nas palavras, os camaradas não gostaram das ideias e acabaram reportando os gestores.\n", "AGUARDAR_TECLA")
        
    jogador.set_carisma(1)

def greve(mapa):

    ## Tem 10% de chance de dar ruim    
    aleatoriedada = random.randint(1, 10)
    
    if aleatoriedada == 1:
        mapa.set_detec_comunista((aleatoriedada*3))
        mapa.set_camaradas(aleatoriedada*10)
        func_janela_texto("A greve foi um sucesso! Os gestores cederam as demandas dos trabalhadores e a empresa se tornou um lugar melhor para se trabalhar.", "AGUARDAR_TECLA")
    else:
        mapa.set_camaradas(aleatoriedada*2)
        mapa.set_detec_comunista(aleatoriedada*10)
        func_janela_texto("A greve foi um fracasso... Os gestores não cederam as demandas dos trabalhadores e a empresa continuou um lugar ruim para se trabalhar.", "AGUARDAR_TECLA")

    
def interface(mapa_atual,):
    status_menu = True
    options = mapa_atual.get_lista_mapa() #Recebe o item da lista do mapa.
    selected_option = 0 #Valor que corresponde a qual item esta selecionado

    print_hud(mapa_atual,jogador)

    while True:
        if status_menu == True:
            options = mapa_atual.get_lista_mapa()
        elif status_menu == False:
            options = mapas_desbloqueados
        time.sleep(0.1)
        # Limpar a tela
        os.system('cls')
        
        print_hud(mapa_atual,jogador)

        # Exibir as opções do menu

        for i, option in enumerate(options):
            if i == selected_option:
                print(f' >> {option}'.center(130))
            else:
                print(f'    {option}'.center(130))
        
        if status_menu == True:
            #Printa uma linha para separar o menu das ações
            print (f'\n\n')
            print("-" * 130)
            print (f'\n\n   {mapa_atual.get_mensagem_acoes(selected_option)}')
            print (f'\n\n')
            print("-" * 130)


        if checador_de_conclusao(mapa_atual) == True:
            if mapa_atual.get_nome_mapa() not in mapas_concluidos:
                mapas_concluidos.append(mapa_atual.get_nome_mapa())
                break
            else:
                pass
        elif checador_de_conclusao(mapa_atual) == False:
            pass
        
        if game_over_check(mapa_atual) == True:
            break

        keyboard_key = keyboard.read_event(suppress=True).name

        # Processar a entrada do usuário
        if keyboard_key == ('up'):
            selected_option = (selected_option - 1) % len(options)
        if keyboard_key == ('down'):
            selected_option = (selected_option + 1) % len(options)
        elif keyboard_key == ('enter'):
            # Executar a ação correspondente à opção selecionada
            if selected_option == 0:
                if status_menu == False:
                    mapa_atual = fabrica
                    status_menu = (True if status_menu == False else False)
                else:
                    trabalhar_duro(jogador, mapa_atual)
            elif selected_option == 1:
                if status_menu == False:
                    mapa_atual = loja
                    status_menu = (True if status_menu == False else False)
                else:
                    sabotagem(jogador, mapa_atual)

            elif selected_option == 2:
                if status_menu == False:
                    mapa_atual = escritorio
                    status_menu = (True if status_menu == False else False)
                else:
                    discurso(jogador, mapa_atual)                   

            elif selected_option == 3:
                if status_menu == False:
                    mapa_atual = gerencia
                    status_menu = (True if status_menu == False else False)
                else:
                    greve(mapa_atual)
                    
            elif selected_option == 4:
                if status_menu == False:
                    mapa_atual = chefes
                else:
                    status_menu = (True if status_menu == False else False)
                    selected_option = 0
            elif selected_option == 5:
                if status_menu == False:
                    status_menu = (True if status_menu == False else False)

def func_inicializar_mapa(mapa):
    mapas_desbloqueados.append(mapa.get_nome_mapa())
    interface(mapa)
    if game_over_check(mapa) == True:
        return True
    func_janela_ASCII("Voce Foi Promovido!",True,5,0)

    
def game_over_check(mapa):
    if mapa.detec_comunista >= 100:
        func_janela_ASCII("Voce foi descoberto!",True,5,1)
        func_janela_ASCII("GAME OVER",True,10,"epic")
        return True

# Jogo de adivinhação
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
        "pergunta": "Sou um sistema ideal, onde a propriedade é coletiva, e a distribuição é baseada nas necessidades coletivas. O que sou? ",
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
            "resposta": "Mais Valia"
        },
        {
            "pergunta": "O que é, sou um processo de transformação social e política que busca estabelecer uma sociedade baseada nos princípios do socialismo.",
            "resposta": "Revolução Socialista"
        }
    ]
}

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

def jogo_adivinhacao(questao, texto_inicial="Para adentrar a este mapa você deve passar em um teste de conceito para mostrar seus conhecimentos."):
    if texto_inicial:
        func_janela_texto(texto_inicial, "AGUARDAR_TECLA")
    
    pergunta = questao['pergunta']
    resposta = questao['resposta']
    
    resposta_correta_tratada = resposta.lower().replace(" ", "")
    tentativas = 3
    while True:
        
        os.system('cls')
        
        if tentativas <= 0:
            func_janela_ASCII("Voce falhou!",True,5,1)
            func_janela_ASCII("GAME OVER",True,10,"epic")
            return False
        
        resposta_usuario = func_janela_texto_com_valor(pergunta)
        resposta_usuario_tratada = resposta_usuario.lower().replace(" ", "")
        
        
        if not resposta_usuario_tratada.isalpha():
            pass
        elif resposta_usuario_tratada.find(resposta_correta_tratada) != -1:
            func_janela_texto(f"Parabéns pelo acerto! Agora está na hora de continuar sua jornada.", "AGUARDAR_TECLA")
            return True
        else:
            tentativas-=1
            plural = "s" if tentativas > 1 else ""
            func_janela_texto(f"Poxa, a resposta não é '{resposta_usuario}', continue tentando!", "AGUARDAR_TECLA")
            func_janela_texto(f"Você possui mais {tentativas} tentativa{plural}.", "AGUARDAR_TECLA")

def main():
    for mapa in lista_de_mapas:
        if mapa.get_nome_mapa() == "Fabrica":
            func_janela_ASCII("A Revolucao de Fulano",True,"AGUARDAR_TECLA","slant")
            func_janela_ASCII("Parte 1 : A Descoberta",True,3,0)
            func_janela_texto(introducao_fulano_part_1,"AGUARDAR_TECLA")
            func_janela_texto(introducao_fulano_part_2,"AGUARDAR_TECLA")
            func_janela_ASCII("Parte 2 : A Consciencia",True,3,0)
            func_janela_texto(introducao_fulano_part_3,"AGUARDAR_TECLA")
            func_janela_ASCII("Parte 3 : Momento de Agir",True,3,0)
            func_janela_texto(introducao_fulano_part_4,"AGUARDAR_TECLA")
            func_janela_texto(introducao,"AGUARDAR_TECLA")
            if not jogo_adivinhacao(questoes[mapa.get_nome_mapa()]):
                break
            func_janela_texto(momento_1,"AGUARDAR_TECLA")
            
            if func_inicializar_mapa(mapa) == True:
                break
        
        if mapa.get_nome_mapa() == "Loja":
            if not jogo_adivinhacao(questoes[mapa.get_nome_mapa()]):
                break
            func_janela_ASCII("Loja",True,4,1)
            func_janela_texto(momento_2,"AGUARDAR_TECLA")
            if func_inicializar_mapa(mapa) == True:
                break
        if mapa.get_nome_mapa() == "Escritorio":
            if not jogo_adivinhacao(questoes[mapa.get_nome_mapa()]):
                break
            func_janela_ASCII("Escritorio",True,4,1)
            func_janela_texto(momento_3,"AGUARDAR_TECLA")
            if func_inicializar_mapa(mapa) == True:
                break
        if mapa.get_nome_mapa() == "Gerencia":
            if not jogo_adivinhacao(questoes[mapa.get_nome_mapa()]):
                break
            func_janela_ASCII("Gerencia",True,4,1)
            func_janela_texto(momento_4,"AGUARDAR_TECLA")
            if func_inicializar_mapa(mapa) == True:
                break
        if mapa.get_nome_mapa() == "Alta Cúpula da Empresa":
            if not jogo_adivinhacao(questoes[mapa.get_nome_mapa()]):
                break
            func_janela_ASCII("A Presidencia",True,4,1)
            func_janela_texto(momento_5,"AGUARDAR_TECLA")
            if func_inicializar_mapa(mapa) == True:
                break
            
            func_janela_texto("Você finalmente chegou aqui, você está a um passo de conquistar os meio de produção, falta um ultimo teste para conquistar seu objetivo.", "AGUARDAR_TECLA")
            func_janela_ASCII("O ultimo passo",True,4,1)
            func_janela_texto("Agora você tera que responder 3 dificieis enigmas, que escondem um profundo siginificado. Após concluir os enigmas, sua vitoria será garantida!", "AGUARDAR_TECLA")
            
            perdeu = False
            for questao in questoes["greve"]:
                if not jogo_adivinhacao(questao, texto_inicial=False):
                    func_janela_texto("Você escorreu no ultimo passo, acabou sendo pego. Foi por muito pouco.", "AGUARDAR_TECLA")
                    func_janela_ASCII("Voce falhou!",True,5,1)
                    func_janela_ASCII("GAME OVER",True,10,"epic")
                    perdeu = True
                    break
                
            if not perdeu:
                func_janela_texto("Parabéns camarada! Após uma longa jornada você conseguiu se infiltrar no sistema e derrubar a ditadura da burguesia. Você trouxe paz e liberdade para nossa sociedade, obrigado!", "AGUARDAR_TECLA")
                func_janela_ASCII("Você completou o jogo!",True,5,1)
            
            break

##############################################################################################

#Variaveis Globais.

##############################################################################################


introducao_fulano_part_1 = (f"Fulano, um estoquista de uma poderosa corporação na cidade de Havana, capital de Cuba, trabalhava tranquilamente em seu turno quando encontrou um antigo livro empoeirado de Karl Marx especificamente o 'Manifesto do Partido Comunista'. Após procurar sem sucesso pelo proprietário e movido pela curiosidade que se instala diante dessa descoberta, ele decidiu levá-lo para casa e ler.")
introducao_fulano_part_2 = (f"Ao mergulhar na leitura do 'Manifesto do Partido Comunista', Fulano se deparou com uma análise contundente da sociedade dividida em classes, destacando a luta histórica entre proletários e burgueses. A cada página, sua incredulidade cresce diante dos fatos mencionados, especialmente a exploração do trabalhador pela classe capitalista. Fulano reflete sobre como seu próprio trabalho é explorado, percebendo a falta de repartição igualitária e os direitos ignorados. ")
introducao_fulano_part_3 = (f"Fulano passou semanas refletindo sobre o que havia lido. A cada dia que passa, as prateleiras que ele organiza parecem carregar não apenas produtos, mas também a história da exploração que ele agora acompanha. Ele começou a notar como seu próprio trabalho era explorado. Ele percebe que longas horas de trabalho e a dedicação ao seu cargo não são recompensadas de maneira justa, não tinha participação nas decisões da empresa e era tratado como uma peça descartável. Fulano também começou a perceber como a sociedade em geral era desigual. Os ricos eram cada vez mais ricos, enquanto os pobres eram cada vez mais pobres.")
introducao_fulano_part_4 = (f"A análise do manifesto não apenas ilumina as contradições da sociedade em que Fulano está inserido, mas também incita uma chama de resistência dentro dele. Ele queria lutar por mudanças. Após semanas de reflexão, Fulano decide agir. Ele inicia sua jornada de conscientização abordando os colegas de trabalho. A luta pela justiça social começa nos bastidores, onde Fulano compartilha sua nova consciência, motivando seus colegas a enxergarem além das aparências da liberdade ilusória que a empresa oferece.")
introducao = (f"Fulano, agora desesperado com a realidade da exploração do trabalho, decide iniciar sua jornada de conscientização a partir de seus colegas. Seu primeiro alvo é o auxiliar de limpeza, uma figura que muitas vezes é invisível, mas essencial para o funcionamento da corporação.")
momento_1 = (f"Fulano decidiu compartilhar suas descobertas, buscando o auxiliar de limpeza nos cantos mais esquecidos da empresa. Entre baldes e vassouras, ele começa a explicar as ideias de Marx, ressaltando como as bases da sociedade capitalista afetam até mesmo aqueles que muitas vezes passam despercebidos. Será necessário superar obstáculos para convencer o colega de trabalho sobre a importância de unir forças.")
momento_2 = (f"O próximo passo é convencer os Vendedores, que embora sejam mais expostos ao público, muitas vezes são vítimas de uma grande competitividade . Fulano dotado do conhecimento que adquiriu, explora os corredores da empresa para encontrar os vendedores. Ele ressalta como a busca incessante por lucro impacta não apenas os trabalhadores, como também a qualidade dos produtos e serviços oferecidos.")
momento_3 = (f"A batalha agora se intensifica ao chegar no supervisor de vendas. Eles muitas vezes são uma ponte entre a base e a gestão. Fulano precisa encontrar maneiras de driblar a resistência e mostrar como a luta pela igualdade beneficia a todos, inclusive aqueles em posições específicas. Estratégia e persuasão serão fundamentais nesse desafio.")
momento_4 = (f"Ao chegar na gerência, Fulano se depara com um desafio de confrontar aqueles que estão mais próximos da liderança. Aqui, ele precisa de argumentos sólidos e articulados sobre como uma mudança no sistema não apenas beneficiaria os trabalhadores,mas também contribuiria para uma gestão mais eficiente e justa. Será necessário enfrentar a pressão e as ameaças para alcançar os que mais tem poder.")
momento_5 = (f"O confronto final acontece no topo de toda corporação, onde Fulano busca sensibilizar o Chefe da empresa. Aqui ele deve apresentar propostas concretas para uma transformação estrutural que vai muito além de interesses individuais. A narrativa termina em uma escolha crucial que determinará o destino da empresa e o impacto nas vidas dos trabalhadores.")

array_texto_fabrica = ["Você intensifica seu trabalho nas linhas de produção, aumentando a eficiência da fábrica.",
                       "Sabotagem discreta nas máquinas para causar pequenos atrasos, sem chamar muita atenção.",
                       "Durante as pausas, você sutilmente compartilha ideias revolucionárias com os colegas.",
                       "Planeja e lidera greves em setores específicos, impactando a produção de maneira estratégica.",
                       "Ir para outro departamento"]

array_texto_loja = ["Oferece um atendimento excepcional aos clientes, mantendo a operação da loja eficiente.",
                    "Sabota as caixas registradoras de forma atrasar sutilmente as transações",
                    "Durante o atendimento, compartilha ideias revolucionárias de forma disfarçada com os clientes.",
                    "Organiza uma paralisação simbólica na loja, chamando a atenção para as condições de trabalho.",
                    "Ir para outro departamento"]

array_texto_escritorio = ["Aprimora os processos administrativos para melhorar a eficiência do escritório.",
                    "Sabota documentos para criar pequenos obstáculos burocráticos.",
                    "Organiza palestras motivacionais com mensagens revolucionárias sutis.",
                    "Vaza informações estratégicas para minar a estabilidade administrativa.",
                    "Ir para outro departamento"] 

array_texto_gerencia = ["Estabelece alianças estratégicas com membros da alta cúpula para influenciar decisões.",
                    "Atua nos bastidores para minar a hierarquia gerencial de maneira disfarçada.",
                    "Organiza reuniões estratégicas para discutir ideias revolucionárias de maneira sutil.",
                    "Coordena ações de desobediência civil dentro da gerência para impactar a estrutura administrativa.",
                    "Ir para outro departamento"]

array_texto_chefes = ["Influencia as decisões da alta cúpula para favorecer os interesses revolucionários.",
                    "Infiltre-se em eventos de elite para obter informações e minar a confiança interna.",
                    "Dá discursos estratégicos durante eventos importantes, compartilhando ideias revolucionárias.",
                    "Coordena ações ousadas para desestabilizar completamente a alta cúpula e seus interesses.",
                    "Ir para outro departamento"]

array_fabrica = ["Produção Intensiva","Desmontar Máquinas de Forma Sutil","Espalhar Ideias Subversivas", "Organizar Greves Setoriais","Voltar"]
fabrica = Mapa('Fabrica',80,0,array_fabrica,array_texto_fabrica)

array_loja = ["Atendimento Exemplar", "Desacelerar Caixas Registradoras", "Conversas Revolucionárias com Clientes", "Paralisação Simbólica","Voltar"]
loja = Mapa('Loja', 130, 0, array_loja,array_texto_loja)

array_escritorio = ["Eficiência Administrativa", "Falsificação de Documentos", "Palestras Motivacionais Subversivas", "Vazamento Estratégico de Informações","Voltar"]
escritorio = Mapa('Escritorio', 200, 0, array_escritorio,array_texto_escritorio)

array_gerencia = ["Alianças Estratégicas", "Desestabilizar Hierarquia de Forma Sutil", "Reuniões de Alto Impacto", "Desobediência Civil na Administração","Voltar"]
gerencia = Mapa('Gerencia', 300, 0, array_gerencia,array_texto_gerencia)

array_chefes = ["Manipulação de Decisões Estratégicas", "Infiltrar-se em Eventos de Elite", "Discursos Subversivos na Alta Cúpula", "Desestabilização Total","Voltar"]
chefes = Mapa('Alta Cúpula da Empresa', 500, 0, array_chefes,array_texto_chefes)

lista_de_mapas = [fabrica,loja,escritorio,gerencia,chefes]

mapas_desbloqueados = []

mapas_concluidos = []

main()