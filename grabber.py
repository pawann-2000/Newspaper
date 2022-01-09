#imported some web scraping libs here
import requests
from bs4 import BeautifulSoup
import pprint

#vars
response = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('.titlelink')
subtext = soup.select('.subtext')

#Testing out this function still, give it a run to see what it does
def grabber(links, subtext):
    hn = []
    for dex, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[dex].select('.score')
        if len(vote):
            votes = int(vote[0].getText().replace(' points', ''))
            if votes>99:
                hn.append({'title': title, 'link': href, 'votes': votes})
    return hn

pprint.pprint(grabber(links, subtext))