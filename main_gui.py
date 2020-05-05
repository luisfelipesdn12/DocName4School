import os
import easygui as egui #fazer a graphic user interface
from datetime import date, timedelta #bibliotecas para receber a informação de datas

title = 'DocName4School'

def main():
    def retornaArquivos():
        files_path = egui.fileopenbox(msg="Escolha o(s) asquivos para renomear.", title=title, multiple=True)
        files_path_splited = [files_path[c].split('\\') for c in range(len(files_path))]

        folder_of_files = '/'.join(files_path_splited[0][:-1])
        files_name = [files_path_splited[c][-1] for c in range(len(files_path_splited))]
        files_name_without_extension = ['.'.join(files_name[c].split('.')[:-1]) for c in range(len(files_name))]
        files_extension = ['.' + files_name[c].split('.')[-1] for c in range(len(files_name))]

        dict_to_return = {
            'folder_of_files' : folder_of_files,
            'files_name' : files_name,
            'files_name_without_extension' : files_name_without_extension,
            'files_extension' : files_extension 
        }

        return(dict_to_return)

    infos_sobre_arquivos = retornaArquivos()

    def retornaTipoDeArquivo():
        msg ='''Que tipo de documento é esse?

        Matéria - cópias ou anotações no caderno;
        Avaliação - provas, testes, exames, atividades para nota, etc;
        Trabalho - pesquisas, redações, atividades em folha a parte para a nota que não se encaixam no item supracitado.
        '''
        tipos_de_arquivo_dict = {
            "Matéria" : "MAT",
            "Avaliação" : "AVA",
            "Trabalho" : "TRA"
        }
        choice = egui.choicebox(msg, title, tipos_de_arquivo_dict.keys())
        return(tipos_de_arquivo_dict[choice])

    def retornaDisciplina():
        msg = "Qual é a disciplina?"
        tipos_de_disciplina_dict = {
            "Português" : "POR",
            "Matemática" : "MAT",
            "Física" : "FIS",
            "Química" : "QUI",
            "Biologia" : "BIO",
            "Geografia" : "GEO",
            "História" : "HIS",
            "Inglês" : "ING",
            "Projeto de Vida" : "PDV",
            "Tecnologia" : "TEC",
            "Educação Física" : "EDF"
        }
        choice = egui.choicebox(msg, title, tipos_de_disciplina_dict.keys())
        return(tipos_de_disciplina_dict[choice])

    def retornaDataEscolhida():
        def hoje(): #retorna a data atual (hoje)
            data = date.today()
            return(data.strftime('%d.%m.%Y'))
        
        def ontem(): #retorna a data atual menos um dia (ontem)
            data = date.today() - timedelta(days=1)
            return(data.strftime('%d.%m.%Y'))
                    
        def anteontem(): #retorna a data atual menos dois dias (anteontem)
            data = date.today() - timedelta(days=2)
            return(data.strftime('%d.%m.%Y'))

        tipos_de_data_dict = {
            f"Hoje ({hoje()})" : f"{hoje()}",
            f"Ontem ({ontem()})" : f"{ontem()}",
            f"Anteontem ({anteontem()})" : f"{anteontem()}"
        }

        msg = "De que dia é?"

        choice = egui.choicebox(msg, title, tipos_de_data_dict.keys())

        return(tipos_de_data_dict[choice])

    nome_sem_quantidade = f'{retornaTipoDeArquivo()}_{retornaDisciplina()}_{retornaDataEscolhida()}'
    print(nome_sem_quantidade)

    infos_sobre_arquivos['new_files_name_without_extension'] = [nome_sem_quantidade + f'_{c}' for c in range(
        len(infos_sobre_arquivos['files_name_without_extension'])
    )]

    infos_sobre_arquivos['new_files_name'] = [
        (name + extension) for name, extension in zip(
            infos_sobre_arquivos['new_files_name_without_extension'],
            infos_sobre_arquivos['files_extension']
        )
    ]

    to_rename_dict = dict()

    for c in range(len(infos_sobre_arquivos['files_extension'])):
        obsolete_path = (
            infos_sobre_arquivos['folder_of_files'] + '/' + infos_sobre_arquivos['files_name'][c]
        )
        new_path = (
            infos_sobre_arquivos['folder_of_files'] + '/' + infos_sobre_arquivos['new_files_name'][c]
        )

        to_rename_dict[obsolete_path] = new_path

    for k, v in to_rename_dict.items():
        os.rename(k, v)

    def abre_dir():
        path = infos_sobre_arquivos['folder_of_files']
        path = os.path.realpath(path)
        os.startfile(path)

    abrir_dir = egui.ynbox(
        msg="Pronto! Seu(s) arquivo(s) foram renomeado(s) com sucesso!",
        title=title,
        choices=("Abrir diretório", "Obrigado"))

    if abrir_dir: abre_dir()
    else: exit()

user_choice = egui.ynbox(
    msg='DocName4School \nEscolha os arquivos e os renomeie!',
    title=title,
    choices=("Escolher arquivos", "Cancelar")
    )

if user_choice: main()
else: exit()