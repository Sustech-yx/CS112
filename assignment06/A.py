import pandas as pd
from math import log2
import numpy as npy

a = list(map(float, input().split(' ')))
b = list(map(float, input().split(' ')))
a_ = npy.array(a)
b_ = npy.array(b)
tmp = npy.ones(5)
a_ += tmp
b_ += tmp
c = b_ / a_
c = list(map(log2, c))

Genes = ['ACTB', 'MAPT', 'GAPDH', 'TP53', 'PSAP']
df = pd.DataFrame({'ctrl': a, 'treated': b, 'l2fc': c}, index=Genes)
print(df)