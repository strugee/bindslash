var bindslash = require('./index.js');

var fs = require('fs');

var program = require('commander');
var ini = require('ini');
var action;

program
	.version('1.0.0')
	.option('-c --config [path]', 'Configuration file to use [bindslash.ini]', 'bindslash.ini');

program
	.command('import')
	.description('import from the system into the bindslash project directory')
	.action(function() {
		action = 'import';
	});

program
	.command('export')
	.description('export from the bindslash project directory into the system')
	.action(function() {
		action = 'export';
	});

program.parse(process.argv);

if (typeof action === 'undefined') {
	process.exitCode = 1;
	program.help();
}

var config = ini.parse(fs.readFileSync('./bindslash.ini', 'utf-8'));
var plugins = [];

for (var plugin in config.bindslash) {
	var dir = config.bindslash[plugin].pluginDir || plugin;

	plugins.push({name: plugin, path: dir});
}

switch (action) {
case 'import':
	bindslash.importConfiguration(plugins);
	break;
case 'export':
	bindslash.exportConfiguration(plugins);
	break;
}
