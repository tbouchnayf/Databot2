
# Dictionary of dataset names and DataFrames
datasets = {
    'Customer Transactions': generate_customer_transactions(),
    'Loan Applications': generate_loan_application_dataset(),
    'Customer Accounts': generate_customer_account_dataset(),
    'Credit Card Transactions': generate_credit_card_transactions_dataset(),
    'Customer Support Interactions': generate_customer_support_interactions_dataset()
}

# Generate the catalog
dataset_catalog = catalog_datasets(datasets)

# Print the dataset descriptions along with their attributes and owners
for dataset_name, description in dataset_catalog.items():
    print(f"Dataset: {dataset_name}")
    print(f"Description: {description}\n")
