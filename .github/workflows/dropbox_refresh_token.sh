#!/bin/bash

APP_KEY="your_app_key"
APP_SECRET="your_app_secret"

echo "Opening browser for authorization..."
open "https://www.dropbox.com/oauth2/authorize?client_id=$APP_KEY&token_access_type=offline&response_type=code"

echo "Enter the authorization code:"
read CODE

echo "Exchanging code for refresh token..."
curl https://api.dropboxapi.com/oauth2/token \
  -d grant_type=authorization_code \
  -d code=$CODE \
  -d client_id=$APP_KEY \
  -d client_secret=$APP_SECRET