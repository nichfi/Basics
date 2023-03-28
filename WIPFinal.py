import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns
from re import sub
#from matplotlib.colors import LinearSegmentedColormap

#removes the commas and money signs from dollar values
def money_convert(money):
    mon=sub(r'[^\d.]', '', money) 
    return mon

#shows all the columns when printing a df
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#Establishing directory fo rbox office data file reference
base_name='ranking_data\\ranking_summary_'

#creating pandas dataframe for boxoffice data
boxoffice=pd.DataFrame()

#for loop to concat all of the box office data
for year in range(1977, 2024):
    
    #reading from local  file BASENAME + YEAR + .csv
    data=pd.read_csv(os.getcwd()+"\\"+base_name+str(year)+'.csv')
    #concatenate to one dataframe
    boxoffice=pd.concat([boxoffice, data])

#creating pandas dataframe for review data
reviews=pd.read_csv(os.getcwd()+"\\"+"review_data\\rotten_tomatoes_movies.csv")

#merging boxoffice and reviews data
merged_data=pd.merge(boxoffice, reviews, how="inner", left_on='title', right_on='movie_title')

#removes a bunch of columns that are not very useful
smaller_data=merged_data[['title', 'worldwide', 'domestic', 'domestic_pct', 'tomatometer_status', \
                          'tomatometer_rating', 'tomatometer_count', 'audience_rating', 'audience_count']]

#converts money from string into a float
converted_mon=map(money_convert, smaller_data['worldwide'])
smaller_data['worldwide']=pd.to_numeric(list(converted_mon))

#converts money from string into a float
converted_dom=map(money_convert, smaller_data['domestic'])
smaller_data['domestic']=pd.to_numeric(list(converted_dom))

#filter the data by revenue to check if the merge/conversion are working correctly
data_check=smaller_data.sort_values(by=['worldwide'], ascending=False)
print(data_check.head())

#EXPERIMENTAL HISTOGRAM AND STUFF BELOW - nich

#remove more columns that are not very useful
heatmapdata = smaller_data[['audience_rating','worldwide','tomatometer_rating']]
#figure settings
fig, (ax1) = plt.subplots(ncols=1, figsize=(10,20), sharex=True, sharey=True)
#currently doing nothing
sns.color_palette("Spectral", as_cmap=True)
#histogram
sns.histplot(x=heatmapdata['tomatometer_rating'], y=heatmapdata['worldwide'],stat = 'density', ax=ax1,log_scale=(False, True))
ax1.set_title('histplot')
plt.show()
