#!/usr/bin/python3

import sys
import os
import importlib

sys.path.append(sys.argv[1])

projectDir = os.getcwd()

for pluginName in ['TestPlugin', 'TestPlugin2']:
    plugin = importlib.import_module(pluginName)
    pluginDataDir = os.path.join(projectDir, pluginName)
    os.makedirs(os.path.join(projectDir, pluginName), exist_ok=True)
    plugin.importConfiguration(os.path.join(projectDir, pluginName))
