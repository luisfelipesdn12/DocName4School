from datetime import date #biblioteca para receber a informação de datas

def tipoDeArquivo():
  tipos_de_arquivo_list = ['MAT', 'AVA', 'TRA']
  while True:
    print('''
  Que tipo de documento é esse?
  [ 1 ] Matéria - cópias ou anotações no caderno;
  [ 2 ] Avaliação - provas, testes, exames, atividades para nota, etc;
  [ 3 ] Trabalho - pesquisas, redações, atividades em folha a parte para a nota que não se encaixam no item supracitado.
    ''')
    user_input = int(input())
    if user_input in [1,2,3]:
      return(tipos_de_arquivo_list[user_input-1])
      break

def disciplina():
  disciplinas = ['POR', 'MAT', 'FIS', 'QUI', 'BIO', 'GEO', 'HIS', 'ING', 'PDV', 'TEC', 'EDF']
  while True:
    print('''
----------------------
Qual é a disciplina?
[ 1 ] Português - POR;
[ 2 ] Matemática - MAT;
[ 3 ] Física - FIS;
[ 4 ] Química - QUI;
[ 5 ] Biologia - BIO;
[ 6 ] Geografia - GEO;
[ 7 ] História - HIS;
[ 8 ] Inglês - ING;
[ 9 ] Projeto de Vida - PDV;
[ 10 ] Tecnologia - TEC;
[ 11 ] Educação Física - EDF.
''')
    user_input = int(input())
    if user_input in range(1, 11):
      return(disciplinas[user_input-1])
      break
 

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

def quantidade():
  print('\n---------------------- \nDigite um valor inteiro que represente a quantidade de arquivos com as mesmas característica supracitadas: \n')
  user_input = int(input())
  return(user_input)

nome_sem_quantidade = f'{tipoDeArquivo()}_{disciplina()}_{dataAtual()}'

for c in range(1, quantidade()+1):
  if c == 1: print('\n----------------------')
  if len(str(c)) >= 2:
    print(f'{nome_sem_quantidade}_{c}')
  else: print(f'{nome_sem_quantidade}_0{c}')