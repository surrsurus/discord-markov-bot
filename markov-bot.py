################################################################################
# IMPORTS
################################################################################

# Discord.py
import discord
client = discord.Client()

# Time
import time

# Markov
import markov

M = markov.Markov()

# Shelving
import shelve

################################################################################
# ADMIN
################################################################################

# ID of admin users who can tell the bot to save and load databases
ADMIN = ['your discord user id here!']

################################################################################
# LOGGING
################################################################################

# Disable logging to file by default
LOG_TO_FILE = True

DEBUG   = '[%]'
MESSAGE = '[*]'
WARN    = '[!]'
FATAL   = '[#]'
OTHER   = '[?]'

if LOG_TO_FILE:
    date = time.strftime('%m-%d-%H-%M-%S')
    logfile = open(date + '-markov.log', 'w')

def log(msg, tag=OTHER):
    print(tag + " " + msg)
    if LOG_TO_FILE:
        logfile.write(tag + " " + msg)

################################################################################
# READY
################################################################################

@client.event
async def on_ready():
    log(client.user.name + ' logged in at ' + date, DEBUG)

################################################################################
# SHELVING
################################################################################

def shelveSave():
    log('Saving DB...', DEBUG)
    file = shelve.open('markov-db', 'n')
    file['db'] = M.table
    file.close()

def shelveLoad():
    log('Loading DB...', DEBUG)
    file = shelve.open('markov-db', 'r')
    M.table = file['db']

def tableClear():
    log('Clearing table...', DEBUG)
    M.table = {}

################################################################################
# EVENT HANDLER
################################################################################

def markovLog(message):
    if len(message.content.split()) > 5:
        log('Recieving from #' + message.channel.name + ': ' + message.content, DEBUG)
        M.addToTable(message.content)

@client.event
async def on_message(message):
    if not message.author.bot:

        if str(message.author.id) in ADMIN:
            if message.content == '!m.save':
                shelveSave()
            elif message.content == '!m.load':
                shelveLoad()
            elif message.content == '!m.clear':
                tableClear()

        if client.user.mentioned_in(message):
            log('Processing request...', DEBUG)
            await client.send_message(message.channel, M.generate())
        else:
            markovLog(message)

################################################################################
# LOGIN
################################################################################

# Token to login
client.run('Secret token here!')
