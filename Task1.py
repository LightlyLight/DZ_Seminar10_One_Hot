"""
В ячейке ниже представлен код генерирующий DataFrame, 
которая состоит всего из 1 столбца. 
Ваша задача перевести его в one hot вид. 
Сможете ли вы это сделать без get_dummies?
"""
import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
# df = pd.DataFrame(lst)
# print(df)

data = pd.DataFrame({'whoAmI':lst})
print(data.head())

def assign_entity(row):
    if row['whoAmI'] == 'human':
        return 1
    elif row['whoAmI']:
        return 0
    else:
        return 'Unknown'

data['Entity'] = data.apply(assign_entity, axis=1)
print(data.sample(15))

