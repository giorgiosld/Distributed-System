# Distributed-System
This repo contains the report about the comparison of leader election algorithms in distributed systems and the code which implements some algorithms that are evaluated. All these materials is about the course of Distributed Systems supplied in the Master Degree (LM-18) at the University of Camerino.

# Leader Election Algorithms

This project implements and compares various leader election algorithms using Docker and Zookeeper.

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

