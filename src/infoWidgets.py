from textual.widget import Widget
from textual.reactive import reactive

from globals import *
from jsonUtils import MapsJson

class PwadTitle(Widget):
    """Dynamic Label for any given name"""
    DEFAULT_CSS = """
    PwadTitle {
        width: auto;
        height: auto; 
    }
    """
    str_body = reactive(SELECTED_FILE)
    def render(self) -> str:

        return f"{self.str_body}"

class PwadAuthor(Widget):
    """Dynamic Label for any given name"""
    DEFAULT_CSS = """
    PwadAuthor {
        width: auto;
        height: auto; 
    }
    """
    str_body = reactive(MapsJson(JSON_FILEPATH).get_from_data('WAD', SELECTED_FILE, 'Author')[0])
    def render(self) -> str:
        return f"{self.str_body}"
