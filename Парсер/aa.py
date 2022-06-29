from requests_html import HTMLSession
import json
import time

session = HTMLSession()

url = 'https://segway.cherry-wheel.com/kickscooters/kickscooter-max'

res = session.get(url)

ab = res.html.find('.top-swiper__link')

link = []

for u in ab:


    r = session.get('https://segway.cherry-wheel.com' + u.attrs['href'])
    
    time.sleep(2)

    r.html.render(timeout=50)

    about = r.html.find('.welcome__swiper-img')

    a = r.html.find('.welcome__title')

    try:
        z, x = a[1].text.split('\n')
    except:
        z, b, n = a[1].text.split('\n')
        x = b + ' ' + n

    print(x)

    list1 = []

    for y in about:
        list1.append('https://segway.cherry-wheel.com' + y.attrs['src'])


    l = list(set(list1))

    dict_v = {

        x : l
    }

    link.append(dict_v)

with open('data.json', 'w', encoding='UTF-8') as f:
    json.dump(link, f, indent=4, ensure_ascii=False, sort_keys=False)


