import requests
from bs4 import BeautifulSoup
from os.path import basename
import datetime
import os
import sys
import re
import time

def scrapping(url):
    '''
    url='https://www.boredpanda.com/black-and-white-celebrity-photos-colorized-machine-learning-deepai-hidreley'
    '''

    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')
    
    title_folder = soup.select('h1.post-title')[0].text.strip()
    title_folder_cleaned = re.sub('[^A-Za-z0-9 ]+', '', title_folder)
    filename = "Votre répertoire" % title_folder_cleaned
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    results_1 = soup.find('div', class_='open-list-items')
    results_2 = soup.find('div', class_='post-content')
    
    '''
    if results_1 != None:

        imgs = results_1.find_all('img', class_='image-size-full',src=True)
        
        for img in imgs:
            i = img.get('src')
            title = img.get('alt')
            
            with open(filename + basename(title) +'.jpg', "wb") as s:
                s.write(requests.get(i).content)
  

    if results_1 != None:
    
        p = results_1.find_all('p', class_='post-content-description')
        
        for imgs in p:
            img = imgs.find('img', class_='image-size-full', src=True)
            i = img.get('src')
            title = imgs.find('span', class_='bordered-description',text=True).text.strip()
            t = re.sub('[^A-Za-z0-9 ]+', '', title )
            
            with open(filename + basename(t) +'.jpg', "wb") as s:
                s.write(requests.get(i).content)
    '''
    n = 0
    
    if results_1 != None:

        imgs = results_1.find_all('img', class_='image-size-full',src=True)
        
        for img in imgs:
            i = img.get('src')
            title = img.get('alt')
            t = re.sub('[^A-Za-z0-9 ]+',' ', title)
            
            if (os.path.exists(filename + basename(t) + '.jpg')):
                n = n + 1
                with open(filename + basename(t) + ' %d.jpg' % n, "wb") as s:
                    s.write(requests.get(i).content)
            else:
                with open(filename + basename(t) + '.jpg', "wb") as s:
                    s.write(requests.get(i).content)
                    
    elif results_2 != None:
        
        imgs = results_2.find_all('img',src=True)
        
        for img in imgs:
            i = img.get('src')
            title = img.get('alt')
            t = re.sub('[^A-Za-z0-9 ]+',        # Search for all non-letters
                        ' ',                    # Replace all non-letters with spaces
                        str(title))
            
            if title != None:
                with open(filename + basename(t) +'.jpg', "wb") as s:
                    s.write(requests.get(i).content)
            else:
                with open(filename + basename(i) +'.jpg', "wb") as s:
                    s.write(requests.get(i).content)
        
    else:
        print("Can't find it!")


if __name__ == "__main__":
    scrapping(sys.argv[1])


