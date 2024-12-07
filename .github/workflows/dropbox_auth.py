import os
import requests
from datetime import datetime, timezone, timedelta
import json

class DropboxTokenManager:
    def __init__(self):
        self.app_key = os.environ['DROPBOX_APP_KEY']
        self.app_secret = os.environ['DROPBOX_APP_SECRET']
        self.refresh_token = os.environ['DROPBOX_REFRESH_TOKEN']

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
        return self.refresh_access_token()

if __name__ == '__main__':
    manager = DropboxTokenManager()
    print(f"DROPBOX_TOKEN={manager.get_valid_token()}")