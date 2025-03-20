from bs4 import BeautifulSoup
import requests
class Website:
    def __init__(self,url):
        self.url  = url
        response  = requests.get(url)
        self.body = response.content
        soup      = BeautifulSoup(self.body,"html.parser")
        self.links = None
        self.title = soup.title.string if soup.title else "No title Found"
        if soup.body:
            for irr in soup.body(['script','style','img','input']):
                irr.decompose()
            self.text = soup.body.get_text(separator='\n',strip=True)
        else:
            self.text = ""
        
        links = []
        for link in soup.find_all('a'):
            if link.get('href'):
                links.append(link.get('href'))
        
        self.links = links
        
    def get_contents(self):
        return f"WEBSITE TITLE : {self.title}\n\nWEBSITE TEXT : {self.text}\n\nWEBSITE LINKS : {self.links}"