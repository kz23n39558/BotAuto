import tweepy

# Добавьте ваши учетные данные Twitter API
consumer_key = 'ВАШ_КЛЮЧ_ПОТРЕБИТЕЛЯ'
consumer_secret = 'ВАШ_СЕКРЕТ_ПОТРЕБИТЕЛЯ'
access_token = 'ВАШ_ТОКЕН_ДОСТУПА'
access_token_secret = 'ВАШ_СЕКРЕТНЫЙ_ТОКЕН_ДОСТУПА'

# Аутентификация в Twitter
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Создание твита
tweet = "Привет, это Twitter бот, созданный с помощью Python! #TwitterBot #Python"

# Публикация твита
api.update_status(tweet)

print("Твит успешно опубликован!")
print("H4ck3r")
