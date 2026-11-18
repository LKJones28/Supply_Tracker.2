from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  def __init__(self, **properties):
    super().__init__(**properties)

  @handle("location_search", "change")
  def location_search_change(self, **event_args):
    """This method is called when the text in this text box is edited"""
    pass  # Write Code Here
