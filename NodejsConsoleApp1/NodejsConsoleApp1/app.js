var Discord = require("discord.js");

var bot = new Discord.Client();
bot.on("ready", () =>
{
    console.log(bot.user)
});
bot.on("message", (message) =>
{
    if (message.contains == "!clear") {
        if (message.author.id == "132902891819237377") {
            message.channel.bulkDelete(message.channel.fetchMessages().findAll("author", bot.users.find("id", "132902891819237377")));
        }
    }
})

bot.login("")
