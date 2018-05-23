#! usr/bin/env python3
#-*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dates = pd.date_range('20180509', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
rows = df[(df.index >= '2018-05-10')&(df.index <= '2018-05-12')]
rows2 = df[df['A'] > 0]
s = pd.Series([1,1,2,3,5])
df['sumAB'] = pd.Series(df['A']+df['B'], index=df.index)
df['10A'] = pd.Series(df['A']*10, index=df.index)
df1 = df.set_index('A')
df['bool'] = (df.A > 1)
df = df.reindex(columns=['C','B','A'])
print(df)
