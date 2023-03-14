import xboxlivepy,requests


def get_auth(email,pass):
    xbox_auth  = xboxlivepy.XboxLiveAuth (email ,  password)
    return xbox_auth

def pull_code(email, passw):
    headers = {'Authorization': get_auth(email, passw)}
    code = requests.post('https://profile.gamepass.com/v2/offers/47D97C390AAE4D2CA336D2F7C13BA074', headers=headers, timeout=None)
    return code.json()['resource']

with open('accounts.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        l = line.strip().split('|')
        email = l[0]    
        password = l[1]
        pull_code(email, password)
    
