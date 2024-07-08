# Distributed-System
This repository contains a report on the comparison of leader election algorithms in distributed systems, along with the code implementing some of the evaluated algorithms. These materials are part of the Distributed Systems course in the Master Degree (LM-18) at the University of Camerino. The project implements and compares various leader election algorithms using Docker and Zookeeper.

## Directory Structure

- `algorithms/`: Contains the implementation of each algorithm.
- `Dockerfile`: Dockerfile for building the Docker image.
- `docker-compose.yml`: Docker Compose file for orchestrating the services.
- `requirements.txt`: List of Python dependencies.
- `README.md`: Project documentation.

## Algorithms

- Bully Algorithm
- RAFT Algorithm
- Proof of Work
- Proof of Stake

## Running the Project

1. **Build the Docker Images**:
   ```bash
   docker compose build

2. **Run the containers**:
    ```bash
   docker compose up

This will start the Zookeeper container first, followed by the containers for each of the algorithms.

