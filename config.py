from secrets import token_hex
from pathlib import Path

session_key = None

WORKING_DIR = Path(__file__).parent
CONFIG_PATH = WORKING_DIR / "config"
KEY_PATH = CONFIG_PATH / ".secret_key"

def get_session_key():
    """Retrieves a secret session key file if it exists, 
    or creates a new one otherwise.
    """
    global session_key
    CONFIG_PATH.mkdir(parents=True, exist_ok=True)

    if KEY_PATH.exists():
        session_key = KEY_PATH.read_text()
        return session_key
    else:
        key = token_hex(24)
        KEY_PATH.write_text(key)
        session_key = key
        return session_key

def init():
    """Initializes server-side configurations."""
    get_session_key()