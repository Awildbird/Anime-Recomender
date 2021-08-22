import requests
from Anime import Anime
from Tag import Tag
# Here we define our query as a multi-line string
query = '''
query ($name: String) { # Define which variables will be used in the query (id)
  MediaListCollection (userName: $name, type: ANIME) { # Insert our variables into the query arguments (id)
    lists{
        entries{
            media{
                title{   
                    english
                    romaji
                }
                tags{
                    name
                    rank
                }
                id
            }
        }
    }
  }
}
'''

# Define our query variables and values that will be used in the query request
variables = {
    'name': 'Awi1dbird'
}

url = 'https://graphql.anilist.co/'

response = requests.post(url, json={'query': query, 'variables': variables})
resp = response.json()
resp = resp["data"]["MediaListCollection"]["lists"][0]["entries"]

animes = []

for x in resp:
    animes.append(Anime(x["media"]["title"]["english"] , x["media"]["tags"] , x["media"]["id"]))

# print(animes[0])

tagList = {}
fulltags = []
for x in animes:
    fulltags.extend(x.getTags())
for x in fulltags:
    if x.getName() in tagList.keys():
        tagList.update({x.getName() : tagList.get(x.getName()) + x.getRank()})
    tagList.setdefault(x.getName(),x.getRank())

sortedTagList = sorted(tagList.items(),key=lambda x:x[1],reverse=True)
# print(sortedTagList)

i=0
searchList=[]
while i<4:
    searchList.append(sortedTagList.pop(0)[0])
    i+=1
    
print(searchList)

query2 = '''
query($tags:[String]){
  Page(page:1, perPage:15){
    media(tag_in: $tags sort:SCORE_DESC type:ANIME){
      title{
        english
        romaji
        }
      id
      meanScore
    }
  }
}
'''

variables2={
    'tags' : searchList
}

response2 = requests.post(url, json={'query': query2, 'variables': variables2})
resp2 = response2.json()
resp2 = resp2['data']['Page']['media']
print(resp2)

recAnime = []
for x in resp2:
    recAnime.append(Anime(x['title']['english'] , None , x['id']))

print(recAnime[0])