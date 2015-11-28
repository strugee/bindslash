#!/usr/bin/python3

import sys
import os
import importlib
import configparser

config = configparser.ConfigParser()
config.read('bindslash.ini')
assert 'bindslash' in config.sections()

projectDir = os.getcwd()

sys.path.append(os.path.join(projectDir, config['bindslash']['pluginPath']))

for pluginName in [name for name in config.sections() if name != 'bindslash']:
    plugin = importlib.import_module(pluginName)
    pluginDataDir = os.path.join(projectDir, pluginName)
    os.makedirs(os.path.join(projectDir, pluginName), exist_ok=True)
    plugin.importConfiguration(os.path.join(projectDir, pluginName))
