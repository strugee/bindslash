'use strict';

var mkdirp = require('mkdirp');

function importConfiguration(plugins) {
	plugins.forEach(function(pluginConfig) {
		var path = pluginConfig.path;
		var plugin = require('bindslash-' + pluginConfig.name);

		plugin.importConfiguration(path);
	});	
}

function exportConfiguration(plugins) {
	plugins.forEach(function(pluginConfig) {
		var path = pluginConfig.path;
		var plugin = require('bindslash-' + pluginConfig.name);

		mkdirp(path, function(err) {
			if (err) throw err;

			plugin.exportConfiguration(path);
		});
	});
}

module.exports.importConfiguration = importConfiguration;
module.exports.exportConfiguration = exportConfiguration;
