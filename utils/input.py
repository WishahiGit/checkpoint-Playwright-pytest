def parse_bool(val):
    """
    Converts a string value to boolean.
    Accepts 'true', 'True', ' TRUE ', etc.
    Returns False for everything else.
    """
    return str(val).strip().lower() == "true"

def extract_login_credentials(data):
    return data.get("email"), data.get("password"), parse_bool(data.get("expected"))
