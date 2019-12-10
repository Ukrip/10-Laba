import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn


def select_messenge(conn):
    sql = 'SELECT * FROM messenger'
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    for row in rows:
        print(row)


def create_messenge(conn, task):
    sql = ''' INSERT INTO messenger (Nick, Messenge, Time)
              VALUES(?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, task)


def update_messenge(conn, data):
    sql = ''' UPDATE messenger
              SET Time = ?
              WHERE Nick = ? AND Messenge = ?'''
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()


def remove_messenge(conn, removed_task):
    sql = ''' DELETE FROM messenger WHERE Nick = ? AND Messenge = ?'''
    cur = conn.cursor()
    cur.execute(sql, removed_task)
    conn.commit()


def main():

    database = r"oleinik.db" 
 
    conn = create_connection(database)

    with conn:
        print("\nВсі нотатки (текст, дата)")
        select_messenge(conn)
        print("\nВставка нового рядка...")
        create_messenge(conn, ('Рома', 'Здарова', '17:00'))
        print("\nВсі нотатки (текст, дата)")
        select_messenge(conn)
        print("\nЗміна рядка...")
        update_messenge(conn, ('18:00', 'Рома', 'Здарова'))
        print("\nВсі нотатки (текст, дата)")
        select_messenge(conn)
        print("\nВидалення рядка")
        remove_messenge(conn, ('Рома', 'Здарова'))
        print("\nВсі нотатки (текст, дата)")
        select_messenge(conn)
        
 
if __name__ == '__main__':
    main()
