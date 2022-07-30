import pandas as pd
p = pd.read_parquet('test.parquet', engine='pyarrow')
print(p)
print('')
print(len(p))
print('')
print(p.temperature)
print('')
print(p.temperature[1])

if int(p.temperature[1])>10:
    print('잘되넹?')
