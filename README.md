# Distributed-System
This repository contains a report on the comparison of leader election algorithms in distributed systems, along with the code implementing some of the evaluated algorithms. These materials are part of the Distributed Systems course in the Master Degree (LM-18) at the University of Camerino. The project implements and compares various leader election algorithms using Docker.

## Directory Structure

- `algorithms/`: Contains the implementation of each algorithm.
- `Distributed System Report`: Contains the LatEx code about the report.
- `Dockerfile`: Dockerfile for building the Docker image.
- `docker-compose.yml`: Docker Compose file for orchestrating the services.
- `requirements.txt`: List of Python dependencies.
- `README.md`: Project documentation.
- `Distributed_System_Report_Saldana.pdf`: Report delivered for the exam.

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


