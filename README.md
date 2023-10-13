# Simple ModbusPoll TCP
Simulator for modbus network testing &amp; data logger

The script allows users to perform operations such as reading and writing holding registers, reading coils, and polling holding registers in a loop.

## Prerequisites
* Python3.12 
* Pymodbus 3.5.4

Install the required library with pip :
```python
pip3 install pymodbus
```
OR
```python
pip3 install pymodbus
```
for more informations about the library please [clcik here.](https://github.com/pymodbus-dev/pymodbus)
## Usage
### Run
Run the script:

```python
python3 simple_modbuspoll_tcp.py
```
Follow the prompts to input the Modbus device details and choose the operation.
Operations
* **Read Holding Registers (R):** Read a specified number of holding registers starting from a given address.
* **Read Coils (RC):** Read a specified number of coils starting from a given address.
* **Write Holding Register (W):** Write a new value to a specified holding register.
* **Write Coil False (WCF):** Write a False value to a specified coil.
* **Write Coil True (WCT):** Write a True value to a specified coil.
* **Poll Holding Registers (poll):** Read holding registers in a loop and save the values to a text file. Users can specify the filename, start address, number of registers, number of reading cycles, and delay  between polls.
* **Quit (q):** Exit the script.

## Logging
The script logs activities to the **dtlog.log** file in the same directory. The log includes timestamped entries with information about the execution.

## Contributing

Feel free to contribute to the development of this script by opening issues or pull requests. Your feedback and suggestions are highly appreciated.

## License
As the pymodbus the script is under the BSD License. [license](https://github.com/holubdavid/SimpleModbusPoll_TCP/blob/main/LICENSE)
