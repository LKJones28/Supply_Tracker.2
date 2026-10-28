from ._anvil_designer import Form1Template
from anvil import *


class Form1(Form1Template):
  def __init__(self, **properties):
    super().__init__(**properties)

  @handle("GoogleMap", "bounds_changed")
  def GoogleMap_bounds_changed(self, **event_args):
    """This method is called when the viewport bounds have changed."""
    pass  # Write Code Here

  @handle("text_box_1", "focus")
  def 1(self, **event_args):
    """This method is called when the TextBox gets focus"""
    pass  # Write Code Here
