import sqlite3

'''a = 'ABCAAC1C'                      #N=8    (кол-во символов)

def strcounter(a):                  #O(N**2)
    for char in a:
        counter = 0
        for sub_char in a:
            if char == sub_char:
                counter += 1
        print(char, counter)

#strcounter(a)


def strcounter1(a):                  #O(N*M)    M=4(кол-во уникальных символов)
    for char in set(a):
        counter = 0
        for sub_char in a:
            if char == sub_char:
                counter += 1
        print(char, counter)



def strcounter2(a):                 #O(N)
    syms_counter = {}
    for char in a:
        syms_counter[char] = syms_counter.get(char, 0) + 1
    print(syms_counter)

strcounter2(a)

a = 'Minecraft'
print(a)

#ДЗ
a = 'а роза упала на лапу азора'

def palindrom(a):
    word = list(a)                          # Превращаем слово или фразу в список
    word = list(filter(str.strip, word))    # Убираем пробелы в списке
    drow = list(a)                          # Создаём новый список, чтобы его перевернуть
    drow.reverse()                          # Переворачиваем новый список
    drow = list(filter(str.strip, drow))    # Убираем пробелы в новом списке
    if word == drow:                        # Сравниваем списки
        print('True')
    else:
        print('False')

palindrom(a)'''


class User():
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender

def creatre_table_user(cursor):
    command = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT,
        surname TEXT,
        gender TEXT);
    """
    cursor.execute(command)

def add_user(cursor, user):
    command = """
    INSERT INTO users (name, surname, gender) VALUES (?,?,?);
    """
    cursor.execute(command, (user.name, user.surname,user.gender))

def get_users_list(cursor):
    command = """
    SELECT * FROM users
    """
    result = cursor.execute(command)
    users = result.fetchall()
    print(users)

def get_user(cursor, user_id):
    command = """
    SELECT * FROM users WHERE id = ?;
    """
    result = cursor.execute(command,(user_id,))
    users = result.fetchall()
    print(users)

def update_user_name(cursor, value, user_id):
    command = """
    UPDATE users SET name = ? WHERE id = ?;
    """
    cursor.execute(command,(value,user_id,))

def delete_users(cursor):
    command = """
    DELETE FROM users;
    """
    cursor.execute(command)

def delete_users_by_name(cursor, user_name):
    command = """
    DELETE FROM users WHERE name = ?;
    """
    result = cursor.execute(command,(user_name,))
    users = result.fetchall()
    print(users)

if __name__ == '__main__':
    with sqlite3.connect('base.db') as cursor :
        print(cursor)
        creatre_table_user(cursor)
        delete_users(cursor)
        add_user(cursor, User(name='Максим', surname='Иванов', gender='male'))
        add_user(cursor, User(name='Дмитрий', surname='Петров', gender='male'))
        add_user(cursor, User(name='Екатерина', surname='Кузнецова', gender='female'))
        get_users_list(cursor)
        update_user_name(cursor, 'Юля', 3)
        delete_users_by_name(cursor, 'Дмитрий')
        get_user(cursor,3)