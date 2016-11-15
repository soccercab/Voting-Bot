var Discord = require("discord.js");

var bot = new Discord.Client();
bot.on("ready", () =>
{
    console.log(bot.user)
});
function patGotGrounded(message) {
    /* 
    This code currently needs to tested.
    I have no idea if this code will actually work so we gotta do that
    */
    if (message.contains == "!clear") {
        if (message.author.id == "132902891819237377") {
            message.channel.bulkDelete(message.channel.fetchMessages().findAll("author", bot.users.find("id", "132902891819237377")));
        }
    }
}
function chatSensor (message) {
    //FINISH THIS AT A LATER TIME OK XD
}
bot.on("message", (message) =>
{
    patGotGrounded(message);
})

bot.login("") // ADD THIS LOCALLY
