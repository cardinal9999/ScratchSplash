#ScratchSplash 
import requests, json
from urllib.parse import urlparse
API = "https://api.scratch.mit.edu/"
def scrape(url):
    return requests.get(url).json()
def get_userid(username):
    user_obj = API + "users/" + username
    user_obj = scrape(user_obj)
    return user_obj["id"]
def get_message_count(username):
    a = scrape(f"https://api.scratch.mit.edu/users/{username}/messages/count")
    return a["count"]
def get_user_country(username):
    user_obj = API + "users/" + username
    user_obj = scrape(user_obj)
    return user_obj["profile"]["country"]
def get_studio_name(studio_id):
    a = API + "studios/" + studio_id
    return scrape(a)["title"]
def get_studio_stats(studio_id):
    a = API + "studios/" + studio_id
    a = scrape(a)
    project = a["stats"]["projects"]
    follows = a["stats"]["followers"]
    if project == 100:
        project = "100+"
    if follows == 100:
        follows = "100+"
    return f"Projects: {project}. Followers: {follows}."
def download_thumbnail(projectid, outfile):
    response = requests.get(f"https://cdn2.scratch.mit.edu/get_image/project/{projectid}_9000x7200.png", stream=True)
    with open(outfile, 'wb') as out_file:
        for chunk in response:
            out_file.write(chunk)
    del response
def get_cloud_info(projectid=554192238):
    a = scrape(f"https://clouddata.scratch.mit.edu/logs?projectid={projectid}&limit=1000000&offset=0")
    return a
def display_user_data(user):
    user_obj = API + "users/" + user
    user_obj = scrape(user_obj)
    a = f"""User stats for {user}:
-> User ID: {user_obj["id"]}
-> Join Date: {user_obj["history"]["joined"]}
-> Country: {get_user_country(user)}
-> About me: {user_obj["profile"]["bio"]}
-> Messages: {get_message_count(user)}
Powered by ScratchSplash
"""
    return a
