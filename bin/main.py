#!/usr/bin/python3

# Copyright 2015 Alex Jordan <alex@strugee.net>.
# 
# This file is part of bindslash.
# 
# bindslash is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
# 
# bindslash is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Affero General Public License for more details.
# 
# You should have received a copy of the GNU Affero General Public
# License along with bindslash. If not, see
# <http://www.gnu.org/licenses/>.

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
