import urllib.request as req, json

pd2FilterListUrl = "https://raw.githubusercontent.com/Project-Diablo-2/LootFilters/main/filters.json"
masterFilterList = {}

with req.urlopen(pd2FilterListUrl) as url:
    authorsData = json.load(url)

if authorsData:
    for d in authorsData:
        authorName  = d["author"]
        displayName = d["name"]
        authorUrl   = d["url"]

        masterFilterList[authorName] = {}
        
        masterFilterList[authorName]["info"] = d
        masterFilterList[authorName]["filters"] = []

        with req.urlopen(authorUrl) as url:
            filterData = json.load(url)
        
        if filterData:
            for f in filterData:
                if ".filter" in f["name"]:
                    masterFilterList[authorName]["filters"].append({
                        "name": f["name"],
                        "url": f["url"],
                        "download_url": f["download_url"]
                    })
    
    masterFilterList.sort()
    jsonData = json.dumps(masterFilterList, indent=4)
    with open("pd2_filters.json", "w") as j:
        j.write(jsonData)
