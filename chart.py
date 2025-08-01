import pandas as pd
import matplotlib.pyplot as plt

# Data from the table
data = {
    'Resistance Profile': [
        'AMP FOX CAZ CRO FEP IPM AMC TZP GEN CIP SXT', 'AMP CAZ CRO FEP AMC GEN CIP SXT', 
        'AMP CAZ CRO FEP SXT', 'AMP FOX CAZ CRO FEP IPM AMC TZP', 'AMP CAZ CRO FEP AMC CIP SXT', 
        'AMP CAZ CRO FEP AMC GEN CIP SXT', 'AMP CAZ CRO FEP CIP SXT', 'AMP CRO CIP SXT', 
        'AMP --- CAZ CRO FEP IPM AMC TZP GEN AMK CIP SXT', 'AMP CAZ CRO FEP SXT', 
        'AMP FOX CAZ CRO FEP IPM AMC --- GEN AMK CIP SXT', 'AMP CAZ CRO FEP AMC GEN CIP SXT', 
        'AMP CAZ CRO FEP AMC TZP CIP SXT', 'AMP CAZ CRO FEP AMC TZP AMK CIP SXT', 
        'AMP CAZ CRO FEP CIP SXT', 'AMP CAZ CRO FEP CIP', 'AMP CAZ CRO FEP CIP', 
        'AMP CRO', 'AMP', 'Others'
    ],
    'Percentages': [13.3, 11.8, 11.0, 8.6, 4.4, 3.2, 2.5, 2.1, 1.7, 1.5, 1.3, 1.3, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 1.1, 28.7]
}

mlst_data = {
    'MLST': ['131', '410', '38', '405', '10', '1193', '448', '101', '156', '44', 'Others'],
    'Percentages': [23.4, 20.7, 4.2, 3.6, 3.4, 3.2, 2.7, 2.5, 2.5, 2.3, 31.4]
}

inc_type_data = {
    'Inc Type': [
        'IncFIB(AP001918)', 'IncFIA', 'Col(Bs512)', 'IncFII(pRSB107)', 'IncFII', 'IncA/C2', 
        'IncQ1', 'Col156', 'Col(MG828)', 'IncX3', 'Others'
    ],
    'Percentages': [16.4, 13.5, 8.9, 6.0, 5.4, 5.2, 4.9, 4.5, 4.3, 3.5, 27.5]
}

# Create DataFrames
df_resistance = pd.DataFrame(data)
df_mlst = pd.DataFrame(mlst_data)
df_inc_type = pd.DataFrame(inc_type_data)

# Create the plot
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(15, 8), sharey=True)

# Plot Resistance Profile
axes[0].barh(df_resistance['Resistance Profile'], df_resistance['Percentages'], color=plt.cm.tab20.colors)
axes[0].set_title('Resistance Profile')

# Plot MLST
axes[1].barh(df_mlst['MLST'], df_mlst['Percentages'], color=plt.cm.tab20.colors)
axes[1].set_title('MLST')

# Plot Inc Type
axes[2].barh(df_inc_type['Inc Type'], df_inc_type['Percentages'], color=plt.cm.tab20.colors)
axes[2].set_title('Inc Type')

# Add legends
handles_resistance = [plt.Line2D([0], [0], color=color, lw=4) for color in plt.cm.tab20.colors[:len(df_resistance)]]
axes[0].legend(handles_resistance, df_resistance['Resistance Profile'], bbox_to_anchor=(1.05, 1), loc='upper left', title='Resistance Profile')

handles_mlst = [plt.Line2D([0], [0], color=color, lw=4) for color in plt.cm.tab20.colors[:len(df_mlst)]]
axes[1].legend(handles_mlst, df_mlst['MLST'], bbox_to_anchor=(1.05, 1), loc='upper left', title='MLST')

handles_inc_type = [plt.Line2D([0], [0], color=color, lw=4) for color in plt.cm.tab20.colors[:len(df_inc_type)]]
axes[2].legend(handles_inc_type, df_inc_type['Inc Type'], bbox_to_anchor=(1.05, 1), loc='upper left', title='Inc Type')

# Adjust layout
plt.tight_layout()
plt.show()
