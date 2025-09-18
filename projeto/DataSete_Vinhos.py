import pandas as pd
import numpy as np



# 1. Carregar a planilha (substitua 'nome_do_seu_arquivo.csv' pelo nome do seu arquivo)
try:
    path_file = r'C:\Users\Danilo e feloza\OneDrive\Documentos\PROJETOS_SENAI\python_datascience\projeto\winemag-data-130k-v2.csv'
    df = pd.read_csv(path_file)
    # 2. Agrupar os dados por país ('country')
    # Calcule a média de 'points' e 'price' e encontre a variedade mais comum
    analysis = df.groupby('country').agg(
        total_vinhos=('country', 'size',),
        media_pontos=('points', 'mean'),
        media_preco=('price', 'mean'),
        variedade_mais_comum=('variety', lambda x: x.mode()[0] if not x.mode().empty else 'N/A')
    ).sort_values(by='media_pontos', ascending=False)

    # 3. Exibir a tabela com a análise
    print("Análise de Padrões de Consumo de Vinho por País:")
    print(analysis.to_markdown())

except FileNotFoundError:
    print("Erro: O arquivo 'winemag-data-130k-v2.csv' não foi encontrado.")
    print("Por favor, verifique se o nome do arquivo está correto e se ele está no mesmo diretório do script.")
except Exception as e:
    print(f"Ocorreu um erro durante a execução do código: {e}")
