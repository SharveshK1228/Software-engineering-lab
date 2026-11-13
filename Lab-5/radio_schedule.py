"""Manage a small in-memory radio programme schedule."""

import sqlite3


def create_connection():
    """Create a fresh schedule database."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        "CREATE TABLE slots (id INTEGER PRIMARY KEY, show TEXT, host TEXT, "
        "start_hour INTEGER, minutes INTEGER)"
    )
    return connection


conn = create_connection()


def add_slot(show, host, start_hour, minutes):
    """Add a programme after validating its fields."""
    if not isinstance(show, str) or not show.strip():
        raise ValueError("show must be a non-empty string")
    if not isinstance(host, str) or not host.strip():
        raise ValueError("host must be a non-empty string")
    if not isinstance(start_hour, int) or not 0 <= start_hour <= 23:
        raise ValueError("start_hour must be between 0 and 23")
    if not isinstance(minutes, int) or minutes <= 0:
        raise ValueError("minutes must be a positive integer")
    conn.execute(
        "INSERT INTO slots (show, host, start_hour, minutes) "
        "VALUES (?, ?, ?, ?)",
        (show.strip(), host.strip(), start_hour, minutes),
    )


def slot_label(show, host):
    """Return a readable programme label."""
    return f"{show} hosted by {host}"


def overlap_free(formula):
    """Return False for invalid input instead of evaluating it."""
    if not isinstance(formula, str):
        return False
    parts = formula.split("<=")
    if len(parts) != 2:
        return False
    try:
        left = int(parts[0].strip())
        right = int(parts[1].strip())
    except ValueError:
        return False
    return left <= right


def morning_shows():
    """Return programme names scheduled before noon."""
    query = "SELECT show FROM slots WHERE start_hour < ? ORDER BY start_hour"
    return [row[0] for row in conn.execute(query, (12,))]


def remove_slot(slot_id):
    """Remove a slot by identifier and report whether one was removed."""
    cursor = conn.execute("DELETE FROM slots WHERE id = ?", (slot_id,))
    return cursor.rowcount > 0


def main():
    """Run a small demonstration when invoked as a script."""
    add_slot("Sunrise Beats", "Vik", 7, 60)
    add_slot("Midday Talk", "Anu", 13, 45)
    print(slot_label("Sunrise Beats", "Vik"))
    print(overlap_free("8 <= 13"), morning_shows())
    remove_slot(2)


if __name__ == "__main__":
    main()
