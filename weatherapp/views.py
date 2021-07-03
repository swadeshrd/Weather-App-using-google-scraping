from django.shortcuts import render

# Create your views here.

def get_html_content(city):
    import requests
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    city = city.replace(' ', '+')
    html_content = session.get(f'https://www.google.com/search?q=weather+in+{city}').text
    return html_content

def home(request):
    weather_data = None
    if 'city' in request.GET:
        #fetch weather data
        city = request.GET.get('city')
        html_content = get_html_content(city)
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html_content, 'html.parser')

        weather_data = dict()
        weather_data['region'] = soup.find('div', attrs={'id': 'wob_loc'}).text
        weather_data['dayTime'] = soup.find('div', attrs={'id': 'wob_dts'}).text
        weather_data['status'] = soup.find('span', attrs={'id': 'wob_dc'}).text
        weather_data['temp'] = soup.find('span', attrs={'id': 'wob_tm'}).text
        weather_data['precipitation'] = soup.find('span', attrs={'id': 'wob_pp'}).text 
        weather_data['humidity'] = soup.find('span', attrs={'id': 'wob_hm'}).text 
        weather_data['wind'] = soup.find('span', attrs={'id': 'wob_ws'}).text 

    return render(request, 'wheatherapp/index.html', {'weather' : weather_data})