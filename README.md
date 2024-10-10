# Blogs Project

This is a simple blog application built with Django. The project allows users to create, read, update, and delete blog posts. It also includes a structured system for managing blog titles and associating them with corresponding blog posts.

## Project Overview

The **Blogs** project provides a platform where users can write and manage blog posts. Each post is associated with a blog title, making it easy to categorize and organize the content. The application leverages Django’s admin interface for managing posts and titles and uses **Bootstrap** for front-end styling.

### Key Features:
- **Create, Read, Update, and Delete (CRUD)** functionality for blog posts.
- Separation of blog titles and content using a relational database model.
- Django's admin site for managing blog content.
- **Bootstrap** integration for responsive design and a clean user interface.

## Models

- **BlogTitle**: Represents the title of the blog and the date it was added.
- **BlogPost**: Contains the text of the blog post and a foreign key relationship to `BlogTitle` to ensure that each post is associated with a specific title.

## Technologies Used
- **Django**: The web framework used to build this project.
- **Python**: The programming language used for development.
- **SQLite**: The database used for data storage.
- **Bootstrap 5**: Front-end framework for styling.
- **django-bootstrap5**: For integrating Bootstrap with Django forms.

## Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/username/blogs-project.git
2. Navigate to the project directory:
   ```bash
   cd blogs-project
3. Set up a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
5. Apply database migrations:
   ```bash
   python manage.py migrate
6. Run the server:
   ```bash
   python manage.py runserver
7. Access the app in your browser at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).
## Admin Access
- To access the Django admin panel for managing blog posts and titles:
- 1. Create a superuser:
     ```bash
     python manage.py createsuperuser
- 2. Log in at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/).
## Folder Structure
    ```bash
    blogs/
    ├── blogs/               # Project configuration files
    ├── blog/                # Blog app where models, views, and templates are located
    ├── templates/           # HTML templates for the project
    ├── static/              # Static files such as CSS and JS
    ├── manage.py            # Django's command-line utility for administrative tasks
## Screenshots
Home Page.
![Home Page.](https://github.com/user-attachments/assets/0a8e4d9a-1323-44a7-8911-e2bfe20c6113)
User authenticattion Page.
![User Authentication.](https://github.com/user-attachments/assets/c4831509-56c3-41e9-8986-1401c6cb2bff)
Blogs Page.
![Blogs](https://github.com/user-attachments/assets/04aef3b1-d406-42ce-ad4d-ebd978edd8f4)
Blogpost Page.
![Blog Post](https://github.com/user-attachments/assets/4c62217e-30cd-4d94-b331-854f7ee0beeb)



## Future Improvements
- Implement a rich text editor for formatting blog posts.
- Add tags and categories to improve post organization.
- Enable pagination for better handling of large number of posts.
## License
- This project is under the Apache Licence - see the [LICENSE](LICENSE) file for details.
## Contact
- For any questions or suggestions, feel free to reach out to me:
-   **Email:** [wchegesalome@gmail.com](mailto:wchegesalome@gmail.com)
-   **GitHub:** [Njoro90260](https://github.com/Njoro90260)
```bash

Feel free to adjust any specific details, like the repository URL, or add more features as needed. Let me know if you need further customization!
