#  TodoMVC Playwright Automation Framework

## 📌 Project Overview

This project is a **professional UI Automation Testing Framework** developed using **Playwright with Python** to automate and validate the TodoMVC demo web application.
It covers all major user workflows, UI validations, and supports cross-browser execution with interactive Allure HTML reporting.

**Application Under Test:**
[https://demo.playwright.dev/todomvc/#/](https://demo.playwright.dev/todomvc/#/)

---

## 🎯 Project Objectives

* Automate complete TodoMVC application functionality
* Validate UI behaviour and user interactions
* Execute tests across multiple browsers
* Generate professional automation execution reports
* Follow industry-standard automation practices

---

## ✅ Features Automated

### 🔹 Todo Creation

* Add single and multiple todos
* Validate empty input
* Validate special characters and long text

### 🔹 Todo Completion

* Mark and unmark todos
* Validate counter changes and completed state
* Clear completed todos

### 🔹 Todo Editing

* Edit todos using double-click
* Save / cancel edit operations
* Prevent empty edit save

### 🔹 Todo Deletion

* Delete individual todos
* Validate empty list behaviour

### 🔹 Filter Tabs

* Validate All / Active / Completed tabs
* Verify correct todo count on each tab
* Validate tab switching

### 🔹 UI Validations

* Header, footer, and placeholder validation
* Clear completed button visibility
* Checkbox and hover behaviour

**Total Automated Test Cases:** 25+

---

## 🏗 Framework Architecture

The framework follows **Page Object Model (POM)** design pattern.

```
todomvc_allure_clean/
│
├── pages/            # Page Object Model classes
├── tests/            # Automated test cases
├── utils/            # Locators and test data
├── pytest.ini        # PyTest configuration
├── requirements.txt
├── reports/          # Allure HTML Dashboard (index.html)
├── screenshots/      # Execution proof screenshots
└── README.md
```

---

## 🌐 Supported Browsers

| Browser           | Supported |
| ----------------- | --------- |
| Chromium (Chrome) | ✅         |
| Firefox           | ✅         |

---

## ⚙ Installation & Setup

```bash
git clone https://github.com/HacktiveMindset/todomvc-playwright-framework.git
cd todomvc-playwright-framework
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
playwright install
```

---

## ▶ Running Tests

```bash
pytest
```

Run on specific browser:

```bash
pytest --browser chromium
pytest --browser firefox
```

---

## 📊 Allure Test Execution Dashboard

After every execution, the framework generates an **interactive Allure HTML dashboard**.

Path:

```
reports/<latest-run-folder>/index.html
```

The dashboard displays:

* Total test execution summary
* Pass / Fail statistics
* Browser-wise execution results
* Step-by-step test logs
* Execution history
* Screenshots of failed tests

Generate dashboard manually:

```bash
pytest --alluredir=reports
allure generate reports -o reports --clean
```

Open:

```
reports/<latest-run-folder>/index.html
```

---

## ✨ Framework Highlights

* Page Object Model architecture
* Reusable automation methods
* Parallel execution ready
* Screenshot capture on failures
* Interactive HTML reporting
* CI/CD friendly structure

---

## 👤 Author

**Piyush Mujmule**


