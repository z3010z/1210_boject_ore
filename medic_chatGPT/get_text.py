import pandas as pd
from aians import AIans

class Getdata:

  def __init__(self, config):
    self.config = config
  
  def result_path(self):
    return self.config["output_path"]
  
  def load_data(self):
    self.data = pd.read_csv(self.config["report_path"])
    return self.data

  def get_report(self):
    return self.data["report"]
  
  def get_symptom(self):
    return self.data.columns.tolist()

  def get_system_prompt(self):
    with open(self.config["template_text_path"], 'r') as file:
      text1 = file.read()
    return text1