# Analysis


## Step 1 - Climate Analysis and Exploration

Using Python and SQLAlchemy to do basic climate analysis and data exploration of your climate database. All of the following analysis are completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.

* Using the provided [starter notebook](climate_starter.ipynb) and [hawaii.sqlite](Resources/hawaii.sqlite) files to complete your climate analysis and data exploration.


### Precipitation Analysis

* Design a query to retrieve the last 12 months of precipitation data.

* Selected only the `date` and `prcp` values.

* Loaded the query results into a Pandas DataFrame and set the index to the date column.

* Sorted the DataFrame values by `date`.

* Plotted the results using the DataFrame `plot` method.

* Using Pandas to print the summary statistics for the precipitation data.

### Station Analysis

* Design a query to calculate the total number of stations.

* Design a query to find the most active stations.

* Designed a query to retrieve the last 12 months of temperature observation data (tobs).

  * Filter by the station with the highest number of observations.
