from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    super().__init__(**properties)

  @handle("location_search", "change")
  def enable_search_btn(self, **event_args):
    self.search_btn.enabled = self.location_name.test != "" and self.location_search.text != ""

  @handle("search_btn", "click")
  def search_for_location(self, **event_args):
    
