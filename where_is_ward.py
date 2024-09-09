import requests
import api_key

url = "https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/trollbat/kr1"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key.imsi_key
}

response = requests.get(url, headers=headers)
accounts = response.json()
puuid = accounts['puuid']

start=0
count=1
url = f"https://asia.api.riotgames.com/lol/match/v5/matches/by-puuid/{puuid}/ids?start={start}&count={count}"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key.imsi_key
}

response = requests.get(url, headers=headers)
matchId_by_puuid = response.json()
matchId = matchId_by_puuid[0]

url = f"https://asia.api.riotgames.com/lol/match/v5/matches/{matchId}/timeline"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept-Language": "ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Charset": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://developer.riotgames.com",
    "X-Riot-Token": api_key.imsi_key
}

response = requests.get(url, headers=headers)
timeLine = response.json()

timeLine_info = timeLine['info']
# print(timeLine_info.keys())
# print(timeLine_info['endOfGameResult'])
# print(timeLine_info['frameInterval'])
# print(type(timeLine_info['frames']))
# print(len(timeLine_info['frames']))

# for i in range(len(timeLine_info['frames'])):
    # print(type(timeLine_info['frames'][i]))
    # print(timeLine_info['frames'][i].keys())
timeLine_info_frames = timeLine_info['frames']

# for i in range(len(timeLine_info_frames[2]['events'])):
#     print(timeLine_info_frames[2]['events'][i])


ward_placed_data = []
for i in range(len(timeLine_info_frames)):
    for j in range(len(timeLine_info_frames[i]['events'])):
        if timeLine_info_frames[i]['events'][j].get('type')=='WARD_PLACED':
            print(timeLine_info_frames[i]['events'][j])








# for i in range(len(timeLine_info_frames[1]['events'])):
#     print(timeLine_info_frames[1]['events'][i])

# for i in range(len(timeLine_info_frames[1]['events'])):
#     print(timeLine_info_frames[1]['events'][i])