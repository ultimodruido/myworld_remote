Roadmap, Issues and Support
---------------------------

At the moment the API is fairly complete for a real time control of the trains.

Unfortunately, the server hangs for unknown reasons every now and then (although,
it may be just my child's fault clicking way too much and random...)

The first step will be to expand the protocol to include other frequencies. Help is appreciated :)
Please use the *decode.py* code as explained in the **Circuit playground firmware** section to decode
other frequencies and post them in the issue section.

Identifying the preamble for a new frequency is actually easy. Just use *decode.py*
to read the remote's transmission with no speed (code: '000') and without pressing
any button (code: '000').

The result code should look like the following::

    Received:  [bla bla numbers]
    Decoded: 0x bla bla hexadecimals numbers
    Decoded: b XXXXX000000YYYYYY111111

The important part is the XXXXX. The code should be divided in two parts,
where the second part is just the same as the first only bit inverted::

    Decoded string: XXXXX  000    000     YYYYYY 111     111
           Subsets: FREQ   SPEED  BUTTON  !FREQ  !SPEED  !BUTTON

It means that the XXXXX and YYYYY parts are one the bit-inverted of the other.

The FREQ dictionary in *protocol.py* should be extended to include the new frequency, so please write me your findings::

    FREQ = {
        'G': '0',
        'H': '1',
        'U': '00110',
        'V': '00111',
        'N': 'XXXXX',
    }


**Additional ideas (but no concrete plan)**

* develop an identification solution based on the RFid technology
* map track sections and (eventually) control turnouts
