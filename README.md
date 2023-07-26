# Anakonda Project
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

A container-based task runner REST API written in python language and
Flask framework to run user tasks in Docker and Kubernetes.

## Table of Contents
- [Introduction](#Introduction)
- [Getting Started](#Getting-Started)
    - [Prerequisites](#Prerequisites)
    - [Installation](#Installation)
- [Usage](#Usage)
    - [API Endpoints](#API-Endpoints)
    - [Supported Runtimes](#Supported-Runtimes)
    - [Project Structure](#Project-Structure)
    - [Error Handling](#Error-Handling)
    - [Logging and Monitoring](#Logging-and-Monitoring)
- [Docker](#Docker)
- [Kubernetes](#Kubernetes)
- [Contributing](#Contributing)
- [License](#License)

## Introduction
Anakonda is a REST API designed to execute tasks on a worker node within different runtimes like Docker or Kubernetes and return the results and status to the user. The API allows users to submit a task in the form of a script file, which is then executed in the specified runtime environment. This project is built using Python and the Flask framework.

## Getting Started

### Prerequisites

To run the project, ensure you have the following prerequisites installed:

- Python 3.7 or above
- Flask
- Docker (optional for Docker runtime)
- Kubernetes (optional for Kubernetes runtime)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Majid-dev/anakonda.git
   cd anakonda
   ```
2. run following docker-compose command
    ```bash
    docker-compose -f docker-compose.base.yaml -f docker-compose.publish.yaml up -d
    ```

## Usage
### API Endpoints
The API exposes the following endpoints:
- GET /api/v1/tasks/<task_id> : return a single task information
- GET /api/v1/tasks : return all tasks information
- POST /api/v1/task : Submit a task for execution. The request should include the task script and runtime information. The API will process the task and return the results and status.
- PATCH /api/v1/tasks/<task_id> : Update a task.
- DELETE /api/v1/tasks/<task_id> : delete a task.


### Supported Runtimes
The API supports two runtimes:
- Docker: To execute tasks within a Docker container.
- Kubernetes: To execute tasks within a Kubernetes pod.
To specify the runtime, include the runtime parameter in the API request.

### Project Structure
The project follows the MVC design pattern and is organized as follows:
- Config: contains environment variables and default configurations.
- Controller: Contains the API controllers to handle incoming requests.
- Model: Contains the data models and database-related logic.
- Resource: Contains API endpoints implementations.
- Schema: Contains database defenition tables.
- Migrations: Contains database migration scripts.
- anakonda.py: The main application file.

### Error Handling
The API uses try-except blocks in the controller to handle errors and return suitable error codes and explanations based on error type in the response.

### Logging and Monitoring
Currently, there are no logging and monitoring features implemented in the project.

## Docker
To run the project using Docker, follow these steps:

Build the Docker image:
```bash
docker build -t anakonda .
```
Run the API using docker-compose:
```bash
docker-compose -f docker-compose.base.yaml -f docker-compose.publish.yaml up -d
```
> Note: To test the API, use the docker-compose.test.yaml file and flages like the command below:
```bash
docker-compose -f docker-compose.base.yaml -f docker-compose.test.yaml up --build --abort-on-container-exit --exit-code-from anakonda
```

## Kubernetes
To deploy the project on a Kubernetes cluster, use the provided deployment manifest:
```bash
kubectl apply -f kubernetes-deployment.yaml
```

## Contributing
Contributions to this Helm chart are welcome! If you find any issues or have improvements to suggest, please open an issue or submit a pull request on the GitHub repository.

## License
This project is licensed under the MIT License - see the LICENSE file for details.