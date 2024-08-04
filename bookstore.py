import sqlite3

# Function to connect to the database.
def connect():
    return sqlite3.connect('ebookstore.db')

# Function to add book.
def add_book():
    conn = connect()
    cursor = conn.cursor()
    id = int(input("Enter book id: "))
    title = str(input("Enter book title: "))
    author = str(input("Enter book author: "))
    qty = int(input("Enter quantity: "))
    cursor.execute("INSERT INTO book (id, title, author, qty) VALUES (?, ?, ?, ?)",
                   (id, title, author, qty))
    conn.commit()
    conn.close()
    print("Book added successfully!")

# Function to update book.
def update_book():
    conn = connect()
    cursor = conn.cursor()
    id = input("Enter the id of the book to update: ")
    title = input("Enter the new title: ")
    author = input("Enter the new author: ")
    qty = input("Enter the new quantity: ")
    cursor.execute("UPDATE book SET title = ?, author = ?, qty = ? WHERE id = ?",
                   (title, author, qty, id))
    conn.commit()
    conn.close()
    print("Book updated successfully!")

# Function to delete book.
def delete_book():
    conn = connect()
    cursor = conn.cursor()
    id = input("Enter the id of the book to delete: ")
    cursor.execute("DELETE FROM book WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    print("Book deleted successfully!")

# Function to search book.
def search_books():
    conn = connect()
    cursor = conn.cursor()
    search_term = input("Enter title or author to search: ")
    cursor.execute("SELECT * FROM book WHERE title LIKE ? OR author LIKE ?",
                   ('%' + search_term + '%', '%' + search_term + '%'))
    books = cursor.fetchall()
    conn.close()
    if books:
        for book in books:
            print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[3]}")
    else:
        print("No books found.")

# Main function which will give the user option to choose when manipulating the database.
def main():
    while True:
        print("\nBookstore Clerk Menu:")
        print("1. Enter book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Search books")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            update_book()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            search_books()
        elif choice == '0':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
