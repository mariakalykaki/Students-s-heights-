# Importing libraries

import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

import math


df =pd.read_csv("class_heights.csv")
students_heights = df.height

plt.hist(students_heights,label='heights')

plt.xlabel('Height(cm)')
plt.ylabel('Frequency')
plt.legend()


men = df.loc[df.gender==0, 'height']
print(men.mean())


sample_size=5
intervals= []
sample_means =[]
for i in range(50):
    sample = np.random.choice(a=men,size=sample_size)
    print(sample)
    sample_mean = sample.mean()
    print(sample_mean)
    
    
    z_critical = stats.norm.ppf(q=0.975)
    print(z_critical)

    men_std = men.std()
    print(men_std)


    margin_of_error = z_critical * (men_std/math.sqrt(sample_size))
    print(margin_of_error)


    confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
    print(confidence_interval)
    
    intervals.append(confidence_interval)
    sample_means.append(sample_mean)
    
    
    
    
plt.figure(figsize=(9,9))
plt.errorbar(x=np.arange(0.1,50,1),y=sample_means,yerr=[(top-bot)/2 for top,bot in intervals],fmt='o')


plt.hlines(xmin=0,xmax=50,y=177.35,linewidth=2.0,color='red')