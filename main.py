import keyboard
import time
import os
import random

class Mapa():
    
    def __init__(self,nome_mapa,camaradas_totais,valor_dificuldade,lista_mapa):
        
        self.lista_mapa = lista_mapa
        self.nome_mapa = nome_mapa
        self.camaradas_totais = int(camaradas_totais)
        self.camaradas_conquistados = int(0)
        self.valor_dificuldade = valor_dificuldade
        self.detec_comunista = int(0)

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

def print_hud(objeto_mapa):
    print ("\n\n")

    print (f'Local: {objeto_mapa.get_nome_mapa()}\n')
    print (f'Trabalhadores: {objeto_mapa.get_camaradas_totais()}\n')
    print (f'Porcentagem Camarada: {objeto_mapa.get_porcentagem_concluida()}\n')
    print (f'Detector de Comunistas: {objeto_mapa.get_detec_comunista()}')

    print ("\n\n")

def level_up(mapa_atual, nome_mapa, mapas_desbloqueados):
    # Verifica se o nome do mapa já está na lista de mapas desbloqueados
    if mapa_atual.get_nome_mapa() not in mapas_desbloqueados:
        mapas_desbloqueados.append(mapa_atual.get_nome_mapa())

def interface(mapa_atual):
    status_menu = True
    options = mapa_atual.get_lista_mapa() #Recebe o item da lista do mapa.
    selected_option = 0 #Valor que corresponde a qual item esta selecionado
    mapas_desbloqueados = ["Fabrica","Loja","Gerencia"]


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
                    print("Voce esta no lugar certo")
                else:
                    print("Opção 1 selecionada")
                    # BEGIN: Opção 1 DO JOGO

            elif selected_option == 1:
                if status_menu == False:
                    print("Voce esta no lugar certo")
                else:
                    print("Opção 2 selecionada")
                    # BEGIN: Opção 2 DO JOGO

            elif selected_option == 2:
                if status_menu == False:
                    print("Voce esta no lugar certo")
                else:
                    print("Opção 3 selecionada")
                    # BEGIN: Opção 3 DO JOGO                    

            elif selected_option == 3:
                if status_menu == False:
                    print("Voce esta no lugar certo")
                else:
                    print("Opção 4 selecionada")
                    # BEGIN: Opção 4 DO JOGO
            elif selected_option == 4:
                status_menu = (True if status_menu == False else False)
            level_up(mapa_atual, mapa_atual.get_nome_mapa(), mapas_desbloqueados)


##############################################################################################

#Variaveis Globais.

##############################################################################################

array_fabrica = ["Produção Intensiva","Desmontar Máquinas de Forma Sutil","Espalhar Ideias Subversivas", "Organizar Greves Setoriais","Voltar"]
fabrica = Mapa('Fabrica',80,0,array_fabrica)

array_loja = ["Atendimento Exemplar", "Desacelerar Caixas Registradoras", "Conversas Revolucionárias com Clientes", "Paralisação Simbólica","Voltar"]
loja = Mapa('Loja', 60, 0, array_loja)

array_escritorio = ["Eficiência Administrativa", "Falsificação de Documentos", "Palestras Motivacionais Subversivas", "Vazamento Estratégico de Informações","Voltar"]
escritorio = Mapa('Escritorio', 40, 0, array_escritorio)

array_gerencia = ["Alianças Estratégicas", "Desestabilizar Hierarquia de Forma Sutil", "Reuniões de Alto Impacto", "Desobediência Civil na Administração","Voltar"]
gerencia = Mapa('Gerencia', 20, 0, array_gerencia)

array_chefes = ["Manipulação de Decisões Estratégicas", "Infiltrar-se em Eventos de Elite", "Discursos Subversivos na Alta Cúpula", "Desestabilização Total","Voltar"]
chefes = Mapa('Alta Cúpula da Empresa', 10, 0, array_chefes)

array_texto_fabrica = ["Você intensifica seu trabalho nas linhas de produção, aumentando a eficiência da fábrica.",
                       "Sabotagem discreta nas máquinas para causar pequenos atrasos, sem chamar muita atenção.",
                       "Durante as pausas, você sutilmente compartilha ideias revolucionárias com os colegas.",
                       "Planeja e lidera greves em setores específicos, impactando a produção de maneira estratégica."]

array_texto_loja = ["Oferece um atendimento excepcional aos clientes, mantendo a operação da loja eficiente.",
                    "Sabota as caixas registradoras de forma atrasar sutilmente as transações",
                    "Durante o atendimento, compartilha ideias revolucionárias de forma disfarçada com os clientes.",
                    "Organiza uma paralisação simbólica na loja, chamando a atenção para as condições de trabalho."]

array_texto_escritorio = ["Aprimora os processos administrativos para melhorar a eficiência do escritório.",
                    "Sabota documentos para criar pequenos obstáculos burocráticos.",
                    "Organiza palestras motivacionais com mensagens revolucionárias sutis.",
                    "Vaza informações estratégicas para minar a estabilidade administrativa."] 

array_texto_gerencia = ["Estabelece alianças estratégicas com membros da alta cúpula para influenciar decisões.",
                    "Atua nos bastidores para minar a hierarquia gerencial de maneira disfarçada.",
                    "Organiza reuniões estratégicas para discutir ideias revolucionárias de maneira sutil.",
                    "Coordena ações de desobediência civil dentro da gerência para impactar a estrutura administrativa."]

array_texto_chefes = ["Influencia as decisões da alta cúpula para favorecer os interesses revolucionários.",
                    "Infiltre-se em eventos de elite para obter informações e minar a confiança interna.",
                    "Dá discursos estratégicos durante eventos importantes, compartilhando ideias revolucionárias.",
                    "Coordena ações ousadas para desestabilizar completamente a alta cúpula e seus interesses."]

interface(fabrica)