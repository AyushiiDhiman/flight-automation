# ✈️ Flight Automation Framework

A complete Selenium + Pytest based automation project built for learning, portfolio, and real-world testing demonstrations.

## ✅ Features
- Selenium WebDriver automation (Chrome)
- Pytest test framework
- JSON-based test data
- Reusable fixtures in `conftest.py`
- Flight booking automation test (BlazeDemo)
- File Organizer automation test
- Manual ChromeDriver path configuration
- Logging support (utils/logger.py)

---

## 📁 Project Structure
```
flight-automation/
│
├── data/
│     └── testdata.json
│
├── tests/
│     ├── test_flight.py
│     ├── test_organizer.py
│     └── conftest.py
│
├── utils/
│     └── logger.py
│
├── organizer.py
├── requirements.txt
└── README.md
```

---

## 🧪 Running Tests
Install dependencies:
```
pip install -r requirements.txt
```
Run all tests:
```
pytest -v
```
Run with HTML report:
```
pytest --html=report.html
```

---

## 🔧 Tech Stack
- Python 3.x
- Selenium 4
- Pytest
- ChromeDriver
- JSON for config/test data

---

## ▶️ Test Cases Included
### ✅ **1. Flight Booking Automation**
- Opens BlazeDemo
- Selects Origin
- Selects Destination
- Searches for flights
- Validates results page

### ✅ **2. File Organizer Automation**
- Creates dummy files
- Runs organizer logic
- Validates files are moved into correct folders

---

## 📘 Configuration
`testdata.json` controls your test inputs:
```
{
    "url": "https://blazedemo.com/",
    "origin": "Mexico City",
    "destination": "Cairo"
}
```

---

## 🚀 Future Enhancements
- Add Page Object Model (POM)
- Add CI/CD pipeline (GitHub Actions)
- Add screenshots on test failure
- Add multiple flight tests
- Add detailed reports

---

## 🤝 Contributions
Pull requests are welcome! Feel free to fork and improve the framework.

---

## 📄 License
Open-source for educational and personal use.
