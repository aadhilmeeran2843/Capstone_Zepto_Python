# Zepto Web Automation Testing using Selenium & Python

This project automates key user workflows on the Zepto grocery website using Selenium WebDriver, Python, and Pytest.
It is designed using a Page Object Model (POM) framework for scalability and maintainability.


🧰 Tech Stack
Component	Tool
Automation	Selenium WebDriver
Language	Python
Test Framework	Pytest
Design Pattern	Page Object Model (POM)
Reporting	Screenshots on Failure
Browser	Google Chrome
📱 System Requirements

Windows 10/11

Python 3.9+ installed

Google Chrome Browser

ChromeDriver (auto-managed)

📦 Installation

Clone the repository:

git clone https://github.com/aadhilmeeran2843/Capstone_Zepto_Python
cd zepto-web-automation


Install dependencies:

pip install -r requirements.txt

⚙️ Run Tests

Execute all tests:

pytest -v


Execute with custom inputs:

pytest -v --base-url "https://www.zeptonow.com/" --pincode "560066"


Reports & screenshots will be saved under:

reports/screenshots/


🧠 Concepts Used

✅ Selenium Web Automation
✅ Page Object Model
✅ WebDriver Manager
✅ Exception handling & Assertions
✅ Logging & failure screenshots

🔍 Known Limitations

Zepto page elements change frequently → occasional locator updates required

Location-based restrictions may impact tests outside supported pincodes

🙌 Author

Aadhil Ahamed Meeran
Test Automation | Python | Selenium
