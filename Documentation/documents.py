help_command = ' \n**Anilist**\n```$next <anime name>\n$anime <anime name>\n$manga <manga name>``` \n **League of legends**\n```$free week\n$mastery <server> <champion> <summoner>\n$sumDivision <region> <summoner>\n$current game <region> <summoner> ```\n**Weather**```$weather\n$weather save <city>\n$weather <city>```\n **Tags**```$tag save <name> <url>\n&<tag>\n$tag list```\n**Math** \n```$der <function>```\n**Extra** ``` $choose <option>, <option>, ...```\n**Words**\n```$ban word <word>\n$unban word <word>\n$see ban permissions\n$delete ban permissions\n$allow ban\n$banned words``` Type *$help <command>* for more information (or $help <command>, <command>, ...)'

help_a= {'next':'Shows the time remaining until next episode.\n Example:```$next Shokugeki no Souma```',
		'anime':'Searches the anime in anilist and post the url to it. \n Example:```$anime Shakugan no Shana```',
		'manga': 'Seaches the manga in anilist and post the url to it. \n Example: ```$manga Bleach```',
		'free week':'Shows the current free-week champions',
		'mastery': 'Shows the mastery leves with that champion of the selected summoner. \n Example:```$mastery lan nami Aztic```'	,
		'sumDivision': 'Shows the current division and tier of the summoner. \n Example:```$sumDivision lan Aztic```',
		'current game': 'Shows the current tier and division of all summoners that are playing in selected summoner game. \n Example:```$current game lan Aztic```',
		'weather': 'Shows the current weather of you saved city. You need to use -$weather save- first. You can see the current weather of any city without saving just typing ```$weather <your city>```',
		'weather save': 'saves any city to consult weather',
		'tag save': 'saves the images as a tag to use it lates',
		'&':'shows the tag',
		'tag list': 'shows all saved tags',
		'choose': 'choose one of the given options',
		'der': 'Shows the derivate of that function (WIP, version 0.0.2)',
		'ban word':'Ban that word from the server. Any message with that word will be deleted',
		'see ban permissions':'See the roles that can ban words',
		'delete ban permission': 'Remove the permissions of that role to ban words',
		'allow ban':'allow a role to ban words',
		'unban word':'Unban the selected word',
		'banned words':'see the banned words',
		'tyranny':'Makes der führer will!',}