import csv

# Nome do arquivo CSV que você deseja editar
nome_arquivo = 'dados_baixados.csv'

# Ler os dados do arquivo CSV
with open(nome_arquivo, 'r', newline='', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    dados = list(leitor)

# Exibindo os dados originais
print("Dados originais:")
for linha in dados:
    print(linha)

# Realizando modificações nos dados
# Exemplo: Adicionar uma nova linha
nova_linha = ["João", 30, "Curitiba"]
dados.append(nova_linha)

# Exemplo: Atualizar valores
for linha in dados:
    if linha[0] == 'Ana':
        linha[1] = 29  # Atualiza a idade

# Salvando os dados modificados de volta ao arquivo CSV
with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados)

print(f"Arquivo CSV atualizado e salvo em {nome_arquivo}")