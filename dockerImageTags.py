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
    'Authorization': 'Bearer no need to enter the PAT token'  # Replace <your_docker_hub_token> with your actual token
}

tags =imagetag(url)
print(tags)


    








    









