import pulseio
import board
import adafruit_irremote

version = "6b"
print("decoder code version" + version)


def decode_pulses(pulses):
    if not 4000*0.8 < pulses[0] < 4000*1.2:
        return 0
    p1 = pulses[1::2]
    p2 = pulses[2::2]
    result_bin = ""
    for i1, i2 in zip(p1, p2):
        if (i2 - i1) > 500:
            result_bin += "1"
        else:
            result_bin += "0"
    try:
        result_hex = hex(int('0b' + result_bin, 2))
    except ValueError:
        result_hex = 0

    print("Decoded: 0x", result_hex)
    print("Decoded: b", result_bin)


# Create a 'pulseio' input, to listen to infrared signals on the IR receiver
pulsein = pulseio.PulseIn(board.IR_RX, maxlen=120, idle_state=True)
# Create a decoder that will take pulses and turn them into numbers
decoder = adafruit_irremote.GenericDecode()

while True:
    pulses = decoder.read_pulses(pulsein)
    print("Received: ", pulses)
    decode_pulses(pulses)


