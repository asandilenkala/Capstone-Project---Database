import sqlite3

# Connect to the database
conn = sqlite3.connect('ebookstore.db')
cursor = conn.cursor()

# Create the book table
cursor.execute('''CREATE TABLE IF NOT EXISTS book (
                    id INTEGER PRIMARY KEY,
                    title TEXT,
                    author TEXT,
                    qty INTEGER)''')

# Insert the given values
books = [
    (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
    (3002, "Harry Potter and the Philosopher's Stone", 'J.K. Rowling', 40),
    (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
    (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37),
    (3005, 'Alice in Wonderland', 'Lewis Carroll', 12),
    (3006, 'The Lord Black', 'Asandile Nkala', 24)
]

cursor.executemany('INSERT OR IGNORE INTO book VALUES (?, ?, ?, ?)', books)

# Commit the transaction
conn.commit()
conn.close()
