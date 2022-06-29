import requests
import eel

@eel.expose
def get_weather(word):
    URL_AUTH = 'https://developers.lingvolive.com/api/v1/authenticate'
    URL_TRANSLATE =  'https://developers.lingvolive.com/api/v1/Minicard'
    KEY = 'ODYzOTdhYTAtZTJkNC00M2I5LWFjZjEtNjFlNGIzMjBjMzNkOmIxMWEyOTM0NmE4MTQ2MDc5Y2QyZDgwNTBiMmEyMmQz'
    headers_auth = {'Authorization':'Basic ' + KEY}
    auth = requests.post(URL_AUTH, headers=headers_auth)

    if auth.status_code == 200:
        token = auth.text
        x = token.split('\"')
        token = x[1]
        
        
        if word:
            headers_translate = {"Authorization":"Bearer "+ token }
            params = {'text':word, 'srcLang': '1049', 'dstLang': '1033'}
                
            r = requests.get(URL_TRANSLATE, headers=headers_translate, params=params)
            r.status_code
                
            res = r.json()
                
            try:
                return res['Translation']['Translation']
            except:
                return 'Не найдено варианта для перевода'
    else:
        return 'Error'

#q = get_weather('Мышь')
#print(q)
eel.init('web')
eel.start('main.html', size=(700, 700))


