# REM Sleep Calculator

Have you ever had morning grogginess? Feeling tired even though you had 8 hours of sleep?


Well amongst all other possiblities, one might be due to you waking up during your deep sleep. Knowledge of Rapid-Eye Movement (REM) cycles can prevent that, and all you need to do is to wake up at the right timings so that you can feel refreshed.

Hence, this bot is a sleep calculator that helps you to calculate the best timings to sleep and wake up, in accordance with the REM sleep cycle.

Link: https://t.me/sleepcalculatorbot

Information about REM sleep cycles: https://www.tuck.com/stages/

## Running Bot Locally
To run this project locally, you have to first create a bot with [BotFather](https://telegram.me/BotFather), and a new API key will be generated. Under 'main.py', uncomment line 77:
```
# key = open('apikey.txt', 'r')
```
and replace line 78: updater = Updater(os.environ['API_KEY']) with:
```
updater = Updater(key.read())
```
Open up the terminal, check that you are in the correct directory, and run:
```
python3 main.py
```

Now, open up the newly created bot on telegram and it should work locally. 
