This art installation, entitled FURdecahedron, was created by Sophia DeVito for CPSC334. The code found in this repo is used to wirelessly communicate with an Arduino ESP32, which is embedded in a furry enclosure. This object contains a number of sensors that affect a sound input as the user moves the dodecahedron around.

To run this installation, the internal ESP32 should be loaded with the arduino code entitled ESP32_UDP_Float.ino. Be sure to change the networkName, networkPswd, and udpAddress to reflect the network you want to use.

The top flap of the FURdecahedron must then be opened up, and the ESP32 connected to the internal 5V power source by the USB.

Next run the python code Python_UDP_Float.py on your computer. Once again, be sure to update the UDP_IP variable to reflect your computer's IP address. Also ensure that you are connected to the same network as the ESP32. You can check that everything is working smoothly at this point by pressing the buttons on the FURdecahedron, which should play a sound on your computer.

The final step is to run the SuperCollider code FURdecaherdron_SC.scd on your computer. Go through and run each function to start up the three synths that are connected to the three photoresistors on the FURdecaherdron. Now, you should hear three tones that correspond to the amount of light being provided to the sensors at this moment.

Now the FURdecaherdron is ready to be experienced! It should be installed in a well lit room, and viewers should be able to pick up, stroke, turn, pet, and play with the piece.
