import pytest

from day08.part1 import sichtbar_von_links
from day08.part1 import sichtbar_von_rechts
from day08.part2 import get_left
from day08.part2 import get_right

@pytest.mark.parametrize("vektor, value, expected",
                         [
                             ("12345", 1, 1),
                             ("12345", 2, 2),
                             ("12345", 3, 3),
                             ("12945", 1, 1),
                             ("12945", 2, 2),
                             ("12945", 3, 1),
                             ("54321", 1, 1),
                             ("54321", 2, 1),
                             ("54321", 3, 1),
                             ("33321", 1, 1),
                             ("33321", 2, 1),
                             ("34421", 1, 1),
                             ("34421", 2, 1),
                          ]
                         )
def test__get_left(vektor, value, expected):
    result = get_left(vektor, value)
    assert result == expected


@pytest.mark.parametrize("vektor, value, expected",
                         [
                             ("12945", 2, 2),
                             ("12345", 1, 1),
                             ("12345", 2, 1),
                             ("12345", 3, 1),
                             ("12945", 1, 1),
                             ("12945", 3, 1),
                             ("54321", 1, 3),
                             ("54321", 2, 2),
                             ("54321", 3, 1),
                             ("33321", 1, 1),
                             ("33321", 2, 2),
                             ("34421", 1, 1),
                             ("34421", 2, 2),
                          ]
                         )
def test__get_right(vektor, value, expected):
    result = get_right(vektor, value)
    assert result == expected

@pytest.mark.parametrize("vektor, value, expected",
                         [
                             ("71349", 3, False),
                             ("12345", 1, True),
                             ("12345", 2, True),
                             ("12345", 3, True),
                             ("12945", 1, True),
                             ("12945", 2, True),
                             ("12945", 3, False),
                             ("54321", 1, False),
                             ("54321", 2, False),
                             ("54321", 3, False),
                             ("33321", 1, False),
                             ("33321", 2, False),
                             ("34421", 1, True),
                             ("34421", 2, False),
                          ]
                         )
def test__sichtbar_von_links(vektor, value, expected):
    result = sichtbar_von_links(vektor, value)
    assert result == expected

@pytest.mark.parametrize("vektor, value, expected",
                         [
                             ("12345", 1, False),
                             ("12345", 2, False),
                             ("12345", 3, False),
                             ("12945", 1, False),
                             ("12945", 2, True),
                             ("12945", 3, False),
                             ("54321", 1, True),
                             ("54321", 2, True),
                             ("54321", 3, True),
                             ("71349", 3, False),
                             ("71343", 3, True),

                          ]
                         )
def test__sichtbar_von_rechts(vektor, value, expected):
    result = sichtbar_von_rechts(vektor, value)
    assert result == expected

