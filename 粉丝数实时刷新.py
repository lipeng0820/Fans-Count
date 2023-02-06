import requests
import json
import time
import os

def scan_kwaiweb():

    cookies = {
        'did': 'web_9be1938827cf3c975289c2d9492b9879',
        'didv': '1618071238252',
        'hdige2wqwoino': '68wExeEHRHw6nGFNjdBH4srtkfXm6xhdf809e7f1',
        'apdid': 'd2a33786-b25a-42bc-bcf4-ebd313a0ac4e60db7e34828899158119c16047dbd79c:1675604309:1',
        'kpf': 'PC_WEB',
        'clientid': '3',
        'kpn': 'KUAISHOU_VISION',
    }

    headers = {
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'did=web_9be1938827cf3c975289c2d9492b9879; didv=1618071238252; hdige2wqwoino=68wExeEHRHw6nGFNjdBH4srtkfXm6xhdf809e7f1; apdid=d2a33786-b25a-42bc-bcf4-ebd313a0ac4e60db7e34828899158119c16047dbd79c:1675604309:1; kpf=PC_WEB; clientid=3; kpn=KUAISHOU_VISION',
        'Origin': 'https://www.kuaishou.com',
        'Referer': 'https://www.kuaishou.com/profile/3xtm9yqzwmy9rbw',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1 Edg/109.0.0.0',
        'accept': '*/*',
        # Already added when you pass json=
        # 'content-type': 'application/json',
    }

    json_data = {
        'operationName': 'visionProfilePhotoList',
        'variables': {
            'userId': '3xtm9yqzwmy9rbw',
            'pcursor': '',
            'page': 'profile',
        },
        'query': 'fragment photoContent on PhotoEntity {\n  id\n  duration\n  caption\n  originCaption\n  likeCount\n  viewCount\n  realLikeCount\n  coverUrl\n  photoUrl\n  photoH265Url\n  manifest\n  manifestH265\n  videoResource\n  coverUrls {\n    url\n    __typename\n  }\n  timestamp\n  expTag\n  animatedCoverUrl\n  distance\n  videoRatio\n  liked\n  stereoType\n  profileUserTopPhoto\n  musicBlocked\n  __typename\n}\n\nfragment feedContent on Feed {\n  type\n  author {\n    id\n    name\n    headerUrl\n    following\n    headerUrls {\n      url\n      __typename\n    }\n    __typename\n  }\n  photo {\n    ...photoContent\n    __typename\n  }\n  canAddComment\n  llsid\n  status\n  currentPcursor\n  tags {\n    type\n    name\n    __typename\n  }\n  __typename\n}\n\nquery visionProfilePhotoList($pcursor: String, $userId: String, $page: String, $webPageArea: String) {\n  visionProfilePhotoList(pcursor: $pcursor, userId: $userId, page: $page, webPageArea: $webPageArea) {\n    result\n    llsid\n    webPageArea\n    feeds {\n      ...feedContent\n      __typename\n    }\n    hostName\n    pcursor\n    __typename\n  }\n}\n',
    }

    response = requests.post('https://www.kuaishou.com/graphql', cookies=cookies, headers=headers, json=json_data)
    res_result = json.loads(response.text)
    final_result = res_result['data']['visionProfilePhotoList']['feeds'][0]['photo']
    print(final_result)


scan_kwaiweb()









# def scan_kwaiweb():
#     kwai_url = 'https://www.kuaishou.com/profile/3xtm9yqzwmy9rbw'
#     headers = {
#         'authority': 'www.kuaishou.com',
#         'sec-ch-ua': '"Chromium";v="94", "Microsoft Edge";v="94", ";Not A Brand";v="99"',
#         'accept': '*/*',
#         'content-type': 'application/json',
#         'sec-ch-ua-mobile': '?0',
#         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
#         'sec-ch-ua-platform': '"macOS"',
#         'origin': 'https://www.kuaishou.com',
#         'sec-fetch-site': 'same-origin',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-dest': 'empty',
#         'referer': kwai_url,
#         'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#         'cookie': 'did=web_1634cc0b9b2888c5c96ddf67acbe35bc; clientid=3; client_key=65890b29; ksCorpDeviceid=3bd4ac0f-e282-42fc-bef1-70b314a34541; _did=web_28211785477DDAD1; apdid=81cd3b94-204f-445f-a234-21d5bb53dfcc6845ddb761b0788405abc73fe2e4f079:1626614360:1; didv=1628567368000; kpf=PC_WEB; kpn=KUAISHOU_VISION; userId=1580353673; kuaishou.server.web_st=ChZrdWFpc2hvdS5zZXJ2ZXIud2ViLnN0EqABYviN6qSECO1opwyAZXNQeKi26gGNJpSOGq2iUhZqPuW2i8Yo3oSQ3tYePw3_hJIDHAUs_NgoVfbcy53fhsmuYlgdnIEgVUs_1Vov77JSc83Vy4x9HKSNc_SgO5gx0OS7NLwpGEqVWHBBHd-5yEO5a_Z5ezNCBlywluy3ew8l-TfQretcG4POnfphQMoN1pbaW300UyhcnO02oNODhFYNHxoSzFZBnBL4suA5hQVn0dPKLsMxIiBvXX9QguBEk40Kz1NkRzBI4fdxV3SJcagbLRVy_0TgsSgFMAE; kuaishou.server.web_ph=8807e29056f7dc3f55ca9c40c7f94c7a11c8',
#     }

    
#     data = '{"operationName":"visionProfilePhotoList","variables":{"userId":"3xtm9yqzwmy9rbw","pcursor":"","page":"profile",},"query":"fragmentphotoContentonPhotoEntity{\nid\nduration\ncaption\noriginCaption\nlikeCount\nviewCount\nrealLikeCount\ncoverUrl\nphotoUrl\nphotoH265Url\nmanifest\nmanifestH265\nvideoResource\ncoverUrls{\nurl\n__typename\n}\ntimestamp\nexpTag\nanimatedCoverUrl\ndistance\nvideoRatio\nliked\nstereoType\nprofileUserTopPhoto\nmusicBlocked\n__typename\n}\n\nfragmentfeedContentonFeed{\ntype\nauthor{\nid\nname\nheaderUrl\nfollowing\nheaderUrls{\nurl\n__typename\n}'

#     #######################################################userId可在http://www.kuaishou.com点开用户信息后，在地址栏中查询。
#     response = requests.post('https://www.kuaishou.com/graphql', headers=headers, data=data)
#     res_result = json.loads(response.text)
#     print(res_result)
#     #res_result['data']['visionProfilePhotoList']['userProfile']['fragmentphotoContentonPhotoEntity']['realLikeCount']
#     return final_result

# print(scan_kwaiweb())