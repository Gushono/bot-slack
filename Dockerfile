# Use the official Python image with version 3.10 as the base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy only the poetry.lock and pyproject.toml files to the container
COPY poetry.lock pyproject.toml ./

# Install Poetry
RUN pip install --no-cache-dir poetry

# Install dependencies from pyproject.toml using Poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-interaction --no-ansi

# Copy the rest of the application code to the container
COPY . .

# Expose the port on which your Flask app runs (adjust the port if needed)
EXPOSE 8080

# Specify the command to run your Flask app
CMD ["flask", "run", "--port=8080"]