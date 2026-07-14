# 1. Use the official lightweight Nginx image from Docker Hub
FROM nginx:alpine

# 2. Copy our static index.html file into Nginx's default public web directory
COPY index.html /usr/share/nginx/html/

# 3. Inform Docker that Nginx runs on port 80
EXPOSE 80