from sqlite3 import connect
from csv import writer
import pandas as pd
import openpyxl


def create_csv():
    con = connect('../sup.sql')
    outfile = open('csv_files/mydump.csv', 'w')
    outcsv = writer(outfile)

    cursor = con.execute('SELECT user.name AS Nome, user.agency AS Ag, register.contact AS Contato, '
                         'register.channel AS Canal, register.attendance AS Atendimento, '
                         'register.associate AS Associado, register.demand AS Demanda, '
                         'register.product_offer AS Oferta_produto, register.product AS Produto, '
                         'register.effective AS Efetivou, register.time_spent AS Tempo_médio_gasto, '
                         'register.time_hour AS Horário_atendimento FROM register '
                         'JOIN user ON register.manager_id=user.id')

    outcsv.writerow(x[0] for x in cursor.description)

    outcsv.writerows(cursor.fetchall())

    outfile.close()


# create_csv()
df_dump = pd.read_csv('csv_files/mydump.csv', sep=',', encoding='windows-1252')
df_contact = pd.DataFrame(
    {'Contato': ['Receptivo', 'Ativo', 'Total'],
     'Nº': [df_dump['Contato'].loc[df_dump['Contato'] == 'Receptivo'].count(),
            df_dump['Contato'].loc[df_dump['Contato'] == 'Ativo'].count(),
            df_dump['Contato'].count()]})
df_channel = pd.DataFrame(
    {'Canal': ['Presencial', 'Telefone', 'E-mail', 'Whatsapp', 'Total'],
     'Nº': [df_dump['Canal'].loc[df_dump['Canal'] == 'Presencial'].count(),
            df_dump['Canal'].loc[df_dump['Canal'] == 'Telefone'].count(),
            df_dump['Canal'].loc[df_dump['Canal'] == 'E-mail'].count(),
            df_dump['Canal'].loc[df_dump['Canal'] == 'Whatsapp'].count(),
            df_dump['Canal'].count()]})
df_attendance = pd.DataFrame(
    {'Atendimento': ['Serviços', 'Negócios', 'Direcionamento', 'Total'],
     'Nº': [df_dump['Atendimento'].loc[df_dump['Atendimento'] == 'Serviço'].count(),
            df_dump['Atendimento'].loc[df_dump['Atendimento'] == 'Negócio'].count(),
            df_dump['Atendimento'].loc[df_dump['Atendimento'] == 'Direcionamento'].count(),
            df_dump['Atendimento'].count()]})
df_associate = pd.DataFrame(
    {'Associado': ['Minha Carteira', 'Outras Carteiras', 'Outras Agências', 'Outras Cooperativas', 'Poupador',
                   'Não associado', 'Total'],
     'Nº': [df_dump['Associado'].loc[df_dump['Associado'] == 'Minha carteira'].count(),
            df_dump['Associado'].loc[df_dump['Associado'] == 'Outras carteiras'].count(),
            df_dump['Associado'].loc[df_dump['Associado'] == 'Outras agências'].count(),
            df_dump['Associado'].loc[df_dump['Associado'] == 'Outras cooperativas'].count(),
            df_dump['Associado'].loc[df_dump['Associado'] == 'Poupador'].count(),
            df_dump['Associado'].loc[df_dump['Associado'] == 'Não associado'].count(),
            df_dump['Associado'].count()]})
df_effective = pd.DataFrame(
    {'Efetivou?': ['Sim', 'Não', 'Total'],
     'Nº': [df_dump['Efetivou'].loc[df_dump['Efetivou'] == 'Sim'].count(),
            df_dump['Efetivou'].loc[df_dump['Efetivou'] == 'Não'].count(),
            df_dump['Efetivou'].count()]})
df_time_spent = pd.DataFrame(
    {'Tempo médio gasto': ['Até 5 minutos', 'Até 15 minutos', 'Acima de 15 minutos', 'Total'],
     'Nº': [df_dump['Tempo_médio_gasto'].loc[df_dump['Tempo_médio_gasto'] == 'Até 5 minutos'].count(),
            df_dump['Tempo_médio_gasto'].loc[df_dump['Tempo_médio_gasto'] == 'Até 15 minutos'].count(),
            df_dump['Tempo_médio_gasto'].loc[df_dump['Tempo_médio_gasto'] == 'Acima de 15 minutos'].count(),
            df_dump['Tempo_médio_gasto'].count()]})
