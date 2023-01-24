import json
# from database import data
from werkzeug.exceptions import NotFound, BadRequest

data = [
    {
        "id": 1,
        "title": "King Charles Cavalier",
        "url": "https://c.neevacdn.net/image/fetch/s--SP80dDyv--/https%3A//tse2.mm.bing.net/th%3Fid%3DOIP.QfYEp32_pdMnqTB6v2YcIQHaHa%26pid%3DApi?savepath=th",
        "description": "My favourite dog breed",
        "likes": 200
    },
    {
        "id": 2,
        "title": "Paradise",
        "url": "https://c.neevacdn.net/image/fetch/s--Nq5gi46v--/https%3A//2.bp.blogspot.com/-vvcPpVBImW4/T5K_DiXejcI/AAAAAAAAFDM/fjSZTWNfHB8/s1600/amazing%2Bwallpaper-6.jpg?savepath=amazing+wallpaper-6.jpg",
        "description": "My favourite place to be",
        "likes": 300
    }
]

def index(req):
    return [post for post in data], 200

def show(req, id):
    return find_by_id(id), 200

def create(req):
    try:
        newPost = req.get_json()
        print(newPost)
        title = newPost["title"]
        description = newPost["description"]
        url = newPost["url"]
        if len(newPost) != 3:
            raise Exception
        newPost["id"] = sorted([i['id'] for i in data])[-1] + 1
        newPost["likes"] = 0
        data.append(newPost)
        
        return newPost, 201
    except:
        raise BadRequest(f"Wrong property given")

def update(req, id):
    try:
        updateInfo = req.get_json()
        title = updateInfo["title"]
        description = updateInfo["description"]
        url = updateInfo["url"]
        if len(updateInfo) != 3:
            raise Exception
        
        post = find_by_id(id, True)
        if post == 0:
            updateInfo["id"] = id
            updateInfo["likes"] = 0
            data.append(updateInfo)
            return updateInfo, 201
        for key, val in updateInfo.items():
            post[key] = val
        return post, 200
    except:
        raise BadRequest(f"Wrong property given")

def destroy(req, id):
    post = find_by_id(id)
    data.remove(post)
    return [post for post in data], 204


def find_by_id(id, isUpdate=False):
        # print('is update')
        # return next(image for image in data if image['id'] == id)
    try:
        return next(image for image in data if image['id'] == id)
    except:
        if isUpdate == True:
            return 0
        raise NotFound(f"We don't have that image with id {id}!")