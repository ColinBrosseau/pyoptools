# standard imports

# third-party imports
import numpy as np
import pytest

# local imports
from pyoptools.raytrace.shape.circular import Circular


@pytest.fixture
def circle():
    return Circular(radius=25)


@pytest.fixture
def x():
    return np.array(
        [
            -14,
            17,
            -1,
            29,
            20,
            -7,
            -16,
            -3,
            21,
            -19,
            22,
            -30,
            -23,
            21,
            8,
            -30,
            5,
            3,
            -17,
            2,
        ]
    )


@pytest.fixture
def y():
    return np.array(
        [
            -23,
            28,
            28,
            0,
            -4,
            28,
            21,
            -28,
            -10,
            -7,
            19,
            23,
            -14,
            20,
            -26,
            -3,
            -12,
            -17,
            11,
            -20,
        ]
    )


@pytest.fixture
def z():
    return np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])


@pytest.fixture
def expected_hit_fhit():
    return np.array(
        [
            False,
            False,
            False,
            False,
            True,
            False,
            False,
            False,
            True,
            True,
            False,
            False,
            False,
            False,
            False,
            False,
            True,
            True,
            True,
            True,
        ]
    )


def test_default_radius():
    c = Circular()
    assert c.radius == 1.0, "Unexpected radius"


def test_hit(circle, x, y, z, expected_hit_fhit):
    expected = expected_hit_fhit

    calculated = circle.hit((x, y, z))
    np.testing.assert_equal(calculated, expected)


def test_fhit(circle, x, y, z, expected_hit_fhit):
    for (x_element, y_element, z_element, expected) in zip(x, y, z, expected_hit_fhit):
        calculated = circle.fhit(x_element, y_element, z_element)
        np.testing.assert_equal(calculated, expected)
