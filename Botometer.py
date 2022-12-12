import botometer

rapidapi_key = ""
twitter_app_auth = {
    'consumer_key': '',
                    'consumer_secret': '',
                    'access_token': '',
                    'access_token_secret': '',
  }
bom = botometer.Botometer(wait_on_ratelimit=True,
                          rapidapi_key=rapidapi_key,
                          **twitter_app_auth)


twitter_handle_input = input("Enter a twitter handle to be checked: ")

# Check a single account by screen name
result = bom.check_account(twitter_handle_input)
cap = result['cap']
overall = cap['english']

if overall >= 2.5:
    print(twitter_handle_input + " is most likely a bot")
else:
    print(twitter_handle_input+" is most likely not a bot")
