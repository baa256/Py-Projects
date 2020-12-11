from pytrends.request import TrendReq
import matplotlib.pyplot as plt


# host language = english US

pytrends = TrendReq(hl='en-US')

#extract data about the keywords, limited to 5 at a time

keywords = ['Python' , 'R' , 'Stata' , 'C++' , 'java']
pytrends.build_payload(keywords, timeframe = 'today 5-y')

#specify and get data

data = pytrends.interest_over_time()

print(data)


#plot data
plt.plot(data)
plt.show()

#add titles

plt.suptitle('Programming Language Searches on Google')
plt.xlabel('years')
plt.ylabel('weekly searches')

#add legend
plt.legend(keywords , loc= 'upper left')
plt.show()

