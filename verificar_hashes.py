def verificar_hashes(lista_hashes):
    for hash_comparacao in lista_hashes:
        hash_calculado, hash_esperado = map(str.strip, hash_comparacao.split(","))

        # Verificando igualdade e imprimindo a saída esperada
        print("Correto" if hash_calculado == hash_esperado else "Inválido")

# Entrada do usuário
hashes_usuario = input()

# Criando a lista de pares de hashes
lista_hashes = hashes_usuario.split(";")

# Chamando a função para verificar os hashes
verificar_hashes(lista_hashes)
