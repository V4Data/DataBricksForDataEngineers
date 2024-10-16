# Sample DataFrame
data = [(1, "Alice"), (2, "Bob"), (3, "Cathy")]
columns = ["id", "name"]
df = spark.createDataFrame(data, columns)

# Display original DataFrame
df.show()

# New column names
new_column_names = ["user_id", "user_name"]

# Change column names using reduce
df_renamed = reduce(
    lambda temp_df, index: temp_df.withColumnRenamed(columns[index], new_column_names[index]),
    range(len(columns)),  # Iterate over index range
    df
)

# Display updated DataFrame
df_renamed.show()