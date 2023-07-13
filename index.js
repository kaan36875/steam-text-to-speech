const SteamUser = require('steam-user');
const client = new SteamUser();
const config = require('./config.json')
const { spawn } = require('child_process');

const logOnOptions = {
	accountName: config.username,
	password: config.password
};

const changeCommand = ".speaker "
const speakers = ["Filiz","Zeina","Matthew","Mizuki","Tatyana","Bianca","Aditi"]
let speaker = "Filiz"

client.logOn(logOnOptions);

client.on('loggedOn', () => {
	console.log('Successfully logged on.');
	client.setPersona(SteamUser.EPersonaState.Online);
});


client.on("friendMessage", function(steamID, message) {
	if (message == ".commands") {
		client.chatMessage(steamID, "'.speaker (isim)' - Changes the speaker.\n'.speakers' - Shows the speaker list.");
	} else if (message == ".speakers") {
		client.chatMessage(steamID, "Filiz - Turkish (F)\nZeina - Arab (F)\nMatthew - American (M)\nMizuki - Japanese (F)\nBianca - Italian (F)\nTatyana - Russian (F)}\nAditi - Indian (F)")
	} else if (message.startsWith(changeCommand)) {
		newSpeaker = message.substring(changeCommand.length);
		if(speakers.includes(newSpeaker)) {
			speaker = newSpeaker
			client.chatMessage(steamID, "Speaker changed to: " + speaker);
		} else {
			client.chatMessage(steamID, "Speaker not found. For speaker list: '.speakers'");
		}
	} else {
		const pythonProcess = spawn('python', ['text2speech.py', message, speaker]);
	}
});