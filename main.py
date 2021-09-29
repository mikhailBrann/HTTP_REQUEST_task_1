import requests

class Hero:
    def __init__(self, name, intelligence):
        self.name = name
        self.intelligence = int(intelligence)

    def __str__(self):
        return f"Имя героя: {self.name}\nИнтелект: {self.intelligence}\n"


def get_intelligence(url, names):
    result_list = []
    for name in names:
        reqst = requests.get(f"{url}/search/{name}")

        if reqst.status_code == 200:
            request_result = reqst.json()

            if request_result['results']:
                for result in request_result['results']:
                    if result['name'] == name and result['powerstats']['intelligence']:
                        result_list.append({'name': result['name'], 'intelligence': result['powerstats']['intelligence']})

    if result_list:
        result_list = sorted(result_list, key=lambda hero_: hero_['intelligence'])
        wiseacre = Hero(result_list[0]['name'], result_list[0]['intelligence'])
        
        return wiseacre
    else:
        return 'Некорректно введены данные'
        

if __name__ == '__main__':
    api_url = 'https://superheroapi.com/api.php/2619421814940190'
    heroes_list = ['Hulk', 'Captain America', 'Thanos']
    wiseacre_hero = get_intelligence(api_url, heroes_list)
    print(wiseacre_hero)