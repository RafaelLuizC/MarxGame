import keyboard

def aguardar_tecla():
    while True:
        print("Pressione uma tecla...")

        # Aguarda até que uma tecla seja pressionada
        tecla_pressionada = keyboard.read_event(suppress=True).name

        print(f"Tecla pressionada: {tecla_pressionada}")

if __name__ == "__main__":
    aguardar_tecla()
