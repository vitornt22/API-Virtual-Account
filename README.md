# API-Virtual-Account
API para conta bancária virtual - Teste Grupo Nexera

Descrição dos endpoints que dispobibilizam  as funcionalidades propostas pelo teste. São eles:

1- Criação da conta 

https://virtual-account.herokuapp.com/account/api/

Endpoint para criação da conta virtual inserindo os formato de dadoa  abaixo na requisição pos


 {
    "owner": "Vitor Neto",  #Titular da conta
    "cpf": "60094287341",   #cpf
    "limit": 1500.0,        #setar o limite de crédito
    "balance": 3000.0,      # setar o saldo da conta para débito
    "accountNumber": "123", # definir o numero da conta bancária
 
 }

2- Realizar débito

https://virtual-account.herokuapp.com/operation/api/toDebit/

Endpoint para realização de débito na conta

{
    "date": "28/10/2022",     #data do pagamento
    "value": 100,             #valor do pagamento
    "description": "Débito de 100 reais ",  #descrição para exibição do extrato
    "installments": null,      #parcelas que será nulo neste caso de débito
    "accountNumber": "123"     #numero da conta
}

3- Realizar crédito

https://virtual-account.herokuapp.com/operation/api/toCredit/

{
    "date": "28/10/2022",     #data do pagamento
    "value": 100,             #valor do pagamento
    "description": "Débito de 100 reais ",  #descrição para exibição do extrato
    "installments": null,      #parcelas que será nulo neste caso de débito
    "accountNumber": "123"     #numero da conta
}


4- https://virtual-account.herokuapp.com/extract/api/{número_da_conta}/getExtracts/{númer_do_mês}/{ano}/?category=

O endpoint retorna um Json contendo o seguintes dados de uma conta:

- saldo inicial do mês e ano passados na url
-lista com os extratos realizados nesse périodo.

ex retorno :

{
    "initialBalance": 7900.0,
    "finalBalance": 7900.0,
    "extracts": [
        {
            "id": 6,
            "date": "22/07/2000",
            "category": "debit",
            "value": 100.0,
            "description": "Descrição",
            "currentBalance": 7900.0,
            "previousBalance": 8000.0,
            "installments": null,
            "accountNumber": 1
        }
    ]
 }

Se adicionarmos "debit" ou "credit" no final da url, teremos um filtro dos extratos, seguindo a categoria buscada na URL














