# Gmail Login Automation Project

## Overview

This automation project validates the Gmail login form using **Playwright**, **Pytest**, and **Allure**.  
It covers both **positive** and **negative** test cases using data-driven input from an Excel file.

The validation logic handles various scenarios including valid login, incorrect credentials, missing fields, malformed emails, script injection attempts, and more.

## Structure

📦 checkpoint-Playwright-pytest
│
├── pages/                      # Page Object Model classes (POM)
│   ├── BasePage.py
│   ├── Home_Page.py
│   ├── Inbox_Page.py
│   └── Login_Page.py
│
├── tests/                      # Test files and test base
│   ├── __init__.py
│   ├── BaseTest.py
│   ├── conftest.py
│   ├── test_home_page.py
│   ├── test_login.py
│   └── screenshots/            # Failure screenshots (Allure attachments)
│
├── utils/                      # Utilities and validation helpers
│   ├── __init__.py
│   ├── input.py                # Parsing logic
│   ├── load_data.py           # Excel reader
│   ├── response_validators.py # UI assertions and validators
│   └── Allure_Attachments.py  # Screenshot capture
│
├── test_data/
│   └── test_cases_login.xlsx  # Data-driven login test cases
│
├── allure-results/            # Allure raw results (generated during run)
├── pytest.ini                 # Pytest configuration
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation


## ✅ Features
🎯 Playwright for UI automation (Gmail login form)

🧱 Page Object Model (POM) for maintainable and modular test structure

📊 Data-driven testing using Excel for positive and negative test coverage

📈 Allure Reporting for rich, visual test reports

✅ Test Coverage includes:

✅ Valid login credentials

❌ Missing or empty fields

⚠️ Invalid email formats (missing @, wrong TLD, Hebrew characters)

🔐 Password length boundaries (too short / too long)

💣 Script injection and special character inputs

🌐 Unsupported domains (e.g., non-Gmail)




---




 
## 📦 Prerequisites

Before starting, make sure the following are installed on your machine:

- [Git](https://git-scm.com/downloads)
- [Python 3.8+](https://www.python.org/downloads/)
- pip (comes with Python)
- Allure CLI (see installation below)

---

## 🛠️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/WishahiGit/checkpoint-Playwright-pytest>
cd checkpoint-Playwright-pytest
```

### 2️⃣ Set up Virtual Environment 

```bash
python -m venv .venv
.venv\Scripts\activate     # On Windows
# OR
source .venv/bin/activate  # On Mac/Linux
```

### 3️⃣ Install Dependencies

Install all required Python packages:

```bash
pip install -r requirements.txt
```

---

## 🚀 How to Run Tests

### Option 1: From Terminal inside the Project

Run all UI tests and generate Allure results with a single command:

```bash
pytest --alluredir=allure-results
```

### Option 2: From External Command Line (CMD / PowerShell)

```bash
cd path\to\project\directory
.venv\Scripts\activate
pytest --alluredir=allure-results
```

---

## 🧪 Run Specific Tests


```bash
pytest -m ui --alluredir=allure-results
```

---

## 📊 Generate Allure Report

```bash
allure serve allure-results
```

---

## Author

Created by Saber Wishahi
