# Use official Python image
FROM python:3.11

# Set working directory inside container
WORKDIR /app

# Copy project files into container
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip && pip install -r requirements.txt

# Expose port for Django app
EXPOSE 8000

# Start Django server using Gunicorn
CMD ["gunicorn", "faq_project.wsgi:application", "--bind", "0.0.0.0:8000"]
