# Elite Athelete Outlet

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
This project is dependent on Docker
Download Docker Here https://www.docker.com/products/docker-desktop/

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository
   ```
   git clone <repository_url>
   ```
2. Navigate to the project directory
   ```
   cd <project_directory>
   ```
3. Start the Docker container
   ```
   docker-compose up
   ```

### Database Migrations
To make database migrations, use the following command:
```
python manage.py makemigrations  # This command creates migration files based on your model changes
python manage.py migrate         # This command applies the migration files to the database
```

To make database migrations( while the container is running), use the following command:
`docker-compose exec web python manage.py migrate`

### Restarting and Running service

```
docker-compose down
docker-compose up -d
```

## Built With

- [Django](https://www.djangoproject.com/) - The web framework used
- [Docker](https://www.docker.com/) - Used for containerization
