import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_excel('finalreport.xlsx')

width = 0.25 
pos = list(range(len(df['Count of keyword 1'])))
fig, ax = plt.subplots(figsize=(10,5))

# Create a bar with pre_score data,
# in position pos,
plt.bar(pos, 
        #using df['pre_score'] data,
        df['Count of keyword 1'], 
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#EE3224', 
        # with label the first value in first_name
        label=df['url'][0]) 

# Create a bar with mid_score data,
# in position pos + some width buffer,
plt.bar([p + width for p in pos], 
        #using df['mid_score'] data,
        df['Count of keyword 2'],
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#F78F1E', 
        # with label the second value in first_name
        label=df['url'][1]) 

# Create a bar with post_score data,
# in position pos + some width buffer,
plt.bar([p + width*2 for p in pos], 
        #using df['post_score'] data,
        df['Count of keyword 3'], 
        # of width
        width, 
        # with alpha 0.5
        alpha=0.5, 
        # with color
        color='#FFC222', 
        # with label the third value in first_name
        label=df['url'][2]) 

# Set the y axis label
ax.set_ylabel('Count')

# Set the chart's title
ax.set_title('Count of keyword in url')

# Set the position of the x ticks
ax.set_xticks([p + 1.5 * width for p in pos])

# Set the labels for the x ticks
ax.set_xticklabels(df['url'])

# Setting the x-axis and y-axis limits
plt.xlim(min(pos)-width, max(pos)+width*4)
plt.ylim([0, max(df['Count of keyword 1'] + df['Count of keyword 2'] + df['Count of keyword 3'])] )
# Adding the legend and showing the plot
plt.legend([x, 'Count of keyword 2', 'Count of keyword 3'], loc='upper left')
plt.grid()
plt.show()
