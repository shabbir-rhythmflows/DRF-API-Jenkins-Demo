# Use an official Python runtime as a parent image
FROM python:3.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/

# Run migrations
RUN python manage.py makemigrations
RUN python manage.py migrate

# Set the environment variable for the superuser username
ENV DJANGO_SUPERUSER_USERNAME admin
# Set the environment variable for the superuser password
ENV DJANGO_SUPERUSER_PASSWORD admin
# Create the superuser
RUN python manage.py createsuperuser --noinput

# Expose port
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
