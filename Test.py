import requests
import json
# set the apikey and limit
import Database

tenorApikey = "E43EM9PO00HC"

# search_term = "omori"


def getRandoTenorGif(searchTerm):
    r = requests.get(
        "https://g.tenor.com/v1/search?q=%s&key=%s&limit=%s" % (searchTerm, tenorApikey, 420))

    if r.status_code == 200:
        # load the GIFs using the urls for the smaller GIF sizes
        top_8gifs = json.loads(r.content)
        # json.dump(r.content, "Testerino.json")
        #json.dump(top_8gifs, open("Testerino.json", "w"), indent=True)
        return top_8gifs["results"][Database.randoMod(100)]["media"][0]["mediumgif"]["url"]
    else:
        return None
