# Saga Acreana

Desenvolvi esse projeto com a intensão de automatizar e facilitar diversas tarefas para um projeto pessoal: [Links do projeto](https://t.co/KjHPFc0acD).

## Automações e facilidade trazidas pelo projeto

* Criação automática de imagens para posts;
* Edição automática de vídeos;
* Textos automáticos para posts;
* Atualização automática de planilhas do Excel;
* Registro facilitado de planilhas do Excel;
* Edição facilitada de imagens.

## Tecnologias usadas

* O programa foi escrito 100% em Python usando das seguintes bibliotecas:
* tkinter (biblioteca padrão do Python, usada para a interface gráfica);
* os, shutil (bibliotecas padrões do Python, usadas para leitura e manipulação de arquivos e pastas);
* openpyxl (biblioteca externa, usada para leitura e manipulação de planilhas de Excel);
* moviepy (biblioteca externa, usada para edição de videos);
* psd_tools (biblioteca externa, usada para manipular arquivo .psd, originários do Photoshop);
* PIL/Pillow (biblioteca externa, usada para editar imagens automaticamente).

## Usando o App

* Antes de usar o App, é necessário ter o Python 3 e todas as bibliotecas externas citadas na máquina;
* Para registrar os dados na planilha e gerar imagens/textos automaticamente, é preciso registrar manualmente os resultados da temporada na planilha "Era Fm.xlsx (Retrospecto times)";
* Para editar os vídeos automaticamente, é preciso colocá-los na pasta "video" e dar-lhe um nome no seguinte formato: "time-a x time-b - Título - Subtítulo - parte (pt0 para vídeo único, pt1 para primeira parte e pt2 para segunda parte)";
* Para abrir o programa, execute o arquivo main.py, ele abrirá uma interface por abas com todas as funções do programa.

## To do

Ainda há o que desenvolver nesse projeto, segue algumas das coisas que possivelmente serão adicionadas logo:

* Refatorar os códigos e documentá-los;
* Adicionar mais templates de imagens:
  * Templates para copas;
  * Templates para ligas.
* Melhorar funções da interface;
* Criar organizador automático de posts;
* Criar agendador automático de posts;
* Criar automação para postagem de vídeos;
* Adicionar mais escudos de times.
