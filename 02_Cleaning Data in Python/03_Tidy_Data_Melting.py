# Tidy Data
# It Formalize the way we describe the shape of data
# Gives us a goal when formatting our data
# Standard way to organize data values within a dataset

# Principles of Tidy Data
# Columns represent separate variables
# Rows represent individual observations
# Observational units form tables
# Tidy data makes it easier to fix common data problems

# Converting to Tidy Data
# The Data Problem we are trying to Fix:
	# Columns containing values, instead of variables.
	# Solution: pd.melt(0)

# Reshaping your data using melt
# Melting data is the process of turning columns of your data into rows of data. Consider the DataFrames from the previous exercise. In the tidy DataFrame, the variables Ozone, Solar.R, Wind, and Temp each had their own column. If, however, you wanted these variables to be in rows instead, you could melt the DataFrame. In doing so, however, you would make the data untidy! This is important to keep in mind: Depending on how your data is represented, you will have to reshape it differently (e.g., this could make it easier to plot values).

# In this exercise, you will practice melting a DataFrame using pd.melt(). There are two parameters you should be aware of: id_vars and value_vars. The id_vars represent the columns of the data you do not want to melt (i.e., keep it in its current shape), while the value_vars represent the columns you do wish to melt into rows. By default, if no value_vars are provided, all columns not set in the id_vars will be melted. This could save a bit of typing, depending on the number of columns that need to be melted.

# The (tidy) DataFrame airquality has been pre-loaded. Your job is to melt its Ozone, Solar.R, Wind, and Temp columns into rows. Later in this chapter, you'll learn how to bring this melted DataFrame back into a tidy form.
import pandas as pd

airquality = pd.read_csv('../Dataset/Cleaning Data in Python/airquality.csv.txt')

# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(frame=airquality, id_vars=['Month','Day'], value_vars=['Ozone', 'Solar.R', 'Wind', 'Temp'])

# Print the head of airquality_melt
print(airquality_melt.head())

# This exercise demonstrates that melting a DataFrame is not always appropriate if you want to make it tidy. You may have to perform other transformations depending on how your data is represented.

# Customizing melted data
# When melting DataFrames, it would be better to have column names more meaningful than variable and value (the default names used by pd.melt()).
# The default names may work in certain situations, but it's best to always have data that is self explanatory.
# You can rename the variable column by specifying an argument to the var_name parameter, and the value column by specifying an argument to the value_name parameter.
# Print the head of airquality
print(airquality.head())

# Melt airquality: airquality_melt
airquality_melt = pd.melt(airquality, id_vars=['Month', 'Day'], var_name='measurement', value_name='reading')

# Print the head of airquality_melt
print(airquality_melt.head())
