# PiHole-Panel 2.6
Connects to one or multiple Pi-hole hosts and reports statistics in real-time and also allows you to use  
it as a control panel to control your Pi-hole hosts independently. 

This program will run on your Pi or desktop computer that is running Raspian, Pop_OS!, Ubuntu, Debian etc...

Includes compliant desktop entry. (Icon belongs to https://github.com/pi-hole)

![](https://raw.githubusercontent.com/daleosm/PiHole-Panel/master/pihole-panel.png)

## Install/Update
```
1. You must use a password with your Pi-hole otherwise the API becomes read-only.
2. Download pihole-panel-latest.deb from above.
3. Open Terminal
```
```
cd ~/Downloads
sudo dpkg -i pihole-panel-latest.deb
```

**Alternatively,** Pop_OS!, Ubuntu and more [experimental](https://raspberrypi.stackexchange.com/questions/44622/how-to-add-ppa-entries-manually-on-raspberry-pi) Raspbian users can use the Ubuntu PPA:
```
sudo add-apt-repository ppa:daleosm/pihole-panel
sudo apt update
sudo apt install pihole-panel
```

## Troubleshoot
```
rm ~/.config/pihole_panel_configs.xml
```

## Uninstall
```
sudo apt remove pihole-panel
```

## Changelog
PiHole-Panel 2.6
-  Fixed alignment for settings items with some themes.

PiHole-Panel 2.5
- Settings window is now centered.

PiHole-Panel 2.3
- Settings window is now a fixed size.
- Code and performance improvements.

PiHole-Panel 2.2
- Fix for default Pi-hole host that is not using standard url.
- Cosmetic fixes to GUI elements.

PiHole-Panel 2.1
- Complete and stable multi-host support.

PiHole-Panel 2.0
- Changes to API now require 3 second update interval.

PiHole-Panel 1.9
- Now compatible with latest API.
- Temporary fix for Gravity Last Updated.

PiHole-Panel 1.8
- Now works with package manager.
- Fix for handling of when Pi-hole host is down.
- Fix for update notification.
