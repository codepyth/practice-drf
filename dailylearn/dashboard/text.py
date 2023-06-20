import pandas as pd
from fuzzywuzzy import fuzz

# Load the small file
small_file = pd.read_csv('coffee_sample_companies_TX.csv', encoding='ISO-8859-1', low_memory=False)

# Load the large file
large_file = pd.read_csv('large_file.csv')

# Define the matching threshold
threshold = 80

# Loop through each company name in the small file
for company_name in small_file['Company Name']:
    # Initialize the best match
    best_match = None
    best_match_score = 0

    # Loop through each company name in the large file
    for large_company_name in large_file['Company Name']:
        # Calculate the similarity score
        score = fuzz.token_set_ratio(company_name, large_company_name)

        # Update the best match if necessary
        if score > best_match_score and score >= threshold:
            best_match = large_company_name
            best_match_score = score

    # Print the result
    if best_match is None:
        print(f"No match found for {company_name}")
    else:
        print(f"Match found for {company_name}: {best_match} ({best_match_score}%)")
