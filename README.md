# Task Management System - Flask and MongoDB

This project is a simple yet well-structured task management system developed using **Python** and **MongoDB**. It enables users to **create**, **delete**, **update**, and **view** tasks in a convenient and efficient manner. The application interacts with **MongoDB**, which stores the tasks, allowing for quick retrieval and modification.

The system is designed to be easy to deploy and manage. For local development, you can quickly spin up the project using **Docker Compose**, which handles both the application and its MongoDB database dependencies. Alternatively, you can deploy the application using **Kubernetes with Minikube**, taking advantage of the provided manifest files to set up the environment seamlessly.

To simplify the setup even further, the project includes a **`./deploy`** script. This script automates the entire deployment process, allowing you to launch the application on **Minikube** with just one command, reducing the complexity and setup time significantly.

## Key Features of the Project:
- **Task Management**: Easily create, update, and delete tasks.
- **MongoDB Integration**: Stores tasks in a **NoSQL database** for fast access and scalability.
- **Docker Compose**: Supports local containerized deployment with **Docker Compose** for easy setup and management.
- **Kubernetes/Minikube Deployment**: Ready-to-use Kubernetes manifests for deploying the application in a **Minikube** local cluster.
- **Automated Deployment**: The **`./deploy`** script simplifies the deployment process, automating Minikube setup and application deployment with just a single command.

This project provides an ideal starting point for understanding basic CRUD operations with **MongoDB** in a web application, as well as how to work with **Docker** and **Kubernetes** for containerized and scalable application deployments.

### Docker Compose Setup

To deploy the project using **Docker Compose**, follow these simple steps:

1. Ensure that the **`docker-compose.yml`** file is in the root directory of your project.

2. In the terminal, navigate to your project directory where the `docker-compose.yml` file is located.

3. Run the following command to build and start the application:

   ```bash
   docker-compose up


### Kubernetes Setup with Minikube

To deploy the project using **Kubernetes** and **Minikube**, follow these steps:

1. **Start Minikube**:
   First, ensure that **Minikube** is installed and running on your machine. Start your Minikube Kubernetes cluster with the following command:

   ```bash
   minikube start 
   kubectl apply -f mongodb-deployment.yaml
   kubectl apply -f python-app-deployment.yaml
