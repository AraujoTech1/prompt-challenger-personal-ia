# Assistente de Delivery com AWS Step Functions e Amazon Bedrock

## Descrição do Projeto

Este projeto simula um fluxo de trabalho do AWS Step Functions para o cardápio de um restaurante, permitindo que o cliente escolha entre diferentes opções de alimentos e bebidas. As opções disponíveis incluem:

- X-burguer
- Suco natural
- Milkshake
- Adicionais

O assistente utiliza a AWS Step Functions para orquestrar as etapas do pedido, integrando serviços como Amazon Bedrock para melhorar a experiência do usuário.

## Tecnologias Utilizadas

- **AWS Step Functions**
- **Amazon Bedrock**
- **Python**

## Funcionalidades

- **Escolha de Itens**
- **Recomendações**
- **Processamento do Pedido**

## Estrutura do Projeto

- `src/`: Código fonte do assistente de delivery.
- `infra/`: Scripts de infraestrutura para configuração dos serviços AWS.

## Código

### src/assistente_delivery.py

```python
import boto3

def obter_recomendacoes(itens_selecionados):
    # Exemplo de integração com o Amazon Bedrock para recomendações
    recomendacoes = []
    for item in itens_selecionados:
        recomendacoes.append(f"Recomendação para {item}")
    return recomendacoes

def processar_pedido(pedido):
    print("Processando o pedido:")
    for item in pedido:
        print(f"- {item}")

if __name__ == "__main__":
    itens_disponiveis = ["X-burguer", "Suco natural", "Milkshake", "Adicionais"]
    print("Itens disponíveis:", itens_disponiveis)
    
    pedido = []
    while True:
        escolha = input("Escolha um item (ou digite 'sair' para finalizar): ")
        if escolha.lower() == 'sair':
            break
        if escolha in itens_disponiveis:
            pedido.append(escolha)
            print(f"{escolha} adicionado ao pedido.")
        else:
            print("Item não disponível.")
    
    recomendacoes = obter_recomendacoes(pedido)
    print("Recomendações:", recomendacoes)
    processar_pedido(pedido)

    ## Captura de Tela

Aqui está uma captura de tela do aplicativo em funcionamento, mostrando a escolha do item:

![Escolha do Item](screenshots/captura%20de%20tela.png)

