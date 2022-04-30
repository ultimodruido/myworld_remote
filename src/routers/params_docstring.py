"""
Module: parameter documentation
Contains only one dictionary, used to collect the documentation description for all PATH parameters
used in the API.
Avoids duplication of code or inconsistencies in the description as it appears in the documentation
"""
param_doc = {
    "train_id":     "ID number of the train as results from the */train_list* command",
    "speed_value":  "Speed command code",
    "port_name":    "Name of the serial port, example 'COM3', used for the communication with the circuit playground",
    "train_name":   "name to be used by the UI to identify the train",
    "frequency":    "the frequency used to transmit commands to the train",
    "box_number":   "the number on the box the train. It can be used by the UI for rendering purposes"
}
