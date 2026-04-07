# Atividade Pandas-2
import pandas as pd
print("="*55)
print("Questões 1 a 10: Manipulação de DataFrames com Pandas")
print("="*55)

# Questão 1
print("\nQuestão 1: Dicionário com dados de 5 alunos")

# Criando o dicionário com os dados dos alunos
dados_alunos = {
    'Nome': ['Ana', 'Beto', 'Carlos', 'Diana', 'Eduardo'],
    'Idade': [20, 22, 21, 23, 19]
}
print("\n--- Dicionário de Alunos ---")
print(dados_alunos)

# Criando o DataFrame a partir do dicionário e exibindo o resultado
df_alunos = pd.DataFrame(dados_alunos)
print("\n--- DataFrame de Alunos ---")
print(df_alunos)
print("="*55)


# Questão 2
print("\nQuestão 2: Lista de dicionários para o setor de RH")

# Criando a lista de dicionários com os dados dos funcionários
lista_rh = [
    {'Nome': 'Ana', 'Cargo': 'Analista'}, 
    {'Nome': 'Bruno', 'Cargo': 'Gerente', 'Bonus': 500}
]

# Criando o DataFrame a partir da lista de dicionários e exibindo o resultado
df_rh = pd.DataFrame(lista_rh)
print(df_rh)
# Explicação: O que acontece com a coluna 'Bonus' para a funcionária Ana?
# Como o dicionário referente à Ana não possui a chave 'Bonus', o Pandas 
# preenche automaticamente esse espaço vazio no DataFrame com o valor NaN 
# (Not a Number), indicando um dado ausente.
print("="*55)


# Questão 3
print("\nQuestão 3: Criando um DataFrame a partir de Series")

# Criando as Series para produtos e preços
produtos = pd.Series(['Notebook', 'Mouse', 'Teclado'], index=['p1', 'p2', 'p3'])
precos = pd.Series([3500.00, 150.00, 250.00], index=['p1', 'p2', 'p3'])

# Criando o DataFrame a partir das Series e exibindo o resultado
df_produtos = pd.DataFrame({'Produto': produtos, 'Preço': precos})
print(df_produtos)
print("="*55)


# Questão 4
print("\nQuestão 4: Adicionando colunas a um DataFrame existente")

# DataFrame de exemplo
print("--- DataFrame de Vendas ---")
df_vendas = pd.DataFrame({
    'Sede A': [1000, 2500, 1500],
    'Sede B': [800, 2000, 1200]
})
print(df_vendas)

# 4.1. Nova coluna com a soma das duas sedes
print("\n4.1. Nova coluna 'Total Vendas' com a soma das duas sedes:")
df_vendas['Total Vendas'] = df_vendas['Sede A'] + df_vendas['Sede B']
print(df_vendas)

# 4.2. Nova coluna calculada como 10% do valor da 'Sede A'
print("\n4.2. Nova coluna 'Imposto' calculada como 10% do valor da 'Sede A':")
df_vendas['Imposto'] = df_vendas['Sede A'] * 0.10
print(df_vendas)

# Exibindo o DataFrame atualizado
print("\n--- DataFrame Atualizado ---")
print(df_vendas)
print("="*55)


# Questão 5
print("\nQuestão 5: Excluindo colunas de um DataFrame")
df_clientes = pd.DataFrame({
    'Nome': ['João', 'Maria'],
    'CPF': ['111.111.111-11', '222.222.222-22'],
    'Telefone': ['9999-1111', '9999-2222']
})
# Exibindo o DataFrame original
print("--- DataFrame Original ---")
print(df_clientes)

# 1. Excluindo a coluna 'CPF' usando o comando del e exibindo o resultado
del df_clientes['CPF']
print("\n--- DataFrame após remover 'CPF' (via del) ---")
print(df_clientes)

# 2. Excluindo a coluna 'Telefone' usando o método pop() e guardando o retorno
telefone_removido = df_clientes.pop('Telefone')
# Exibindo o conteúdo da coluna removida
print("\n--- Conteúdo da coluna 'Telefone' removida ---")
print(telefone_removido)

