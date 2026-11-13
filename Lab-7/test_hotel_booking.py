"""Property-based robustness checks for hotel booking input parsers."""

from hypothesis import given, strategies as st

from hotel_booking import booking_label, nights_stayed, room_floor


@given(st.one_of(st.text(), st.none(), st.integers(), st.lists(st.text())))
def test_nights_stayed_never_crashes(value):
    result = nights_stayed(value)
    assert isinstance(result, int)
    assert result >= 0


@given(st.one_of(st.text(), st.none(), st.integers(), st.lists(st.text())))
def test_room_floor_never_crashes(value):
    result = room_floor(value)
    assert isinstance(result, int)
    assert result >= 0


@given(st.one_of(st.text(), st.none(), st.integers(), st.lists(st.text())))
def test_booking_label_never_crashes(value):
    result = booking_label(value)
    assert isinstance(result, str)
