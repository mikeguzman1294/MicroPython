# Micropython Code

## ESP32 Micropython Code/Flashing
***
### **Libraries Setup**

*The set of command line instructions is intended to run in a rshell session*

**1.1**

In order to make available all the required libraries to the ESP32 board first we have to connect to it through rshell. *See project root file README  for reference.*

After succesful connection, run the following command to copy all the required libraries to the board's rootfolder (/pyboard).

```
cp Library_Demo/OLED_Display/ssd1306.py Library_Demo/OLED_Display/pbm_buffer.py Library_Demo/BLE/ble_advertising.py Library_Demo/BLE/ble_uart_peripheral.py /pyboard
```

*Notice that if any of the paths are changed after cloning the repo, this would change the relative paths and may make this command to not work.*


**1.2**

On the other hand, in order to delete all the required libraries from the board, run the following command:

```
rm /pyboard/ble_advertising.py /pyboard/ble_uart_peripheral.py /pyboard/pbm_buffer.py /pyboard/ssd1306.py
```