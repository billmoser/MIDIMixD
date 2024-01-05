# MIDIMixD - an Ableton Live Remote Script for the Akai MIDIMIX

## Overview

The primary use case for this is to enable device parameter editing while using the MIDIMIX in your mixing process.  In the initial mode, the functionality is nearly the same as when using Live's default `MIDI Mix` script.  However, there are two key differences: 
- In session view, the first-scene clip slots of the controlled tracks are now highlighted with a colored box
- The `REC ARM` buttons now operate as track selection buttons

The remaining controls -- pots, sends, mute/solo buttons, and volume faders -- operate as before.

To enter the new device-edit mode, hold down the `SOLO` button and then press the `BANK RIGHT` button (`SOLO`-`BANK RIGHT`).  In this mode, the only change is that the top two rows of encoders now operate as parameter controls for the first sixteen parameters of whatever device is selected.

To return to the initial mode, press `SOLO`-`BANK LEFT` on the MIDIMIX.

## Installation
The best place to install this is in the `Remote Scripts` folder of your `User Library`.  Open  `Live > Settings > Library` (`Live > Preferences > Library` on Windows) to find the library location.  You'll have to create the `Remote Scripts` folder first if it doesn't exist.

## Limitations
I don't have much experience developing controller scripts for Live.  It's probably possible to retain the `REC ARM` functionality of the original Live script in the default mode, but I couldn't find a way.

## Tips
There also didn't seem to be a simple way to enable device selection from the MIDIMIX.  So, keyboard shortcuts are your friend here.  Once you've selected a track, if the device view does not already have the focus, hit `SHIFT-TAB` twice to set the focus.  Then, you can use your left/right arrow keys to select the desired device.  Once the focus has been set for a track, it will persist while selecting other tracks, until you shut down Live.  As far as I can tell, Live does not save these settings when you exit the application.

## Notes
The script assumes that the MIDIMIX is in factory default configuration.  If you've changed that, you'll need to update `elements.py` with the new `CC/NOTE` values.

## Contributions
If you have a worthwhile addition or enhancement, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".

How to Fork the Project:
- Create your Feature Branch (git checkout -b feature/AmazingFeature)
- Commit your Changes (git commit -m 'Add some AmazingFeature')
- Push to the Branch (git push origin feature/AmazingFeature)
- Open a Pull Request

## License
Distributed under the MIT License. See the LICENSE file for more information.