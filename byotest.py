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


def test_exception_was_raised(func, args, message):
    try:
        func(*args)

        assert False, "Exception was not raised"
    except Exception as e:

        assert e.args[0] == message, "The message that was provided did not match the message thrown"
