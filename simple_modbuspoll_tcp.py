import datetime
from pymodbus.client import ModbusTcpClient
import logging
from os import path
import time

class ModbusController:
    def __init__(self, ip, port, unit_num):
        self.client = ModbusTcpClient(ip, port=port, timeout=2)
        self.unit_num = unit_num

    def connect(self):
        self.client.connect()

    def disconnect(self):
        self.client.close()

    def read_holding_registers(self, start, numof):
        return self.client.read_holding_registers(start, numof, slave=self.unit_num)

    def read_coils(self, start, numof):
        return self.client.read_coils(start, numof, slave=self.unit_num)

    def write_register(self, regid, value):
        self.client.write_register(regid, value, slave=self.unit_num)

    def write_coils(self, regid, values):
        self.client.write_coils(regid, values, slave=self.unit_num)

    def write_coils_false(self, regid):
        self.client.write_coils(regid, [False] * 1, slave=self.unit_num)

    def write_coils_true(self, regid):
        self.client.write_coils(regid, [True] * 1, unit=self.unit_num)

def main():
    logging.basicConfig(filename='dtlognl.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    ip = str(input('IP: '))
    port_num = int(input('Port: '))  # TCP port
    unit_num = int(input('Unit ID: '))  # MODBUS slave id

    modbus_controller = ModbusController(ip, port_num, unit_num)
    modbus_controller.connect()

    while True:
        op = input("""Operation:
        R - read holding registers (max. 20 register)
        W - write holding register
        poll - read holding registers in a loop and save them to txt.
        WCF - write coil False
        WCT - write coil True
        RC - read coils
        q - quit.
        cmd: """)

        if op.lower() == 'r':
            start = int(input('Read from: '))
            numof = int(input('Num of registers: '))
            sens = modbus_controller.read_holding_registers(start, numof)
            print(sens.registers)

        elif op.lower() == 'rc':
            start = int(input('Read from: '))
            numof = int(input('Num of registers: '))
            sens = modbus_controller.read_coils(start, numof)
            print(sens.bits)

        elif op.lower() == 'poll':
            filename=   str(input('Filename (with path): '))
            start =     int(input('Read from: '))
            numof =     int(input('Num of registers: '))
            cycle =     int(input('Num of reading cycle: '))
            pollwait =  float(input('Delay: '))
            
            with open(filename, 'a') as file:
                try:
                    for x in range(0, cycle):
                        sens = modbus_controller.read_holding_registers(start, numof)
                        date = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
                        print(str(x) + ". %s," % date + ",".join(str(x) for x in sens.registers))
                        file.write("%s," % date)
                        file.write(",".join(str(x) for x in sens.registers) + "\n")
                        file.flush
                        time.sleep(pollwait)
                    file.close()
                except:
                    file.close()
                

        elif op.lower() == 'w':
            regid = int(input('Register: '))
            value = int(input('New value: '))
            modbus_controller.write_register(regid, value)

        elif op.lower() == 'wcf':
            regid = int(input('Register: '))
            modbus_controller.write_coils_false(regid)

        elif op.lower() == 'wct':
            regid = int(input('Register: '))
            modbus_controller.write_coils_true(regid)

        elif op.lower() == 'ttfill':
            modbus_controller.write_coils(22, [False] * 1)
            time.sleep(1)
            modbus_controller.write_coils(70, [True] * 1)
            time.sleep(1)
            modbus_controller.write_coils(71, [False] * 1)

        elif op.lower() == 'lph':
            while True:
                litre = 0
                sens = modbus_controller.read_holding_registers(35, 2)
                prew = sens.registers[0]

                while litre < 1:
                    sens = modbus_controller.read_holding_registers(35, 2)
                    litre = sens.registers[0] - prew

                start_time = datetime.datetime.now()
                prew = sens.registers[0]
                litre = 0
                while litre < 1:
                    sens = modbus_controller.read_holding_registers(35, 2)
                    litre = sens.registers[0] - prew
                end_time = datetime.datetime.now()
                print((1 / (end_time - start_time).total_seconds()) * 3600)

        elif op.lower() == 'q':
            break

    modbus_controller.disconnect()

if __name__ == "__main__":
    main()
