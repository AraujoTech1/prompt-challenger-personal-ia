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
