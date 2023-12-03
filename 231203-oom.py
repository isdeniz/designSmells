import subprocess
import os
import zipfile
import shutil
import pandas as pd

outputs = os.listdir('/Users/isdeniz/Documents/analysis-example')
print(outputs)

designCodeSmells = pd.DataFrame()
designCodeSmellsSummary = pd.DataFrame()


for fname in outputs:
    if not (fname.startswith('.')):
        path = '/Users/isdeniz/Documents/analysis-example/' + fname + '/' + 'designCodeSmells.csv'
        newds = pd.read_csv(f'{path}')
        temp = fname
        if newds.shape[0] == 0:
            newds.loc[0,'info'] = temp
            newdss = newds.groupby(by=['Code Smell'], as_index=False)['info'].count()
            newdss.loc[0,'info'] = pd.NA
            newdss.loc[0,'repoInfo'] = temp
            newdss.loc[0,'oom type'] = 'design smell'
        else:
            newds['info'] = temp
            newdss = newds.groupby(by=['Code Smell'], as_index=False)['info'].count()
            newdss['repoInfo'] = temp
            newdss['oom type'] = 'design smell'
        designCodeSmells = pd.concat([newds, designCodeSmells], ignore_index=True)
        designCodeSmellsSummary = pd.concat([newdss, designCodeSmellsSummary], ignore_index=True)
    
print(designCodeSmells.shape[0])
print(designCodeSmells.head())
print(designCodeSmellsSummary.shape[0])
print(designCodeSmellsSummary)




