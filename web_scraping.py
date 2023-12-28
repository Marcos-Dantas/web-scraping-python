from bs4 import BeautifulSoup
import urllib3
import aiohttp
import random

# Desabilitar os avisos de SSL inseguro, para usar-o quebrador de verificação captcha Web Unbloqued
urllib3.disable_warnings()

all_fields_required_on_response = {
    'website',
    'rank_global',
    'category',
    'total_visits',
    'bounce_rate',
    'pages_per_visit',
    'avg_visit_duration',
    'last_month_change',
    'top_countries',
    'gender_distribution',
    'age_distribution',
    'first_categories_of_interests',
    'first_topics',
    'main_traffic_sources',
    'social_traffic_to_website'
}
async def parser(soup, website):
    response_json = {}
    
    response_json['website'] = website

    elementos = soup.find_all(class_='wa-rank-list__value')
    elementos2 = soup.find_all(class_='wa-rank-list__info')
        
    response_json['rank_global'] = elementos[0].text.replace('#', '')

    response_json['rank_country'] = f""" {elementos[1].text.replace('#', '')} - {elementos2[0].text}"""
    response_json['category'] = f"""{elementos[2].text.replace('#', '')} - {elementos2[1].text}"""

    elementos = soup.find_all(class_='engagement-list__item')

    response_json['total_visits'] = elementos[0].text.replace('Total Visits', '')
    response_json['bounce_rate'] = elementos[1].text.replace('Bounce Rate', '')
    response_json['pages_per_visit'] = elementos[2].text.replace('Pages per Visit', '')
    response_json['avg_visit_duration'] = elementos[3].text.replace('Avg Visit Duration', '')
    response_json['last_month_change'] = elementos[5].text.replace('Last Month Change', '')

    countries = {}
    elementos = soup.find_all(class_='wa-geography__country wa-geography__legend-item')
    
    for elemento in elementos:
        countries[elemento.find(class_='wa-geography__country-name').text] = elemento.find(class_='wa-geography__country-traffic-value').text

    response_json['top_countries'] = countries

    elementos = soup.find_all(class_='wa-demographics__gender-legend-item-value')

    response_json['gender_distribution'] = {
        'female': elementos[0].text,
        'males': elementos[1].text
    }

    elementos = soup.find(class_='wa-demographics__age-chart')
    elementos = elementos.find_all(class_='wa-demographics__age-data-label')

    response_json['age_distribution'] = {
        'range_18_24': elementos[0].text,
        'range_25_34': elementos[1].text,
        'range_35_44': elementos[2].text,
        'range_45_54': elementos[3].text,
        'range_55_64': elementos[4].text,        
        'range_65+': elementos[5].text,    
    }

    elementos = soup.find_all(class_='wa-interests__chart-item')
    response_json['first_categories_of_interests'] = [
        elementos[0].text, elementos[1].text, elementos[2].text,
        elementos[3].text, elementos[4].text
    ]
    
    response_json['first_topics'] = [
        elementos[5].text, elementos[6].text, elementos[7].text,
        elementos[8].text, elementos[9].text
    ]

    website_competitors_info = {}
    website_competitors = []
    elementos = soup.find_all(class_='wa-competitors__list-item')
    
    website_competitors_info['website'] = elementos[0].find_all(class_='wa-competitors__list-column')[0].text
    website_competitors_info['affinity'] = elementos[0].find_all(class_='wa-competitors__list-column')[1].text
    website_competitors_info['monthly_visits'] = elementos[0].find_all(class_='wa-competitors__list-column')[2].text
    website_competitors_info['category'] = elementos[0].find_all(class_='wa-competitors__list-column')[3].text
    website_competitors_info['rank_by_category'] = elementos[0].find_all(class_='wa-competitors__list-column')[4].text
    
    website_competitors.append(website_competitors_info)

    website_competitors_info['website'] = elementos[1].find_all(class_='wa-competitors__list-column')[0].text
    website_competitors_info['affinity'] = elementos[1].find_all(class_='wa-competitors__list-column')[1].text
    website_competitors_info['monthly_visits'] = elementos[1].find_all(class_='wa-competitors__list-column')[2].text
    website_competitors_info['category'] = elementos[1].find_all(class_='wa-competitors__list-column')[3].text
    website_competitors_info['rank_by_category'] = elementos[1].find_all(class_='wa-competitors__list-column')[4].text
    
    website_competitors.append(website_competitors_info)

    website_competitors_info['website'] = elementos[2].find_all(class_='wa-competitors__list-column')[0].text
    website_competitors_info['affinity'] = elementos[2].find_all(class_='wa-competitors__list-column')[1].text
    website_competitors_info['monthly_visits'] = elementos[2].find_all(class_='wa-competitors__list-column')[2].text
    website_competitors_info['category'] = elementos[2].find_all(class_='wa-competitors__list-column')[3].text
    website_competitors_info['rank_by_category'] = elementos[2].find_all(class_='wa-competitors__list-column')[4].text
    
    website_competitors.append(website_competitors_info)

    website_competitors_info['website'] = elementos[3].find_all(class_='wa-competitors__list-column')[0].text
    website_competitors_info['affinity'] = elementos[3].find_all(class_='wa-competitors__list-column')[1].text
    website_competitors_info['monthly_visits'] = elementos[3].find_all(class_='wa-competitors__list-column')[2].text
    website_competitors_info['category'] = elementos[3].find_all(class_='wa-competitors__list-column')[3].text
    website_competitors_info['rank_by_category'] = elementos[3].find_all(class_='wa-competitors__list-column')[4].text
    
    website_competitors.append(website_competitors_info)

    website_competitors_info['website'] = elementos[4].find_all(class_='wa-competitors__list-column')[0].text
    website_competitors_info['affinity'] = elementos[4].find_all(class_='wa-competitors__list-column')[1].text
    website_competitors_info['monthly_visits'] = elementos[4].find_all(class_='wa-competitors__list-column')[2].text
    website_competitors_info['category'] = elementos[4].find_all(class_='wa-competitors__list-column')[3].text
    website_competitors_info['rank_by_category'] = elementos[4].find_all(class_='wa-competitors__list-column')[4].text
    
    website_competitors.append(website_competitors_info)

    elementos = soup.find(class_='wa-traffic-sources__channels')
    elementos = elementos.find_all(class_='wa-traffic-sources__channels-data-label')

    response_json['main_traffic_sources'] = {
        'direct_traffic': elementos[0].text,
        'reference_traffic': elementos[1].text,
        'organic_search': elementos[2].text,
        'paid_search': elementos[3].text,
        'social': elementos[4].text,        
        'email': elementos[5].text,    
        'exhibition': elementos[5].text,    
    }

    elementos = soup.find(class_='wa-social-media__chart')
    elementos = elementos.find_all(class_='wa-social-media__chart-data-label')
    
    response_json['social_traffic_to_website'] = {
        'youtube': elementos[0].text,
        'facebook': elementos[1].text,
        'twitter': elementos[2].text,
        'whatsap': elementos[3].text,
        'reddit': elementos[4].text,        
        'others': elementos[5].text,    
    }

    return response_json

async def make_scraping(domain_name):
    
    url = f'https://www.similarweb.com/website/{domain_name}/' 

    headers = {
        'authority': 'scrapeme.live',
        'dnt': '1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'none',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-user': '?1',
        'sec-fetch-dest': 'document',
        'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    }

    # Faz a requisição assíncrona usando a função make_async_request()
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, ssl=False, proxy='http://UserTestAplication:4S7TwLXXAlw8qb@unblock.oxylabs.io:60000') as response:

            if response.status  == 200:
                response_text = await response.text()
                soup = BeautifulSoup(response_text, 'html.parser')
                # caso retorne a pagina de erro do site
                if soup.find(class_='error__title') or soup.find_all(class_='wa-rank-list__value')[0].text == '- -':
                    return '404'
                else:
                    response = await parser(soup, domain_name)

                return response
            
            else:
                return response.status
