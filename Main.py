from PyQt5 import QtWidgets, QtCore
from App import Ui_MainWindow
from pymodbus.client import ModbusTcpClient
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLCDNumber
import struct

class New_Dashboard(QMainWindow):
    readings_updated = QtCore.pyqtSignal(list, list)  # Signal to send updated readings
    def __init__(self, ip_address, port):
        super(New_Dashboard, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ip_address = ip_address
        self.port = port
        self.client = None
        
        # Initialize the Modbus client and connect
        self.connect()
        self.plc_status = 0  # or some initial value

        # Access QLCDNumber widget from the UI
        self.VOLTAGE1_IN = self.ui.VOLTAGE1_IN
        self.VOLTAGE2_IN = self.ui.VOLTAGE_2
        self.VOLTAGE3_IN = self.ui.VOLTAGE3_IN
        self.VOLTAGE4_IN = self.ui.VOLTAGE4_IN
        self.VOLTAGE5_IN = self.ui.VOLTAGE5_IN
        self.VOLTAGE6_IN = self.ui.VOLTAGE6_IN
        # Access QGraphics widget from the UI
        
        self.Display1 = self.ui.Display1
        self.Display2 = self.ui.Display1_2
        self.Display3 = self.ui.Display1_3
        self.Display4 = self.ui.Display1_4
        self.Display5 = self.ui.Display1_5
        self.Display6 = self.ui.Display1_6
        self.plc_screen1 =self.ui.plc_screen

    
        
        # Set up a QTimer to read registers periodically
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_readings)
        self.timer.start(1000)  # Update every 1000 milliseconds (1 second)
        
    def update_readings(self):
        if not self.client.is_socket_open():  # Check if the client socket is open
            print("Client is disconnected. Attempting to reconnect...")
            self.connect()  # Attempt to reconnect
            if not self.client.is_socket_open():
                self.update_plc_screen_style(False)
                return
        
        try:
            self.read_register()
            self.read_coil()
            self.update_plc_screen_style(True)
        except Exception as e:
            print(f"Error during update_readings: {e}")
            self.update_plc_screen_style(False)  # Update to disconnected style on error

        
    def connect(self):
        try:
            self.client = ModbusTcpClient(self.ip_address, port=self.port)
            connection = self.client.connect()
            if connection:
                print(f"Connected to Modbus server at {self.ip_address}:{self.port}")
  
            else:
                print("Failed to connect to Modbus server.")
        except Exception as e:
            print(f"Connection error: {e}")
            
    def update_plc_screen_style(self, connected):
        """
        Update the background color of plc_screen1 based on plc_status.
        Green if connected, red if disconnected.
        """
        if connected:
            # Connected: Green background
            self.plc_screen1.setStyleSheet("background-color: rgb(0, 170, 0);")
        else:
            # Disconnected: Red background
            self.plc_screen1.setStyleSheet("background-color: rgb(255, 0, 0);")

    def read_register(self):
        address = 0
        count = 12
        
        # Check if the client is connected before attempting to read
        if not self.client.is_socket_open():
            print("Client is disconnected. Skipping register read.")
            # Set all displays to zero if not connected
            self.VOLTAGE1_IN.display(0)
            self.VOLTAGE2_IN.display(0)
            self.VOLTAGE3_IN.display(0)
            self.VOLTAGE4_IN.display(0)
            self.VOLTAGE5_IN.display(0)
            self.VOLTAGE6_IN.display(0)
            return
        
        try:
            # Read holding registers
            register_response = self.client.read_holding_registers(address, count)
            
            if not register_response.isError():
                # Convert the raw register values to floating-point numbers
                registers = register_response.registers
                for i in range(0, len(registers), 2):
                    if i + 1 < len(registers):
                        # Combine two consecutive 16-bit registers into a 32-bit float
                        high = registers[i]
                        low = registers[i + 1]
                        
                        # Convert to bytes and then to a float
                        byte_data_le = struct.pack('<HH', high, low)
                        float_value_le = struct.unpack('<f', byte_data_le)[0]
                        
                        # Print and update the LCD display with the value
                        if i // 2 == 0:
                            self.VOLTAGE1_IN.display(float_value_le)
                        elif i // 2 == 1:
                            self.VOLTAGE2_IN.display(float_value_le)
                        elif i // 2 == 2:
                            self.VOLTAGE3_IN.display(float_value_le)
                        elif i // 2 == 3:
                            self.VOLTAGE4_IN.display(float_value_le)
                        elif i // 2 == 4:
                            self.VOLTAGE5_IN.display(float_value_le)
                        elif i // 2 == 5:
                            self.VOLTAGE6_IN.display(float_value_le)
                    else:
                        print(f"Skipping incomplete register pair at index {i}")
            else:
                print("Error reading holding registers")
                # Reset displays to zero in case of an error
                self.VOLTAGE1_IN.display(0)
                self.VOLTAGE2_IN.display(0)
                self.VOLTAGE3_IN.display(0)
                self.VOLTAGE4_IN.display(0)
                self.VOLTAGE5_IN.display(0)
                self.VOLTAGE6_IN.display(0)
        
        except Exception as e:
            print(f"Exception during register read: {e}")
            # Reset displays to zero in case of an exception
            self.VOLTAGE1_IN.display(0)
            self.VOLTAGE2_IN.display(0)
            self.VOLTAGE3_IN.display(0)
            self.VOLTAGE4_IN.display(0)
            self.VOLTAGE5_IN.display(0)
            self.VOLTAGE6_IN.display(0)


    def read_coil(self):
        coil_start_address = 0
        coil_count = 6
        
        # Check if the client is connected before attempting to read
        if not self.client.is_socket_open():
            print("Client is disconnected. Skipping coil read.")
            # Set all displays to red if not connected
            displays = [self.Display1, self.Display2, self.Display3, self.Display4, self.Display5, self.Display6]
            for display in displays:
                display.setStyleSheet("background-color: rgb(255, 0, 0);")
            return False
    
        try:
            # Read coil status
            coil_response = self.client.read_coils(coil_start_address, coil_count)
            
            if not coil_response.isError():
                # List of Display widgets
                displays = [self.Display1, self.Display2, self.Display3, self.Display4, self.Display5, self.Display6]
                
                for i in range(min(coil_count, len(displays))):
                    print(f"Coil {i}: {coil_response.bits[i]}")
                    if coil_response.bits[i]:  # Check if the coil is True (active)
                        displays[i].setStyleSheet("background-color: rgb(0, 170, 0);")
                    else:
                        displays[i].setStyleSheet("background-color: rgb(255, 0, 0);")
                
                # Return True if any coil is active
                return any(coil_response.bits[:min(coil_count, len(displays))])
            else:
                print("Error reading coils")
                # Set all displays to red in case of error
                displays = [self.Display1, self.Display2, self.Display3, self.Display4, self.Display5, self.Display6]
                for display in displays:
                    display.setStyleSheet("background-color: rgb(255, 0, 0);")
                return False
            
        except Exception as e:
            print(f"Exception during coil read: {e}")
            # Set all displays to red in case of exception
            displays = [self.Display1, self.Display2, self.Display3, self.Display4, self.Display5, self.Display6]
            for display in displays:
                display.setStyleSheet("background-color: rgb(255, 0, 0);")
            return False

        

    def closeEvent(self, event):
        if self.client:
            self.client.close()
            print("Connection closed.")
        super().closeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    qt_app = New_Dashboard('192.168.1.100', 502)
    qt_app.show()
    sys.exit(app.exec_())
