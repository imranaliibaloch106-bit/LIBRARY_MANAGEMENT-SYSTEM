import sqlite3

def connect():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    author TEXT NOT NULL,
                    year INTEGER,
                    status TEXT DEFAULT 'Available'
                )''')
    conn.commit()
    conn.close()

def insert(title, author, year):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title="", author="", year=""):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR year LIKE ?", 
                ('%'+title+'%', '%'+author+'%', '%'+str(year)+'%'))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(book_id):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()

def update(book_id, title, author, year, status):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, status=? WHERE id=?",
                (title, author, year, status, book_id))
    conn.commit()
    conn.close()

def borrow_book(book_id):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET status='Borrowed' WHERE id=? AND status='Available'", (book_id,))
    conn.commit()
    conn.close()

def return_book(book_id):
    conn = sqlite3.connect("library.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET status='Available' WHERE id=? AND status='Borrowed'", (book_id,))
    conn.commit()
    conn.close()
