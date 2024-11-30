# Projeto EcoBreathe | Dashboard

Este projeto é um sistema de visualização de dados coletados por um microcontrolador **ESP32** e sensores **DHT22** conectados a uma Máquina Virtual. Ele permite monitorar e analisar informações de **temperatura** e **umidade** em tempo real, exibindo gráficos interativos e informativos.

---

## 📋 Funcionalidades

- **Visualização Gráfica**: Gráficos interativos que mostram os dados coletados por sensores IoT ao longo do tempo.
- **Consulta Personalizada**: Escolha do número de amostras mais recentes a serem exibidas, de 1 a 100.
- **Média Dinâmica**: Exibição de uma linha indicando a média dos valores coletados.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Bibliotecas**:
  - [`requests`](https://pypi.org/project/requests/): Para consumo de APIs RESTful.
  - [`matplotlib`](https://matplotlib.org/): Para criar gráficos dinâmicos e visuais.
- **Serviço Backend**: FIWARE Orion Context Broker para gerenciamento dos dados.

---

## 🚀 Pré-requisitos

1. **Python 3.x** instalado na sua máquina.  
   Caso não tenha instalado, siga as instruções no site oficial: [Python.org](https://www.python.org/).

2. Instale as bibliotecas necessárias:
   ```bash
   pip install requests matplotlib

---

## ⚙️ Faça você também!

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio

2. Abra o arquivo `main.py` e substitua o valor da variável `ip` pelo IP da sua Máquin Virtual:
   ```python
   ip = 'SEU_IP'

3. Execute o Script
   ```python
   python main.py

---

## 🧑‍💻 Como funciona

```markdown
---

## 📊 Como Usar

1. Ao executar o script, você será solicitado a inserir:
   - **Número de amostras** (`lastN`): Escolha entre 1 e 100.
   - **Tipo de dado**: Escolha entre `temperature` (temperatura) ou `humidity` (umidade).

2. O sistema acessará os dados na API e exibirá um gráfico com:
   - **Valores coletados** ao longo do tempo.
   - **Linha de média** para facilitar a análise.

3. O gráfico será atualizado dinamicamente com base nos parâmetros escolhidos.

Exemplo de entrada:
```bash
Digite um valor para lastN (entre 1 e 100): 50
Digite 'temperature' para visualizar o gráfico de temperatura ou 'humidity' para o gráfico de umidade: temperature

```

---

## 🖥️ Exibição dos Gráficos
<div>
  
  ![Captura de tela 2024-11-30 122303](https://github.com/user-attachments/assets/3278d5bb-a755-456d-83ee-70c16f07fbc2)

  
  ![Captura de tela 2024-11-30 122329](https://github.com/user-attachments/assets/36db048c-acf6-40a4-aa86-22a881bd12a6)

</div>
