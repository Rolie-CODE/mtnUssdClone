MTN MoMo Console Application (Python)
Project Overview

This project is a Python-based console application that simulates core functionalities of the MTN Mobile Money (MoMo) service. The application is designed to replicate common MoMo operations such as wallet management, money transfers, PIN verification, and contact handling within a terminal environment.

The primary objective of this project is to demonstrate practical Python programming skills through a real-world inspired fintech use case. The application focuses on clean logic, modular functions, and persistent data storage.

This project is currently under development and is not yet feature-complete.

Features Implemented
Core Functionality

Menu-driven MoMo-style interface

Money transfer to saved contacts

Wallet balance management

PIN verification and PIN change

Add and manage contacts

Phone number validation

Terminal screen management for improved user experience

Data Persistence

User data (wallet balance, PIN, and contacts) is stored in a JSON file

Data is automatically loaded at application startup

Data is saved whenever critical changes occur, including:

Successful transactions

PIN updates

Contact additions

This approach allows the application to maintain state across multiple sessions.

Technologies Used

Python 3

Standard Python libraries:

os for terminal operations

json for file-based data storage

Project Structure
momo_app/
│
├── main.py            # Application logic
├── momo_data.json     # Persistent data storage (auto-generated)
└── README.md

Current Limitations

No transaction history tracking

Single-user simulation only

Limited error handling in some menu flows

Some menu options are placeholders

PIN is stored in plain text

Codebase is currently procedural (OOP refactor planned)

Planned Enhancements

Implement transaction history logging

Secure PIN storage using hashing

Support for multiple user wallets

Improved input validation and error handling

Refactor using Object-Oriented Programming principles

Add unit tests

Develop a graphical or web-based interface

Learning Outcomes

This project demonstrates proficiency in:

Python control flow and function design

Dictionary-based data management

File handling and JSON serialization

State persistence in applications

Building real-world inspired console applications

Author

Roland Tenkorang
Computer Science Student
Aspiring Software Developer

Project Status

In Development
This project is actively being improved as part of ongoing learning and portfolio development.
