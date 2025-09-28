# Kodi Refresh Rate Switcher for Wayland
This little Kodi addon brings the ability for automatic refresh rate switching under Gnome Wayland.  
The addon uses GNOME Display Controller (gdctl) to automatically switch the display refresh rate, when a playback starts and stop.


## How to use
1. Download the .zip from the release page and install it. (Follow this guide, if you don't know how to install an addon in Kodi: https://kodi.wiki/view/Archive:Install_add-ons_from_zip_files)
2. Open the addon settings (Configure) and enter your default settings (see Addon Configuration)
3. Disable "Adjust display refresh rate" in Kodi settings -> Player -> Videos 
4. Enjoy your videos 

## Addon Configuration
Needed infos can be obtained by running `gdctl show`
- **Screen Name**: The name of the screen running Kodi.  
Examples: `HDMI-0`, `DP-0` or `HDMI-1`
- **Primary Screen?**: Enable if Kodi is running on your primary screen. 
- **Default Screen Resolution**: Your curent screen resolution.  
Examples: `1920x1080` or `3840x2160`
- **Default Refresh Rate**: Your default refresh rate.  
Examples: `50`,`60` or `120`
- **gdctl string**: If you're using multiple screens, gdctl needs some more parameters.  
Example: `--logical-monitor --monitor=HDMI-0 --right-of DP-0`  
More infos about it: https://man.archlinux.org/man/gdctl.1.en  