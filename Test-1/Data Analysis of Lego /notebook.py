
# Import modules
import pandas as pd

# Read colors data
colors = pd.read_csv('colors.csv')

# Print the first few rows
colors.head()

#3. Exploring Colors
# <p>Now that we have read the <code>colors</code> data, we can start exploring it! Let us start by understanding the number of colors available.</p>

# How many distinct colors are available?
num_colors = colors.shape[0]
num_colors

#4. Transparent Colors in Lego Sets
# <p>The <code>colors</code> data has a column named <code>is_trans</code> that indicates whether a color is transparent or not. It would be interesting to explore the distribution of transparent vs. non-transparent colors.</p>

colors_summary = colors.groupby('is_trans').count()
colors_summary

#5. Explore Lego Sets
# <p>Another interesting dataset available in this database is the <code>sets</code> data. It contains a comprehensive list of sets over the years and the number of parts that each of these sets contained. </p>
# <p><img src="https://imgur.com/1k4PoXs.png" alt="sets_data"></p>
# <p>Let us use this data to explore how the average number of parts in Lego sets has varied over the years.</p>

sets = pd.read_csv('sets.csv')

# Create a summary of average number of parts by year: `parts_by_year`
parts_by_year = sets.groupby('year')['num_parts'].mean()
parts_by_year.head()

# Plot trends in average number of parts by year
parts_by_year.plot(x='year', y='num_parts')

#6. Lego Themes Over Years
# <p>Lego blocks ship under multiple <a href="https://shop.lego.com/en-US/Themes">themes</a>. Let us try to get a sense of how the number of themes shipped has varied over the years.</p>

# In[212]:


# # themes_by_year: Number of themes shipped by year
#This is easy and less clutter approach
# themes_by_year = pd.DataFrame(sets.groupby('year')['theme_id'].nunique())
# themes_by_year.head(5)

# themes_by_year: Number of themes shipped by year
themes_by_year = sets[['year', 'theme_id']].\
 groupby('year', as_index = False).\
    agg({"theme_id": pd.Series.nunique})
print(themes_by_year.head())
