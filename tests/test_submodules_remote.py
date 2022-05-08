from submodules.remote import _inverted_bit_char, Remote
from unittest.mock import Mock


def test__inverted_bit_char():
    assert _inverted_bit_char('1') == '0'
    assert _inverted_bit_char('0') == '1'


def test__inverted_bit_char_wrong_input():
    # number
    assert _inverted_bit_char(1) == ''
    # long string
    assert _inverted_bit_char('xxx') == ''


def test_remote_send():
    r = Remote('COM7')
    # mock serial transmission
    r._send = Mock()
    # force transmission flag
    r.ready = True

    r.send('H', 'F1', 'LIGHT')
    r._send.assert_called_with('H', 'F1', 'LIGHT')

    r.send('H', 'STOP', None)
    r._send.assert_called_with('H', 'STOP', 'NO_FN')

    r._send.call_count = 0
    r.send('P', 'FROG', None)
    assert r._send.call_count == 0


def test_remote__send():
    r = Remote('COM7')
    # force transmission flag
    r.ready = True

    r.serial = Mock()
    r.serial.write = Mock()

    # test STOP
    r.send('G', 'STOP', None)
    r.serial.write.assert_called_with(b'C00000001111111!\n\r')

    # test light
    r.send('H', 'F1', 'LIGHT')
    r.serial.write.assert_called_with(b'C10011000110011!\n\r')
