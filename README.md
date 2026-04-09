# predictive-nps-modeling

# Predictive Modeling of Fan Satisfaction (NPS)

## Overview
This project develops a predictive model to estimate **Net Promoter Score (NPS)** for sporting events using operational and contextual data.

The goal is to identify the key drivers of fan satisfaction and enable teams to proactively improve the fan experience.

---

## Business Problem

Fan satisfaction is influenced by multiple factors, including:
- Team performance  
- Attendance and crowding  
- Operational execution  

However, these drivers are not always clearly quantified.

This project answers:
- What factors most strongly influence NPS?
- Can we predict satisfaction before an event occurs?
- How can teams use these insights?

---

## Data Sources

- Post-event survey responses (NPS)  
- Attendance (turnstile / scans)  
- Game context (date, time)  
- Environmental variables (temperature)  

---

## Feature Engineering

Key features included:

- **Win Percentage (W%)** – proxy for team performance  
- **Attendance** – proxy for crowd size  
- **Game Timing** – weekday vs weekend  
- **Temperature**  

Highly correlated variables were excluded to improve model clarity.

---

## Modeling Approach

- Regression-based modeling in Python  
- Focus on interpretability and feature impact  
- Train/test split for evaluation  

---

## Key Insights

- Team performance was the strongest driver of NPS  
- Attendance had a measurable impact on satisfaction  
- Operational variables influenced specific experience areas  

---

## Impact

- Enabled forecasting of fan satisfaction  
- Supported operational and staffing decisions  
- Provided a foundation for future predictive modeling  

---

## Tools & Technologies

- Python (Pandas, Scikit-learn)  
- SQL  
- Power BI  

---

## Future Enhancements

- Classification modeling (Promoter vs Detractor)  
- Real-time prediction  
- Expanded feature set  
