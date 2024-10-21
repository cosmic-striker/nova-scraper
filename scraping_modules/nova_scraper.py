import whois
import requests
from bs4 import BeautifulSoup

def whois_lookup(domain):
    try:
        domain_info = whois.whois(domain)
        if domain_info:
            return f"Domain Name: {domain_info.domain_name}\nRegistrar: {domain_info.registrar}\nCreation Date: {domain_info.creation_date}\nExpiration Date: {domain_info.expiration_date}\nName Servers: {domain_info.name_servers}"
        else:
            return "No WHOIS information found."
    except Exception as e:
        return f"Error fetching domain info: {e}"

def basic_web_scraping(email):
    url = f"https://www.google.com/search?q={email}+breach"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            search_results = soup.find_all('h3')
            results = [result.text for result in search_results[:5]]  # Return top 5 results
            if results:
                return f"Top search results for {email}:\n" + "\n".join(results)
            else:
                return f"No information found for {email}."
        else:
            return f"Failed to retrieve search results. Status code: {response.status_code}"
    except Exception as e:
        return f"Error fetching search results: {e}"
