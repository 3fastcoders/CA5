# CA5
Running the Docker Compose Stack
This repository contains a Docker Compose configuration for setting up a stack consisting of a Python web application (my-app), MongoDB, and Mongo Express. Follow the instructions below to run the stack using Docker Compose.

Prerequisites
Docker installed on your machine.
Steps

1) Clone the Repository:
  git clone <https://github.com/3fastcoders/CA5.git>
  cd <CA5>


2) Set Environment Variables:
  Create a .env file in the root directory of the repository and define the following environment variables:
  
  MONGO_USERNAME=<your_mongo_username>
  MONGO_PASSWORD=<your_mongo_password>
  
3) Run Docker Compose:

  Execute the following command to start the Docker Compose stack:
  docker-compose up -d
  (This command will pull the necessary images from Docker Hub (if not already present locally) and start the services defined in the docker-compose.yml file in detached        mode.)

4) Accessing the Services:

  Web Application (my-app):
  Open a web browser and navigate to http://localhost:8080 to access the Python web application.
  
  Mongo Express:
  Open a web browser and navigate to http://localhost:8081 to access the Mongo Express interface for MongoDB administration.
  
  MongoDB:
  MongoDB itself is not accessed through a web browser. It is accessible programmatically by the application.

5) Stopping the Stack:
  To stop and remove the Docker containers created by the stack, run the following command:
  docker-compose down
