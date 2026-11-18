from ._anvil_designer import Form1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    super().__init__(**properties)

  def enable_search_btn(self, **event_args):
    self.search_btn.enabled = self.location_name.text != "" and self.location_search.text != ""

  def search_for_location(self, **event_args):
    results = GoogleMap.geocode(address=self.location_search.text)
    result = results[0].geometry.location
    print(result)
