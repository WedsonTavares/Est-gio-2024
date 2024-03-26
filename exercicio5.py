def inverter_string(s):
    # Inicializa uma string vazia para armazenar a string invertida
    string_invertida = ""

    # Percorre a string original de trás para frente e concatena cada caractere na string invertida
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]

    # Retorna a string invertida
    return string_invertida

# String de exemplo
string_original = input("Digite a string que deseja inverter: ")

# Chamando a função para inverter a string
string_invertida = inverter_string(string_original)

# Exibindo a string invertida
print("String invertida:", string_invertida)
