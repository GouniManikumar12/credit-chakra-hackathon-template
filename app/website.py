from typing import Dict, List
import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

class WebsiteScraper:
    def __init__(self):
        """
        Initialize website scraper with common headers
        """
        self.session = requests.Session()
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }

    def scrape_website(self, url: str) -> Dict:
        """
        Scrape content from a website
        
        Args:
            url: Website URL to scrape
            
        Returns:
            Dictionary containing scraped content
        """
        try:
            response = self.session.get(url, headers=self.headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract basic information
            data = {
                'title': self._extract_title(soup),
                'description': self._extract_description(soup),
                'contact_info': self.extract_contact_info(response.text),
                'links': self._extract_links(soup, url),
                'images': self._extract_images(soup, url),
                'text_content': self._extract_text_content(soup)
            }
            
            return data
            
        except requests.RequestException as e:
            print(f"Error scraping {url}: {str(e)}")
            return {}

    def extract_contact_info(self, html_content: str) -> Dict:
        """
        Extract contact information from HTML content
        
        Args:
            html_content: HTML content to parse
            
        Returns:
            Dictionary containing contact information
        """
        soup = BeautifulSoup(html_content, 'html.parser')
        
        # Common patterns for contact information
        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        phone_pattern = r'(?:\+\d{1,3}[-. ]?)?\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}'
        
        # Find all text content
        text_content = soup.get_text()
        
        # Extract emails and phone numbers
        emails = re.findall(email_pattern, text_content)
        phones = re.findall(phone_pattern, text_content)
        
        # Look for address patterns
        addresses = self._find_addresses(soup)
        
        return {
            'emails': list(set(emails)),  # Remove duplicates
            'phones': list(set(phones)),  # Remove duplicates
            'addresses': addresses
        }

    def _extract_title(self, soup: BeautifulSoup) -> str:
        """Extract page title"""
        title = soup.find('title')
        return title.text.strip() if title else ''

    def _extract_description(self, soup: BeautifulSoup) -> str:
        """Extract meta description"""
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        return meta_desc.get('content', '') if meta_desc else ''

    def _extract_links(self, soup: BeautifulSoup, base_url: str) -> List[str]:
        """Extract all links from the page"""
        links = []
        for a in soup.find_all('a', href=True):
            href = a['href']
            full_url = urljoin(base_url, href)
            links.append(full_url)
        return list(set(links))  # Remove duplicates

    def _extract_images(self, soup: BeautifulSoup, base_url: str) -> List[str]:
        """Extract all image URLs from the page"""
        images = []
        for img in soup.find_all('img', src=True):
            src = img['src']
            full_url = urljoin(base_url, src)
            images.append(full_url)
        return list(set(images))  # Remove duplicates

    def _extract_text_content(self, soup: BeautifulSoup) -> str:
        """Extract main text content"""
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
        
        text = soup.get_text()
        # Clean up text
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = ' '.join(chunk for chunk in chunks if chunk)
        return text

    def _find_addresses(self, soup: BeautifulSoup) -> List[str]:
        """Find potential addresses in the content"""
        # Look for common address indicators
        address_elements = []
        
        # Look for elements with address-related classes or IDs
        for element in soup.find_all(['div', 'p', 'span']):
            if any(term in str(element.get('class', [])).lower() for term in ['address', 'location', 'contact']):
                address_elements.append(element.get_text().strip())
        
        # Look for elements with address-related text
        for element in soup.find_all(text=re.compile(r'address|location|contact', re.I)):
            address_elements.append(element.strip())
        
        return list(set(address_elements))  # Remove duplicates 