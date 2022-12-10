import pytest

from day08.part1 import sichtbar_von_links
from day08.part1 import sichtbar_von_rechts

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

