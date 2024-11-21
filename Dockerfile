# Step 1: Use the base Python 3.12 image
FROM python:3.12-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the local code to the container
COPY . /app/

# Step 4: Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the port that Django will run on
EXPOSE 8000

# Step 6: Run migrations and then start the Django development server
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
