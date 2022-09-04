from base64 import encode
from encodings import utf_8
import requests
import json

def scrap():
    json_data = {}
    params = {
                'page': 0,
                'title': "बालेन"
            }
    url = "https://bg.annapurnapost.com/api/search"
    try: 
        with open('annapurna_post.json', encoding='utf-8') as f:
            json_data = json.load(f)
            title = json_data.get('metadata').get('title')
            page = json_data.get('metadata').get('page') + 1
    except:
        json_data["metadata"]=params
        json_data["data"]=[]
        json.dump(json_data, open('annapurna_post.json', 'w'), indent=4)
        title = json_data.get('metadata').get('title')
        page = json_data.get('metadata').get('page') + 1
    temp_page = page
    while(page<=temp_page+2):
        try:
            params['page']=page
            params['title']=title
            json_each_page = {}
            res = requests.get(url, params=params)
            data = res.json()
            if (res.status_code == 200 ):
                json_data["metadata"]['page'] = params['page']
                json_each_page["current_page"] = params["page"]
                json_each_page["article"] = data["data"]["items"]
                json_each_page["title"] = params["title"]
                json_data["data"].append(json_each_page)
                json.dump(json_data, open('annapurna_post.json', 'w'), indent=4)
                print("Page:", page, 'success')
                page = page + 1
                params['page'] = page
        except Exception as e:
            print(e)

if __name__ == '__main__':
    scrap()
    print("Scraping complete")
