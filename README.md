# DocName4School
Um gerador de nome para documentos escaneados, sobretudo para uso acadêmico.

[![Run on repl.it](https://repl.it/badge/github/luisfelipesdn12-email/DocNameSchool)](https://DocNameSchool.luisfelipe27.repl.run)

![Logo](https://i.ibb.co/3WkqHsq/IMG-20200207-233118.jpg)

Eu uso apps de escanear folhas com a câmera do celular para organizar e armazenar minhas avaliações, matérias e trabalhos escolares.
Já tentei diversas formas de nomear os arquivos para organiza-los bem.

[![TecTudo - CamScanner](https://s2.glbimg.com/uEr5hudzWJne-2txXrYWhtuU8eU=/0x0:1920x1080/1000x0/smart/filters:strip_icc()/i.s3.glbimg.com/v1/AUTH_08fbf48bc0524877943fe86e43087e7a/internal_photos/bs/2018/M/9/2J1QJPT96lga05PIInAA/tutorial-pdf-camscanner.jpg)](https://www.techtudo.com.br/dicas-e-tutoriais/2018/09/como-salvar-documentos-em-pdf-com-o-app-camscanner.ghtml)

Cheguei a conclusão de que é uma boa nomear como arquivos de câmera, nomeados automáticamente com o tipo de arquivo, data, etc.

A maneira que encontrei foi a seguinte:

TipoDeDocumento_Disciplina_Data_Quantidade

------
## Tipos de documento:

* Matéria - MAT: cópias ou anotações no caderno;

* Avaliação - AVA: provas, testes, exames, atividades para nota, etc;

* Trabalho - TRA: pesquisas, redações, atividades em folha a parte para a nota que não se encaixam no item supracitado.


|Tipo de documento | Sigla|
|---|---|
|Matéria|MAT|
|Avaliação|AVA|
|Trabalho|TRA|

------
## Disciplinas:

* Português - POR;

* Matemática - MAT;

* Física - FIS;

* Química - QUI;

* Biologia - BIO;

* Geografia - GEO;

* História - HIS;

* Inglês - ING;

* Projeto de Vida - PDV;

* Tecnologia - TEC;

* Educação Física - EDF.


|Disciplina |Sigla|
|--|---|
|Portugues |POR|
|Matemática|MAT|
|Física | FIS|
| Química| QUI|
|Biologia | BIO|
|Geografia| GEO|
|História | HIS|
|Inglês |ING|
|Projeto de Vida |PDV|
| Tecnologia | TEC|
|Educação Física | EDF|

------
## Quantidades: 
Simplesmente para ter controle e evitar duplicidades caso os prefixos fossem iguais.
Coisas como: 01, 02 etc

------
Por exemplo, se eu for nomear um trabalho, de 3 folhas, de química, e no dia 02/02/2002; os três arquivos serão:

* TRA_QUI_02.02.2002_01, 
* TRA_QUI_02.02.2002_02 e 
* TRA_QUI_02.02.2002_03.

---
---

# Tipos de uso:

Há duas maneiras de usar o programa: 

## Simples:
Mais simples porém menos usual, que utiliza `input()`s e `print()`s;

## Inline:
Se roda o programa com argumentos inline, no modelo: `python script.py arquivo_para_renomear.extensão`

![](https://i.ibb.co/Pr5q8Vb/main-inline-demo.gif)
> GIF demonstrativo da segunda maneira.


### Passo a passo:

![frame 1](https://im5.ezgif.com/tmp/ezgif-5-68aa62d843e0-gif-im/frame_0_delay-1.5s.gif)
1. Colocar o `script.py`, e o `arquivo_para_renomear.extensão` no mesmo diretório.
pode ser na Área de Trabalho, ou em uma pasta separada. 
Abrir o CMD e colocá-lo no diretório escolhido com o comando:
```
cd {insira o diretório aqui}
```

![frame 2](https://i.ibb.co/vBH6tYJ/frame-1-delay-2-5s.png)
2. Inserir o comando:
```
python script.py arquivo_para_renomear.extesão
```

![frame 3](https://cdn.discordapp.com/attachments/676419554154643489/676420422853459979/frame_2_delay-1.5s.png)
3. Definir o tipo de documento.

![frame 4](https://cdn.discordapp.com/attachments/676419554154643489/676420422547406889/frame_3_delay-1.5s.png)
4. Definir a disciplina.

![frame 5](https://cdn.discordapp.com/attachments/676419554154643489/676420423696515072/frame_4_delay-1.5s.png)
5. Definir a data.

![frame 6](https://cdn.discordapp.com/attachments/676419554154643489/676420423113637889/frame_5_delay-4s.png)
Pronto!

----
Nas duas o programa perguntará o tipo de arquivo, a disciplina e a data; porém apenas o primeiro jeito possibilita a escolha de quantidade, uma vez que no segundo o sufixo é sempre `_01`, nomeado automáticamente.
