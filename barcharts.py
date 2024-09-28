#Quantitative comparison and statistical visualizations

#Quantitative comparisons: Bar Charts
#instructions
'''Call the ax.bar method to plot the "Gold" column as a function of the country.
Use the ax.set_xticklabels to set the x-axis tick labels to be the country names.
In the call to ax.set_xticklabels rotate the x-axis tick labels by 90 degrees by using the rotation key-word argument.
Set the y-axis label to "Number of medals".'''

fig, ax = plt.subplots()

# Plot a bar-chart of gold medals as a function of country
ax.bar(medals.index, medals["Gold"])

# Set the x-axis tick labels to the country names
ax.set_xticklabels(medals.index, rotation = 90)

# Set the y-axis label
ax.set_ylabel("Number of medals")

plt.show()



#instructions
'''Call the ax.bar method to add the "Gold" medals. Call it with the label set to "Gold".
Call the ax.bar method to stack "Silver" bars on top of that, using the bottom key-word argument so the bottom of the bars will be on top of the gold medal bars, and label to add the label "Silver".
Use ax.bar to add "Bronze" bars on top of that, using the bottom key-word and label it as "Bronze".'''

# Add bars for "Gold" with the label "Gold"
ax.bar(medals.index, medals["Gold"], label= "Gold")

# Stack bars for "Silver" on top with label "Silver"
ax.bar(medals.index, medals["Silver"], bottom= medals['Gold'], label = 'Silver')

# Stack bars for "Bronze" on top of that with label "Bronze"
ax.bar(medals.index, medals['Bronze'], bottom = medals['Gold'] + medals['Silver'], label = 'Bronze')

# Display the legend
ax.legend()

plt.show()


#Quantitative comparisons: Histograms
#instructions
'''Use the ax.hist method to add a histogram of the "Weight" column from the mens_rowing DataFrame.
Use ax.hist to add a histogram of "Weight" for the mens_gymnastics DataFrame.
Set the x-axis label to "Weight (kg)" and the y-axis label to "# of observations".'''

fig, ax = plt.subplots()
# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing["Weight"])

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics["Weight"])

# Set the x-axis label to "Weight (kg)"
ax.set_xlabel("Weight (kg)")

# Set the y-axis label to "# of observations"
ax.set_ylabel("# of observations")

plt.show()


#instructions
'''Use the hist method to display a histogram of the "Weight" column from the mens_rowing DataFrame, label this as "Rowing".
Use hist to display a histogram of the "Weight" column from the mens_gymnastics DataFrame, and label this as "Gymnastics".
For both histograms, use the histtype argument to visualize the data using the 'step' type and set the number of bins to use to 5.
Add a legend to the figure, before it is displayed.'''

fig, ax = plt.subplots()

# Plot a histogram of "Weight" for mens_rowing
ax.hist(mens_rowing["Weight"],histtype = 'step',label = 'Rowing', bins = 5)

# Compare to histogram of "Weight" for mens_gymnastics
ax.hist(mens_gymnastics["Weight"], histtype = 'step',label = 'Gymnastics', bins = 5)

ax.set_xlabel("Weight (kg)")
ax.set_ylabel("# of observations")

# Add the legend and show the Figure
ax.legend()
plt.show()


#statistical Plotting

#instructions
'''Add a bar with size equal to the mean of the "Height" column in the mens_rowing DataFrame and an error-bar of its standard deviation.
Add another bar for the mean of the "Height" column in mens_gymnastics with an error-bar of its standard deviation.
Add a label to the the y-axis: "Height (cm)"'''

fig, ax = plt.subplots()

# Add a bar for the rowing "Height" column mean/std
ax.bar("Rowing", mens_rowing["Height"].mean(), yerr= mens_rowing["Height"].std())

# Add a bar for the gymnastics "Height" column mean/std
ax.bar("Gymnastics", mens_gymnastics['Height'].mean(), yerr = mens_gymnastics['Height'].std())

# Label the y-axis
ax.set_ylabel("Height (cm)")

plt.show()


#instructions
'''Use the ax.errorbar method to add the Seattle data: the "MONTH" column as x values, the "MLY-TAVG-NORMAL" as y values and "MLY-TAVG-STDDEV" as yerr values.
Add the Austin data: the "MONTH" column as x values, the "MLY-TAVG-NORMAL" as y values and "MLY-TAVG-STDDEV" as yerr values.
Set the y-axis label as "Temperature (Fahrenheit)".'''

fig, ax = plt.subplots()

