from django.shortcuts import render
from django.http import JsonResponse
import requests
from bs4 import BeautifulSoup


# Renders home page
def index(request):
    return render(request, 'theorem/index.html')


# Fetch title and description for the given url
def get_url_details(request):
    entered_url = request.POST.get('url')
    title_text, description_text = '', ''
    fetch_url = requests.get(entered_url)

    # using the BeaitifulSoup module
    soup = BeautifulSoup(fetch_url.text, 'html.parser')

    # displaying the title
    for title in soup.find_all('title'):
        title_text = title.get_text()
    for meta_data in soup.find_all('meta'):
        if 'name' in meta_data.attrs and meta_data.attrs['name'] == 'description':
            description_text = meta_data.attrs['content']
    return JsonResponse({'status': 200, 'title': title_text, 'description': description_text})
