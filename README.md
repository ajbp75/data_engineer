# Data Engineering Pipeline – Bronze & Silver Layers (Spark + TDD)

This repository contains a real-world data engineering case study demonstrating a layered data pipeline using **Bronze** and **Silver** layers, implemented with **PySpark** and **Test-Driven Development (TDD)** principles.

The project focuses on data quality, scalability, and maintainability, following best practices commonly used in production-grade data platforms.

---

## 📌 Overview

This project implements an end-to-end data pipeline with the following goals:

- Ingest raw data into a **Bronze layer**
- Apply cleansing, validation, and business rules in a **Silver layer**
- Use **Apache Spark (PySpark)** for scalable data processing
- Enforce **data quality and correctness through unit tests (TDD)**

The pipeline is designed to be deterministic, testable, and ready to support downstream analytical or Gold-layer workloads.

---

## 🏗️ Architecture

**Layered Data Architecture**

- **Bronze Layer**
  - Raw data ingestion
  - Minimal transformations
  - Schema preservation
  - Source-aligned datasets

- **Silver Layer**
  - Data cleansing and normalization
  - Schema enforcement
  - Business rule validation
  - Analytics-ready datasets

All transformations are implemented using **Spark**, with explicit schemas and reproducible logic.

---

## 🛠️ Tech Stack

- **Python**
- **PySpark**
- **Apache Spark**
- **pytest** (unit testing)
- **AWS-compatible storage** (e.g., S3 or local filesystem)
- **Git** for version control

---

## 📁 Project Structure

├── bronze/ # Raw ingestion layer
├── silver/ # Cleaned and validated data layer
├── tests/ # Unit tests (TDD)
├── notebooks/ # Optional exploratory notebooks
├── requirements.txt # Project dependencies
└── README.md # Project documentation


---

## ✅ Key Features

- Layered **Bronze → Silver** data architecture
- **Spark-based transformations** for scalability
- Explicit schema definitions
- Data quality and business rule validation
- **Test-Driven Development (TDD)** applied to data transformations
- Modular and maintainable codebase

---

## 🧪 Testing & Data Quality

All critical transformation logic in the Silver layer is covered by **unit tests**, following TDD principles:

- Schema validation tests
- Business rule tests
- Deterministic input/output validation

Tests ensure that data quality issues are detected early and that pipeline behavior remains stable as the code evolves.

---

## 🚀 How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/ajbp75/data_engineer.git
   cd data_engineer


python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows

pip install -r requirements.txt


python bronze/main.py
python silver/main.py

pytest
