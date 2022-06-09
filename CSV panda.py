import pandas as pd

# dictionary of lists
d = {'Car': ['BMW', 'Lexus', 'Audi', 'Mercedes', 'Jaguar', 'Bentley'],'Date_of_purchase': ['2020-10-10', '2020-10-12', '2020-10-17', '2020-10-16', '2020-10-19', '2020-10-22']
}

# creating dataframe from the above dictionary of lists
dataFrame = pd.DataFrame(d)
print("DataFrame...\n",dataFrame)

# write dataFrame to SalesRecords CSV file
# dataFrame.to_csv("C:\\Users\\anifa\\Desktop\\GITB\\R-Pi\\SalesRecords.csv")

# display the contents of the output csv
print("The output csv file written successfully and generated...")