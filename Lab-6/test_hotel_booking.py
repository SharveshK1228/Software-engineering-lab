"""Tests for hotel booking cost, refund, and upgrade decisions."""

import pytest

from hotel_booking import booking_cost, cancellation_refund, room_upgrade


@pytest.mark.parametrize(
    ("room", "nights", "guests", "peak", "expected"),
    [
        ("standard", 2, 2, False, 4000),
        ("deluxe", 1, 1, False, 3500),
        ("suite", 1, 1, True, 7500),
        ("standard", 2, 3, False, 5000),
        ("standard", 7, 2, False, 12600),
        ("deluxe", 7, 3, True, 30713),
    ],
)
def test_booking_cost(room, nights, guests, peak, expected):
    assert booking_cost(room, nights, guests, peak) == expected


@pytest.mark.parametrize("room", ["unknown", ""])
def test_unknown_room_raises(room):
    with pytest.raises(ValueError, match="unknown room"):
        booking_cost(room, 1, 1, False)


@pytest.mark.parametrize("nights", [0, -1])
def test_invalid_nights_raises(nights):
    with pytest.raises(ValueError, match="invalid nights"):
        booking_cost("standard", nights, 1, False)


@pytest.mark.parametrize(
    ("days", "member", "expected"),
    [(10, False, 1000), (7, True, 1000), (3, False, 500), (2, True, 750), (1, False, 0), (0, True, 250)],
)
def test_cancellation_refund_branches(days, member, expected):
    assert cancellation_refund(1000, days, member) == expected


@pytest.mark.parametrize(
    ("room", "member", "free", "expected"),
    [("standard", True, 1, "deluxe"), ("deluxe", True, 1, "suite"),
     ("standard", False, 1, "standard"), ("suite", True, 1, "suite"),
     ("standard", True, 0, "standard")],
)
def test_room_upgrade_branches(room, member, free, expected):
    assert room_upgrade(room, member, free) == expected
