import io
import pandas as pd

def random_choice(data):
    df = pd.read_csv(data)
    result = df.sample(n=1)
    buffer = io.StringIO()
    result.to_csv(buffer, index=False)
    return buffer