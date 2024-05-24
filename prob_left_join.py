from Levenshtein import distance as levenshtein_distance
import pandas as pd

# Example function to calculate similarity
def calculate_similarity(phone1, phone2):
    max_len = max(len(phone1), len(phone2))
    return 1 - (levenshtein_distance(phone1, phone2) / max_len)

# Example function to assign probability based on similarity
def assign_probability(similarity):
    return max(0, min(1, similarity))

# Data from the tables
personal_info = [
    {"Name": "Faustino Perez Vilar", "Phone": "657-971-5216", "Age": 35, "Race": "Hispanic", "Marital Status": "Now married", "Children": "One or more", "US Citizen": "Yes", "Employed": "Employed"},
    {"Name": "Dhanush Bhagat", "Phone": "440-661-0801", "Age": 69, "Race": "Asian", "Marital Status": "Widowed", "Children": "One or more", "US Citizen": "Yes", "Employed": "Not in labor force"},
    {"Name": "Michelle Lopez", "Phone": "646-987-3061", "Age": 43, "Race": "White non-Hispanic", "Marital Status": "Now married", "Children": "No children", "US Citizen": "Yes", "Employed": "Not in labor force"},
    {"Name": "Katie Crawford", "Phone": "713-195-6688", "Age": 65, "Race": "White non-Hispanic", "Marital Status": "Now married", "Children": "No children", "US Citizen": "Yes", "Employed": "Employed"},
    {"Name": "Jesse Gregory", "Phone": "516-207-6656", "Age": 75, "Race": "Other race", "Marital Status": "Now married", "Children": "No children", "US Citizen": "Yes", "Employed": "Not in labor force"},
    {"Name": "Tony Williamson", "Phone": "817-207-4188", "Age": 44, "Race": "White non-Hispanic", "Marital Status": "Now married", "Children": "One or more", "US Citizen": "Yes", "Employed": "Employed"},
    {"Name": "Sarah Martinez", "Phone": "904-162-7212", "Age": 24, "Race": "White non-Hispanic", "Marital Status": "Never married", "Children": "No children", "US Citizen": "Yes", "Employed": "Unemployed"},
    {"Name": "Valerie Green", "Phone": "731-591-7576", "Age": 39, "Race": "Black non-Hispanic", "Marital Status": "Divorced", "Children": "One or more", "US Citizen": "Yes", "Employed": "Employed"},
    {"Name": "Melissa Robertson", "Phone": "731-591-3185", "Age": 29, "Race": "Black non-Hispanic", "Marital Status": "Now married", "Children": "One or more", "US Citizen": "Yes", "Employed": "Employed"},
    {"Name": "Derrick Jackson", "Phone": "301-487-7489", "Age": 55, "Race": "White non-Hispanic", "Marital Status": "Divorced", "Children": "No children", "US Citizen": "Yes", "Employed": "Employed"},
    {"Name": "Colleen Delacruz", "Phone": "508-374-7320", "Age": 61, "Race": "White non-Hispanic", "Marital Status": "Never married", "Children": "No children", "US Citizen": "Yes", "Employed": "Employed"},
    {"Name": "Prisha Sharaf", "Phone": "303-883-3703", "Age": 36, "Race": "Asian", "Marital Status": "Now married", "Children": "No children", "US Citizen": "No", "Employed": "Employed"},
    {"Name": "Cornelio Santiago Álamo", "Phone": "409-897-2374", "Age": 23, "Race": "Hispanic", "Marital Status": "Now married", "Children": "No children", "US Citizen": "Yes", "Employed": "Employed"},
    {"Name": "Douglas Riley", "Phone": "316-356-5704", "Age": 59, "Race": "White non-Hispanic", "Marital Status": "Now married", "Children": "One or more", "US Citizen": "Yes", "Employed": "Employed"},
    {"Name": "Katie Crawford", "Phone": "531-941-3438", "Age": 25, "Race": "White non-Hispanic", "Marital Status": "Never married", "Children": "One or more", "US Citizen": "Yes", "Employed": "Employed"}
]

