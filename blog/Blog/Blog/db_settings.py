SECRET_KEY = 'django-insecure-ydx%#3elkt6p1$amcu9jfzssu%0&&*0o^=g2ws!(fqmf983_^h'

DbSqLITE = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


DbMysql = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',          
        'NAME': 'DbE21G3',                     
        'USER': 'dbe21g3',
        'PASSWORD': '',
        'HOST': 'dbsolapp01.sol.app.br',         
        'OPTIONS':  {
            'ssl': {
                'ca': '/home/adriano/desenv/Proway/G3/ssl/server-ca.pem',
                'cert': '/home/adriano/desenv/Proway/G3/ssl/client-cert.pem',
                'key': '/home/adriano/desenv/Proway/G3/ssl/client-key.pem'
            }
        }
    }
}

#DATABASES = DbSqLITE
#DATABASES = DbMysql