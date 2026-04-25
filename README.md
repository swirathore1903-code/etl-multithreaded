
# Multi-Threaded ETL Pipeline 🚀

## 📌 Overview

This project implements a **multi-threaded ETL (Extract, Transform, Load) pipeline** in Python using a producer-consumer architecture. It processes data in parallel, applies transformations, and stores results in a structured format using SQLite.

---

## ⚙️ Features

* Parallel ETL using Python threading
* Producer-consumer model with thread-safe queues
* Thread synchronization using `queue.join()`
* Data transformation and validation
* SQLite database integration for persistent storage
* Performance benchmarking with visualization

---

## 🏗️ Architecture

Extract → Transform → Load → Store (SQLite)

---

## 🛠️ Tech Stack

* Python
* Pandas
* SQLite
* Matplotlib
* Multithreading

---

## ▶️ How to Run

### 1. Install dependencies

pip install pandas matplotlib

### 2. Run the project

python benchmark.py

---

## 📁 Output

* `output/result.csv` → Processed data
* `database/etl.db` → SQLite database (generated at runtime)
* `output/performance.png` → Performance graph

---

## 🧠 Key Concepts Demonstrated

* Multithreading and concurrency
* Producer-consumer architecture
* Thread synchronization using queues
* ETL pipeline design
* Data validation and preprocessing
* Performance benchmarking

---

## 📊 Performance Insight

Execution time decreases with increasing threads up to an optimal limit, after which thread overhead reduces efficiency.

---

## ⚠️ Note

The `database/` and `output/` folders are excluded from version control using `.gitignore` since they contain generated files.

---

## 🚀 Future Improvements

* Integrate PostgreSQL or other databases
* Add real-time data streaming
* Implement logging and error handling
* Build a visualization dashboard

---

## 👩‍💻 Author

GitHub: https://github.com/swirathore1903-code
