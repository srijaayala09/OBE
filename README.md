<h1 align="center">OBE</h1>
<p align='ccenter'>OBE introduces an Outcome-Based Education (OBE) result management system for streamlined and effective academic assessment and reporting. It not only rectifies the deficiencies of conventional systems but also incorporates additional features for enhanced functionality. </p>

![](https://github.com/whomping-willow/OBE/blob/main/static/images/homeAnimation.gif)


## Skills and Experience
- ⚛ Django
- 📱 Visual Studio Code
- 💻 HTML, CSS, JS, Python, Bootstrap, JavaScript

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
  - [1. Create a virtual environment](#1-create-a-virtual-environment)
  - [2. Activate the virtual environment](#2-activate-the-virtual-environment)
  - [3. Install required dependencies](#3-install-required-dependencies)
  - [4. Run migrations](#4-run-migrations)
  - [5. Create an admin user](#5-create-an-admin-user)
- [Run the application](#run-the-application)
- [View the application](#view-the-application)
- [Features](#features)
- [Usage](#Usage)

## Prerequisites
Make sure you have the following prerequisites installed:
- Python 3.10.4 or above
## Installation
1. **Create a virtual environment:**
   From the root directory run:
   ```bash
   python -m venv venv
   ```
2. **Activate the virtual environment:**
   From the root directory run:
     On Linux/macOS:
   ```bash
    source venv/bin/activate
   ```
    On Windows:
    ```bash
    venv\scripts\activate
    ```
3. **Install required dependencies:**
   From the root directory run:
    ```bash
    pip install -r requirements.txt
    ```
4. **Run migrations:**
    From the root directory run:
    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```
5. **Create an admin user:**
    From the root directory run:
     ```bash
    python manage.py createsuperuser
     ```
When prompted, enter a username, email, and password.

## Run the application
  From the root directory run:
  ```bash
    python manage.py runserver
  ```

## View the application
  Go http://127.0.0.1:8000/ to view the application.

## Features

- **Students:**
  - *Search and view individual results or results of the whole batch.*
  ![image](https://github.com/whomping-willow/OBE/assets/51289468/7beb78ea-cf60-4710-b8c7-9e067466c653)
  
  - *Download Result Card.*
    
    ![image](https://github.com/whomping-willow/OBE/assets/51289468/a8596c03-adb8-499f-8a98-2aea6a586c74)


- **Teachers:**
  - *Prepare results for their courses.*
    ![image](https://github.com/whomping-willow/OBE/assets/51289468/fa9b50b0-b22b-471e-964b-708608cb20a5)
    ![image](https://github.com/whomping-willow/OBE/assets/51289468/02b7fce5-86a5-4223-b069-80691bd44b7d)
  - *View marksheet*
    ![image](https://github.com/whomping-willow/OBE/assets/51289468/85e00e87-75c8-4d90-a2a7-1bcfef0e92a3)

  - Analyze course outcomes and program outcomes using Co-Po attainment graphs.
    ![image](https://github.com/whomping-willow/OBE/assets/51289468/bddb9668-2a8d-4c27-9fb8-d38f662abb7b)


- **System:**
  - Smooth and error-free result management.

- **Department Chairman:**
  - Monitor the overall condition of the result for any batch.
    ![image](https://github.com/whomping-willow/OBE/assets/51289468/e74c73d4-5e6f-424a-a5d4-c1a0ec9566ab)

    

- **University:**
  - Monitor the result condition of any department.
    ![image](https://github.com/whomping-willow/OBE/assets/51289468/6219ebb0-4f65-4436-9f72-490f5803afb6)

  

## Usage

- The application is designed to provide the following functionalities:

  - **Student Section:**
    - Search and view individual or batch results.

  - **Teacher Section:**
    - Prepare and analyze results for courses.

  - **Chairman Section:**
    - Monitor the overall result condition for a batch.

  - **University Section:**
    - Monitor departmental result conditions.















