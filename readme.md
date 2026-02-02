<img src="/branding/goh.png" style="filter:invert(100%);" alt="GoveeOverHTTP logo">

## A Govee BLE Web Wrapper

#### By Joe Jagger
#### Govee Library by Cyprus Snodgrass
##### https://pypi.org/project/govee-api-ble/

# !! WORK IN PROGRESS !!
31/01/2026: Development is probably going to be very slow. To test, I have to run a VSC SSH server on my raspberry pi, since I don't have a BT adapter, but since I don't have a power brick, it passes out every few minutes of not being used. 


I have a rather annoyingly common situation. I have a set of H613E Govee BLE lights. I love them dearly, except I despise their manufacturer. Govee's app is slow, mobile only with no pc build, clunky, bloated, and full to the absolute brim with advertisements for their other products. Also, they refuse to release an official BLE bridge. Hence:

### Why does this exist?
I want my lights to turn on and off. And I want to change their colour. But I don't want to go through my phone and through some stupid app that takes way too long to connect to do so.


### How do I use it?
GOH exposes itself on TCP Port 8585. From there, numerous HTTP-based endpoints can be used as either a standalone dashboard, or as an integrative toolset to build your own app upon. You probably know Vue / React. I don't. GO WILD!

I plan to create docker dists at some point, wherein you pass in the BLE Iface and it Just Works (TM).



I have attempted to keep this light due to the fact I'm going to be running it on a Raspberry PI 3B.

# API Documentation:
To begin with, Authentication can be set in the config.json file. If you set "authkey" to nil, then the server will not expect authentication, else, it will expect user auth in the header X-GOH-AUTH.

Furthermore, a toggle function is impossible (for now, unless I personally rewrite the library which I am tempted to do) since govee_api_ble provides no interface for pulling the power state.

## [Auth Not Yet Implemented!]

# Dashboard WebUI is @ /goh/dash/ 

---
### /goh/api/set_power
#### Method: GET
Simple endpoint allowing for the setting of the device on and off.

Usage: ``http://device:8585/goh/api/set_power?state=[true/false]``

To use this, pass true or false into the request arguments. No square brackets.


---

### /goh/api/set_colour
#### Method: GET
Simple endpoint allowing for the setting of the device's colour.

Usage: ``http://device:8585/goh/api/set_colour?rgb=RGB-VALUES-SEPERATED``

To use this, pass your rgb values seperated by dashes into the args.

Segments are supposed to be supported, but I don't have a light unit capable of running segmented lighting, hence it is untested.

## Planned: HTML Colour auto-conversion, 'smooth change' setting, etc.


---

### /goh/api/set_brightness
#### Method: GET
Simple endpoint allowing for the setting of the device's brightness.

Usage: ``http://device:8585/goh/api/set_brightness?percent=[0-100]``

To use this, pass your brightness amount as a 0-100 number.


---