# imported some web scraping libs here
import requests
from bs4 import BeautifulSoup
import pprint

# vars
response = requests.get('https://news.ycombinator.com/news')
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.select('.titlelink')
subtext = soup.select('.subtext')

# Testing out this function still, give it a run to see what it does


def grabber(links, subtext):
    hn = []

    for index, item in enumerate(links):

        title = item.getText()
        href = item.get('href', None)
        vote = subtext[index].select('.score')

        if len(vote):
            votes = int(vote[0].getText().replace(' points', ''))
            
            if votes > 99:
                hn.append({'title': title, 'link': href, 'votes': votes})

    return sort_stories_by_votes(hn)

# Sorting function to sort the votes in descending order


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


pprint.pprint(grabber(links, subtext))