df_time_hour = pd.DataFrame(
    {'Horário atendimento': ['08:00-10:00', '10:00-12:00', '12:00-15:00', '15:00-17:00',
                             'Total'],
     'Nº': [df_dump['Horário_atendimento'].loc[df_dump['Horário_atendimento'] == '08:00-10:00'].count(),
            df_dump['Horário_atendimento'].loc[df_dump['Horário_atendimento'] == '10:00-12:00'].count(),
            df_dump['Horário_atendimento'].loc[df_dump['Horário_atendimento'] == '12:00-15:00'].count(),
            df_dump['Horário_atendimento'].loc[df_dump['Horário_atendimento'] == '15:00-17:00'].count(),
            df_dump['Horário_atendimento'].count()]})

products = ['Cartões', 'Canais digitais', 'Seguros', 'Previdência', 'Investimentos', 'Poupança programada',
            'Capital programado', 'Crédito geral', 'Débito automático', 'Cobrança', 'Consórcios']
df_product = pd.DataFrame(
    {'Produtos': [
        'Cartões', 'Canais digitais', 'Seguros', 'Previdência', 'Investimentos', 'Poupança programada',
        'Capital programado', 'Crédito geral', 'Débito automático', 'Cobrança', 'Consórcios', 'Outros',
        'Total'],
        'Nº': [df_dump['Produto'].loc[df_dump['Produto'] == 'Cartões'].count(),
               df_dump['Produto'].loc[df_dump['Produto'] == 'Canais digitais'].count(),
               df_dump['Produto'].loc[df_dump['Produto'] == 'Seguros'].count(),
               df_dump['Produto'].loc[df_dump['Produto'] == 'Previdência'].count(),
               df_dump['Produto'].loc[df_dump['Produto'] == 'Investimentos'].count(),
               df_dump['Produto'].loc[df_dump['Produto'] == 'Poupança programada'].count(),
               df_dump['Produto'].loc[df_dump['Produto'] == 'Capital programado'].count(),
               df_dump['Produto'].loc[df_dump['Produto'] == 'Crédito geral'].count(),
               df_dump['Produto'].loc[df_dump['Produto'] == 'Débito automático'].count(),
               df_dump['Produto'].loc[df_dump['Produto'] == 'Cobrança'].count(),
               df_dump['Produto'].loc[df_dump['Produto'] == 'Consórcios'].count(),
               df_dump['Produto'].loc[~df_dump['Produto'].isin(products)].count(),
               df_dump['Produto'].count()]})

demands = ['Conta corrente/Poupador', 'Cartões', 'Canais digitais', 'Seguros e previdência', 'Consórcio',
           'Cobrança', 'Crédito geral', 'Recuperação de crédito', 'Descontos de recebíveis']
df_demands = pd.DataFrame(
    {'Demanda': ['Conta corrente/Poupador', 'Cartões', 'Canais digitais', 'Seguros e previdência',
                 'Consórcio', 'Cobrança', 'Crédito geral', 'Recuperação de crédito', 'Descontos de recebíveis',
                 'Outros', 'Total'],
     'Nº': [df_dump['Demanda'].loc[df_dump['Demanda'] == 'Conta corrente/Poupador'].count(),
            df_dump['Demanda'].loc[df_dump['Demanda'] == 'Cartões'].count(),
            df_dump['Demanda'].loc[df_dump['Demanda'] == 'Canais digitais'].count(),
            df_dump['Demanda'].loc[df_dump['Demanda'] == 'Seguros e previdência'].count(),
            df_dump['Demanda'].loc[df_dump['Demanda'] == 'Consórcio'].count(),
            df_dump['Demanda'].loc[df_dump['Demanda'] == 'Cobrança'].count(),
            df_dump['Demanda'].loc[df_dump['Demanda'] == 'Crédito geral'].count(),
            df_dump['Demanda'].loc[df_dump['Demanda'] == 'Recuperação de crédito'].count(),
            df_dump['Demanda'].loc[df_dump['Demanda'] == 'Descontos de recebíveis'].count(),
            df_dump['Demanda'].loc[~df_dump['Demanda'].isin(demands)].count(),
            df_dump['Demanda'].count()]})

