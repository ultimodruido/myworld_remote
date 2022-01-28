import pulseio
import board
import supervisor
import digitalio
from time import sleep
from array import array

version = "7b"
print("transmitter code version " + version)

# CONFIGURATION
pulseout = pulseio.PulseOut(board.IR_TX, frequency=38000, duty_cycle=2 ** 15)
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT


# HELPER FUNCTIONS
def get_pulses_length(bin_data):
    pulses = [4000]
    for bit in bin_data:
        if bit == "1":
            pulses.extend([500, 1500])
        elif bit == "0":
            pulses.extend([500, 500])
        else:
            print("error case non found")
    return pulses


def ir_send(pulses):
    pulseout.send(pulses)


# MAIN LOOP
while True:
    # print("Running main loop")
    if supervisor.runtime.serial_bytes_available:
        value = input().strip()
        print(f"{value}_Received\r")
        try:
            if (value[0] == "C") & (value[-1] == "!"):
                led.value = True
                cmd = value[1:-1].split('.')
                if cmd[0] == "__":
                    pulses = get_pulses_length(cmd[1])
                    transmit_array = array('H', 3 * pulses)
                else:
                    pulses_a = get_pulses_length(cmd[0])
                    pulses_b = get_pulses_length(cmd[1])
                    transmit_array = array('H', 3 * pulses_a + 2 * pulses_b)
                # print(f"Array prepared: {transmit_array}")
                ir_send(transmit_array)
                print(f"{value}_OK\r")
                led.value = False

        except Exception as e:
            print(f"{value}_ERROR\r")

    sleep(0.3)
