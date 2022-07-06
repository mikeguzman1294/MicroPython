# Micropython for ESP32

## Micropython Development Environment Setup
*This tutorial assumes that a distribution of Python 3 is installed in a local computer. If not installed, download the latest version through this link <https://www.python.org/downloads/>*

*The set of command line instructions is intended to run in a Windows machine*
***
### **1. Create and Launch Python Virtual Environment**

**1.1**

In order to manage the required Python libraries for this project it is recommended to create a Python virtual environment in the project's root folder.

This step should only be done once after cloning the project's repository!

To create a virtual environment use the following command:

```
python -m venv venv
```
*Note: The sencond venv in this command is the name the created virtual environment will receive. It is recommended to use 'venv' by convention.*

**1.2**

To activate the venv run the following command:
```
venv\scripts\activate
```
**1.3**

To install the required libraries for the project run the following command:
```
pip install -r packages.txt
```
This step should only be done once after cloning the project's repository as well!

Step documetation:
<https://stackoverflow.com/questions/63932002/unable-to-clone-python-venv-to-another-pc>

### **2. Flash ESP32 Controller Board**

First we need to flash the Micropython firmware to the board.

In order to do this, first erase the microcontroller's flash memory.
Next, program the bin file contained in the Firmware rlative path.

The required set of command line instructions for this is the following (make sure venv is active):
```
esptool.py erase_flash

esptool.py --chip esp32 --port COM3 --baud 460800 write_flash -z 0x1000 Firmware\esp32-20210902-v1.17.bin
```

### **3. Interact with ESP32 Board**

**3.1 Connect to board**

Connect to rshell running the following command:

```
rshell --port <serial_port_name>
```
Replace <serial_port_name> with the serial port in which your port is connected. You can check the port number in Windows Device Manager. An example in which the board is connected to port COM3 would be:

```
rshell --port COM3
```
*To exit rshell press Ctrl+D*

Rshell common Windows issue documentation: <https://core-electronics.com.au/guides/getting-started-with-raspberry-pi-pico/>

**3.2 Enter Python shell prompt**

To enter rpl in your board through command line write the follwing command inside the rshell terminal:
```
repl
```
*To exit repl press Ctrl+X*

**3.3 Add/remove scripts**

To program a script in the board we have to move it to the board's root directory and press the Enable button in the ESP32 to execute it.

To move an script (main script in the example) from the project's root directory to the board's root directory run the following command (while being in rshell prompt):
```
cp main.py /pyboard
```
To move an script (main script in the example) from the project's root directory to the board's root directory run the following command (while being in rshell prompt):
```
rm /pyboard/main.py
```
BEFORE EXITING RSHELL ALWAYS REMEMBER TO REMOVE MAIN SCRIPT FROM THE BOARD MEMORY. OTHERWISE YOU WILL NOT BE ABLE TO RECONNECT TO RSHELL AND YOU WILL HAVE TO RE-FLASH THE BOARD!






