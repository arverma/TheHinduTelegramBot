# Python Script To Download TheHindu Newspaper
##What it does?
* Download TheHindu newspaper form `https://www.newspaperpdf.online/download-the-hindu-adfree.php`
* Deletes the previously downloaded newspaper.
* Sends the newspaper to the subscribed users of a telegram bot.

## Requirements:
* Install these libraries:
    * BeautifulSoup
    * requests
    * glob

## To run
* Clone the repo
* `cd PythonScriptToDownloadTheHindu`
* Subscribe to `@BotFather` on telegram.
* Create a bot and get your bot token.
* Paste the bot token in `bot.py`
* Subscibe to `@chatid_echo_bot` and know your `chaid`
* Paste the `chatid` in chat_id.csv e.g., `chatid1,chatid2,chatid3,etc.`
* `python3 main.py`

```
aman@Apples-MacBook-Pro-2 theHindu % python3 main.py                                   
aman@Apples-MacBook-Pro-2 theHindu % ls
README.md		TheHindu_22_0.pdf	download_file.py	test.py			venv
TheHindu_1_Jul_0.pdf	__pycache__		main.py			utils.py
```

### Tips
* Create a `cron` job in your pc to execute the script everyday at 7am.