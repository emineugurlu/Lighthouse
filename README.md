# 🚀 Lighthouse: Distributed Log Management System

A professional-grade, asynchronous log collection and processing system built with a modern microservices architecture.

## 📝 About the Project
Lighthouse is a distributed system designed to handle high-volume log data without blocking main application threads. It uses a **Producer-Consumer** pattern where log entries are ingested via an API and queued in a high-speed message broker (Redis) before being processed and persisted by an independent worker.

## 🏗 System Architecture
The project follows a decoupled architecture to ensure high availability:
1. **Producer (FastAPI):** Receives logs and instantly pushes them to the queue.
2. **Message Broker (Redis):** Acts as a resilient buffer, storing logs in a FIFO (First-In, First-Out) structure.
3. **Consumer (Worker):** A standalone background process that retrieves logs from the queue and saves them to permanent storage.



## 🛠 Tech Stack
- **Python 3.11**
- **FastAPI** (High-performance web framework)
- **Redis** (In-memory data structure store / Message Broker)
- **Docker & Docker Compose** (Containerization and orchestration)
- **Pydantic** (Data validation and settings management)

## 🧠 What I Learned During This Project
This project was a significant milestone in my development as a Computer Engineer. Key takeaways include:
- **Asynchronous Processing:** Implementing `BackgroundTasks` to handle operations outside the request-response cycle.
- **Distributed Systems:** Learning how to decouple services using a message broker like Redis.
- **Containerization:** Managing multi-container environments using Docker Compose.
- **Logic & Flow:** Handling data serialization/deserialization with JSON and Python dictionaries.
- **Debugging:** Solving real-world connection and import issues in a containerized environment.

## 🚀 Installation & Usage
### Running with Docker
To spin up the entire infrastructure:
```bash
docker-compose up --build
````
| <img src="https://github.com/user-attachments/assets/6b248d5e-9e0c-4c3f-9a4b-eadc8fcd3d7a" width="300" height="300" style="object-fit:cover;"> | <img src="https://github.com/user-attachments/assets/da4bf2cf-5ab8-4183-9f74-3579822c1e8b" width="300" height="300" style="object-fit:cover;"> | <img src="https://github.com/user-attachments/assets/280e47e9-8585-438c-8be0-95703f3da911" width="300" height="300" style="object-fit:cover;"> |

Access API Docs: http://localhost:8000/docs

##Running the Worker Locally
````bash
python app/worker.py
````
Developed by Emine Computer Engineer
