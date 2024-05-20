# Django Learning Repository

Welcome to my Django Learning Repository! This repository contains all the code and projects I create while learning Django, a high-level Python web framework that encourages rapid development and clean, pragmatic design.

## About

This repository is a personal collection of Django projects and exercises that I am working on as I learn the framework. Each project folder contains a README with more detailed information about the specific project, its purpose, and any unique setup instructions.

## Projects

Here is a list of the projects currently included in this repository:

1. **Hello World Project** - A simple introductory project to set up a Django environment and create a basic "Hello World" page.
2. **Blog Application** - A more complex project featuring a fully functional blog with user authentication, CRUD operations, and a rich-text editor.
3. **E-commerce Site** - A mock e-commerce site with product listings, shopping cart functionality, and order processing.

(Continue listing other projects as you add them)

## Setup

To run any of the projects in this repository, follow these general steps:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/your-repo-name.git
    cd your-repo-name
    ```

2. **Install uv** (if you haven't already):
    ```bash
    pip install uv
    ```

3. **Create a virtual environment using uv**:
    ```bash
    uv venv
    source uv-env/bin/activate   # On Windows use `uv-env\Scripts\activate`
    ```

4. **Install Django in the virtual environment**:
    ```bash
    uv pip install django
    ```

5. **Start a new Django project**:
    ```bash
    django-admin startproject <project-name>
    cd <project-name>
    ```

6. **Apply migrations and run the server**:
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

For project-specific setup instructions, refer to the README file inside each project folder.

## Usage

Once the server is running, you can access the web applications via your web browser at `http://127.0.0.1:8000`. Each project may have different routes and functionalities, so be sure to check the individual project README files for more details.

## Resources

Here are some resources that I found helpful while learning Django:

- [Django Official Documentation](https://docs.djangoproject.com/en/stable/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)
- [Mozilla Developer Network (MDN) Django Tutorial](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
- [The Django Book](https://djangobook.com/)
- [Tutorial](https://youtube.com/playlist?list=PLu71SKxNbfoDOf-6vAcKmazT92uLnWAgy&si=CbfpNW07Zf43Gt08).

## Contributing

This is a personal learning project, but if you have suggestions or improvements, feel free to fork the repository and submit a pull request. I am open to feedback and collaboration.

---

Happy coding!
