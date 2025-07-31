import pytest
from userData import User


@pytest.mark.parametrize("notification, expected_result", [
    ([True, None], None),
    ([None, None], None),
    ([False, None], None),
    ([None, True], None),
    ([None, False], None),
])
def test_notifications(notification, expected_result):
    assert User.notifications(notification) == expected_result