import pandas as pd
from twilio.rest import Client

# Biblioteca da Twilio para envio de SMS - https://www.twilio.com/pt-br/docs/libraries/python

# Config da conta do Twilio
# Your Account SID from twilio.com/console - LEMBRE-SE DE AJUSTAR ISSO CONFORME O account_sid DA SUA CONTA
account_sid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
# Your Auth Token from twilio.com/console - LEMBRE-SE DE AJUSTAR ISSO CONFORME O auth_token DA SUA CONTA
auth_token = "your_auth_token"
client = Client(account_sid, auth_token)

# Lógica - Passo a passo da solução
#  Abrir todos os arquivos de excel .xlsx
#  Para cada arquivo .xslx:
#  + Verificar se algum valor na coluna Vendas daquele arquivo é maior que 55k
#  + Se for maior que 55k -> envia um SMS com o nome, o mês e o valor das vendas do vendedor
#  + Se não for maior que 55k -> não fazer nada

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx') #f de formatação, algum item será uma variavel dentro da str
    #tabela_vendas = pd.read_excel(mes + '.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any(): #.any() para algum valor dentro do campo especificado da tabela
        # .loc[linha, coluna] para localizar/ filtrar algo  -> .loc retorna uma tabela e não um valor/ texto
        # .values[0] para retornar o valor ao invés de uma tabela
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} o vendedor {vendedor} bateu a meta de 55k e vendeu ${vendas:,.2f}.')

        # Envio do SMS
        message = client.messages.create(
            # LEMBRE-SE DE ALTERAR O NÚMERO DO DESTINATÁRIO
            to="+15558675309",
            # LEMBRE-SE DE ALTERAR O NÚMERO DE PRIGEM DISPONÍVEL NA PLATAFORMA DO TWILIO
            from_="+15017250604",
            body=f'No mês de {mes} o vendedor {vendedor} bateu a meta de 55k e vendeu ${vendas:,.2f}.')
        print(message.sid)

