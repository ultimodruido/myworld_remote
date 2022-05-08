import pytest

from submodules.rolling_stock import RollingStock, UnknownTrainError


def test_add_train():
    rs = RollingStock()
    fate_train_1 = rs.add_train('fake_train', 'H', '11211', None)
    fate_train_2 = rs.add_train('train_fake', 'G', '22122', None)
    assert rs.trains == [fate_train_1, fate_train_2]


def test_get_train_by_id():
    rs = RollingStock()
    fate_train_1 = rs.add_train('fake_train', 'H', '11211', None)
    fate_train_2 = rs.add_train('train_fake', 'G', '22122', None)

    assert rs.get_train_by_id(0) == fate_train_1

    with pytest.raises(UnknownTrainError):
        rs.get_train_by_id(5)

    with pytest.raises(UnknownTrainError):
        rs.get_train_by_id('5')


def test_get_train_list():
    rs = RollingStock()
    fate_train_1 = rs.add_train('fake_train', 'H', '11211', None)
    fate_train_2 = rs.add_train('train_fake', 'G', '22122', None)
    assert rs.get_train_list() == [fate_train_1.get_dict_repr(), fate_train_2.get_dict_repr()]


def test_remove_train():
    rs = RollingStock()
    fate_train_1 = rs.add_train('fake_train', 'H', '11211', None)
    fate_train_2 = rs.add_train('train_fake', 'G', '22122', None)

    with pytest.raises(UnknownTrainError):
        rs.remove_train(5)
    with pytest.raises(UnknownTrainError):
        rs.remove_train('5')

    rs.remove_train(1)
    assert rs.trains == [fate_train_1]
