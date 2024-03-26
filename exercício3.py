def complete_sequence(sequence):
    # Verifica qual é a letra da sequência
    if sequence == 'a':
        # Inicializa a sequência com os valores fornecidos
        seq = [1, 3, 5, 7]
        # Completa a sequência adicionando o próximo número
        seq.append(seq[-1] + 2)
    
    elif sequence == 'b':
        seq = [2, 4, 8, 16, 32, 64]
        # Completa a sequência dobrando o último número
        seq.append(seq[-1] * 2)
    
    elif sequence == 'c':
        seq = [0, 1, 4, 9, 16, 25, 36]
        # Completa a sequência adicionando o quadrado do próximo número
        seq.append((len(seq)) ** 2)
    
    elif sequence == 'd':
        seq = [4, 16, 36, 64]
        # Completa a sequência adicionando o próximo quadrado perfeito
        seq.append(81)
    
    elif sequence == 'e':
        seq = [1, 1, 2, 3, 5, 8]
        # Completa a sequência somando os dois últimos números
        seq.append(seq[-1] + seq[-2])
    
    elif sequence == 'f':
        seq = [2, 10, 12, 16, 17, 18, 19]
        # Completa a sequência adicionando o próximo número
        seq.append(seq[-1] + 1)
    
    else:
        return "Sequência não reconhecida."

    # Retorna a sequência completa
    return seq

# Testando cada sequência e imprimindo os resultados
print("Sequência a:", complete_sequence('a'))
print("Sequência b:", complete_sequence('b'))
print("Sequência c:", complete_sequence('c'))
print("Sequência d:", complete_sequence('d'))
print("Sequência e:", complete_sequence('e'))
print("Sequência f:", complete_sequence('f'))
