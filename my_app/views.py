import requests
from requests.compat import quote_plus
from django.shortcuts import render
from bs4 import BeautifulSoup
from . import models

BASE_CraigList_URL = "https://mumbai.craigslist.org/search/bbb?query={}"
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'


# Create your views here.

def home(request):
    return render(request, 'Base.html')  # it call the function home as default


def new_search(request):
    # to fetch the request string from the frontend
    search = request.POST.get('Search')

    # creating a new object for search from models and to save all the search made on the site to searches

    models.Search.objects.create(search=search)

    # function used to add (+) sign in the string
    print(quote_plus(search))

    # final url of craigslist
    final_url = BASE_CraigList_URL.format(quote_plus(search))

    # Fetching the address from requests module
    response = requests.get(final_url)

    # converting response to text
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')

    # find_all the links where class is result-title
    post_listing = soup.find_all('li', {'class': 'result-row'})
    final_posting = []

    for post in post_listing:
        post_titles = post.find(class_='result-title').text
        post_url = post.find('a').get('href')

        if post.find(class_='result-price'):
            post_price = post.find(class_='result-price').text
        else:
            # post_price = 'N/A'
            post_price = ""
        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL.format(post_image_id)
        else:
            post_image_url = 'https://www.craigslist.org/images/peace.jpg'

        final_posting.append((post_titles, post_url, post_price, post_image_url))

    # creating a dictionary for front-end
    stuff_for_frontend = {
        'Search': search,
        'final_postings': final_posting,
    }

    # it call new search function
    return render(request, 'my_app/new-search.html', stuff_for_frontend)