additional_info = [
    {"Name": "Faustino Perez Vilar", "Phone": "657-971-5215", "Gender": "Male", "Age": 37, "Education": "HS Grad", "Family Income": "$20K to less than $40K", "Internet Access": "Yes"},
    {"Name": "Dhanush Bhagat", "Phone": "440-661-0801", "Gender": "Female", "Age": 69, "Education": "Postgraduate", "Family Income": "$150K or more", "Internet Access": "Yes"},
    {"Name": "Michelle Lopez", "Phone": "646-987-3061", "Gender": "Female", "Age": 43, "Education": "Less than HS", "Family Income": "$20K to less than $40K", "Internet Access": "No"},
    {"Name": "Katie Crawford", "Phone": "713-195-6689", "Gender": "Female", "Age": 65, "Education": "Some college", "Family Income": "$40K to less than $75K", "Internet Access": "Yes"},
    {"Name": "Jesse Gregory", "Phone": "516-207-6656", "Gender": "Male", "Age": 75, "Education": "Some college", "Family Income": "$40K to less than $75K", "Internet Access": "No"},
    {"Name": "Tony Williamson", "Phone": "817-207-4189", "Gender": "Male", "Age": 44, "Education": "Some college", "Family Income": "$75K to less than $150K", "Internet Access": "Yes"},
    {"Name": "Sarah Martinez", "Phone": "904-162-7212", "Gender": "Female", "Age": 24, "Education": "Some college", "Family Income": "Less than $20K", "Internet Access": "Yes"},
    {"Name": "Valerie Green", "Phone": "731-591-7577", "Gender": "Female", "Age": 39, "Education": "Some college", "Family Income": "$40K to less than $75K", "Internet Access": "Yes"},
    {"Name": "Melissa Robertson", "Phone": "731-591-3185", "Gender": "Female", "Age": 29, "Education": "HS Grad", "Family Income": "Less than $20K", "Internet Access": "Yes"},
    {"Name": "Derrick Jackson", "Phone": "301-487-7480", "Gender": "Male", "Age": 55, "Education": "College grad", "Family Income": "$20K to less than $40K", "Internet Access": "Yes"},
    {"Name": "Colleen Delacruz", "Phone": "508-374-7321", "Gender": "Female", "Age": 61, "Education": "College grad", "Family Income": "$20K to less than $40K", "Internet Access": "Yes"},
    {"Name": "Prisha Sharaf", "Phone": "303-883-3703", "Gender": "Male", "Age": 36, "Education": "Postgraduate", "Family Income": "$150K or more", "Internet Access": "Yes"},
    {"Name": "Kristen Mclean", "Phone": "914-723-0234", "Gender": "Female", "Age": 54, "Education": "Postgraduate", "Family Income": "$150K or more", "Internet Access": "Yes"},
    {"Name": "Cornelio Santiago Álamo", "Phone": "409-897-2375", "Gender": "Male", "Age": 23, "Education": "HS Grad", "Family Income": "$20K to less than $40K", "Internet Access": "No"},
    {"Name": "Douglas Riley", "Phone": "316-356-5704", "Gender": "Male", "Age": 59, "Education": "HS Grad", "Family Income": "Less than $20K", "Internet Access": "Yes"}
]

# Convert lists to DataFrames
df_personal_info = pd.DataFrame(personal_info)
df_additional_info = pd.DataFrame(additional_info)

# Perform the left join with reconciliation based on phone numbers from the first table
joined_data = []

for _, row1 in df_personal_info.iterrows():
    match_found = False
    for _, row2 in df_additional_info.iterrows():
        similarity = calculate_similarity(row1["Phone"], row2["Phone"])
        probability = assign_probability(similarity)
        if probability > 0.85:  # Threshold for considering a match
            joined_row = row1.to_dict()
            joined_row.update(row2.to_dict())
            joined_row["Probability"] = probability
            joined_data.append(joined_row)
            match_found = True
    if not match_found:
        joined_row = row1.to_dict()
        joined_row.update({key: None for key in df_additional_info.columns if key not in joined_row})
        joined_row["Probability"] = None
        joined_data.append(joined_row)

df_joined = pd.DataFrame(joined_data)

df_joined = df_joined.drop(['Phone'], axis=1)

# Save to CSV
output_path = "probabilistic_left_join_result.csv"
df_joined.to_csv(output_path, index=False)

print(f"File saved to {output_path}")
