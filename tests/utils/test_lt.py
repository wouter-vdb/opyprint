# test_lt

from frozendict import NoCopyFrozenDict as FrozenDict
from pytest import raises

from opyprint import dict_lt, lt


def test_basics():
    assert {'a': 1} == {'a': 1}
    assert {'a': 1} != {'a': 2}
    assert {'a': 1} != {'b': 1}

    assert FrozenDict({'a': 1}) == FrozenDict({'a': 1})
    assert FrozenDict({'a': 1}) != FrozenDict({'a': 2})
    assert FrozenDict({'a': 1}) != FrozenDict({'b': 1})

    assert ('a',) < ('b',)

    with raises(TypeError):
        assert {'a': 1} < {'b': 1}

    with raises(TypeError):
        assert FrozenDict({'a': 1}) < FrozenDict({'b': 1})

    assert isinstance(sorted({'a', 'b'}), list)
    assert sorted({'a', 'c', 'b'}) < sorted({'b', 'c'})


def test_dict_lt_with_dict():
    assert not dict_lt({'a': 1}, {'a': 1})
    assert_dict_lt({'a': 1}, {'b': 1})
    assert_dict_lt({'a': 1}, {'a': 2})

    assert_dict_lt({'a': 1}, {'a': 1, 'b': 1})
    assert_dict_lt({'a': 1, 'b': 1}, {'a': 1, 'c': 1})


def test_dict_lt_with_frozendict():
    assert not dict_lt(FrozenDict({'a': 1}), FrozenDict({'a': 1}))
    assert_dict_lt(FrozenDict({'a': 1}), FrozenDict({'b': 1}))
    assert_dict_lt(FrozenDict({'a': 1}), FrozenDict({'a': 2}))

    assert_dict_lt(FrozenDict({'a': 1}), FrozenDict({'a': 1, 'b': 1}))
    assert_dict_lt(FrozenDict({'a': 1, 'b': 1}),
                   FrozenDict({'a': 1, 'c': 1}))


def assert_dict_lt(obj_1, obj_2):
    assert dict_lt(obj_1, obj_2)
    assert not dict_lt(obj_2, obj_1)
    assert not dict_lt(obj_1, obj_1)
    assert not dict_lt(obj_2, obj_2)

    assert lt(obj_1, obj_2)
    assert not lt(obj_2, obj_1)
    assert not lt(obj_1, obj_1)
    assert not lt(obj_2, obj_2)
