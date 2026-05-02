Day 5 Report — End-to-End EDA & Dashboard

Setup Status

* Python environment configured with pandas, seaborn, matplotlib
* Dataset successfully loaded and processed
* Visualizations generated without errors


Task Inventory

* Converted Date column into datetime format
* Performed time-series analysis using resampling
* Created pivot table for Product vs Sales
* Generated correlation heatmap
* Built multi-plot dashboard (bar + line chart)
* Created box plot to identify outliers
* Generated pairplot for feature relationships
* Created cumulative sum plot
* Performed scenario analysis (15% revenue projection)
* Calculated top product contribution percentage


Debugging Log

1. File path error → fixed by placing CSV in same directory
2. Data type issue → resolved using pd.to_numeric()
3. Date parsing issue → fixed using pd.to_datetime()


Key Insights

* Sales trends vary across time periods
* Certain products contribute significantly more revenue
* Outliers impact overall distribution
* Correlation helps understand relationships between variables

Reflection

Transaction count is crucial because high revenue may come from a few large transactions, which can be misleading. A balanced analysis requires both revenue and transaction frequency.

Conclusion

Day 5 strengthened my ability to perform end-to-end analysis, from data preprocessing to visualization and business insight generation.
