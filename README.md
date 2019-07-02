# PiHole-Panel 2.3
Connects to one or multiple Pi-hole hosts and reports statistics in real-time and also allows you to use  
it as a control panel to control your Pi-hole hosts independently. 

This program will run on your Pi or desktop computer that is running Raspian, Ubuntu, Debian etc...

Includes compliant desktop entry. (Icon belongs to https://github.com/pi-hole)

![](https://raw.githubusercontent.com/daleosm/PiHole-Panel/master/main_window.png)
![](https://raw.githubusercontent.com/daleosm/PiHole-Panel/master/setup.png)
![](https://raw.githubusercontent.com/daleosm/PiHole-Panel/master/setup_done.png)

## Install/Update
```
Download PiHole-Panel-latest.deb from above
```
```
cd ~/Downloads
sudo dpkg -i PiHole-Panel-latest.deb
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
