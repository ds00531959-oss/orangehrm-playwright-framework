# OrangeHRM Automation Framework using Playwright (Python)

## 🚀 Project Overview

This project is an end-to-end test automation framework developed for OrangeHRM using **Playwright**, **Python**, and **Pytest**. It follows the **Page Object Model (POM)** design pattern to create reusable, maintainable, and scalable test scripts.

The framework automates major HR workflows such as Login, Add Employee, Search Employee, Update Employee, Delete Employee, Invalid Login validation, and Forgot Password functionality.

---

## 🛠️ Tech Stack

* Python 3
* Playwright
* Pytest
* Page Object Model (POM)
* Pytest HTML Reports
* Pytest Markers
* Logging
* Screenshots on Failure

---

## 📁 Project Structure

```text
orangeHRM_login/
│── pages/
│── tests/
│── utils/
│── logs/
│── reports/
│── screenshots/
│── conftest.py
│── config.py
│── pytest.ini
│── requirements.txt
└── README.md
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
cd orangeHRM_login
```

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright browsers:

```bash
playwright install
```

---

## ▶️ Run Test Cases

Run all tests:

```bash
pytest
```

Run Smoke tests:

```bash
pytest -m smoke
```

Run Sanity tests:

```bash
pytest -m sanity
```

Run Regression tests:

```bash
pytest -m regression
```

Generate an HTML report:

```bash
pytest --html=reports/report.html --self-contained-html
```

---

## ✅ Automated Test Scenarios

* Login
* Invalid Login
* Forgot Password
* Add Employee
* Search Employee
* Update Employee
* Delete Employee

---

## ⭐ Key Features

* Page Object Model (POM) architecture
* Reusable Base Page methods
* Smoke, Sanity, and Regression test categorization
* HTML test reporting
* Screenshot capture on test failures
* Organized project structure
* Easy execution using Pytest markers
* Scalable and maintainable automation framework

---

## 📌 Future Enhancements

* Allure Reporting
* GitHub Actions CI/CD
* Jenkins Integration
* Parallel Test Execution
* Cross-Browser Testing

---

## 👨‍💻 Author

**Dharmendra Kumar**

Automation Testing | Playwright | Python | Pytest | Manual Testing
