import pandas as pd
import matplotlib.pyplot as plt

cities = pd.read_csv('california_cities.csv')

cities['density'] = cities['population_total'] / cities['area_total_km2']


top_density = cities.sort_values(by='density', ascending=False).head(10)

plt.figure(figsize=(10, 6))
plt.barh(top_density['city'], top_density['density'], color='coral')

plt.xlabel('MDDS (people/km²)')
plt.title('Top 10 thành phố lớn nhất theo diện tích ở California')

plt.gca().invert_yaxis()

plt.tight_layout()
plt.show()