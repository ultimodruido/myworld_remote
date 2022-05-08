import pytest

from submodules.train import Train
from unittest.mock import Mock


def test_update():
    update_callback_mock = Mock()
    t = Train('faketrain', 'H', '', update_callback_mock)
    t.update()
    update_callback_mock.assert_called_with('H', 'STOP', None)

    t.update(speed='F3')
    update_callback_mock.assert_called_with('H', 'F3', None)

    t.update(command='SOUND1')
    # keeps 'F3' from previous call
    update_callback_mock.assert_called_with('H', 'F3', 'SOUND1')


def test_toggle_light():
    update_callback_mock = Mock()
    t = Train('faketrain','H', '', update_callback_mock)
    t.toggle_light()
    update_callback_mock.assert_called_with('H', 'STOP', 'LIGHT')


def test_play_sound():
    update_callback_mock = Mock()
    t = Train('faketrain','H', '', update_callback_mock)
    t.play_sound('SOUND1')
    update_callback_mock.assert_called_with('H', 'STOP', 'SOUND1')
    t.play_sound('SOUND2')
    update_callback_mock.assert_called_with('H', 'STOP', 'SOUND2')

    update_callback_mock.call_count = 0
    t.play_sound('SOUND_fake')
    assert update_callback_mock.call_count == 0


def test_horn():
    update_callback_mock = Mock()
    t = Train('faketrain', 'H', '', update_callback_mock)
    t.horn()
    update_callback_mock.assert_called_with('H', 'STOP', 'HORN')


def test_set_name():
    update_callback_mock = Mock()
    t = Train('faketrain', 'H', '', update_callback_mock)
    t.set_name('mind_blown')
    assert t.name == 'mind_blown'


def test_set_frequency():
    update_callback_mock = Mock()
    t = Train('faketrain', 'H', '', update_callback_mock)
    t.set_frequency('G')
    assert t.frequency == 'G'

    #with pytest.raises(TypeError):
    #    t.set_frequency(1)


def test_set_box():
    update_callback_mock = Mock()
    t = Train('faketrain', 'H', '', update_callback_mock)
    t.set_box('11231')
    assert t.box == '11231'


def test_get_dict_repr():
    update_callback_mock = Mock()
    t = Train('faketrain', 'H', '11211', update_callback_mock)
    assert t.get_dict_repr() == {'box': '11211', 'frequency': 'H', 'name': 'faketrain'}
