# Gym Membership Management System

A Python-based command-line system for managing gym members and membership plans. This project includes full CRUD functionality, MySQL database integration, and a modular structure separating database logic from application flow.

## Features
- Create, retrieve, update, and delete gym members
- Create, retrieve, update, and delete membership plans
- Modular database access layer using `db.py`
- Input validation helpers for safer updates
- Clean, extensible structure for future expansion

## Requirements
- Python 3.x
- MySQL Server
- `mysql-connector-python` package

## Install & Running
Install the connector using:
```bash
pip install mysql-connector-python
```

Running the Application:
From the project’s root directory, run:
```bash
python main.py
```

## Project Structure
db.py - Database connection handler
main.py - CLI flow logic
members.py - Member CRUD operations
memberships.py - Membership CRUD operations
README.md - Project documentation

## Future Improvements:
- Add stricter input validation for numeric fields
- Add required-input loops for more robust data entry
- Improve printed output formatting
- Add additional system modules (classes, trainers, billing)
- Potential expansion into a GUI or web-based system

## Author
Sean MacNabb  
Software Engineer in the making