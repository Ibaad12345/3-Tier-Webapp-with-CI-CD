# 1. Start with an official, lightweight Python operating system layer
FROM python:3.11-slim

# 2. Set the folder inside the container where our work will happen
WORKDIR /app

# 3. Copy our list of dependencies into the container
COPY requirements.txt .

# 4. Install the Python libraries listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of our backend application code into the container
COPY . .

# 6. Inform Docker that the container will listen on port 8000
EXPOSE 8000

# 7. Define the command to start our web server when the container boots up
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]