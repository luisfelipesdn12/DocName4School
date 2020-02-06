from datetime import date #biblioteca para receber a informação de datas

def tipoDeArquivo():
  tipos_de_arquivo = ['TRA', 'AVA', 'MAT']

def disciplina():
  disciplinas = []

def dataAtual():
  #pega o dia atual, se tiver apenas um número: coloca um '0' na frente
  dia = str(date.today().day)
  if len(dia) == 2:
    dia = dia
  else: dia = f'0{dia}'

  #pega o mês atual, se tiver apenas um número: coloca um '0' na frente
  mes = str(date.today().month)
  if len(mes) == 2:
    mes = mes
  else: mes = f'0{mes}'

  data_atual = f'{dia}.{mes}.{date.today().year}'
  return(data_atual)

