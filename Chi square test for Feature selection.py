import seaborn as sns
import pandas as pd
dataset = sns.load_dataset('tips')
dataset_table = pd.crosstab(dataset['sex'],dataset['smoker'])
observed_values = dataset_table.values
from scipy.stats import chi2_contingency
val = chi2_contingency(dataset_table)
expected_values = val[3]
no_of_rows = len(dataset_table.iloc[0:2,0])
no_of_columns = len(dataset_table.iloc[0,0:2])
ddof = (no_of_columns-1)*(no_of_rows-1)
alpha = 0.05
from scipy.stats import chi2
chi_squares = sum([(o-e)**2./e for o,e in zip(observed_values,expected_values)])
chi_square_stats = chi_squares[0] + chi_squares[1]
p_val = 1-chi2.cdf(chi_square_stats,df =ddof)
print("chi_square_stats",chi_square_stats)
print("p_val",p_val)
no_rel = "there is no relation between sex and smoker"
rel = "there is a relation between sex and smoker"
if p_val<=alpha:
    print(rel)
else:
    print(no_rel)