# Add Seattle temperature data in each month with error bars
ax.errorbar(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"], yerr=seattle_weather["MLY-TAVG-STDDEV"])

# Add Austin temperature data in each month with error bars
ax.errorbar(austin_weather['MONTH'], austin_weather['MLY-TAVG-NORMAL'], yerr = austin_weather['MLY-TAVG-STDDEV'])

# Set the y-axis label
ax.set_ylabel("Temperature (Fahrenheit)")

plt.show()


#instructions
'''Create a boxplot that contains the "Height" column for mens_rowing on the left and mens_gymnastics on the right.
Add x-axis tick labels: "Rowing" and "Gymnastics".
Add a y-axis label: "Height (cm)".'''

fig, ax = plt.subplots()

# Add a boxplot for the "Height" column in the DataFrames
ax.boxplot([mens_rowing['Height'], mens_gymnastics['Height']])

# Add x-axis tick labels:
ax.set_xticklabels(['Rowing', 'Gymnastics'])

# Add a y-axis label
ax.set_ylabel("Height (cm)")

plt.show()



#Scatter plots
#instructions
'''Using the ax.scatter method, add the data to the plot: "co2" on the x-axis and "relative_temp" on the y-axis.
Set the x-axis label to "CO2 (ppm)".
Set the y-axis label to "Relative temperature (C)"'''

fig, ax = plt.subplots()

# Add data: "co2" on x-axis, "relative_temp" on y-axis
ax.scatter(climate_change['co2'], climate_change['relative_temp'])

# Set the x-axis label to "CO2 (ppm)"
ax.set_xlabel("CO2 (ppm)")

# Set the y-axis label to "Relative temperature (C)"
ax.set_ylabel("Relative temperature (C)")

plt.show()



#instructions
'''Using the ax.scatter method add a scatter plot of the "co2" column (x-axis) against the "relative_temp" column.
Use the c key-word argument to pass in the index of the DataFrame as input to color each point according to its date.
Set the x-axis label to "CO2 (ppm)" and the y-axis label to "Relative temperature (C)".'''

fig, ax = plt.subplots()

# Add data: "co2", "relative_temp" as x-y, index as color
ax.scatter(climate_change['co2'], climate_change['relative_temp'], c = climate_change.index)

# Set the x-axis label to "CO2 (ppm)"
ax.set_xlabel("CO2 (ppm)")

# Set the y-axis label to "Relative temperature (C)"
ax.set_ylabel("Relative temperature (C)")

plt.show()



#Sharing visualizations with other

#instructions
'''Select the 'ggplot' style, create a new Figure called fig, and a new Axes object called ax with plt.subplots.
Select the 'Solarize_Light2' style, create a new Figure called fig, and a new Axes object called ax with plt.subplots.'''

# Use the "ggplot" style and create new Figure/Axes
plt.style.use('ggplot')
fig,ax = plt.subplots()

ax.plot(seattle_weather["MONTH"], seattle_weather["MLY-TAVG-NORMAL"])
plt.show()

# Use the "Solarize_Light2" style and create new Figure/Axes
plt.style.use('Solarize_Light2')
fig,ax = plt.subplots()

ax.plot(austin_weather["MONTH"], austin_weather["MLY-TAVG-NORMAL"])
plt.show()


#Saving your visualizations
#instructions
'''Examine the figure by calling the plt.show() function.
Save the figure into the file my_figure.png, using the default resolution.
Save the figure into the file my_figure_300dpi.png and set the resolution to 300 dpi.'''

# Show the figure
plt.show()

# Save as a PNG file
fig.savefig('my_figure.png')

# Save as a PNG file with 300 dpi

fig.savefig('my_figure_300dpi.png', dpi = 300)


#instructions
'''Set the figure size as width of 3 inches and height of 5 inches and save it as 'figure_3_5.png' with default resolution.
Set the figure size to width of 5 inches and height of 3 inches and save it as 'figure_5_3.png' with default settings.'''

# Set figure dimensions and save as a PNG
fig.set_size_inches([3,5])
fig.savefig('figure_3_5.png')

# Set figure dimensions and save as a PNG
fig.set_size_inches([5,3])
fig.savefig('figure_5_3.png')



#Automating figure from data

#instructions
'''Create a variable called sports_column that holds the data from the "Sport" column of the DataFrame object.
Use the unique method of this variable to find all the unique different sports that are present in this data, and assign these values into a new variable called sports.
Print the sports variable to the console.'''

# Extract the "Sport" column
sports_column = summer_2016_medals["Sport"]

# Find the unique values of the "Sport" column
sports = sports_column.unique()

# Print out the unique sports values
print(sports)



#instructions
'''Iterate over the values of sports setting sport as your loop variable.
In each iteration, extract the rows where the "Sport" column is equal to sport.
Add a bar to the provided ax object, labeled with the sport name, with the mean of the "Weight" column as its height, and the standard deviation as a y-axis error bar.
Save the figure into the file "sports_weights.png".'''

fig, ax = plt.subplots()

# Loop over the different sports branches
for sport in sports:
  # Extract the rows only for this sport
  sport_df = summer_2016_medals[summer_2016_medals['Sport'] == sport]
  # Add a bar for the "Weight" mean with std y error bar
  ax.bar(sport, sport_df['Weight'].mean(), yerr=sport_df['Weight'].std())

ax.set_ylabel("Weight")
ax.set_xticklabels(sports, rotation=90)

# Save the figure to file
fig.savefig('sports_weights.png')