from flask import Flask, render_template, request
from scraping_modules.nova_scraper import whois_lookup, basic_web_scraping

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape():
    target = request.form['target']
    
    # Check if input is an email (basic web scraping) or a domain (WHOIS lookup)
    if '@' in target:
        result = basic_web_scraping(target)
    else:
        result = whois_lookup(target)
    
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
