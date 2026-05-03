import re
import pandas as pd

import sys

def parse_chat(file_path):
    data = []
    pattern = r"(\d{2}/\d{2}/\d{2}), \d{2}:\d{2} - (.*?): (.*)"

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            match = re.match(pattern, line)
            if match:
                data.append({
                    "date": match.group(1),
                    "customer": match.group(2),
                    "message": match.group(3)
                })
    # print(data)
    # sys.exit()
    df = pd.DataFrame(data)
    df["date"] = pd.to_datetime(df["date"], format="%d/%m/%y")
    # print(df)
    # sys.exit()

    return df