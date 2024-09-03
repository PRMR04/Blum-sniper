from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import threading
import time

# List of bot tokens, each corresponding to a different Telegram account
BOT_TOKENS = [
    '7436158848:AAG6GbfQuehIH2J2vUVhaQgWEaph_1f_V0A'
    # Add more tokens as needed
]

# Function to start the game loop and repeat until all games are finished
def start_game_loop(update: Update, context: CallbackContext) -> None:
    max_games = 5  # Define the total number of games to be played
    current_game = 0
    
    while current_game < max_games:
        # Start a new game
        start_game(update, context)
        current_game += 1
        
        # Brief pause before starting the next game
        time.sleep(2)  # Adjust based on game restart timing

    # Notify that all games are finished
    context.bot.send_message(chat_id=update.effective_chat.id, text="All games finished!")

# Function to simulate starting and playing one game
def start_game(update: Update, context: CallbackContext) -> None:
    # Simulate pressing the play button to start the game
    context.bot.send_message(chat_id=update.effective_chat.id, text="Play")
    time.sleep(1)  # Short delay to simulate interaction timing

    # Simulate playing the game by tapping green snowflakes
    tap_green_snowflakes(update, context)

# Function to simulate tapping green snowflakes until the timer expires
def tap_green_snowflakes(update: Update, context: CallbackContext) -> None:
    start_time = time.time()  # Record the current time
    game_duration = 60  # Assuming the game timer runs for 60 seconds
    
    while time.time() - start_time < game_duration:
        # Simulate tapping a green snowflake
        context.bot.send_message(chat_id=update.effective_chat.id, text="Tap green snowflake")
        
        # Short delay to simulate the game's response time
        time.sleep(0.5)  # Adjust based on the game's response speed

    # Notify that the current game round is over
    context.bot.send_message(chat_id=update.effective_chat.id, text="Game Over - Timer Expired")

# Function to start a bot instance for a given token
def start_bot(token: str) -> None:
    # Set up the Updater
    updater = Updater(token)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the command that starts the game loop
    dispatcher.add_handler(CommandHandler("startgames", start_game_loop))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop it
    updater.idle()

# Main function to manage and run all bot instances
def main() -> None:
    threads = []
    
    # Create and start a new thread for each bot
    for token in BOT_TOKENS:
        thread = threading.Thread(target=start_bot, args=(token,))
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()