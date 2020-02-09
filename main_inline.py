from datetime import date, timedelta #bibliotecas para receber a informação de datas

import os 
from sys import argv

script, source = argv

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
    #repete a pergunta caso algum erro de exceção ocorra
    try:
      user_input = int(input())
      if user_input in [1,2,3]:
        return(tipos_de_arquivo_list[user_input-1])
        break
    except: pass

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
    #repete a pergunta caso algum erro de exceção ocorra
    try:
      user_input = int(input())
      if user_input in range(1, 11):
        return(disciplinas[user_input-1])
        break
    except: pass
 
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
  return('01')

# destination file path 
dest = f'{tipoDeArquivo()}_{disciplina()}_{dataEscolhida()}_{quantidade()}{source[source.find("."):]}'


# Now rename the source path 
# to destination path 
# using os.rename() method 
os.rename(source, dest) 
print(f"Nome alterado com sucesso de '{source}' para '{dest}'") 

