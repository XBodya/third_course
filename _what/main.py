import numpy as np
import pandas as pd

# Установка семени для воспроизводимости
np.random.seed(42)

# Параметры для каждой группы
group_a = np.random.normal(loc=50, scale=10, size=34)  # Группа A
group_b = np.random.normal(loc=60, scale=10, size=33)  # Группа B
group_c = np.random.normal(loc=55, scale=10, size=33)  # Группа C

# Создание DataFrame
data = {
    'Group': ['2031'] * len(group_a) + ['2033'] * len(group_b) + ['2032'] * len(group_c),
    'Value': np.concatenate([group_a, group_b, group_c])
}

df = pd.DataFrame(data)

# Вывод первых 10 строк
print(df.head(10))
df.to_csv('.\\_what\\output.csv')
