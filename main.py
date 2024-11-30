import requests
import matplotlib.pyplot as plt

def fetch_data(sensor, lastN):
    '''
    Busca os dados de uma API remota com base no sensor selecionado e no número de entradas recentes.
    
    Parâmetros:
        sensor (str): O tipo de sensor ('temperature' ou 'humidity').
        lastN (int): Número de pontos de dados recentes a serem recuperados.
        
    Retorna:
        list: Uma lista de entradas de dados se bem-sucedido, caso contrário, uma lista vazia.
    '''
    ip = 'SEU IP'  # Substitua 'SEU IP' pelo endereço IP real
    url = f"http://{ip}:8666/STH/v1/contextEntities/type/dht22/id/urn:ngsi-ld:teste123/attributes/{sensor}?lastN={lastN}"

    headers = {
        'fiware-service': 'smart',
        'fiware-servicepath': '/'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Gera um HTTPError para respostas ruins (4xx ou 5xx)

        data = response.json()
        sensor_data = data['contextResponses'][0]['contextElement']['attributes'][0]['values']
        return sensor_data
    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados da API: {e}")
    except KeyError:
        print("Formato de resposta inesperado da API.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

    return []

def plot_graph(sensor, data):
    '''
    Cria e exibe um gráfico com base nos dados buscados.
    
    Parâmetros:
        sensor (str): O tipo de sensor ('temperature' ou 'humidity').
        data (list): As entradas de dados a serem plotadas.
        
    Retorna:
        None
    '''
    if not data:
        print("Sem dados disponíveis para exibir no gráfico.")
        return

    try:
        values = [entry['attrValue'] for entry in data]
        timestamps = [entry['recvTime'] for entry in data]

        # Calcula a média dos valores
        avg_value = sum(values) / len(values)

        plt.figure(figsize=(12, 6))
        plt.plot(timestamps, values, marker='o', linestyle='-', color='darkgreen')

        # Adiciona uma linha horizontal para a média
        plt.axhline(avg_value, color='lime', linestyle='--', label=f'Média: {avg_value:.2f}')

        plt.title(f'Gráfico de {sensor.capitalize()} ao longo do tempo', fontsize=16)
        plt.xlabel('Tempo', fontsize=12)
        plt.ylabel(sensor.capitalize(), fontsize=12)
        plt.xticks(rotation=45, fontsize=10)
        plt.yticks(fontsize=10)
        plt.grid(True, linestyle='--', alpha=0.5)

        # Adiciona uma legenda
        plt.legend(fontsize=12)

        # Configura o fundo e o estilo
        plt.gca().set_facecolor('white')
        plt.gcf().set_facecolor('white')

        plt.tight_layout()
        plt.show()
    except KeyError:
        print("Erro ao processar dados para o gráfico. Verifique se o formato dos dados está correto.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado ao plotar o gráfico: {e}")

# Solicita ao usuário um valor para "lastN" entre 1 e 100
while True:
    try:
        lastN = int(input("Digite um valor para lastN (entre 1 e 100): "))
        if 1 <= lastN <= 100:
            break
        else:
            print("O valor deve estar entre 1 e 100. Tente novamente.")
    except ValueError:
        print("Por favor, digite um número válido.")

# Solicita ao usuário qual gráfico ele deseja visualizar
while True:
    sensor = input("Digite 'temperature' para visualizar o gráfico de temperatura ou 'humidity' para o gráfico de umidade: ").strip().lower()
    if sensor in ['temperature', 'humidity']:
        break
    else:
        print("Opção inválida. Por favor, digite 'temperature' ou 'humidity'.")

# Busca os dados e exibe o gráfico
sensor_data = fetch_data(sensor, lastN)
plot_graph(sensor, sensor_data)
