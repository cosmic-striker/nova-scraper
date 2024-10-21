
# 🚀 NOVA Scraper 🌌

**NOVA Scraper** is your go-to lightweight tool for uncovering **WHOIS domain data** and performing **email breach scraping** with just a few clicks! Built with the power of Flask and Python, NOVA Scraper delivers quick results in a stylish, dark-themed interface, optimized for user experience.

![NOVA Scraper Banner](static/nova_banner.png) 

## 🌟 Key Features

- 🔍 **WHOIS Lookup**: Get detailed domain registration data, including registrar info, creation and expiration dates, and more.
- 🕵️ **Email Breach Scraping**: Quickly check whether an email is associated with known breaches using simple web scraping.
- 🎨 **Sleek Dark UI**: Enjoy a visually appealing, responsive interface with a tech-focused design.
- ⚡ **Fast and Lightweight**: Results are presented instantly in a clear, organized format.

## 🛠️ Project Structure

```
nova_scraper/
├── app.py                    # Main Flask application
├── templates/
│   ├── index.html            # Input form page
│   └── result.html           # Results display page
├── static/
│   ├── style.css             # Custom styles for the app
│   ├── nova_logo.png         # NOVA Scraper logo
│   └── nova_banner.png       # Banner image for README
└── scraping_modules/
    └── nova_scraper.py       # WHOIS lookup and web scraping logic
```

---

## 🚀 Getting Started

Getting started with NOVA Scraper is as easy as 1-2-3! Follow these simple steps to run the app locally on your machine.

### 1️⃣ Prerequisites

Ensure you have the following installed:
- **Python 3.7+**
- Flask and required libraries (`whois`, `requests`, `beautifulsoup4`)

### 2️⃣ Installation

Clone the repository to your local machine:
```bash
git clone https://github.com/cosmic-striker/nova_scraper.git
cd nova_scraper
```

Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the required dependencies:
```bash
pip install -r requirements.txt
```

### 3️⃣ Running the App

Fire up the Flask server:
```bash
python app.py
```

Then, navigate to the app in your browser at:
```
http://127.0.0.1:5000
```

---

## 🎨 Visual Walkthrough

### 🌐 Home Page

The **NOVA Scraper** home page provides a clean, intuitive form where users can enter either a domain for WHOIS lookup or an email for breach scraping.

![Home Page](static/nova_home_screenshot.png) 

### 🕵️ Scraping Results

After entering a domain or email, NOVA Scraper quickly presents results in a clear, formatted view. Whether it's WHOIS data or breach-related information, the results are easy to read and navigate.

![Results Page](static/nova_results_screenshot.png) 

---

## 💡 Features Breakdown

### WHOIS Lookup 🔍
Enter any domain, and NOVA Scraper will fetch comprehensive details like:
- Domain registrar
- Creation and expiration dates
- Name servers

Example:
```
Domain Name: example.com
Registrar: Example Registrar
Creation Date: 1995-01-01
Expiration Date: 2025-01-01
Name Servers: ns1.example.com, ns2.example.com
```

### Email Breach Scraping 🕵️
Quickly find whether an email address is associated with public breaches. The app scrapes data from search engines to provide relevant results.

Example:
```
Top search results for example@example.com:
1. Breach reported in XYZ dataset
2. Leaked credentials on ABC platform
```

---

## 👨‍💻 Contributing

Got an idea to make **NOVA Scraper** even better? Contributions are more than welcome!

1. Fork the repository.
2. Create a new feature branch: `git checkout -b feature/your-feature`.
3. Make your changes and commit them: `git commit -m 'Added feature'`.
4. Push to the branch: `git push origin feature/your-feature`.
5. Submit a pull request and let's make magic happen! ✨

---

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 🚀 Ready to Scrape the Web?

With NOVA Scraper, uncovering WHOIS data and email breach info has never been easier. Give it a try today and experience fast, lightweight scraping with just a few clicks!

![NOVA Scraper Footer](static/nova_footer.png) 
