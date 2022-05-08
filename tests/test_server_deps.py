from src.server_deps import reply, Message


def test_reply_simple():
    result = reply('/test', True)
    expected_result = Message(entry_point='/test', result=True, data={})
    assert result == expected_result


def test_reply_with_data():
    result = reply('/test', True, train=2, captain="string")
    expected_result = Message(entry_point='/test', result=True, data={'train': 2, 'captain': 'string'})
    assert result == expected_result
