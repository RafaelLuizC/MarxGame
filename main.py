import keyboard
import time
import os

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

    def __init__(self,carisma,força,agilidade,):
        pass



def print_hud(objeto_mapa):
    print ("\n\n")

    print (f'Local: {objeto_mapa.get_nome_mapa()}\n')
    print (f'Trabalhadores: {objeto_mapa.get_camaradas_totais()}\n')
    print (f'Porcentagem Camarada: {objeto_mapa.get_porcentagem_concluida()}\n')
    print (f'Detector de Comunistas: {objeto_mapa.get_detec_comunista()}')

    print ("\n\n")

def level_up(mapa_atual):
    pass

def interface(mapa_atual):
    options = mapa_atual.get_lista_mapa()
    selected_option = 0

    print_hud(mapa_atual)

    while True:
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
                mapa_atual.set_camaradas(10)
                # BEGIN: Opção 1
            elif selected_option == 1:
                print("Opção 2 selecionada")
                # BEGIN: Opção 2
            elif selected_option == 2:
                print("Opção 3 selecionada")
                # BEGIN: Opção 3



array_fabrica = ["Sabotagem","Discursar","Trabalhar Duro"]

fabrica = Mapa('Fabrica',80,0,array_fabrica)

interface(fabrica)
