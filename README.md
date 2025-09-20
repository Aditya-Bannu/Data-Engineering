# 🚀 Data Engineer Portfolio

This portfolio demonstrates **end-to-end data engineering skills** including database design, ETL pipelines, orchestration, testing, CI/CD, and containerization.

---

## 📂 Project Structure

```
01_batch_etl_pipeline/   # Example batch ETL with Airflow
02_streaming_pipeline/   # Example streaming pipeline with Kafka + Spark
03_sql_analytics/        # Analytical SQL queries
tests/                   # Unit tests for ETL & SQL
.github/workflows/       # GitHub Actions CI/CD pipeline
requirements.txt         # Python dependencies
Dockerfile               # Docker image for ETL pipeline
docker-compose.yml       # Multi-container setup (Postgres, Airflow, Kafka, Spark)
```

---

## 🛠️ Setup Instructions

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/data-engineer-portfolio.git
cd data-engineer-portfolio
```

### 2️⃣ Install Dependencies (Local)
```bash
pip install -r requirements.txt
```

### 3️⃣ Run Unit Tests
```bash
pytest tests/
```

### 4️⃣ Run with Docker
Build the Docker image:
```bash
docker build -t dataeng .
```

Run containers (Postgres, Airflow, Kafka, Spark):
```bash
docker-compose up -d
```

Check running containers:
```bash
docker ps
```

Access services:
- **Airflow UI** → [http://localhost:8080](http://localhost:8080)
- **Postgres DB** → `localhost:5432`
- **Kafka Broker** → `localhost:9092`
- **Spark UI** → [http://localhost:8081](http://localhost:8081)

---

## ✅ CI/CD Pipeline
- GitHub Actions workflow runs:
  - **Flake8** (linting)
  - **SQLFluff** (SQL linting)
  - **Pytest** (unit tests)

---

## 📊 Projects Included

### 1. Batch ETL (Airflow + Python)
- Fetches weather API data
- Transforms & stores in Postgres

### 2. Streaming Pipeline (Kafka + Spark)
- Real-time events simulation
- Spark processes & aggregates messages

### 3. SQL Analytics
- Business insights with advanced SQL queries

---

## 📌 Next Steps
- Add more Airflow DAGs (scheduling)
- Extend streaming examples with real data
- Add dbt for advanced SQL transformations

---

💡 This portfolio is designed to showcase **Data Engineering, SQL, and DevOps practices** that make you job-ready.
