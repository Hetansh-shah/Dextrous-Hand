import struct
import crcmod
import time
import serial
import keyboard  # Requires 'pip install keyboard'

def modbus_crc(data):
    """Calculate Modbus RTU CRC16"""
    crc16 = crcmod.predefined.mkPredefinedCrcFun("modbus")
    return struct.pack('<H', crc16(data))

def move_hand(angles):
    """ Sends custom angles to move the robotic hand """
    ser = serial.Serial(
    port="COM7",  
    baudrate=115200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=2
)
    angle_bytes = struct.pack(">HHHHHH", *angles)  # Convert angles to bytes
    command = bytearray([0x01, 0x10, 0x05, 0xCE, 0x00, 0x06, 0x0C]) + angle_bytes
    command += modbus_crc(command)  # Add CRC

    ser.write(command)
    response = ser.read_all()
    ser.close()

start_position = [1000, 1000, 1000, 1000,1000 , 1000]  # Fully open hand
sequences = [
    [1000, 0, 0, 0, 500, 800],  #Little finger
    [0, 1000, 0, 0, 500, 800],  #Ring  finger
    [0, 0, 1000, 0, 500, 800],  #Middle finger
    [0, 0, 0, 1000, 500, 800],  #Index finger
    [1000, 1000, 1000, 1000, 0, 0],  #Thumb finger
    [1000, 0, 0, 1000, 500, 800],  #Spider man
    [1000, 0, 0, 0, 500, 800],  #Call me
    [1000, 1000, 1000, 500, 500, 200],  #Nice 👌
]

print("Performing Sequential Finger Movement... Press 'X' to stop.")

while True:
    if keyboard.is_pressed("x"):
        print("\nStopping gesture.")
        break  # Exit loop when "X" is pressed

    for angles in sequences:
        move_hand(angles)
        time.sleep(0.8)  # Small delay for a smooth effect

    move_hand(start_position)  # Reopen the hand
    time.sleep(0.8)
