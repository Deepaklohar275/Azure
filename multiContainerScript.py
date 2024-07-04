import requests
import json
# url = 'https://hub.docker.com/repository/docker/deepaklohar/snyk/tags
# Function to fetch tags from Docker Hub
def fetch_docker_tags(url):
    tags = []
    while url:
        response = requests.get(url)
        data = response.json()
        tags.extend(data['results'])
        url = data.get('next')
    return tags

# Function to process tags and save to a JSON file
def process_tags(tags):
    processed_tags = {}
    for tag in tags:
        tag_name = tag['name']
        for image in tag['images']:
            digest = image['digest']
            if digest not in processed_tags:
                processed_tags[digest] = []
            processed_tags[digest].append(tag_name)
    return processed_tags

# Fetch and process tags
url = "https://hub.docker.com/v2/repositories/deepaklohar/snyk/tags"
tags = fetch_docker_tags(url)
processed_tags = process_tags(tags)

# Save to JSON file
with open('openjdk-tags.json', 'w') as f:
    json.dump(processed_tags, f, indent=2)

print("Tags have been processed and saved to openjdk-tags.json")
