import nuke
import os

###############################################################################
# Settings
###############################################################################

# Path of directories containing Nuke plugins in subdirectories
NUKE_PLUGINS_ROOT_PATHS = [
    "./",
]

# Manually add Nuke plugins. Those path will be directly appended to the NUKE_PLUGIN_PATH
NUKE_PLUGINS_PATHS = [
    
]

# Scan for .nuke file for subfolder.
SCAN_SUBDIR = True


###############################################################################
# Plugin Search
###############################################################################

# Loop through subdirectories recursively that contain a .nuke file
def child_plugins(root):
    if not os.path.isdir(root):
        return
    directory_content = os.listdir(root)
    if ".nuke" in directory_content:
        yield root
    else:
        return
    for content in directory_content:
        if content.startswith("_"):
            continue
        plugin_path = os.path.join(root, content)
        if os.path.isdir(plugin_path):
            for child_path in child_plugins(plugin_path):
                yield child_path
                
# Find plugins
def find_plugins(roots_paths, use_dot_nuke = True):
    plugins_path = []

    for root in NUKE_PLUGINS_ROOT_PATHS:
        os.path.normpath(root)
        os.path.abspath(root)

        if use_dot_nuke:
            plugins_path.extend(list(child_plugins(root)))
                                
        else:
            plugins_path.extend(
                [f.path for f in os.scandir(root) if f.is_dir()]
                )
    
    # Remove duplicates    
    plugins_path = list(dict.fromkeys(plugins_path))
    return plugins_path
    
if __name__ == "__main__":
    plugins = find_plugins(NUKE_PLUGINS_ROOT_PATHS, SCAN_SUBDIR)

    # Appends manual plugin, to scanned plugins
    plugins.extend(NUKE_PLUGINS_PATHS)

    # Add plugins to nuke
    for plugin in plugins:   
        nuke.pluginAddPath(plugin)