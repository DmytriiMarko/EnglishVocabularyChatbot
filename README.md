# English Vocabulary Chatbot Installation Guide

This guide will help you set up and run the English Vocabulary Chatbot on your local machine.

## Prerequisites

Make sure you have the following components installed:

- Python 3.8 or higher
- MySQL server
- Git (optional, for cloning the repository)

## Step 1: Cloning the Repository

Clone this repository to your machine using the following Git command:

```
git clone https://github.com/DmytriiMarko/EnglishVocabularyChatbot.git
```

Or download the ZIP archive of this repository and extract it on your machine.

## Step 2: Setting Up the Database

Create a MySQL database. Edit the configuration file `cfg.ini` to set up the database connection. Specify the connection details that correspond to your MySQL server.

```bash
[Database]
host = DB_HOST
user = DB_USER
password = DB_PASSWORD
database = DB_NAME
```

## Step 3: API Keys Configuration

Open the `cfg.ini` file and configure the necessary API keys for your project.
```bash
[Telegram]
token = YOUR_BOT_TOKEN

[Utilities]
translate_key = MICROSOFT_TRANSLATE_API_KEY
mono_token = MONOBANK_TOKEN
mono_jar = MONOBANK_JAR
telegraph_api = TELEGRAPH_API
```

Make sure you have entered valid API keys. Check the documentation of the services you are using to obtain the required API keys.

## Step 4: Installing Dependencies

Install the required dependencies using `pip`:

```
pip install -r requirements.txt
```

## Step 5: Running the Bot

Run the bot using the command:

```
python run.py
```

Your bot should be accessible on your messenger. Start learning English with the English Vocabulary Chatbot!

## Author

- [Marko Dmytrii](https://github.com/DmytriiMarko)


Please note that you should provide your own database details and project author information in this guide. Also, ensure you have all necessary permissions and keys for your bot to work correctly.
