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
    5. Categorias de artigo
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
2. attrs==21.2.0
3. backcall==0.2.0
4. bleach==4.0.0
5. certifi==2021.5.30
6. cffi==1.14.6
7. charset-normalizer==2.0.6
8. colorama==0.4.4
9. cryptography==3.4.8
10. debugpy==1.4.1
11. decorator==5.0.9
12. defusedxml==0.7.1
13. Django==3.2.6
14. django-ckeditor==6.1.0
15. django-crispy-forms==1.12.0
16. django-filter==2.4.0
17. django-js-asset==1.2.2
18. django-localflavor==3.1
19. django-widget-tweaks==1.4.8
20. djangorestframework==3.12.4
21. entrypoints==0.3
22. idna==3.2
23. ipython==7.26.0
24. ipython-genutils==0.2.0
25. jedi==0.18.0
26. Jinja2==3.0.1
27. jsonschema==3.2.0
28. jupyter-client==7.0.1
29. jupyter-core==4.7.1
30. jupyterlab-pygments==0.1.2
31. MarkupSafe==2.0.1
32. matplotlib-inline==0.1.2
33. mistune==0.8.4
34. nbclient==0.5.4
35. nbconvert==6.1.0
36. nbformat==5.1.3
37. nest-asyncio==1.5.1
38. oauthlib==3.1.1
39. packaging==21.0
40. pandocfilters==1.4.3
41. parso==0.8.2
42. pickleshare==0.7.5
43. Pillow==8.3.1
44. prometheus-client==0.11.0
45. prompt-toolkit==3.0.20
46. pycparser==2.20
47. Pygments==2.10.0
48. PyJWT==2.1.0
49. pyparsing==2.4.7
50. pyrsistent==0.18.0
51. python-dateutil==2.8.2
52. python-stdnum==1.16
53. python3-openid==3.2.0
54. pytz==2021.1
55. pywin32==301
56. pywinpty==1.1.3
57. pyzmq==22.2.1
58. requests==2.26.0
59. requests-oauthlib==1.3.0
60. Send2Trash==1.8.0
61. six==1.16.0
62. social-auth-app-django==5.0.0
63. social-auth-core==4.1.0
64. sqlparse==0.4.1
65. terminado==0.11.1
66. testpath==0.5.0
67. tornado==6.1
68. traitlets==5.0.5
69. urllib3==1.26.6
70. wcwidth==0.2.5
71. webencodings==0.5.1

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



