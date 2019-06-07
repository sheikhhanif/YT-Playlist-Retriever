# packages
from requests import get
from bs4 import BeautifulSoup

def get_playlist(url):
    """
    This function will return all the titles of playlist videos
    """
    
    response = get(url)
    html_soup = BeautifulSoup(response.text, 'html.parser')
    pl = html_soup.find_all('h4', class_='yt-ui-ellipsis yt-ui-ellipsis-2')
    with open('playlist.txt', 'a') as file:
        for li in pl:
            file.write(li.text)

            
# reading list of urls
with open('urls.txt', 'r') as u:
    urls = u.readlines()

# looping over in each url and calling get_playlist function to extract videos titles
for url in urls:
    url = url.replace('\n','')
    get_playlist(url)

