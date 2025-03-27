import pandas as pd #imports pandas to give us some new functions to utilize.
import matplotlib.pyplot as plt #imports matplotlib to give us some more functions to use

skittle_data = { #sets up our array for our skittle data
    "Skittle Color": ["Green (Green apple)", "Orange", "Red (Strawberry)", "Purple (Grape)", "Yellow (Lemon)"], #Sets up a dictionary for the skittle colors and flavors
    "Number of Skittles": [22, 13, 25, 20, 10], #Sets up a dictionary that has the number of skittles there were of each flavor/color
}

favorite_data = { #sets up an array for favorite flavors/colors
    "Skittle Color": ["Red (Strawberry)", "Green (Green apple)", "Purple (Grape)", "Yellow (Lemon)", "Orange"], #same dictionary for the flavors/colors
    "Favorite Percentage": [19, 8, 44, 19, 10], #dictionary with the favorite flavors of people. 
}

df = pd.DataFrame(skittle_data) #creates our first dataframe for skittle_data
favorite_df = pd.DataFrame(favorite_data) #create our second dataframe for favorite_data

colors = ['green', 'orange', 'red', 'purple', 'yellow'] #Sets up a dictioany for the straight up colors.

fig, axs = plt.subplots(1, 3, figsize=(20, 6)) #sets figure 1 and 3 to the size of 20x6

df.plot(kind='bar', x='Skittle Color', y='Number of Skittles', color=colors, legend=False, ax=axs[0]) #plots our skittle colors and number of skittles

max_value = df["Number of Skittles"].max() #finds max value in the first bar chart
axs[0].set_ylim(0, max_value + 10) #adds a padding of 10 to make the chart cleaner.

max_index = df["Number of Skittles"].idxmax() #find max index of our Number of Skittles data set
bars = axs[0].patches #extracts visual infomration for bars
bars[max_index].set_edgecolor('black') #sets tallest bar to have a black boarder
bars[max_index].set_linewidth(3) #sets black boarder width to 3

axs[0].annotate(f"Most Popular!\nRed Skittles", #prints above the graph Most popular skittles
                 (bars[max_index].get_x() + bars[max_index].get_width() / 2, bars[max_index].get_height()), #Sets the size
                 xytext=(0, 10), #text position
                 textcoords='offset points', #offsets
                 ha='center', #centers text
                 arrowprops=dict(facecolor='black', arrowstyle='->')) #adds an arrow pointing to the bar

axs[0].set_xlabel("Skittle Color") #sets x label to Skittle Color
axs[0].set_ylabel("Number of Skittles") #sets y label to Number of Skittles
axs[0].set_title("Skittles in 6 Skittle Bags") #sets title of the chart to Skittles in 6 skittle bags
axs[0].tick_params(axis='x', rotation=45) #rotates the title to be more readable

wedges, texts, autotexts = axs[1].pie(df['Number of Skittles'], labels=df['Skittle Color'], colors=colors, autopct='%1.1f%%', startangle=140) #adds components to the pie chart

favorite_color = "Red (Strawberry)" #adds a label for the favorite color to the pie chart
axs[1].annotate(f"Favorite Color!\n{favorite_color}", #Says Favorite color
                 xy=(0, 0),  #where its displayed
                 xytext=(1.2, 0.5),  #position of text
                 textcoords='axes fraction', #text coordinates
                 fontsize=12, #font size set to 12
                 bbox=dict(boxstyle="round,pad=0.3", edgecolor='black', facecolor='lightyellow')) #pads around the text to make the box

axs[1].set_title("Skittle Color Distribution") #Sets title to Skittle Color Distribution

favorite_df.plot(kind='bar', x='Skittle Color', y='Favorite Percentage', color=colors, legend=False, ax=axs[2]) #plots the third chart, bar graph

for i, v in enumerate(favorite_df['Favorite Percentage']): # Makes the percentages numbers
    axs[2].text(i, v + 1, f'{v}%', ha='center', va='bottom', fontsize=10) #takes the percents and adds percent sign and font size to 10.

max_favorite_value = favorite_df["Favorite Percentage"].max() #Finds the largest favorite percentage.
axs[2].set_ylim(0, max_favorite_value + 5)  #adds padding to the chart to make it more readable

axs[2].set_xlabel("Skittle Color") #sets x label to Skittle Color
axs[2].set_ylabel("Favorite Percentage")  #sets y label to Favorite Percentage
axs[2].set_title("Favorite Skittles Color (Survey Results)") #sets title of the chart to Favorite Skittles Color (Survey Results)
axs[2].tick_params(axis='x', rotation=45) #rotates text to be more readable

plt.tight_layout() #tightens layout for cleaner look
plt.show() #shows the charts
