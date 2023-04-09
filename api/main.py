import requests

invite_url = input("https://discord.gg/G79YRQ2tvX ")
invite_code = invite_url.split("/")[-1]

authorization_token = input("MTA5NDIzMTg3MzcwNzg0NzgyMw.GznjJJ.2XEd0b0buqpIHlbMqypXqjLbvETaqDgTpwhdQQ ")

api_invite_url = "https://discord.com/api/v9/invites/" + invite_code

resp = requests.post(api_invite_url, headers={"Authorization": authorization_token})

if resp.ok:
    print("Success!")
else:
    print("Error:" + resp.status_code, resp.text)
