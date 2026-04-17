import pandas as pd

def save_candidate(data):

    df = pd.DataFrame([data])

    try:
        existing = pd.read_csv("candidates.csv")
        df = pd.concat([existing, df])
    except:
        pass

    df.to_csv("candidates.csv", index=False)