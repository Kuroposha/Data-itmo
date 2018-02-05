import os.path as Path
import sqlite3

def connect(db_name=None):
    """Устанавливает соединение с БД """
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    # здесь бюудет магия

    return conn


def initialize(conn, creation_script=None):
    """Инициализирует структуру БД """
    if creation_script is None:
        creation_script = Path.join(Path.dirname(__file__),\
                          'resourses', 'schema.sql')# позволяет склеивать пути
                          #с разделителем тек сисит
        # возвращает род. кат из файла
    with conn, open(creation_script) as f:
        #если ресурс не создан в КМ, то КМ не закрывает этот ресурс
        conn.executescript(f.read())
