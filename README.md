# Kodi Refresh Rate Switcher for Wayland
This little Kodi addon brings the ability for automatic refresh rate switching under Gnome Wayland.  
The addon uses GNOME Display Controller (gdctl) to automatically switch the display refresh rate, when a playback starts and stop.

## Requirements
- You need to be running GNOME on Wayland
- Your GNOME version needs to have the gdctl command, this should be the case for GNOME 48 and newer.

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
- **Switch to HDR mode for HDR content**: Enable this if your screen supports HDR and you want to enable HDR when playing HDR content (if your screen supports HDR, there should be an HDR toggle in your GNOME display settings). This toggle adds "--color-mode bt2100" to the gdctl command whenever HDR content is played.
- **Path to the gdctl binary**: This defaults to just "gdctl". If the gdctl command is not in a standard location or in your PATH variable, you can specify the full path here.
Example when using the flatpak version of Kodi: `/run/host/bin/gdctl` (Make sure to grant the host-os permissions to the flatpak, see below)
- **gdctl string**: If you're using multiple screens, gdctl needs some more parameters.  
Example: `--logical-monitor --monitor=HDMI-0 --right-of DP-0`  
More infos about it: https://man.archlinux.org/man/gdctl.1.en

## Kodi via Flatpak info
When using a flatpak version of Kodi, you need to do two things to make this addon work:
- set up the Path to the gdctl binary in the addon configuration
- Enable host-os (or greater) permissions for the tv.kodi.Kodi flatpak.
Enabling the permissions for the kodi flatpak can be done in a number of ways. The easiest is to use "Flatseal", a graphics application specifically designed for this. Install it via flathub or command line ( flatpak install com.github.tchx84.Flatseal ), launch it, select Kodi on the left, and toggle the 2nd item (filesystem=host-os) in the "Filesystem section".
Alternatively you can grant the permissions via command line: `flatpak --user override tv.kodi.Kodi --filesystem=host-os` if your Kodi flatpak was installed in user space (find out using the `flatpak list` command), or `sudo flatpak override tv.kodi.Kodi --filesystem=host-os` for a system-wide installed Kodi flatpak.