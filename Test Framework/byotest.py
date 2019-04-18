def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)


def test_not_equal(a, b):
    assert a != b, "Did not expect {0} but got {1}".format(a, b)


def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(
        collection, item)


def test_not_in(collection, item):
    assert item not in collection, "{0} is not in {1}".format(item, collection)


def test_between(a, b, c):
    assert c >= a and c <= b, "{2} is not between {0} and {1}".format(a, b, c)


test_not_equal(0, 0)

test_is_in([1, 2], 3)

test_not_in([1, 2], 2)

test_between(1, 3, 4)

test_are_equal(([1, 2, 3, 4, 5]), 2)
