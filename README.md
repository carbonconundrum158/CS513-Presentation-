DATA ORGANIZATION 


Per-patient file format
Time,Variable,Value
0,HR,82
0,SysABP,120
0,MAP,85
0.5,HR,86
1,SysABP,118
...


Time: hours since ICU admission (floating point). The dataset is already clipped to the first 48 hours.

Variable: short code for a vital sign, lab, or derived measurement (e.g., HR, SysABP, MAP, RespRate, Temp, SpO2, WBC, Hgb, Glucose, Sodium, Creatinine, etc.).

Value: numeric value as text. Some rows may be non-numeric (rare) or blank; handle robustly.