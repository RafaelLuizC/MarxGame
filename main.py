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

    def set_detec_comunista(self,novo_valor):
        if novo_valor < 0:
            self.detec_comunista = (self.detec_comunista - novo_valor)
        else:
            self.detec_comunista = (self.detec_comunista + novo_valor)

class Jogador():
    def __init__(self,nome,carisma,força,agilidade,sorte):
        self.nome = nome
        self.carisma = carisma
        self.força = força
        self.agilidade = agilidade
        self.sorte = sorte

    def get_nome(self):
        return self.nome
    
    def get_carisma(self):
        return self.carisma
    
    def get_força(self):
        return self.força

    def get_agilidade(self):
        return self.agilidade
    
    def get_sorte(self):
        return self.sorte

###################

def func_janela_texto(text,tempo_sleep):
    # Inicializa a janela
    stdscr = curses.initscr()
    
    # Obtém as dimensões do terminal
    term_height, term_width = stdscr.getmaxyx()

    print(term_height, term_width)

    # Define as dimensões da janela
    height = min(200, term_height - 2)
    width = min(110, term_width - 2)

    # Define as margens
    margin_y = min(15, (term_height - height) // 2)
    margin_x = min(15, (term_width - width) // 2)

    # Cria uma nova janela com as dimensões e margens especificadas
    win = curses.newwin(height, width, margin_y, margin_x)

    # Divide o texto em linhas
    lines = textwrap.wrap(text, width - 2 * margin_x)

    # Calcula o número de páginas
    pages = len(lines) // (height - 2 * margin_y) + 1

    for page in range(pages):
        # Limpa a janela
        win.clear()

        # Imprime cada linha do texto
        for i in range(height - 2 * margin_y):
            # Calcula o índice da linha
            index = page * (height - 2 * margin_y) + i

            # Verifica se o índice é válido
            if index < len(lines):
                # Imprime a linha na posição calculada
                win.addstr(margin_y + i, margin_x, lines[index])

        # Atualiza a janela para mostrar o texto
        win.refresh()

    if type(tempo_sleep) == str:
        stdscr.getch()
    else:
        time.sleep(tempo_sleep)

    # Finaliza a janela
    curses.endwin()

    #text - Recebe o valor do texto
    #gerar_ascii - Recebe True/False para checar se o texto deve ser formatado para ASCII.
    #tempo_sleep - Checa quanto tempo vai ficar parado. 

def func_janela_ASCII(text,gerar_ascii,tempo_sleep):
    os.system('cls')
    # Inicializa a janela
    stdscr = curses.initscr()

    if gerar_ascii == True: #Função que serve para gerar um ascii, caso venha True na Variavel gerar_ascii, ele formata para art.
        #Caso falso, ele imprime no centro da tela.
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

def print_hud(objeto_mapa):
    print ("\n\n")

    print (f'Local: {objeto_mapa.get_nome_mapa()}\n')
    print (f'Trabalhadores: {objeto_mapa.get_camaradas_totais()}\n')
    print (f'Porcentagem Camarada: {objeto_mapa.get_porcentagem_concluida()}\n')
    print (f'Detector de Comunistas: {objeto_mapa.get_detec_comunista()}')

    print ("\n\n")

def interface(mapa_atual):
    status_menu = True
    options = mapa_atual.get_lista_mapa() #Recebe o item da lista do mapa.
    selected_option = 0 #Valor que corresponde a qual item esta selecionado

    print_hud(mapa_atual)

    while True:
        if status_menu == True:
            options = mapa_atual.get_lista_mapa()
        elif status_menu == False:
            options = mapas_desbloqueados
        time.sleep(0.1)
        # Limpar a tela
        os.system('cls')
        
        print_hud(mapa_atual)

        # Exibir as opções do menu

        for i, option in enumerate(options):
            if i == selected_option:
                print(">>", option)
            else:
                print("  ", option)
        
        if status_menu == True:
            print (f'\n\n\n {mapa_atual.get_mensagem_acoes(selected_option)}')
            
        keyboard_key = keyboard.read_event(suppress=True).name

        if checador_de_conclusao(mapa_atual) == True:
            if mapa_atual.get_nome_mapa() not in mapas_concluidos:
                mapas_concluidos.append(mapa_atual.get_nome_mapa())
                break
            else:
                pass
        elif checador_de_conclusao(mapa_atual) == False:
            pass

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
                    print("Opção 1 selecionada")
                    mapa_atual.set_camaradas(10)

            elif selected_option == 1:
                if status_menu == False:
                    mapa_atual = loja
                    status_menu = (True if status_menu == False else False)
                else:
                    print("Opção 2 selecionada")
                    # BEGIN: Opção 2 DO JOGO

            elif selected_option == 2:
                if status_menu == False:
                    mapa_atual = escritorio
                    status_menu = (True if status_menu == False else False)
                else:
                    print("Opção 3 selecionada")
                    # BEGIN: Opção 3 DO JOGO                    

            elif selected_option == 3:
                if status_menu == False:
                    mapa_atual = gerencia
                    status_menu = (True if status_menu == False else False)
                else:
                    print("Opção 4 selecionada")
                    # BEGIN: Opção 4 DO JOGO
            elif selected_option == 4:
                if status_menu == False:
                    mapa_atual = chefes
                else:
                    status_menu = (True if status_menu == False else False)
                    selected_option = 0
            elif selected_option == 5:
                if status_menu == False:
                    status_menu = (True if status_menu == False else False)

def main():
    for mapa in lista_de_mapas:
        func_janela_ASCII("A Revolucao de Fulano",True,"AGUARDAR_TECLA")
        func_janela_ASCII("Parte 1: A Descoberta",True,3)
        func_janela_texto(string_intro,"AGUARDAR_TECLA")
        mapas_desbloqueados.append(mapa.get_nome_mapa())
        interface(mapa)

##############################################################################################

#Variaveis Globais.

##############################################################################################


string_intro = (f"Fulano, um estoquista de uma poderosa corporação na cidade de Havana, capital de Cuba, trabalhava tranquilamente em seu turno quando encontrou um antigo livro empoeirado de Karl Marx especificamente o 'Manifesto do Partido Comunista'. Após procurar sem sucesso pelo proprietário e movido pela curiosidade que se instala diante dessa descoberta, ele decidiu levá-lo para casa e ler.                 \n Ao mergulhar na leitura do 'Manifesto do Partido Comunista', Fulano se deparou com uma análise contundente da sociedade dividida em classes, destacando a luta histórica entre proletários e burgueses. A cada página, sua incredulidade cresce diante dos fatos mencionados, especialmente a exploração do trabalhador pela classe capitalista. Fulano reflete sobre como seu próprio trabalho é explorado, percebendo a falta de repartição igualitária e os direitos ignorados.")


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
loja = Mapa('Loja', 60, 0, array_loja,array_texto_loja)

array_escritorio = ["Eficiência Administrativa", "Falsificação de Documentos", "Palestras Motivacionais Subversivas", "Vazamento Estratégico de Informações","Voltar"]
escritorio = Mapa('Escritorio', 40, 0, array_escritorio,array_texto_escritorio)

array_gerencia = ["Alianças Estratégicas", "Desestabilizar Hierarquia de Forma Sutil", "Reuniões de Alto Impacto", "Desobediência Civil na Administração","Voltar"]
gerencia = Mapa('Gerencia', 20, 0, array_gerencia,array_texto_gerencia)

array_chefes = ["Manipulação de Decisões Estratégicas", "Infiltrar-se em Eventos de Elite", "Discursos Subversivos na Alta Cúpula", "Desestabilização Total","Voltar"]
chefes = Mapa('Alta Cúpula da Empresa', 10, 0, array_chefes,array_texto_chefes)

lista_de_mapas = [fabrica,loja,escritorio,gerencia,chefes]

mapas_desbloqueados = []

mapas_concluidos = []

main()