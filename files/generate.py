from sqlite3 import connect
from csv import writer
import pandas as pd
import openpyxl


def create_csv(file_name, db_path, ag_id):
    con = connect(db_path)
    outfile = open(file_name, 'w')
    outcsv = writer(outfile)

    cursor = con.execute('SELECT user.name AS Nome, user.agency AS Ag, register.contact AS Contato, '
                         'register.channel AS Canal, register.attendance AS Atendimento, '
                         'register.associate AS Associado, register.demand AS Demanda, '
                         'register.product_offer AS Oferta_produto, register.product AS Produto, '
                         'register.effective AS Efetivou, register.time_spent AS Tempo_medio_gasto, '
                         'register.time_hour AS Horario_atendimento FROM Register '
                         'JOIN user ON register.manager_id=user.id '
                         'WHERE user.agency = ' + ag_id)
    outcsv.writerow(x[0] for x in cursor.description)

    outcsv.writerows(cursor.fetchall())

    outfile.close()


def divide_dataframes(df, name='Total'):
    df_contact = pd.DataFrame(
        {'Contato': ['Receptivo', 'Ativo', 'Total'],
         'Nº': [df['Contato'].loc[df['Contato'] == 'Receptivo'].count(),
                df['Contato'].loc[df['Contato'] == 'Ativo'].count(),
                df['Contato'].count()]})
    df_channel = pd.DataFrame(
        {'Canal': ['Presencial', 'Telefone', 'E-mail', 'Whatsapp', 'Total'],
         'Nº': [df['Canal'].loc[df['Canal'] == 'Presencial'].count(),
                df['Canal'].loc[df['Canal'] == 'Telefone'].count(),
                df['Canal'].loc[df['Canal'] == 'E-mail'].count(),
                df['Canal'].loc[df['Canal'] == 'Whatsapp'].count(),
                df['Canal'].count()]})
    df_attendance = pd.DataFrame(
        {'Atendimento': ['Serviços', 'Negócios', 'Direcionamento', 'Total'],
         'Nº': [df['Atendimento'].loc[df['Atendimento'] == 'Serviço'].count(),
                df['Atendimento'].loc[df['Atendimento'] == 'Negócio'].count(),
                df['Atendimento'].loc[df['Atendimento'] == 'Direcionamento'].count(),
                df['Atendimento'].count()]})
    df_associate = pd.DataFrame(
        {'Associado': ['Minha Carteira', 'Outras Carteiras', 'Outras Agências', 'Outras Cooperativas', 'Poupador',
                       'Não associado', 'Total'],
         'Nº': [df['Associado'].loc[df['Associado'] == 'Minha carteira'].count(),
                df['Associado'].loc[df['Associado'] == 'Outras carteiras'].count(),
                df['Associado'].loc[df['Associado'] == 'Outras agências'].count(),
                df['Associado'].loc[df['Associado'] == 'Outras cooperativas'].count(),
                df['Associado'].loc[df['Associado'] == 'Poupador'].count(),
                df['Associado'].loc[df['Associado'] == 'Não associado'].count(),
                df['Associado'].count()]})
    df_effective = pd.DataFrame(
        {'Efetivou?': ['Sim', 'Não', 'Total'],
         'Nº': [df['Efetivou'].loc[df['Efetivou'] == 'Sim'].count(),
                df['Efetivou'].loc[df['Efetivou'] == 'Não'].count(),
                df['Efetivou'].count()]})
    df_time_spent = pd.DataFrame(
        {'Tempo médio gasto': ['Até 5 minutos', 'Até 15 minutos', 'Acima de 15 minutos', 'Total'],
         'Nº': [df['Tempo_medio_gasto'].loc[df['Tempo_medio_gasto'] == 'Até 5 minutos'].count(),
                df['Tempo_medio_gasto'].loc[df['Tempo_medio_gasto'] == 'Até 15 minutos'].count(),
                df['Tempo_medio_gasto'].loc[df['Tempo_medio_gasto'] == 'Acima de 15 minutos'].count(),
                df['Tempo_medio_gasto'].count()]})
    df_time_hour = pd.DataFrame(
        {'Horário atendimento': ['08:00-10:00', '10:00-12:00', '12:00-15:00', '15:00-17:00',
                                 'Total'],
         'Nº': [df['Horario_atendimento'].loc[df['Horario_atendimento'] == '08:00-10:00'].count(),
                df['Horario_atendimento'].loc[df['Horario_atendimento'] == '10:00-12:00'].count(),
                df['Horario_atendimento'].loc[df['Horario_atendimento'] == '12:00-15:00'].count(),
                df['Horario_atendimento'].loc[df['Horario_atendimento'] == '15:00-17:00'].count(),
                df['Horario_atendimento'].count()]})

    products = ['Cartões', 'Canais digitais', 'Seguros', 'Previdência', 'Investimentos', 'Poupança programada',
                'Capital programado', 'Crédito geral', 'Débito automático', 'Cobrança', 'Consórcios']
    df_product = pd.DataFrame(
        {'Produtos': [
            'Cartões', 'Canais digitais', 'Seguros', 'Previdência', 'Investimentos', 'Poupança programada',
            'Capital programado', 'Crédito geral', 'Débito automático', 'Cobrança', 'Consórcios', 'Outros',
            'Total'],
            'Nº': [df['Produto'].loc[df['Produto'] == 'Cartões'].count(),
                   df['Produto'].loc[df['Produto'] == 'Canais digitais'].count(),
                   df['Produto'].loc[df['Produto'] == 'Seguros'].count(),
                   df['Produto'].loc[df['Produto'] == 'Previdência'].count(),
                   df['Produto'].loc[df['Produto'] == 'Investimentos'].count(),
                   df['Produto'].loc[df['Produto'] == 'Poupança programada'].count(),
                   df['Produto'].loc[df['Produto'] == 'Capital programado'].count(),
                   df['Produto'].loc[df['Produto'] == 'Crédito geral'].count(),
                   df['Produto'].loc[df['Produto'] == 'Débito automático'].count(),
                   df['Produto'].loc[df['Produto'] == 'Cobrança'].count(),
                   df['Produto'].loc[df['Produto'] == 'Consórcios'].count(),
                   df['Produto'].loc[~df['Produto'].isin(products)].count(),
                   df['Produto'].count()]})

    demands = ['Conta corrente/Poupador', 'Cartões', 'Canais digitais', 'Seguros e previdência', 'Consórcio',
               'Cobrança', 'Crédito geral', 'Recuperação de crédito', 'Descontos de recebíveis']
    df_demands = pd.DataFrame(
        {'Demanda': ['Conta corrente/Poupador', 'Cartões', 'Canais digitais', 'Seguros e previdência',
                     'Consórcio', 'Cobrança', 'Crédito geral', 'Recuperação de crédito', 'Descontos de recebíveis',
                     'Outros', 'Total'],
         'Nº': [df['Demanda'].loc[df['Demanda'] == 'Conta corrente/Poupador'].count(),
                df['Demanda'].loc[df['Demanda'] == 'Cartões'].count(),
                df['Demanda'].loc[df['Demanda'] == 'Canais digitais'].count(),
                df['Demanda'].loc[df['Demanda'] == 'Seguros e previdência'].count(),
                df['Demanda'].loc[df['Demanda'] == 'Consórcio'].count(),
                df['Demanda'].loc[df['Demanda'] == 'Cobrança'].count(),
                df['Demanda'].loc[df['Demanda'] == 'Crédito geral'].count(),
                df['Demanda'].loc[df['Demanda'] == 'Recuperação de crédito'].count(),
                df['Demanda'].loc[df['Demanda'] == 'Descontos de recebíveis'].count(),
                df['Demanda'].loc[~df['Demanda'].isin(demands)].count(),
                df['Demanda'].count()]})

    df_nome = pd.DataFrame({'Nome': [name]})
    df_registers = pd.concat([df_contact, df_channel, df_attendance, df_associate, df_demands, df_product, df_effective,
                              df_time_hour, df_time_spent, df_nome], axis=1).convert_dtypes()
    return df_registers
