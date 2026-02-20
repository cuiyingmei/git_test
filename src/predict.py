import pandas as pd
import numpy as np

np.random.seed(42)
n = 500

df = pd.DataFrame({
    area np.random.normal(50, 10, n),
    age np.random.randint(0, 30, n),
    foot_traffic np.random.normal(5000, 1000, n),
    nearby_households np.random.normal(3000, 500, n),
})

df[target] = (
    df[area]  20
    - df[age]  5
    + df[foot_traffic]  0.02
    + df[nearby_households]  0.01
    + np.random.normal(0, 50, n)
)

df.to_csv(datasample.csv, index=False)
print(data created)