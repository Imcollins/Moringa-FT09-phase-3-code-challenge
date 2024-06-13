from .connection import get_db_connection

def create_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS magazines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            author_id INTEGER,
            magazine_id INTEGER,
            FOREIGN KEY (author_id) REFERENCES authors (id),
            FOREIGN KEY (magazine_id) REFERENCES magazines (id)
        )
    ''')

    conn.commit()
    conn.close()

def insert_sample_data():
    conn = get_db_connection()
    cursor = conn.cursor()

    
    cursor.execute("INSERT INTO authors (name) VALUES ('John Doe')")
    cursor.execute("INSERT INTO authors (name) VALUES ('John gates')")
    
    
    cursor.execute("INSERT INTO magazines (name, category) VALUES ('Tech Daily', 'Technology')")
    cursor.execute("INSERT INTO magazines (name, category) VALUES ('Fashion ', 'Fashion')")

    conn.commit()
    conn.close()


if __name__ == "_main_":
    create_tables()
    insert_sample_data()