df_nome = pd.DataFrame({'Nome': ['Total']})
df_total = pd.concat([df_contact, df_channel, df_attendance, df_associate, df_demands, df_product, df_effective,
                          df_time_hour, df_time_spent, df_nome], axis=1).convert_dtypes()

df_managers = df_dump['Nome'].unique()
dfs = []
for name in df_managers:
    df_person = df_dump.loc[df_dump['Nome'] == name]

    df_contact = pd.DataFrame(
        {'Contato': ['Receptivo', 'Ativo', 'Total'],
         'Nº': [df_person['Contato'].loc[df_person['Contato'] == 'Receptivo'].count(),
                df_person['Contato'].loc[df_person['Contato'] == 'Ativo'].count(),
                df_person['Contato'].count()]})
    df_channel = pd.DataFrame(
        {'Canal': ['Presencial', 'Telefone', 'E-mail', 'Whatsapp', 'Total'],
         'Nº': [df_person['Canal'].loc[df_person['Canal'] == 'Presencial'].count(),
                df_person['Canal'].loc[df_person['Canal'] == 'Telefone'].count(),
                df_person['Canal'].loc[df_person['Canal'] == 'E-mail'].count(),
                df_person['Canal'].loc[df_person['Canal'] == 'Whatsapp'].count(),
                df_person['Canal'].count()]})
    df_attendance = pd.DataFrame(
        {'Atendimento': ['Serviços', 'Negócios', 'Direcionamento', 'Total'],
         'Nº': [df_person['Atendimento'].loc[df_person['Atendimento'] == 'Serviço'].count(),
                df_person['Atendimento'].loc[df_person['Atendimento'] == 'Negócio'].count(),
                df_person['Atendimento'].loc[df_person['Atendimento'] == 'Direcionamento'].count(),
                df_person['Atendimento'].count()]})
    df_associate = pd.DataFrame(
        {'Associado': ['Minha Carteira', 'Outras Carteiras', 'Outras Agências', 'Outras Cooperativas', 'Poupador',
                       'Não associado', 'Total'],
         'Nº': [df_person['Associado'].loc[df_person['Associado'] == 'Minha carteira'].count(),
                df_person['Associado'].loc[df_person['Associado'] == 'Outras carteiras'].count(),
                df_person['Associado'].loc[df_person['Associado'] == 'Outras agências'].count(),
                df_person['Associado'].loc[df_person['Associado'] == 'Outras cooperativas'].count(),
                df_person['Associado'].loc[df_person['Associado'] == 'Poupador'].count(),
                df_person['Associado'].loc[df_person['Associado'] == 'Não associado'].count(),
                df_person['Associado'].count()]})
    df_effective = pd.DataFrame(
        {'Efetivou?': ['Sim', 'Não', 'Total'],
         'Nº': [df_person['Efetivou'].loc[df_person['Efetivou'] == 'Sim'].count(),
                df_person['Efetivou'].loc[df_person['Efetivou'] == 'Não'].count(),
                df_person['Efetivou'].count()]})
    df_time_spent = pd.DataFrame(
        {'Tempo médio gasto': ['Até 5 minutos', 'Até 15 minutos', 'Acima de 15 minutos', 'Total'],
         'Nº': [df_person['Tempo_médio_gasto'].loc[df_person['Tempo_médio_gasto'] == 'Até 5 minutos'].count(),
                df_person['Tempo_médio_gasto'].loc[df_person['Tempo_médio_gasto'] == 'Até 15 minutos'].count(),
                df_person['Tempo_médio_gasto'].loc[df_person['Tempo_médio_gasto'] == 'Acima de 15 minutos'].count(),
                df_person['Tempo_médio_gasto'].count()]})
    df_time_hour = pd.DataFrame(
        {'Horário atendimento': ['08:00-10:00', '10:00-12:00', '12:00-15:00', '15:00-17:00',
                                 'Total'],
         'Nº': [df_person['Horário_atendimento'].loc[df_person['Horário_atendimento'] == '08:00-10:00'].count(),
                df_person['Horário_atendimento'].loc[df_person['Horário_atendimento'] == '10:00-12:00'].count(),
                df_person['Horário_atendimento'].loc[df_person['Horário_atendimento'] == '12:00-15:00'].count(),
                df_person['Horário_atendimento'].loc[df_person['Horário_atendimento'] == '15:00-17:00'].count(),
                df_person['Horário_atendimento'].count()]})

    products = ['Cartões', 'Canais digitais', 'Seguros', 'Previdência', 'Investimentos', 'Poupança programada',
                'Capital programado', 'Crédito geral', 'Débito automático', 'Cobrança', 'Consórcios']
    df_product = pd.DataFrame(
        {'Produtos': [
            'Cartões', 'Canais digitais', 'Seguros', 'Previdência', 'Investimentos', 'Poupança programada',
            'Capital programado', 'Crédito geral', 'Débito automático', 'Cobrança', 'Consórcios', 'Outros',
            'Total'],
            'Nº': [df_person['Produto'].loc[df_person['Produto'] == 'Cartões'].count(),
                   df_person['Produto'].loc[df_person['Produto'] == 'Canais digitais'].count(),
                   df_person['Produto'].loc[df_person['Produto'] == 'Seguros'].count(),
                   df_person['Produto'].loc[df_person['Produto'] == 'Previdência'].count(),
                   df_person['Produto'].loc[df_person['Produto'] == 'Investimentos'].count(),
                   df_person['Produto'].loc[df_person['Produto'] == 'Poupança programada'].count(),
                   df_person['Produto'].loc[df_person['Produto'] == 'Capital programado'].count(),
                   df_person['Produto'].loc[df_person['Produto'] == 'Crédito geral'].count(),
                   df_person['Produto'].loc[df_person['Produto'] == 'Débito automático'].count(),
                   df_person['Produto'].loc[df_person['Produto'] == 'Cobrança'].count(),
                   df_person['Produto'].loc[df_person['Produto'] == 'Consórcios'].count(),
                   df_person['Produto'].loc[~df_person['Produto'].isin(products)].count(),
                   df_person['Produto'].count()]})

    demands = ['Conta corrente/Poupador', 'Cartões', 'Canais digitais', 'Seguros e previdência', 'Consórcio',
               'Cobrança', 'Crédito geral', 'Recuperação de crédito', 'Descontos de recebíveis']
    df_demands = pd.DataFrame(
        {'Demanda': ['Conta corrente/Poupador', 'Cartões', 'Canais digitais', 'Seguros e previdência',
                     'Consórcio', 'Cobrança', 'Crédito geral', 'Recuperação de crédito', 'Descontos de recebíveis',
                     'Outros', 'Total'],
         'Nº': [df_person['Demanda'].loc[df_person['Demanda'] == 'Conta corrente/Poupador'].count(),
                df_person['Demanda'].loc[df_person['Demanda'] == 'Cartões'].count(),
                df_person['Demanda'].loc[df_person['Demanda'] == 'Canais digitais'].count(),
                df_person['Demanda'].loc[df_person['Demanda'] == 'Seguros e previdência'].count(),
                df_person['Demanda'].loc[df_person['Demanda'] == 'Consórcio'].count(),
                df_person['Demanda'].loc[df_person['Demanda'] == 'Cobrança'].count(),
                df_person['Demanda'].loc[df_person['Demanda'] == 'Crédito geral'].count(),
                df_person['Demanda'].loc[df_person['Demanda'] == 'Recuperação de crédito'].count(),
                df_person['Demanda'].loc[df_person['Demanda'] == 'Descontos de recebíveis'].count(),
                df_person['Demanda'].loc[~df_person['Demanda'].isin(demands)].count(),
                df_person['Demanda'].count()]})

    df_nome = pd.DataFrame({'Nome': [name]})
    df_registers = pd.concat([df_contact, df_channel, df_attendance, df_associate, df_demands, df_product, df_effective,
                              df_time_hour, df_time_spent, df_nome], axis=1).convert_dtypes()
    dfs.append(df_registers)

with pd.ExcelWriter('c:\\Temp\\test.xlsx') as writer:
    for df in dfs:
        df.to_excel(writer, sheet_name=f'{df["Nome"].loc[~df["Nome"].isna()].item()}', index=False)
    df_total.to_excel(writer, sheet_name='Total', index=False)
