import requests
from bs4 import BeautifulSoup
import csv

# Define three base URLs corresponding to Brest, Nantes, and Rennes, respectively
BASE_URLS = [
    ('https://www.imt-atlantique.fr/fr/annuaire-enseignants-chercheurs?search_api_fulltext=&f%5B0%5D=localisation_chercheur%3A1236', 'brest'),
    ('https://imt-atlantique.fr/fr/annuaire-enseignants-chercheurs?search_api_fulltext=&f%5B0%5D=localisation_chercheur%3A1233', 'nante'),
    ('https://www.imt-atlantique.fr/fr/annuaire-enseignants-chercheurs?search_api_fulltext=&f%5B0%5D=localisation_chercheur%3A1239', 'rennes')
]

# Maximum number of pages to scrape
MAX_PAGES = 15  # Adjust this number based on how many pages you need to scrape

def generate_email(name):
    # Split the name and convert to lowercase
    parts = name.lower().split()
    # Join with dots and add the email domain
    email = '.'.join(parts) + '@imt-atlantique.fr'
    return email

def scrape_page(url, csv_writer, dept):
    # Fetch the page content
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all user blocks on the page
        users = soup.find_all('div', class_='user--view-mode-vue-dep')
        
        for user in users:
            name = user.find('div', class_='field-user--dynamic-token-fielduser-nom-prenom').text.strip()
            designation = user.find('div', class_='field-user--field-poste').text.strip() if user.find('div', class_='field-user--field-poste') else 'N/A'
            contact_link = user.find('div', class_='field-user--dynamic-token-fielduser-user-lien-contact').find('a')['href']
            telephone = user.find('div', class_='field-user--field-telephone').text.strip() if user.find('div', class_='field-user--field-telephone') else 'NULL'
            email = generate_email(name)  # Generate the email address
            
            # Write the extracted information to the CSV file
            csv_writer.writerow([
                name,
                dept,  # Set dept based on the function parameter
                designation,
                contact_link,
                telephone,
                email,
                'NULL',  # ResearchGate
                'NULL',  # LinkedIn
                'NULL'   # Facebook
            ])
    else:
        print(f'Error fetching the page: {url}')

def main():
    # Open the CSV file in write mode
    with open('teacher_info.csv', mode='w', newline='', encoding='utf-8') as file:
        # Create a CSV writer object
        csv_writer = csv.writer(file)
        
        # Write the header row
        csv_writer.writerow([
            'name',
            'dept',
            'designation',
            'extension',
            'telephone',
            'email',
            'researchgate',
            'linkedin',
            'facebook'
        ])
        
        # Iterate through each URL
        for base_url, dept in BASE_URLS:
            # Iterate through the specified number of pages
            for page in range(MAX_PAGES):
                # Construct the URL for the current page
                page_url = f'{base_url}&page={page}'
                
                # Scrape the current page
                print(f'Scraping page: {page_url}')
                scrape_page(page_url, csv_writer, dept)

if __name__ == '__main__':
    main()
