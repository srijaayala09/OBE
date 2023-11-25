<h1 align="center">OBE Result Management System</h1>
This project is a web application based on Outcome Based Education (OBE) Result Management System.

![](https://github.com/whomping-willow/OBE/blob/main/static/images/homeAnimation.gif)

## JU_Trio
We are JU_Trio from the Computer Science and Engineering department at JU, passionate about content creation in the fields of Design and Development. We thrive on learning new languages and frameworks such as Django, JavaScript, CSS, and utilizing tools like Git. Exploring IDEs like Visual Studio Code is also a part of our journey. Collaboration and teamwork are aspects we truly enjoy in our work.

## Team Members
1. **Iffat Ara Sanzida**
2. **Nurun Nahar Fiha**
3. **Serajum Monira**

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
- Features
- Usage
- [Copyright and License](#copyright-and-license)

## Prerequisites
Make sure you have the following prerequisites installed:
- Python 3.10.4 or# OBE Result Management System
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

## Copyright and License
    Copyright © 2023 Iffat-Fiha-Monira. All rights reserved.

## Features

- **Students:**
  - Search and view individual results or results of the whole batch.
    ![image](https://github.com/whomping-willow/OBE/assets/51289468/7beb78ea-cf60-4710-b8c7-9e067466c653)

  - Download Result Card
    ![image](https://github.com/whomping-willow/OBE/assets/51289468/a8596c03-adb8-499f-8a98-2aea6a586c74)


- **Teachers:**
  - Prepare results for their courses.
  - Analyze course outcomes and program outcomes using Co-Po attainment graphs.

- **System:**
  - Smooth and error-free result management.

- **Department Chairman:**
  - Monitor the overall condition of the result for any batch.

- **University:**
  - Monitor the result condition of any department.
  

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

```arduino
Feel free to use this template and customize it further based on your specific project details and preferences.
```

---













