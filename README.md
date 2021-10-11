# InfoCode

### Equipe G3 Turma Entra 21/2021:
>>#### Integrantes: 
>>###### Jean Santos França
>>###### Antônio Bruno Kremer Lamim
>>###### Evanildo Batista 
>>###### Luan Gabriel Fausto Pereira 


## STATUS DO PROJETO: em desenvolvimento

### Conteúdo deste documento:

- Descrição
- Layout 
- Deploy
- Pré-Requisitos
- Dependencias e Libs Instaladas
- Como rodar a aplicação teste na WEB
- Como rodar a aplicação em seu PC
- Databases 
- Solução de Problemas
- Contribuites
- Tarefas em Aberto (TODO)
- Licenças 


## Descrição

Blog com artigos sobre programação e tecnologia em geral, integrado a uma Rede Social, que tem o intuito de atingir a comunidade tecnológica, incentivando a propagação de conteúdo, compartilhamento de experiências e expansão de Networking. Nosso site foi desenvolvido em Python, Django, Html, Css e MySQL e as principais bibliotecas que utilizamos foram bootstrap, djangorestframework, django-crispy-forms e django-localflavor que nos permitem fazer o seguinte: Djangorestframework nos permite fazer a construção da nossa API, com bootstrap podemos fazer a configuração geral da parte de front end possibilitando preparar o layout para se adequar a vários tamanhos de tela, com Djangolocalflavor podemos fazer as configurações gerais do nosso site e com Djangocrispyforms fazemos a construção melhorada dos nossos forms.

## Layout 

> Home  
>>      Artigos  
>>      Sobre
>>      Barra de pesquisa
>>      Categorias

> Indicações
>>       Slides
>>       Livros e Cursos

> Post Detail
>>       Post
>>       Comentários

> Rede social
>>       Feed
>>       Perfil de Usuário
>>       Editar Perfil

>#### Admin
>
>>>######     AUTENTICAÇÃO E AUTORIZAÇÃO
>>>     Grupos
>>>     Usuários
>
>>######      COMENTARIOS
>>>     Comentários
>
>>######      MAIN
>>>     Categorias
>>>     Comentários
>>>     Curtidas
>>>     Indicações
>>>     Posts
>
>>######      SOCIAL
>>>     Likes
>>>     Publicações

## Deploy da aplicação

- aplicativo disponivel em Heroku.com 



## Pré-requisitos
- Python 3.8
- IDE para edição dos codigos 
- Django 
- Mysql Server 

## Dependências e Libs Instaladas
#### Veja mais detalhes em <a href="https://github.com/BrunoKremer/g3-rede-social-blog/network/dependencies"> Dependencias ByGitHub.com</a>

- asgiref==3.4.1
- certifi==2021.5.30
- cffi==1.14.6
- charset-normalizer==2.0.4
- cryptography==3.4.8
- defusedxml==0.7.1
- Django==3.2.6
- django-ckeditor==6.1.0
- django-crispy-forms==1.12.0
- django-filter==2.4.0
- django-js-asset==1.2.2
- django-localflavor==3.1
- django-widget-tweaks==1.4.8
- djangorestframework==3.12.4
- idna==3.2
- oauthlib==3.1.1
- Pillow==8.3.1
- pycparser==2.20
- PyJWT==2.1.0
- PyMySQL==1.0.2
- python-social-auth==0.3.6
- python-stdnum==1.16
- python3-openid==3.2.0
- pytz==2021.1
- requests==2.26.0
- requests-oauthlib==1.3.0
- social-auth-app-django==5.0.0
- social-auth-core==4.1.0
- sqlparse==0.4.1
- urllib3==1.26.6

## Como rodar a aplicação na WEB 

- http://projeto-teste-212.heroku.com   

- Blog
  - Você pode navegar entre todos os artigos e indicações
  - Pode interagir fazendo comentários
- Rede social
  - Faça seu cadastro
  - Logo após você pode incluir novas informações pessoais
  - Siga outras pessoas
  - Interaja e faça publicações

## Como rodar os testes e desenvolvimento da app

- Faça download do repositorio no https://github.com/BrunoKremer/g3-rede-social-blog
- Instale os Pré-requisitos
- Crie um VENV para utilizar
- Inclua as bibliotecas listadas acima com o comando pip install -r requirements.txt
- Coloque o Django-server para rodar com o comando python manage.py runserver 
- Acesse localhost:8000
- Para mais informações acesse http://djangoproject.com 

## Database

- Na versão inicial utilizamos o gerenciador de banco de ddos SqLite.
- Na versão de apresentação utilizamos o GDB Mysql Server na Gogole Cloud fornecido pelo nosso instrutor do projeto. 
- Endereços de conexão: Server.IP db01solapp.sol.app.br DatabaseName: E21G3
- 
## Solução de problemas

## Contribuintes

####    Adriano Machado - Instrutor Python Entra21
        Orientação pedagogica e treinamento em Python, Django, Databases, programação BackEnd e FrontEnd. 
        
        adriano@machado.tec.br +55 (67) 9 9263-6781

####    Antônio Bruno Kremer Lamim - Líder
        Desenvolvimento Front-end e Back-end
        brunokremer022@gmail.com | +55 (47) 9 9903-3958

####    Evanildo Batista - DBA
        Desenvolvimento de Banco de Dados
        niko.batista@hotmail.com | +55 (47) 9 9925-2598

####    Jean Carlos P. de F. dos Santos - Conteúdo
        Desenvolvimento Back-end e testes.
        Jeancarlossantos12@gmail.com | +55 (47) 9 9214-5877

####    Luan Gabriel - Conteúdo
        Auxilio na pesquisa e inclusão de conteúdos
        luangabrielfaustonobrac@gmail.com | +55 (47) 9 9154-3131

#### Tarefas em aberto

- [ ] Diagrama de Banco de Dados.
- [ ] Formulário de comentários
- [ ] Model para seguir pessoas
- [ ] Responsividade
- [ ] Troca de mensagens

## Licença

Permissions of this strong copyleft license are conditioned on making available complete source code of licensed works and modifications, which include larger works using a licensed work, under the same license. Copyright and license notices must be preserved. Contributors provide an express grant of patent rights.

Veja mais em: https://github.com/BrunoKremer/g3-rede-social-blog/blob/main/LICENSE