# Webhook

## Project Title
Practice with Webhooks in Flask and python-telegram-bot

## Project Description
This project is a simple demonstration of how to use webhooks in Flask and the python-telegram-bot library. It showcases the integration of a Flask web application with the Telegram Bot API using webhooks.

## Installation

### Prerequisites
- Python 3.6 or higher
- pip (Python package manager)

### Installation Steps

1. Clone this repository to your local machine:

   ```shell
   git clone <repository_url>
   cd practice-webhooks-flask-telegram-bot
   ```

2. Create a virtual environment (optional but recommended):

   ```shell
   python -m venv venv
   ```

3. Activate the virtual environment:

   - **Windows**:

     ```shell
     venv\Scripts\activate
     ```

   - **macOS and Linux**:

     ```shell
     source venv/bin/activate
     ```

4. Install the required Python packages:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. Create a Telegram bot on Telegram by talking to the [BotFather](https://core.telegram.org/bots#botfather) and obtain your bot token.

2. Create a `.env` file in the project directory with the following content, replacing `<YOUR_BOT_TOKEN>` with your actual bot token:

   ```env
   TELEGRAM_BOT_TOKEN=<YOUR_BOT_TOKEN>
   ```

3. Run the Flask web application:

   ```shell
   python app.py
   ```

4. Set up a publicly accessible server or use a service like ngrok to create a public URL for your local server. Update the Telegram bot's webhook URL to point to this public URL, followed by `/webhook`.

5. Once the webhook is set up and working, you can interact with your Telegram bot by sending messages to it.

## Project Structure

The project structure is as follows:

- `app.py`: The main Flask application file.
- `bot.py`: Contains the Telegram bot setup and webhook handling.
- `.env`: Environment variable file for storing your Telegram bot token.
- `requirements.txt`: Lists the required Python packages for this project.
