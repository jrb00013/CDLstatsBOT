const { Client, GatewayIntentBits } = require('discord.js');
const fs = require('fs');
const path = require('path');
const config = require('./config.json');
const apiHandler = require('./api_handler.js');

const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.MessageContent] });

client.once('ready', () => {
    console.log(`${client.user.tag} has logged in.`);
});

client.on('messageCreate', async (message) => {
    if (message.content.startsWith("!rankedstats")) {
        const player = message.content.split(" ")[1];
        const stats = await apiHandler.getRankedStats(player);
        message.channel.send(`Ranked Stats for ${player}: ${stats}`);
    }
});

// Log in to Discord
client.login(config.DISCORD_TOKEN);
