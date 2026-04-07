def analisar_nome_completo():
    nome_completo = input("Digite o nome completo: ").strip()
    
    partes_do_nome = nome_completo.split()
    
    print("\n--- Resultados da Análise ---")
    
    posicao_busca = 0
    
    for nome in partes_do_nome:
        tamanho = len(nome)
        
        posicao_inicial = nome_completo.find(nome, posicao_busca)
        
        nome_invertido = nome[::-1]
        
        print(f"\nNome: {nome}")
        print(f"- Caracteres: {tamanho}")
        print(f"- Posição inicial: {posicao_inicial}")
        print(f"- Invertido: {nome_invertido}")
        
        posicao_busca = posicao_inicial + tamanho

if __name__ == "__main__":
    analisar_nome_completo()