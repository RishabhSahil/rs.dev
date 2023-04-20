from bs4 import BeautifulSoup as bs
import requests
from googletrans import Translator, constants
#pip3 install googletrans==3.1.0a0
# import wikipedia

def Search_result(command):
    user_query=str(command)
    URL = "https://sarise.herokuapp.com/search?q=" + user_query

    headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.57'
    }
    page = requests.get(URL, headers=headers)
    soup = bs(page.content, 'html.parser')
    result = soup.find(class_='answer').get_text()
    return result

def search_query(command):
    user_query=str(command)
    if "who is rishabh" in user_query or "who was the founder of rishabh" in user_query or "rishabh kon h" in user_query:
        data={
            "about":"Rishabh is a founder of 'RISHABH' Search Engine All Social Media Account",
            "links":{
                "Instagram":"https://www.instagram.com/_rishabh_yaduvanshi_/",
                "Youtube":"https://www.youtube.com/channel/UCvNJtprg0qKG8qG9LaLPBew",
                "GitHub":"https://github.com/RishabhSahil",
                "Telegram":"https://t.me/rishabh_sahil",
                "RISHABH Search Engine App Download":"https://rishabh-app-store.herokuapp.com/details/rishabh-search-engine/",
                "RISHABHINSTA App Download":"https://rishabh-app-store.herokuapp.com/details/rishabh-insta/",
                "RISHABH":"http://rishabhsahil.github.io/",
                "RISHABHINSTA":"http://rishabhinsta.herokuapp.com/",
                "Spotify":"https://open.spotify.com/user/31esoiwso3lx6xbdngzzldeb5aw4?si=08eabc0b4f784b76",
                "Linkdin":"https://www.linkedin.com/in/rishabh-kumar-221647242/"
            }
        }
        # qu=list(data["link"].keys())
        # link=list(data["link"].values())
        # about="Rishabh is a founder of 'RISHABH' Search Engine All Social Media Account"
        # data={
        #     "about":about,
        #     "id":qu,
        #     "links":link 
        # }
  
        return data

    else:
        answer = Search_result(user_query) 
        data={
            "links":{
              answer:"https://rishabhsahil.github.io/search?q="+user_query  
            }
        }
        return data
    
# aa=search_query("rishabh kon hai?")
# # # # print(list(aa["link"].values())+)

# # # print(str(list(aa.values())))
# # for i in aa["links"]:
# #     print(aa["links"])
# #     # while ib:
# #     #     for j in aa["links"]:
# #     #         print(j)
# #     #         ib=False

# print(aa["links"].keys())

# data={
#     "links":{
#         "Instagram":"https://www.instagram.com/_rishabh_yaduvanshi_/",
#         "Youtube":"https://www.youtube.com/channel/UCvNJtprg0qKG8qG9LaLPBew",
#         "GitHub":"https://github.com/RishabhSahil",
#         "Telegram":"https://t.me/rishabh_sahil",
#         "apps1":"https://rishabh-app-store.herokuapp.com/details/rishabh-search-engine/",
#         "apps2":"https://rishabh-app-store.herokuapp.com/details/rishabh-insta/",
#         "demo1":"http://rishabhsahil.github.io/",
#         "demo2":"http://rishabhinsta.herokuapp.com/",
#         "spotify":"https://open.spotify.com/user/31esoiwso3lx6xbdngzzldeb5aw4?si=08eabc0b4f784b76"
#     }
# }

# for key, value in data['links'].items():
#     print(key,value)

# data = search_query("who is rishabh")

# aa=list(data["links"].keys()) 
# # ab=list(data["links"].values())

# for i in aa:
#     print(i)
#     for j in range(0,1):
#         print(data["links"][i])
#         # print(j)

class Search_result:
    def search(self,command):
        data = search_query(command=command)
        aa=list(data["links"].keys()) 
        return aa
            # for j in range(0,1):
            #     print(data["links"][i])
            #     # print(j)
# rishabh = Search_result()
# aa=rishabh.search(command="who is rishabh")
# # sahil = Employ("sahil","kumar",44500)
# print(aa)


