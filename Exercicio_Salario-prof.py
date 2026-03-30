import pandas as pd

# Configuração global para exibir apenas 2 casas decimais no Pandas
pd.options.display.float_format = 'R$ {:,.2f}'.format

# 1. Carregar o arquivo
df = pd.read_csv('salario_prof.csv', sep=';')

# 2. Limpeza de dados (Espaços e Conversão Numérica)
df.columns = df.columns.str.strip()
df['UF'] = df['UF'].str.strip()
df['Região'] = df['Região'].str.strip()

df['Salário inicial'] = (
    df['Salário inicial']
    .astype(str)
    .str.replace('.', '', regex=False)
    .str.replace(',', '.', regex=False)
    .str.strip()
    .astype(float)
)
print("\nDados carregados e limpos com sucesso!\n")
print("="*70)
print("ANÁLISE DE SALÁRIOS DOCENTES")
print("="*70)

# 1. O estado com MENOR salário
print("\n1. Estado com o menor salário:")
estado_menor = df.loc[df['Salário inicial'].idxmin()]
print(f"-> {estado_menor['UF']}: R$ {estado_menor['Salário inicial']:,.2f}")

# 2. O estado com o MAIOR salário
print("\n2. Estado com o maior salário:")
estado_maior = df.loc[df['Salário inicial'].idxmax()]
print(f"-> {estado_maior['UF']}: R$ {estado_maior['Salário inicial']:,.2f}")

# 3. Posição de Goiás (GO) no ranking
print("\n3. Posição de Goiás no ranking nacional:")
df_ranking = df.sort_values(by='Salário inicial', ascending=False).reset_index(drop=True)
df_ranking['Posição'] = df_ranking.index + 1
posicao_go = df_ranking[df_ranking['UF'] == 'GO'].iloc[0]
print(f"-> Goiás está na {posicao_go['Posição']}ª posição com R$ {posicao_go['Salário inicial']:,.2f}")

# 4. Média salarial nacional (Todos os estados)
print("\n4. Média salarial nacional:")
media_nacional = df['Salário inicial'].mean()
print(f"-> Média Brasil: R$ {media_nacional:,.2f}")

# 5. Média salarial por Região
print("\n5. Média salarial por Região (Ordenada):")
media_por_regiao = df.groupby('Região')['Salário inicial'].mean().sort_values(ascending=False)
print(media_por_regiao)

# 6. Maior salário por Região
print("\n6. Maior salário por Região:")
maior_por_regiao = df.groupby('Região')['Salário inicial'].max().sort_values(ascending=False)
print(maior_por_regiao)

# 7. Menor salário por Região
print("\n7. Menor salário por Região:")
menor_por_regiao = df.groupby('Região')['Salário inicial'].min().sort_values(ascending=False)
print(menor_por_regiao)

# 8. Região com a MAIOR média salarial
print("\n8. Região com a maior média salarial:")
print(f"-> {media_por_regiao.idxmax()} (R$ {media_por_regiao.max():,.2f})")

# 9. Região com a MENOR média salarial
print("\n9. Região com a menor média salarial:")
print(f"-> {media_por_regiao.idxmin()} (R$ {media_por_regiao.min():,.2f})")

print("\n" + "="*70)