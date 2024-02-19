# About This
As a prank for a friend who went overseas and lost internet access, I created a simple chatbot fueled by their past chat logs. They were known for their wit and humor, so I hoped this would make it feel like they were still participating in our conversations.

## What can I use this for?
Want to add some fun to your chat? Just add lines to the lines.txt file and the !chat comman will randomly pick one to use!

## How to use
* Create a Discord bot:

    * Visit the Discord Developer Portal: https://discordapp.com/developers/applications/
    * Follow the steps to create a new application and a bot user.
    * Important: Keep your bot token secure and don't share it with anyone.

* Create a .env file:

    * Create a file named .env in your project directory.
    * Add the line DISCORD_TOKEN="YourTokenHere" and replace YourTokenHere with your actual 
      bot token.

* Host your bot:

   * Choose where you'd like to host your bot: on a cloud service or locally.
   * Ensure your hosting environment can read the .env file for the bot token.

# Commands

* !Hello - The bot will respond to the author who issues the command.

* !knockknock - The bot will respond simply with I hate knock knock jokes

* !help - The bot will respond with a direct message. You can fill this out however you see   fit on line 39 	await message.author.send("Hello, I am sending you a direct message!")

* !chat - Will pick a random line from the lines.txt file in the chat.
