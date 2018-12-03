import os
import pandas as pd

df = pd.read_csv('ham10000/HAM10000_metadata.csv')

cancer = ['mel']

dxs = set([x[1]['dx'] for x in df.iterrows()])

print(dxs)

for dx in dxs:
    os.mkdir('ham10000/{}'.format(dx))

for index, row in df.iterrows():    
    os.rename('ham10000/Images/{}.jpg'.format(row['image_id']), 'ham10000/{}/{}.jpg'.format(row['dx'], row['image_id']))