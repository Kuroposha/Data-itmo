# #Искючения
# import sqlite3
#
# try:
#     n = int(input())#ValueError
#     Import pickle
# except (ValueError, ImportError) as e:
#     print(e)
# # except ImportError as e:
# #     print(e)
# except:
#     print('Error!')
import sqlite3

try:
    conn = sqlite3.connect(':memory:')
    cursor = conn.execute('select * from tbl')
    prine(cursor.fetchall)
except sqlite3.DatabaseError:
    print(e)

finally:
    print('Закрываем соединение')
    conn.close()
