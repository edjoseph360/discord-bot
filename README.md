# discord-bot
This project was to create a bot to use in discord servers. I made it for personal use in my own server with my friends. 

The bots name is jeff. To use the bot you must get a token from the discord developer portal and place it in the bot.py file on line 128 in the parenthesis for the client.run function. The bot must then be added to your server through the discord developer portal. 

To use the reddit cog. You will need to get access to the reddit api. To do this apply at https://www.reddit.com/prefs/apps. Then in the reddit.py file in the cogs folder place your information between lines 6-10. 

Once these steps are done, your bot is ready to run through the command line or a server. 

The command to get the bot to acivate is simply 'jeff ' with a space at the end. This is followed by a command and any arguements that command may take. For example, 'jeff reddit news' where 'reddit' is the command and 'news' is the arguement. 

commands included in the bot are:
coinflip - returns heads or tails
8ball- returns a response typical to an 8 ball
reddit- returns a random post from the subreddit arguement given to it
clear- deletes the last few messages. default is 5. can take an arguement.  
