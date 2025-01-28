
# Online Bookstore Project

This is a fully-featured online bookstore application built using **Django**, **PostgreSQL**, and **Docker**. The project includes a custom user model, robust authentication, image uploads, permissions, search functionality, and many other features tailored for an e-commerce platform.

## Features

- **Custom User Model**: User registration and authentication with email and password.
- **Social Authentication**: Integration with third-party social platforms (Google, Facebook, etc.) using `django-allauth`.
- **Image Uploading**: Users can upload book cover images.
- **Search Functionality**: Complex search filters for books based on price, genre, author, and more.
- **Reviews and Ratings**: Customers can leave reviews and ratings for books.
- **Permissions**: Fine-grained permissions for users based on their roles (e.g., admin, regular user).
- **Dockerized**: The application is fully containerized using Docker to ensure consistency across environments.
- **PostgreSQL Database**: Uses PostgreSQL as the primary database for storing data.
- **Security**: Implements best practices for securing sensitive user data.

## Project Structure

```
.
├── app/                    # Django application code
│   ├── books/              # Books app
│   ├── users/              # User model and authentication
│   ├── reviews/            # Reviews and ratings
│   └── ...
├── config/                 # Project settings and configuration
│   └── settings.py         # Django settings file
├── docker/                 # Docker configuration files
│   ├── Dockerfile          # Dockerfile to build the image
│   └── docker-compose.yml  # Docker Compose configuration
├── requirements.txt        # Project dependencies
└── manage.py               # Django management script
```

## Prerequisites

- **Docker**: Install Docker and Docker Compose on your machine.
- **Python**: Python 3.8+ (in Docker container, but for local development, Python may be useful for testing).
- **PostgreSQL**: PostgreSQL is used as the database for this project.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Sam-Waithaka/Online-Bookstore.git
cd online-bookstore
```

### 2. Build Docker Containers

Build and start the application using Docker Compose:

```bash
docker-compose up --build
```

This command will:

- Build the Docker images for the Django application.
- Start a PostgreSQL container for the database.
- Create and start all necessary containers.

### 3. Run Migrations

After the containers are up and running, you need to run the migrations to set up your database.

```bash
docker-compose exec web python manage.py migrate
```

### 4. Create a Superuser (Optional)

To access the Django admin panel, you can create a superuser.

```bash
docker-compose exec web python manage.py createsuperuser
```

Follow the prompts to create a superuser with admin rights.

### 5. Access the Application

Once everything is running, you can access the application at:

```
http://localhost:8000
```

The admin panel will be available at:

```
http://localhost:8000/admin
```

## Running Tests

To run the tests for the application, use the following command:

```bash
docker-compose exec web python manage.py test
```

## Project Configuration

### Docker Configuration

The project is containerized with Docker to ensure a consistent development and production environment.

#### Dockerfile

This file is used to build the Django application image. It sets up Python, installs dependencies, and copies the necessary project files.

#### docker-compose.yml

Docker Compose is used to define and run multi-container Docker applications. It includes configurations for:

- **Web**: The Django application.
- **DB**: PostgreSQL database.
- **Redis**: (Optional) For caching or background tasks if needed.

## Environment Variables

You can configure your environment variables in a `.env` file. Make sure to include sensitive information such as `SECRET_KEY`, `DEBUG`, `DATABASE_URL`, and others.

Example `.env` file:

```
SECRET_KEY=your-secret-key
DEBUG=True
DATABASE_URL=postgres://user:password@db:5432/bookstore
```

### Setting Up Environment Variables

To set up the environment variables, create a `.env` file in the root directory and add your configuration values. This will be loaded automatically by Django using libraries like `django-environ`.

## Features Roadmap

- **User Profiles**: Extend the user model to support user profiles.
- **Order Management**: Add functionality for managing orders and payments.
- **Recommendation Engine**: Implement a book recommendation system.
- **Improved Search**: Integrate Elasticsearch for advanced book searching.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **Django**: The framework powering this project.
- **PostgreSQL**: The database for storing application data.
- **Docker**: The containerization platform for easy deployment.
- **django-allauth**: For implementing social authentication.
- **Bootstrap**: For responsive design.

## Contributing

Feel free to fork this project, submit issues, or create pull requests for any improvements or new features you'd like to add!

---

Happy coding! 😊
