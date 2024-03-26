def descobrir_interruptores():
    # Ligar o primeiro interruptor
    print("Ligando o primeiro interruptor...")
    # Simular o tempo de espera
    print("Esperando alguns minutos...")
    # Desligar o primeiro interruptor e ligar o segundo interruptor
    print("Desligando o primeiro interruptor e ligando o segundo interruptor...")

    # Observar o estado das lâmpadas
    print("Indo até a sala das lâmpadas para observar o estado...")
    lampada1 = input("Estado da lâmpada 1 (acesa ou apagada): ")
    lampada2 = input("Estado da lâmpada 2 (acesa ou apagada): ")

    # Determinar qual interruptor controla cada lâmpada
    if lampada1 == "acesa":
        print("O primeiro interruptor controla a lâmpada 1.")
    elif lampada2 == "acesa":
        print("O segundo interruptor controla a lâmpada 2.")
    else:
        print("O terceiro interruptor controla a lâmpada 1.")

# Chamando a função para resolver o problema
descobrir_interruptores()
