import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Personaliza el esquema de color
sns.set_palette("husl", 8)

df = pd.read_csv("pima-indians-diabetes.csv")

# Create a figure with 8 subplots (one for each numerical column)
fig, axs = plt.subplots(4, 2, figsize=(12, 12), squeeze=False)

# Iterate through the numerical columns and create histograms
for i, col in enumerate(df.select_dtypes(include=['float64', 'int64']).columns):
    sns.histplot(df[col], ax=axs[i//4, i%2], kde=False, color=sns.color_palette()[i % 8])
    axs[i//4, i%2].set_title(col.capitalize())
    axs[i//4, i%2].set_xlabel('Value')
    axs[i//4, i%2].set_ylabel('Frequency')

# Remove unused subplots
fig.delaxes(axs[3, 1])

# Show the plot
plt.tight_layout()
plt.show()

# Create histograms for specific columns
# Create histograms for specific columns
sns.histplot(df['Glucose'], kde=False, color=sns.color_palette()[0])
plt.title('Glucose Histogram')
plt.ylabel('numero de personas')
plt.show()

sns.histplot(df['BloodPressure'], kde=False, color=sns.color_palette()[1])
plt.title('Blood Pressure Histogram')
plt.show()

sns.histplot(df['SkinThickness'], kde=False, color=sns.color_palette()[2])
plt.title('Skin Thickness Histogram')
plt.show()

sns.histplot(df['Insulin'], kde=False, color=sns.color_palette()[3])
plt.title('Insulin Histogram')
plt.show()

sns.histplot(df['BMI'], kde=False, color=sns.color_palette()[4])
plt.title('BMI Histogram')
plt.show()

sns.histplot(df['DiabetesPedigreeFunction'], kde=False, color=sns.color_palette()[5])
plt.title('Diabetes Pedigree Function Histogram')
plt.show()

sns.histplot(df['Age'], kde=False, color=sns.color_palette()[6])
plt.title('Age Histogram')
plt.show()

sns.histplot(df['Outcome'], kde=False, color=sns.color_palette()[7])
plt.title('Outcome Histogram')
plt.show()
