# discord-markov-bot
A Discord bot in Python 3 that forms Markov Chains from what it reads

# How Do I Use This Bot?

1) Create a new bot user for it in your Discord account
2) Invite it to the server of your choosing (get permission first, or make sure it's your own server)
3) Run the bot from the commandline. (Note, you'll need the python discord API too, and put your token at the bottom of the markov-bot.py file)

# Bot Commands
@ mention the bot to get a markov response, otherwise make sure to set yourself as an admin, and you can use the following commands:

- `!m.save` - Save what the bot's read from the channels it's in to `markov-db`
- `!m.load` - Load the `markov-db` file into the bot
- `!m.clear` - Clear everything the bot's read

## Acknowledgements
Inspired by [this](https://gist.githubusercontent.com/agiliq/131679/raw/33ff96bbb536b71e989276d9f7a728037b124048/gistfile1.py_)
