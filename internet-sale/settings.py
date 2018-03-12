class BaseConfig(object):
    SECRET_KEY = 'Random string'
    PONY = {
        'provider': 'sqlite',
        'dbname': 'estore.sqlite'
    }
    WTF_CSRF_SECRET_KEY = 'Secret key'
    
