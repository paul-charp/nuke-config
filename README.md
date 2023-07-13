# nuke-config
Simple config to add Nuke Plugins like "packages"

## Setup
Add the `nuke` directory to the `NUKE_PLUGIN_PATH` environment variable.

## How it works
Edit the `init.py` to set the plugin paths.
To loop through subdirectories add a `.nuke` file and set the `SCAN_SUBDIR` variable to `True`.


