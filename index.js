'use strict';

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

		plugin.exportConfiguration(path);
	});
}

module.exports.importConfiguration = importConfiguration;
module.exports.exportConfiguration = exportConfiguration;
