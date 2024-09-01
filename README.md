Here's a README file for the bookstore clerk program:

# Bookstore Clerk Program

## Description

This program is designed for use by a bookstore clerk to manage an inventory of books.
The program allows the clerk to add new books to the database, update book 
information, delete books from the database, and search the database to find specific books.
The program interacts with a database called `ebookstore` and manages a table named `book` with the following structure:


| ID   | Title                                       | Author                  | Quantity |
|------|---------------------------------------------|-------------------------|----------|
| 3001 | A Tale of Two Cities                        | Charles Dickens         | 30       |
| 3002 | Harry Potter and the Philosopher's Stone    | J.K. Rowling            | 40       |
| 3003 | The Lion, the Witch, and the Wardrobe       | C.S. Lewis              | 25       |
| 3004 | The Lord of the Rings                       | J.R.R. Tolkien          | 37       |
| 3005 | Alice in Wonderland                         | Lewis Carroll           | 12       |

You may also add additional values to the table as needed.

## Features

The program offers the following functionalities:

1. **Enter Book**: Add a new book to the database.
2. **Update Book**: Update the information of an existing book in the database.
3. **Delete Book**: Remove a book from the database.
4. **Search Books**: Search for a specific book in the database.
5. **Exit**: Exit the program.

The program will present the user with a menu to select the desired action, and it will perform the function based on the user's choice.

## Installation and Setup

1. **Database Setup**: 
   - Create a database named `ebookstore`.
   - Create a table named `book` with the following structure:

     ```sql
     CREATE TABLE book (
         id INT PRIMARY KEY,
         title VARCHAR(255),
         author VARCHAR(255),
         qty INT
     );
     ```

   - Populate the table with the following data:

     ```sql
     INSERT INTO book (id, title, author, qty) VALUES
     (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
     (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K. Rowling', 40),
     (3003, 'The Lion, the Witch and the Wardrobe', 'C.S. Lewis', 25),
     (3004, 'The Lord of the Rings', 'J.R.R. Tolkien', 37),
     (3005, 'Alice in Wonderland', 'Lewis Carroll', 12);
     ```

2. **Running the Program**:
   - Ensure that you have Python installed on your system.
   - Install any necessary Python packages.
   - Run the program using the Python interpreter.

3. **Usage**:
   - The program will display a menu with options to add, update, delete, search books, or exit.
   - Enter the corresponding number to perform the desired action.

## Example Usage

- **Adding a Book**: When selecting the "Enter Book" option, the program will prompt you for the book's details (ID, title, author, quantity) and add the book to the database.
- **Updating a Book**: Select the "Update Book" option to modify an existing book's details in the database.
- **Deleting a Book**: Choose "Delete Book" to remove a book from the database.
- **Searching for a Book**: Use the "Search Books" option to find a specific book by entering search criteria.

## License

This project is licensed under the MIT License.

## Contributing

Feel free to fork this repository and submit pull requests if you would like to contribute to the development of this program.


This README file provides an overview of the program, instructions on how to set up and run it, and details about its features.
