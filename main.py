from datetime import date, timedelta #bibliotecas para receber a informação de datas

#coleta e retorna a opção de tipo de arquivo do usuário
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

#coleta e retorna a opção de disciplina do usuário:
def disciplina():
  disciplinas = ['POR', 'MAT', 'FIS', 'QUI', 'BIO', 'GEO', 'HIS', 'ING', 'PDV', 'TEC', 'EDF']
  #repete a pergunta até o input ser válido: 
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
 
#retorna a data escolhida pelo usuário entre hoje, onte e anteontem:
def dataEscolhida(): 
	def hoje(): #retorna a data atual (hoje)
		data = date.today()
		return(data.strftime('%d.%m.%Y'))
	
	def ontem(): #retorna a data atual menos um dia (ontem)
		data = date.today() - timedelta(days=1)
		return(data.strftime('%d.%m.%Y'))
				
	def anteontem(): #retorna a data atual menos dois dias (anteontem)
		data = date.today() - timedelta(days=2)
		return(data.strftime('%d.%m.%Y'))

  #repete a pergunta até o input ser válido:
	while True:
		user_input = int(input(f'''
----------------------
De que dia é?
[ 1 ] Hoje ({hoje()});
[ 2 ] Ontem ({ontem()});
[ 3 ] Anteontem ({anteontem()});

'''))
		if user_input in range(1, 4):
			break

	if user_input == 1:
		return(hoje())
	if user_input == 2:
		return(ontem())
	if user_input == 3:
		return(anteontem())

#retorna o número de arquivos com as variáveis anteriores iguais; definido pelo usuário:
def quantidade():
  print('\n---------------------- \nDigite um valor inteiro que represente a quantidade de arquivos com as mesmas característica supracitadas: \n')
  user_input = int(input())
  return(user_input)

#defino o 'nome_sem_quantidade' antes, pois se eu fosse definir no laço for, a pergunta da quantidade viria antes das outras, uma vez que é usada como parâmetro do laço.
nome_sem_quantidade = f'{tipoDeArquivo()}_{disciplina()}_{dataEscolhida()}'

#laço de insere a quantidade no final e imprime na tela:
for c in range(1, quantidade()+1):
  if c == 1: print('\n----------------------')
  if len(str(c)) >= 2:
    print(f'{nome_sem_quantidade}_{c}')
  else: print(f'{nome_sem_quantidade}_0{c}')