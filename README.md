<p align="center">
  <img src="https://telegra.ph/file/d382d2fad1fdd2a4ccca4.png" alt="ROSE BUCKET Logo">
</p>
<h1 align="center">
  <b>Miss Rozy : A Permanent file Store BOT</b>
</h1>
<p>I am the first permanent file store with Automatic thumbnail extracting + Automatic Movie Posting feature. Its all extra feature's source code is written by The Sir LazyDeveloperr. </p>

### `Miss Rozy` : Give her a STAR ⭐️
I am hte first permanent file store with Automatic thumbnail extracting + Automatic Movie Posting feature. Its all extra feature's source code is written by The Sir [LazyDeveloperr](https://github.com/LazyDeveloperr).<b>So Copy pasters -> Must give credit to [LazyDeveloperr](https://github.com/LazyDeveloperr) else 🖕<b/>

## Commands:

- `/start` - start the bot
- `/clear_batch` - Clear User Batch Files
- `/status` - Show number of users in DB [Owner Only]
- `/broadcast` - Broadcast replied message to DB Users [Owner Only]
- `/ban_user` - [user_id] [ban_duration] [ban_reason] Ban Any User [Owner Only]
- `/unban_user` - [user_id] Unban Any User [Owner Only]
- `/banned_users` - Get All Banned Users [Owner Only]

### Features:
- In PM Just Forward or Send any file it will save on Database & give you the Access Link.
- In Channel Add Bot as Admin with Edit Rights. When you will send any file or media in Channel it will Edit the Broadcast Message with Saved Link Button.
- You can also Broadcast anythings via this Bot.
- You can also Do Force Sub to a Channel to allow access the Bot.
- Save Multiple Files in Same Link. (Batch)

## Configs:
- `LAZY_MODE` - Value should be `True` or `False` *(Optional)*
	- If `True` all messages will be forwarded to the Main Movie Channel as a Post.
- `LAZY_CHANNEL` - Only fill this field with single `Channel id` if you have enabled `LAZY_MODE` *(Required)*
	- If `True` all messages will be forwarder *As Copy*. If `False` all messages will be forwarder with Forward Tag.
- `LAZY_PIC` - BOT startup picture *(required)*
- `LP_CHANNEL_USRNM` - Give your main channel username `without @`  *(REQUIRED)*. This value will be used in post template 
	- The default value will be `LAZY_DEVELOPER`.
- `LPCH_ADMIN_USRMN` - Give your username `without @` *(Optional)*. This will be used in post template
	- If `True` all messages will be forwarder *As Copy*. If `False` all messages will be forwarder with Forward Tag.
- `API_ID` - Get this from [@TeleORG_Bot](https://t.me/TeleORG_Bot)
- `API_HASH` - Get this from [@TeleORG_Bot](https://t.me/TeleORG_Bot)
- `BOT_TOKEN` - Get this from [@BotFather](https://t.me/BotFather)
- `BOT_USERNAME` - You Bot Username. *(Without [@])*
- `DB_CHANNEL` - A Telegram Channel ID.
	- Make a Channel for Storing Files. We will use that as Database. Channel must be Private! Else you will be Copyright by [Telegram DMCA](https://t.me/dmcatelegram)!
- `BOT_OWNER` - Bot Owner UserID
	- Put your Telegram UserID for doing Broadcast.
- `DATABASE_URL` - MongoDB Database URI
	- This for Saving UserIDs. When you will Broadcast, bot will forward the Broadcast to DB Users.
- `UPDATES_CHANNEL` - Force Sub Channel ID *(Optional)*
	- ID of a Channel which you want to do Force Sub to use the bot. 
- `LOG_CHANNEL` - Logs Channel ID
	- This for some getting user info. If any new User added to DB, Bot will send Log to that Logs Channel. You can use same DB Channel ID.
- `FORWARD_AS_COPY` - Value should be `True` or `False` *(Optional)*
	- If `True` all messages will be forwarder *As Copy*. If `False` all messages will be forwarder with Forward Tag.
- `BROADCAST_AS_COPY` - Value should be `True` or `False` *(Optional)*
  	- Broadcast with Forward Tag or as Copy.*(Without Forward Tag)*
- `BANNED_USERS` - Banned unwanted members
         - Put all banned user IDs & Separate with space.
- `BANNED_CHAT_IDS` - All Banned Channel IDs *(Optional)*
	- Put all banned channel IDs & Separate with space.

### Video Tutorial:
[![YouTube](https://img.shields.io/badge/YouTube-Video%20Tutorial-red?logo=youtube)](https://youtu.be/Rtjyz3lEZwE)

### Deploy Now:
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/LazyDeveloperr/MissRozy)

### Support Group:
<a href="https://t.me/LazyDeveloperSupport"><img src="https://img.shields.io/badge/Telegram-Join%20Telegram%20Group-blue.svg?logo=telegram"></a>

### Follow on:
<p align="left">
<a href="https://github.com/LazyDeveloperr"><img src="https://img.shields.io/badge/GitHub-Follow%20on%20GitHub-inactive.svg?logo=github"></a>
</p>
<p align="left">
<a href="https://instagram.com/LazyDeveloperr"><img src="https://img.shields.io/badge/Instagram-Follow%20on%20Instagram-important.svg?logo=instagram"></a>
</p>

### Demo Bot:
<a href="https://telegram.me/MissRozy_BOT"><img src="https://img.shields.io/badge/Demo-Telegram%20Bot-blue.svg?logo=telegram"></a>

	
##🌟Credits
- 🔥Thank you [LazyDeveloper](https://github.com/LazyDeveloperr) for adding `LAZY_MODE` (an advance feature.)
- ⚡️Thank you [LazyDeveloper](https://github.com/LazyDeveloperr) for `FIXING ERRORS` and adding extra veriables.
- ❤️Thank you [LazyDeveloper](https://github.com/LazyDeveloperr) for for your contribution & also thank you for helping us in our journey


* **Language:** [Python3](https://www.python.org)
* **Library:** [Pyrogram](https://docs.pyrogram.org)
