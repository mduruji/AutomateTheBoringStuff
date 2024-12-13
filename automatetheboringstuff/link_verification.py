"""
Write a program that, given the URL of a web page, will attempt to download every linked page on the page.
The program should flag any pages that have a 404 “Not Found” status code and print them out as broken links.
"""

import requests, bs4, pyinputplus as pyp

#Pass in the url
#Request for the web page
#Do a check for 404 links and print them out as broken links
#Ask chatgpt for a website to test the code


def get_url():
    url = pyp.inputURL('Enter a URL > ')
    return url


def get_page(url):
    try:
        page = requests.get(url)
        page_parser = bs4.BeautifulSoup(page.text, 'html.parser')
        links = page_parser.findAll('a')

        for link in links:
            try:
                complete_url = 'https:' + link.get('href')
                requests.get(complete_url)
                print(complete_url)
            except requests.exceptions.HTTPError as e:
                if e == 404:
                    print('Broken link > ', url)
    except requests.exceptions.InvalidURL as e:
        print("Url reports the error: ", e, '\nTry another link')


input_url = get_url()
get_page(input_url)
