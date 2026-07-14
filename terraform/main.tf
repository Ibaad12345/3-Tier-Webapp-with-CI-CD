# 1. Declare that we need the Docker provider plugin
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

# 2. Configure the Docker provider
provider "docker" {}

# 3. Define a resource to fetch the Nginx image
resource "docker_image" "nginx" {
  name         = "nginx:alpine"
  keep_locally = false
}

# 4. Define a resource to run an Nginx container using that image
resource "docker_container" "nginx_server" {
  image = docker_image.nginx.image_id
  name  = "terraform-test-nginx"

  ports {
    internal = 80
    external = 9000
  }
}