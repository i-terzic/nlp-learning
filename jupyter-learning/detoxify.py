from detoxify import Detoxify
import pandas as pd

datasets = ['Fuck you', 'I like you', 'I don\' like you', 'You son of a bitch']


results = Detoxify('original').predict(datasets)

print(pd.DataFrame(results, index=['yessir']).round(5))
