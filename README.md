# System Optimization and Monitoring Project

This project provides a FastAPI-based backend integrated with C++ modules to monitor and optimize system processes. It includes endpoints for monitoring, cleaning, and optimizing system performance while generating detailed reports.

---

## **Table of Contents**
1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Requirements](#requirements)
4. [Setup and Installation](#setup-and-installation)
5. [Usage](#usage)
6. [Endpoints](#endpoints)
7. [Future Improvements](#future-improvements)

---

## **Features**
- **Process Monitoring:** Retrieves running processes with their memory usage.
- **System Cleaning:** Deletes temporary files and logs the operation.
- **Performance Optimization:** Optimizes and generates summaries of system performance.
- **MongoDB Integration:** Stores logs and reports for further analysis.
- **C++ Modules Integration:** Executes system-level operations via compiled C++ binaries.
- **Scalable Architecture:** Cleanly separated logic, routes, and services for maintainability.

---

## **Project Structure**
```plaintext
project_root/
├── app/
│   ├── __init__.py          # Initializes the FastAPI app
│   ├── main.py              # Main entry point for the application
│   ├── config.py            # MongoDB configuration and app settings
│   ├── routes/
│   │   ├── __init__.py      # Initialization for route modules
│   │   ├── monitor.py       # Endpoints for process monitoring
│   │   ├── optimize.py      # Endpoints for optimization processes
│   │   ├── clean.py         # Endpoints for system cleaning
│   │   ├── summary.py       # Endpoints for report summaries
│   ├── services/
│   │   ├── __init__.py      # Initialization for service modules
│   │   ├── monitor_service.py # Logic for monitoring processes
│   │   ├── optimize_service.py # Logic for optimization processes
│   │   ├── clean_service.py    # Logic for cleaning system
│   │   ├── summary_service.py  # Logic for generating reports
│   ├── models/
│   │   ├── __init__.py      # Initialization for data models
│   │   ├── process.py       # Data model for processes
│   │   ├── clean.py         # Data model for files to clean
│   │   ├── log.py           # Data model for logs
├── scripts/
│   ├── system_monitor.cpp   # C++ module for monitoring processes
│   ├── system_cleaner.cpp   # C++ module for cleaning system
├── requirements.txt         # Python dependencies
├── Dockerfile               # Docker configuration
├── .env                     # Environment variables (e.g., MongoDB URL)
└── README.md                # Project documentation
```
## **Requirements**
- **Python 3.8+**
- **FastAPI**
- **MongoDB**
- **C++ Compiler (e.g., GCC or MSVC)**

---

## **Setup and Installation**

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/system-optimization.git
   cd system-optimization
2. Install Python Dependencies:

```bash
pip install -r requirements.txt
```

3. Compile C++ Modules: Navigate to the scripts/ directory and compile:

```bash
g++ system_monitor.cpp -o system_monitor.exe -lpsapi
g++ system_cleaner.cpp -o system_cleaner.exe -lpsapi
```


4. Set Up MongoDB:

Start a local or cloud MongoDB instance.
Update the .env file with your MongoDB connection string:
```arduino
MONGO_URI=mongodb://localhost:27017
```

5. Run the Application:

```bash
python -m app.main
```

6. Access API Documentation: Visit http://127.0.0.1:8000/docs for interactive Swagger documentation.



## **Usage**

### **System Monitoring**
- Retrieves a list of currently running processes along with their memory usage.
- Example request:
  ```bash
  curl -X GET "http://127.0.0.1:8000/monitor"
  ```
-   Example response:
```json
[
  {
    "pid": 1234,
    "name": "chrome.exe",
    "memory_usage": 10584
  },
  {
    "pid": 5678,
    "name": "explorer.exe",
    "memory_usage": 4216
  }
  ]
```

### **System Monitoring**
- Retrieves a list of currently running processes along with their memory usage.
- Example request:
  ```bash
  curl -X GET "http://127.0.0.1:8000/monitor"
  ```
  
  Example response:
  ```json
  [
  {
    "pid": 1234,
    "name": "chrome.exe",
    "memory_usage": 10584
  },
  {
    "pid": 5678,
    "name": "explorer.exe",
    "memory_usage": 4216
  }
  ]
  ```

### **System Cleaning**
- Cleans temporary files and unnecessary system files.
- Example request:
```bash
curl -X POST "http://127.0.0.1:8000/clean"
```
- Example response:
```json
{
  "status": "success",
  "files_removed": 154,
  "space_freed_mb": 1024
}
```
## **Endpoints**
| Method | Endpoint        | Description                                      |
|--------|-----------------|--------------------------------------------------|
| `GET`  | `/monitor`      | Returns a list of running processes and their memory usage. |
| `POST` | `/clean`        | Cleans system temporary files and logs the operation. |
| `GET`  | `/optimize`     | Optimizes system processes and returns a summary of the operation. |
| `GET`  | `/summary`      | Generates and returns a system performance summary, including memory usage, processes, and optimization results. |


