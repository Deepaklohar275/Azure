import yaml
import requests


def imagetag (url):
    tags = []
    r= requests.get(url, headers=headers)
    response_dict = r.json()
    image_dicts = response_dict['results']
    image_dict= image_dicts[0]
    for image_dict in image_dicts:
        #print(image_dict['name'])
        tags.append(image_dict['name'])
    return tags


url = "https://hub.docker.com/v2/repositories/deepaklohar/snyk/tags"
headers = {
    'Accept': 'application/json',  # Specify that you want a JSON response
}
tags =imagetag(url)
#save to YAML as a Data Variable
data = {'imageTags': tags}
print(data)
print(tags)


with open('image_tags.yaml', 'w') as file:
    yaml.dump(data, file)
    
    

    








    









