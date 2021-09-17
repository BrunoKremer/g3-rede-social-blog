# g3-rede-social-blog



**Título**

    - Infocode - Rede Social e Blog

**Status**

    - Status do projeto: O projeto se encontra em desenvolvimento 80% concluído.  :warning:

**Tabela de conteúdo**

    1-Site blog pagina inicial.
    2-Ultimos artigos postados.
    3-Aba comunidade direcionando o usuario para a pagina de cadastro/login da rede social.
    4-Informações de contato.
    5-Filtro por categoria dos artigos.
    6-Barra de pesquisa, para localizar artigos pelos nome do autor e/ou assunto.


**Descrição**

    - Esse projeto tem como objetivo a criação de um blog e de uma mini rede social.
    - Esse projeto visa tanto pessoas experientes na área da tecnologia  mas também toda e qualquer pessoa que visa começar a aprender ou aprimorar os seus conhecimentos na área.
    - O blog contara com artigos voltados as mais variadas  linguagens de programação, frameworks,
    linguagens de marcação, etc...
    - A mini rede social sera um espaço para programadores de variados niveis e linguagens para compartilhar e atualizar seus conhecimentos e habilidades e expandir seu "Networking".

**Layout ou Deploy da aplicação**

    1. Blog / Página inicial / Menu
    2. Menu / Home / Sobre / 
    3. Barra de pesquisa
    4. Rede social com redirecionamento
    5. Python / HTML / CSS / JavaScript / Django / Java / Geral / Indicações
    6. Tópicos
    7. Páginas
    8. Integrantes do Projeto
    9. Redirecionamento para Rede Social



**Pré requisitos**

  • Instalado Python
  • Instalado Django
  • Instalado Git
  • Instalado algum editor de cód. 

    Sistema operacional
    
  • Windows 7, 8, 10
    

**Dependências e Libs instaladas**

1. asgiref==3.4.1
2. Django==3.2.6
3. django-ckeditor==6.1.0
4. django-filter==2.4.0
5. django-js-asset==1.2.2
6. djangorestframework==3.12.4
7. Pillow==8.3.1
8. pytz==2021.1
9. sqlparse==0.4.1

**Como rodar a aplicação**

#    1. Acesse a pasta do arquivo
#    2. Execute python manage.py runserver no cmd
#    3. Acesse localhost:8000

# **Como rodar os testes**

#      1. Instalar o github
#      2. Baixar o repositório https://github.com/BrunoKremer/g3-rede-social-blog
#      3. Vá para o diretório blog no cmd
#      3.1 Abra a pasta Scripts e digite activate
#      3.2 Volte para o diretório anterior
#      4. Baixar todas dependências e bibliotecas descritas anteriormente
#      5. Abra o Chrome e o endereço http://localhost:8000/
    
# **Database**

#      1. Neste projeto está sendo utilizado o banco de dados SQlite
#      2. Ele estará sendo alimentado tanto por uma API quanto pelo django admin
#      3. Já tem algumas tabelas do Blog criadas nele e conforme os dias, vamos inserindo mais elementos.

# Databases
#      Tabela: Posts 
#      Campos : categoria, titulo, conteudo, criado_por, criado_em, foto

#      Tabela : Categoria
#      Campos: categoria

#      Tabela : Indicacao
#      Campos : indicacao, titulo, categoria, autor, criado_em, sinopse


# **Solução de problemas**

#      1. Resolução de possíveis problemas, caso venham a acontecer.

# **Contribuintes**

#      Autores:

#      1. Antonio Bruno -Líder de equipe de desenvolvimento - (brunokremer022@gmail.com)
#      2. Evanildo - Desenvolvimento de banco de dados
#      3. Jean França - Conteúdo dos aplicativos
#      4. Luan Gabriel - Documentação e Conteúdo
    

# **Tarefas em aberto**

#      1. Terminar este arquivo README

#      2. Criar arquivo models blog
#           [x] - Models de postagem
#           [x] - Models de categoria
#           [x] - Models de cursos e livros

#      3. Criar views
#           [x] - Views que retorna todos itens
#           [x] - Outras views, como filtros, etc.

#      4. Layout
#           [x] - Desenvolver tela principal do blog
#           [x] - Desenvolver demais telas
#           [ ] - Colocar esse layout em código

# **Licença**

# Todo o desenvolvimento descrito aqui em suas partes esta sendo liberado em A Lincença Pública em Geral GNU. Você pode copiar, por partes ou por inteiro a sua vontade. Se você for utilizar mais de 20% do código aqui, por favor, me avise, e registre em seus documentos. Obrigado.



