"""Small input parsing utilities used by the hotel booking example."""


def nights_stayed(days):
    """Return nights between a valid ``check-in-check-out`` pair; else 0."""
    if not isinstance(days, str):
        return 0
    parts = days.split("-")
    if len(parts) != 2:
        return 0
    try:
        check_in, check_out = (int(part.strip()) for part in parts)
    except ValueError:
        return 0
    if check_in < 1 or check_out <= check_in:
        return 0
    return check_out - check_in


def room_floor(room_code):
    """Extract a floor digit from a room code like D-305; else 0."""
    if not isinstance(room_code, str):
        return 0
    parts = room_code.strip().split("-")
    if len(parts) != 2 or not parts[0].isalpha() or not parts[1].isdigit():
        return 0
    return int(parts[1][0])


def booking_label(names_csv):
    """Build a lead guest label; return an empty string for invalid input."""
    if not isinstance(names_csv, str):
        return ""
    names = [name.strip() for name in names_csv.split(",") if name.strip()]
    if not names:
        return ""
    return f"{names[0].title()} +{len(names) - 1}"


def main():
    """Demonstrate the parsing helpers using sample values."""
    print("==== Running nights_stayed ====")
    print("Nights:", nights_stayed("12-15"))
    print("\n==== Running room_floor ====")
    print("Floor:", room_floor("D-305"))
    print("\n==== Running booking_label ====")
    print("Booking Label:", booking_label("ravi, priya"))


if __name__ == "__main__":
    main()
