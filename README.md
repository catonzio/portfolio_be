# Portfolio Backend

This repository contains the backend and database components for my portfolio website. The application is built with FastAPI (Python) and uses PostgreSQL as the database. It is dockerized for convenient deployment using Docker Compose.

## Technologies Used

- **FastAPI (Python):** FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. Learn more about FastAPI [here](https://fastapi.tiangolo.com/).

- **PostgreSQL:** PostgreSQL is a powerful, open-source relational database system. Learn more about PostgreSQL [here](https://www.postgresql.org/).

## Deployment

To deploy the portfolio backend and database using Docker Compose, follow these steps:

### Prerequisites

- Ensure that you have [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/) installed on your machine.

### Configuration

1. Clone this repository:

    ```bash
    git clone https://github.com/catonzio/portfolio_be
    cd portfolio_be
    ```

2. Create a `.env` file in the root of the project with the following environment variables:

    ```env
    # Example .env file, customize as needed
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_DB=
    POSTGRES_SERVER=

    PGADMIN_MAIL=
    PGADMIN_PW=

    PGADMIN_DEFAULT_EMAIL=
    PGADMIN_DEFAULT_PASSWORD=

    MAIL_USERNAME=
    MAIL_PASSWORD=
    MAIL_FROM=
    MAIL_PORT=
    MAIL_SERVER=
    TEMPLATE_FOLDER=
    ```

    Adjust the values according to your preferences.

### Run the Application

3. Build and start the containers using Docker Compose:

    ```bash
    docker-compose up -d --build
    ```

4. Access the FastAPI application at `http://localhost:8000`.

### Stop the Application

To stop and remove the containers:

```bash
docker-compose down
```

## Additional information

- **API Documentation:** The FastAPI application automatically generates API documentation. Access it at http://localhost:8000/docs after starting the application.

- **Database Connection:** The PostgreSQL database is available at localhost:5432. Use the configured credentials to connect.