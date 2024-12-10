import yaml
from get_text import Getdata
from aians import AIans
import json
import pandas as pd

if __name__ == "__main__":
    config_path = "config.yaml"
    with open(config_path, 'r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    getdata = Getdata(config = config)
    df = getdata.load_data()
    reports = getdata.get_report()
    symptoms = getdata.get_symptom()
    ai_reply = AIans()
    text1 = getdata.get_system_prompt()
    for i in range(len(reports)):
        for j in range(len(symptoms)-2):
            text2 = f"report: {reports[i]}\n + does this report mention {symptoms[j+2]}?"
            response = ai_reply.gpt_response(text1, text2)
            yes_no = json.loads(response)["Answer"]
            df.iloc[i, j+2] = yes_no

    df.to_csv(getdata.result_path(), index = False)
