import pandas as pd
import requests
import os
import matplotlib.pyplot as plt

# Download files if they don't exist
urls = {
    'Outcomes-a.txt': 'https://physionet.org/files/challenge-2012/1.0.0/Outcomes-a.txt',
    'Outcomes-b.txt': 'https://physionet.org/files/challenge-2012/1.0.0/Outcomes-b.txt'
}

for filename, url in urls.items():
    if not os.path.exists(filename):
        with open(filename, 'wb') as f:
            f.write(requests.get(url).content)

# Read files separately
outcomes_a = pd.read_csv('Outcomes-a.txt')# A is the test data 
outcomes_b = pd.read_csv('Outcomes-b.txt')# B is the control Group to ensure we are not overfitting 

"""
Dataset Column Explanations:
- SAPS-I: Simplified Acute Physiology Score I - A severity of illness scoring system
  used in ICUs to assess patient condition and predict mortality risk (higher = sicker)
- SOFA: Sequential Organ Failure Assessment - Measures degree of organ dysfunction
  across 6 organ systems (respiratory, coagulation, liver, cardiovascular, CNS, renal)
- Length_of_stay: Duration of hospital stay in days
- Survival: Days survived after hospital discharge (-1 indicates patient died in hospital)
- In-hospital_death: Binary indicator (1 = died in hospital, 0 = survived to discharge)
- RecordID: Unique patient identifier
"""

print("Outcomes A shape:", outcomes_a.shape)
print("Outcomes B shape:", outcomes_b.shape)
print("\nMissing values in Outcomes A:\n", outcomes_a.isnull().sum())
print("\nMissing values in Outcomes B:\n", outcomes_b.isnull().sum())


# Create analysis plots for key variables in Outcomes A
print("\nCreating analysis plots for Outcomes A...")
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# SAPS-I distribution for Outcomes A
axes[0,0].hist(outcomes_a['SAPS-I'], alpha=0.7, color='blue', bins=20)
axes[0,0].set_title('SAPS-I Distribution (Outcomes A)')
axes[0,0].set_xlabel('SAPS-I Score')
axes[0,0].set_ylabel('Frequency')

# SOFA distribution for Outcomes A
axes[0,1].hist(outcomes_a['SOFA'], alpha=0.7, color='green', bins=20)
axes[0,1].set_title('SOFA Distribution (Outcomes A)')
axes[0,1].set_xlabel('SOFA Score')
axes[0,1].set_ylabel('Frequency')

# Length of stay distribution for Outcomes A
axes[1,0].hist(outcomes_a['Length_of_stay'], alpha=0.7, color='orange', bins=20)
axes[1,0].set_title('Length of Stay Distribution (Outcomes A)')
axes[1,0].set_xlabel('Days')
axes[1,0].set_ylabel('Frequency')

# In-hospital death rate for Outcomes A
death_rate_a = outcomes_a['In-hospital_death'].mean()
survival_rate_a = 1 - death_rate_a
axes[1,1].bar(['Survived', 'Died'], [survival_rate_a, death_rate_a], color=['lightgreen', 'lightcoral'])
axes[1,1].set_title('Survival vs Death Rate (Outcomes A)')
axes[1,1].set_ylabel('Rate')
axes[1,1].set_ylim(0, 1)

plt.tight_layout()
plt.show()