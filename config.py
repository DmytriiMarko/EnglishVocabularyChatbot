import configparser

config = configparser.ConfigParser()
config.read('cfg.ini')

# Database configuration
database_config = config['Database']

dbconfig = {
    'host': database_config.get('host'),
    'user': database_config.get('user'),
    'password': database_config.get('password'),
    'database': database_config.get('database')
}

# Telegram bot token
telegram_config = config['Telegram']
token = config['Telegram']['token']

utilities_config = config['Utilities']

# Microsoft Translate API key
translate_key = utilities_config.get('translate_key')

# Monobank API key and jar link
mono_token = utilities_config.get('mono_token')
mono_jar = utilities_config.get('mono_jar')

# Telegraph API key
telegraph_api = utilities_config.get('telegraph_api')
