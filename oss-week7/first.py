import requests

url = ("https://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json")
parsms = {"key: "  "   ","targetDt: " "20260824"}

response = requests.get(url,params=parsms,timeout = 10)
print(response.status_code)

data = response.json()

result = data['boxOfficeResult']
print(result.keys())

movies = result['dailyBoxOfficeList']

print(len(movies))
print(type(movies))

first= movies[0]

print(first['rank'])
print(first['movieNm'])
print(first['audiCnt'])

for movie in movies[:5]:
    rank = movie['rank']
    name = movie['movieNm']
    audi = int(movie['audiCnt'])
    print(f"{rank}위 {name} {audi: ,} 명")



    