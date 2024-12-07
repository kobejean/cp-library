import os
import requests
from datetime import datetime, timezone, timedelta
import json

class DropboxTokenManager:
    def __init__(self):
        self.app_key = os.environ['DROPBOX_APP_KEY']
        self.app_secret = os.environ['DROPBOX_APP_SECRET']
        self.refresh_token = os.environ['DROPBOX_REFRESH_TOKEN']
        self.token_file = '.dropbox_token.json'

    def load_cached_token(self):
        try:
            with open(self.token_file, 'r') as f:
                data = json.load(f)
                expiry = datetime.fromisoformat(data['expiry'])
                if expiry > datetime.now(timezone.utc):
                    return data['access_token']
        except (FileNotFoundError, json.JSONDecodeError, KeyError):
            pass
        return None

    def refresh_access_token(self):
        response = requests.post(
            'https://api.dropboxapi.com/oauth2/token',
            data={
                'grant_type': 'refresh_token',
                'refresh_token': self.refresh_token,
                'client_id': self.app_key,
                'client_secret': self.app_secret,
            }
        )
        
        if response.status_code != 200:
            raise Exception(f"Failed to refresh token: {response.text}")
            
        data = response.json()
        token_data = {
            'access_token': data['access_token'],
            'expiry': (datetime.now(timezone.utc) + 
                      timedelta(seconds=data['expires_in'])).isoformat()
        }
        
        with open(self.token_file, 'w') as f:
            json.dump(token_data, f)
            
        return data['access_token']

    def get_valid_token(self):
        token = self.load_cached_token()
        if not token:
            token = self.refresh_access_token()
        return token

if __name__ == '__main__':
    manager = DropboxTokenManager()
    print(f"DROPBOX_TOKEN={manager.get_valid_token()}")