import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('random_walk.csv')
df['distance'] = np.sqrt(df['x']**2 + df['y']**2)
max = df['distance'].max()
av = df['distance'].mean()
f = df[df['distance'] > av]
print(f)

f.to_json('filtered_walk.json', orient='records', indent=3)

plt.figure(figsize = (10, 6))
plt.plot(df['x'], df['y'], color = 'green', label = 'Траєкторія')

plt.scatter(df['x'].iloc[0], df['y'].iloc[0], color='lightgreen', s=200, label='Старт', zorder=5)
plt.scatter(df['x'].iloc[-1], df['y'].iloc[-1], color='yellow', s=200, label='Фініш', zorder=5)

plt.title('Траєкторія блукання', fontsize=15)
plt.xlabel('Координата X', fontsize=15)
plt.ylabel('Координата Y', fontsize=15)
plt.legend()
plt.show()
