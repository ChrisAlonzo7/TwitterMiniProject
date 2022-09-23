import botometer

rapidapi_key = "edbd4ef82cmsh451f77e71d3ce33p16e014jsn78dd"
twitter_app_auth = {
    'consumer_key': '7JR2f1PlJoXlAdQTrunkfXs5J',
                    'consumer_secret': '5vhD76MR6JPa2DUU5r4DKePoJVN4LhnLGc5BMA9ojiVXWGOoED',
                    'access_token': '1569770373687967744-wyHHAosi5GbOJMk3ry5JMHZh6hYQJe',
                    'access_token_secret': 'LtbE9OKi7oNgcBHfeBQRUJWy6djj7kndaCq8LSc0uU8IR',
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