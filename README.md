# Library Management System

This is a pet project developed to manage a library system effectively. The project is built with Django and consists of the following apps:

## Project Structure

- **Authentication**: Handles user authentication, registration, and role-based access.
- **Books**: Manages book-related functionality such as creation, listing, and updates.
- **Authors**: Manages author-related information.
- **Orders**: Handles borrowing and return orders for library books.
- **Library (Main App)**: Central app that connects all functionalities.

Each app includes detailed models, templates, and views to provide a seamless library management experience.

---

## Features

- User authentication with role-based access control (librarians and visitors).
- Comprehensive management of books and authors.
- Order tracking for library operations.
- Modular structure for ease of scaling and maintenance.

---

## Installation and Setup

Follow these steps to set up the project on your local machine:

1. **Clone the Repository**  
   ```bash
   git clone <repository-url>
   cd <repository-directory>
2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
3. **Configure the Database**
   - Create a PostgreSQL database.
   - Update the database connection string in settings.py under the DATABASES section.
4. **Apply Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
5. **Run the Development Server**
   ```bash
   python manage.py runserver
6. **Access the Application**
   Open your browser and navigate to http://localhost:8000.

## Technologies used

  - Backend: Django (Python)
  - Database: PostgreSQL
  - Frontend: Django Templates, HTML, CSS
  - Authentication: CustomUser model with role-based access
