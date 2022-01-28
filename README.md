# mute-button
Python Code and some setup bits to run a Raspberry Pi as an HID and send commands to Zoom

## Basics
Essentially, this script is designed to wait for a GPIO button press (pull high wiring, I think), and then send a series of keyboard commands to highlight Zoom and toggle mute state.  
These keyboard commands are:
* CTRL+ALT+SHIFT - Moves focus to Zoom from anywhere in the OS
* ALT+A - Toggles mute state

## Operation
The script assumes that you've appropriately configured the Raspberry Pi as a keyboard-type Human Interface Device.  
It requires write access to an output buffer, and must be run as sudo

## Key Assumptions
Ensure that you've appropriately mapped the button and LED GPIO pins in the initialization step.  If these change, make sure they change in code.  

