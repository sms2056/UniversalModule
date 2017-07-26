import importlib
import os

def enumerate_plugins(dirpath, class_):
    if os.path.isfile(dirpath):
        dirpath = os.path.dirname(dirpath)

    plugin_count = 0
    for fname in os.listdir(dirpath):
        if fname.endswith(".py") and not fname.startswith("__init__"):
            module_name, _ = os.path.splitext(fname)
            try:
                plugin_count = plugin_count + 1
                # importlib **plugins** ----------->Need to modify
                importlib.import_module("%s.%s" % ('plugins', module_name))
            except ImportError as e:
                print(e)

    subclasses = class_.__subclasses__()[:]
    loadplugin_count = len(subclasses)
    print('[#]All plugins : {total} \n[#]Successfully loaded : {load}'.format(total = plugin_count, load = loadplugin_count))
    if plugin_count > loadplugin_count:
        print('[!]It is possible that the parent class (\'CrawlerClass\') is not marked in the plugin.')
    return subclasses