def languages():
    LANGUAGES = {
        'af': 'afrikaans',
        'sq': 'albanian',
        'am': 'amharic',
        'ar': 'arabic',
        'hy': 'armenian',
        'az': 'azerbaijani',
        'eu': 'basque',
        'be': 'belarusian',
        'bn': 'bengali',
        'bs': 'bosnian',
        'bg': 'bulgarian',
        'ca': 'catalan',
        'ceb': 'cebuano',
        'ny': 'chichewa',
        'zh-cn': 'chinese (simplified)',
        'zh-tw': 'chinese (traditional)',
        'co': 'corsican',
        'hr': 'croatian',
        'cs': 'czech',
        'da': 'danish',
        'nl': 'dutch',
        'en': 'english',
        'eo': 'esperanto',
        'et': 'estonian',
        'tl': 'filipino',
        'fi': 'finnish',
        'fr': 'french',
        'fy': 'frisian',
        'gl': 'galician',
        'ka': 'georgian',
        'de': 'german',
        'el': 'greek',
        'gu': 'gujarati',
        'ht': 'haitian creole',
        'ha': 'hausa',
        'haw': 'hawaiian',
        'iw': 'hebrew',
        'he': 'hebrew',
        'hi': 'hindi',
        'hmn': 'hmong',
        'hu': 'hungarian',
        'is': 'icelandic',
        'ig': 'igbo',
        'id': 'indonesian',
        'ga': 'irish',
        'it': 'italian',
        'ja': 'japanese',
        'jw': 'javanese',
        'kn': 'kannada',
        'kk': 'kazakh',
        'km': 'khmer',
        'ko': 'korean',
        'ku': 'kurdish (kurmanji)',
        'ky': 'kyrgyz',
        'lo': 'lao',
        'la': 'latin',
        'lv': 'latvian',
        'lt': 'lithuanian',
        'lb': 'luxembourgish',
        'mk': 'macedonian',
        'mg': 'malagasy',
        'ms': 'malay',
        'ml': 'malayalam',
        'mt': 'maltese',
        'mi': 'maori',
        'mr': 'marathi',
        'mn': 'mongolian',
        'my': 'myanmar (burmese)',
        'ne': 'nepali',
        'no': 'norwegian',
        'or': 'odia',
        'ps': 'pashto',
        'fa': 'persian',
        'pl': 'polish',
        'pt': 'portuguese',
        'pa': 'punjabi',
        'ro': 'romanian',
        'ru': 'russian',
        'sm': 'samoan',
        'gd': 'scots gaelic',
        'sr': 'serbian',
        'st': 'sesotho',
        'sn': 'shona',
        'sd': 'sindhi',
        'si': 'sinhala',
        'sk': 'slovak',
        'sl': 'slovenian',
        'so': 'somali',
        'es': 'spanish',
        'su': 'sundanese',
        'sw': 'swahili',
        'sv': 'swedish',
        'tg': 'tajik',
        'ta': 'tamil',
        'te': 'telugu',
        'th': 'thai',
        'tr': 'turkish',
        'uk': 'ukrainian',
        'ur': 'urdu',
        'ug': 'uyghur',
        'uz': 'uzbek',
        'vi': 'vietnamese',
        'cy': 'welsh',
        'xh': 'xhosa',
        'yi': 'yiddish',
        'yo': 'yoruba',
        'zu': 'zulu',
    }
    return LANGUAGES
    # data = LANGUAGES
    # aa=list(data.keys()) 
    # # print(aa)

    # for i in aa:
    #     i
    #     # print(i)
    #     for j in range(0,1):
    #         j
    #         # print(i)
    #         # print(data[i])
    #         # print(j)

    #     # print(data)


def rishabh_translate(text,lang="en"):
    try:
        translater =Translator()
        result = translater.translate(text=text,dest=lang)
        return result
    except:
        pass


# # data = languages()
# # aa=list(data.keys()) 
# # # # print(aa)
# # # translator = Translator()
# translation = rishabh_translate(text="aap kon hai？",lang="en")
# # print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

# # for i in aa:
# #     i
# #     # print(i)
# #     for j in range(0,1):
# #         j
# #         # print(i)
# #         if i == translation.src:
# #             print(data[translation.src])
# #         if i == translation.dest:
# #             print(data[translation.dest])
# #         # print(data[i])
# #         # print(j)

# #     # print(data)

data = languages()
data2=list(data.keys())
# print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
# lang = translation.src
# for i in data2:
#     # print(i)
#     i
#     for j in range(0,1):
#         if i==lang.lower():
#             print(data[i])


    