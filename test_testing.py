def get_formatted_name(first, last):
    """Generate a neatly formatted full name."""
    full_name = f"{first} {last}"
    return full_name.title()


def test_get_formatted_name():
    assert get_formatted_name(first="giancarlos", last="isasi") == "Giancarlos Isasi"