# Exibindo o DataFrame final após as exclusões
print("\n--- DataFrame Final ---")
print(df_clientes)
print("="*55)


# Questão 6
print("\nQuestão 6: Utilizando o loc para recuperar dados específicos")

# Criando um DataFrame com dados de países
df_paises = pd.DataFrame(
    {'População': [214, 45, 19], 'Idioma': ['Português', 'Espanhol', 'Espanhol']},
    index=['Brasil', 'Argentina', 'Chile']
)
print(df_paises)

# Utilizando o loc para recuperar apenas os dados do Brasil
print("\n--- Recuperando dados do Brasil ---")
dados_brasil = df_paises.loc['Brasil']
print(dados_brasil)
print("="*55)


# Questão 7
print("\nQuestão 7: Utilizando o iloc para recuperar dados específicos")

# Criando um DataFrame com dados de carros
df_carros = pd.DataFrame({
    'Modelo': ['Fusca', 'Gol', 'Palio', 'Civic', 'Corolla', 'Onix']
})
print("--- DataFrame de Carros ---")
print(df_carros)

# Utilizando o iloc para recuperar os dados do 4º e 5º carro
print("\n--- Recuperando os dados do 4º e 5º carro ---")

# O 4º carro está no índice 3 e o 5º carro está no índice 4
selecao = df_carros.iloc[3:5]
print(selecao)
print("="*55)


# Questão 8
print("\nQuestão 8: Recortando um DataFrame utilizando o iloc")

# Criando um DataFrame histórico com 20 linhas
print("--- DataFrame Histórico ---")
df_historico = pd.DataFrame({'Valor Histórico': range(101, 121)})
print(df_historico)

# Extraindo da 5ª linha (índice 4) até a 12ª linha (índice 11)
print("\n--- Recorte do DataFrame Histórico (5ª a 12ª linha) ---")
df_recorte = df_historico[4:12]
print(df_recorte)
print("="*55)


# Questão 9
print("\nQuestão 9: Concatenando DataFrames e redefinindo índices")

# Criando dois DataFrames representando o estoque de duas lojas
print("--- DataFrames das Lojas ---")
df_loja1 = pd.DataFrame({'Produto': ['A', 'B'], 'Estoque': [10, 20]})
df_loja2 = pd.DataFrame({'Produto': ['C', 'D'], 'Estoque': [30, 40]})
print("Loja 1:")
print(df_loja1) 
print("Loja 2:")
print(df_loja2)

# Concatenando loja2 ao final da loja1 e redefinindo os índices
print("\n--- DataFrame Concatenado ---")
df_resultado = pd.concat([df_loja1, df_loja2], ignore_index=True)
print(df_resultado)
print("="*55)


# Questão 10
print("\nQuestão 10: Explorando atributos de um DataFrame")

# Criando um DataFrame com dados de funcionários
df_funcionarios = pd.DataFrame({
    'Nome': ['Aline', 'Bruno', 'Carla', 'Diego'],
    'Salario': [3500, 4200, 5100, 2900]
})
print("--- DataFrame de Funcionários ---")
print(df_funcionarios)

# transposta do DataFrame, tipos de dados, quantidade total de elementos e as duas últimas linhas
print("\n10.1. Transposta do DataFrame:")
print(df_funcionarios.T)

# Os tipos de dados (dtypes) de cada coluna do DataFrame
print("\n10.2. Tipos de dados (dtypes):")
print(df_funcionarios.dtypes)

# A quantidade total de elementos (size) presente no DataFrame
print("\n10.3. Quantidade total de elementos (size):")
print(df_funcionarios.size)

# As duas últimas linhas do DataFrame utilizando o método tail()
print("\n10.4. Apenas as duas últimas linhas (tail):")
print(df_funcionarios.tail(2))
print("="*55)

# Mensagem final de conclusão da atividade
print("\nAtividade Pandas-2 concluída com sucesso!")
print("="*55)