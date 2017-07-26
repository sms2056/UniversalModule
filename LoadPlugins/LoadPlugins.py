import os
WorkPath = os.getcwd()
PluginsPath = os.path.join(WorkPath, 'plugins')

from Plugin import enumerate_plugins
from plugins.BaseClass import BaseClass
#load plugins
subclasses = enumerate_plugins(PluginsPath, BaseClass)
#call plugins
for sub in subclasses:
    sub().on_call()
