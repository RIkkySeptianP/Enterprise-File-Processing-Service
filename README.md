# Enterprise File Processing Service

A Python-based background service that automatically monitors incoming files, validates them, processes them, archives completed files, and records operational logs.

---

## Overview

Enterprise File Processing Service is designed to simulate a production-ready file automation service commonly used in enterprise environments.

The application continuously watches a configured input directory, validates incoming files, processes them according to business rules, archives completed files, and records all activities into log files.

This project demonstrates backend automation concepts including background services, file monitoring, validation, logging, and clean modular architecture.

---

## Features

- Monitor incoming files automatically
- File validation
- Background processing
- Automatic archive
- Processing log generation
- Configurable directories
- Modular architecture

---

## Workflow

```
Input Folder
      │
      ▼
File Detected
      │
      ▼
Validation
      │
 ┌────┴────┐
 │         │
 ▼         ▼
Success   Failed
 │         │
 ▼         ▼
Process   Failed Folder
 │
 ▼
Archive
 │
 ▼
Logging
```

---

## Project Structure

```
enterprise-file-processing-service

│
├── app.py
├── config.py
├── watcher.py
├── validator.py
├── processor.py
├── archive.py
├── logger.py
│
├── config.json
├── requirements.txt
├── README.md
│
├── input/
├── processing/
├── output/
├── archive/
├── failed/
└── logs/
```

---

## Technologies

- Python 3
- Watchdog
- Pandas
- Pathlib
- Logging
- JSON
- Shutil

---

## Current Version

### Version 1

- Folder monitoring
- File validation
- Processing pipeline
- Archive completed files
- Logging system

---

## Future Improvements

- CSV parsing
- PDF processing
- Excel report generation
- Email notification
- Duplicate file detection
- Scheduler
- Docker support
- Kubernetes deployment

---

## Purpose

This project was created as part of my backend engineering portfolio to demonstrate enterprise file automation using Python.

It is inspired by real-world enterprise systems where files are received, validated, processed, archived, and logged automatically.

---

## Author

**Rikky Septian Prasetiyo**

Senior Backend Engineer

.NET | Python | Enterprise Systems

Currently learning Kotlin, Docker, and Kubernetes 🇯🇵
