# Car Maintenance CLI

Car Maintenance CLI is a command-line tool that helps users manage and keep track of their vehicle's maintenance schedule and expenses. This tool is designed for car enthusiasts and anyone looking to maintain their vehicles effectively.

## Table of Contents

- [Car Maintenance CLI](#car-maintenance-cli)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Built With](#built-with)
  - [Authors](#authors)

## Features

- **User Registration:** Create an account to store car information.
- **Car Information:** Add and manage multiple cars, including make, model, year, and VIN.
- **Maintenance Record:** Record various maintenance activities, including date, type, cost, and notes.
- **Service Reminders:** Get upcoming maintenance reminders based on mileage or time intervals.
- **Expense Tracking:** Track maintenance expenses and filter by date or service type.
- **Backup and Restore:** Securely back up and restore data.

## Getting Started

### Prerequisites

- Python (3.6+)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Kevin-Curado-Santos/car-maintenance-cli.git

    cd car-maintenance-cli
    ```

2. Install the required packages:
3. Run the application:

   ```bash
   python car_cli.py [-h] {add,fuel,maintenance,service,expenses,insurance,list}
   ```

    - **add:** Add a new car or maintenance record.
    - **fuel:** Add a new fuel record.
    - **maintenance:** Add a new maintenance record.
    - **service:** Add a new service reminder.
    - **expenses:** View expenses.
    - **insurance:** View insurance information.
    - **list:** List cars or maintenance records.
    - **-h, --help:** Show help message and exit.

## Built With

- [Python](https://www.python.org/)

## Authors

- **Kevin Curado-Santos** - [Kevin-Curado-Santos](https://github.com/Kevin-Curado-Santos)
