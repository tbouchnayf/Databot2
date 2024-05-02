#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize Faker to generate random data

fake = Faker()

def generate_customer_transactions(num_records=100, owner="Alice Johnson"):
    data = {
        "Transaction ID": [f"T{1000+i}" for i in range(num_records)],
        "Customer ID": [random.randint(10000, 99999) for _ in range(num_records)],
        "Date and Time": [fake.date_time_this_year() for _ in range(num_records)],
        "Transaction Amount": np.random.uniform(10, 5000, num_records).round(2),
        "Transaction Type": [random.choice(["Deposit", "Withdrawal", "Payment"]) for _ in range(num_records)],
        "Merchant/Recipient": [fake.company() if random.choice([True, False]) else None for _ in range(num_records)],
        "Category": [random.choice(["Groceries", "Utilities", "Entertainment", "Dining", "Other"]) for _ in range(num_records)],
        "Account Balance after Transaction": np.random.uniform(1000, 10000, num_records).round(2)
    }

    df = pd.DataFrame(data)
    # Adding metadata about the owner
    df.attrs['Owner'] = owner

    return df


def generate_loan_application_dataset(num_records=100, owner="John Doe"):
    data = {
        "Application ID": [f"A{1000+i}" for i in range(num_records)],
        "Customer ID": [random.randint(10000, 99999) for _ in range(num_records)],
        "Loan Amount": np.random.uniform(5000, 50000, num_records).round(2),
        "Loan Term": [random.choice([12, 24, 36, 48, 60]) for _ in range(num_records)],
        "Interest Rate": np.random.uniform(1.5, 5.5, num_records).round(2),
        "Loan Purpose": [random.choice(["Home", "Education", "Personal", "Auto"]) for _ in range(num_records)],
        "Credit Score": np.random.randint(300, 850, num_records),
        "Employment Status": [random.choice(["Employed", "Self-employed", "Unemployed", "Student"]) for _ in range(num_records)],
        "Annual Income": np.random.uniform(20000, 150000, num_records).round(2),
        "Debt-to-Income Ratio": np.random.uniform(0, 1, num_records).round(2),
        "Application Status": [random.choice(["Approved", "Denied"]) for _ in range(num_records)]
    }

    df = pd.DataFrame(data)
    # Adding metadata about the owner
    df.attrs['Owner'] = owner

    return df


def generate_customer_account_dataset(num_records=100, owner="Alex Smith"):
    data = {
        "Account ID": [f"AC{10000+i}" for i in range(num_records)],
        "Customer ID": [random.randint(10000, 99999) for _ in range(num_records)],
        "Account Type": [random.choice(["Savings", "Checking"]) for _ in range(num_records)],
        "Account Opening Date": [fake.date_between(start_date="-10y", end_date="today") for _ in range(num_records)],
        "Current Balance": np.random.uniform(100, 100000, num_records).round(2),
        "Interest Rate": np.random.uniform(0.01, 0.05, num_records).round(2),
        "Overdraft Limit": [random.choice([0, 500, 1000, 1500, 2000]) for _ in range(num_records)],
        "Account Status": [random.choice(["Active", "Closed"]) for _ in range(num_records)]
    }

    df = pd.DataFrame(data)
    # Adding metadata about the owner
    df.attrs['Owner'] = owner

    return df


def generate_credit_card_transactions_dataset(num_records=100, owner="Charlie Brown"):
    data = {
        "Transaction ID": [f"T{2000+i}" for i in range(num_records)],
        "Card Number": [fake.credit_card_number(card_type=None) for _ in range(num_records)],
        "Customer ID": [random.randint(10000, 99999) for _ in range(num_records)],
        "Date and Time": [fake.date_time_this_year() for _ in range(num_records)],
        "Amount": np.random.uniform(10, 1000, num_records).round(2),
        "Merchant": [fake.company() for _ in range(num_records)],
        "Location": [fake.city() for _ in range(num_records)],
        "MCC (Merchant Category Code)": [fake.bban() for _ in range(num_records)],
        "Fraud Flag": [random.choice([True, False]) for _ in range(num_records)]
    }

    df = pd.DataFrame(data)
    # Adding metadata about the owner
    df.attrs['Owner'] = owner

    return df


def generate_customer_support_interactions_dataset(num_records=100, owner="David Charles"):
    data = {
        "Interaction ID": [f"I{3000+i}" for i in range(num_records)],
        "Customer ID": [random.randint(10000, 99999) for _ in range(num_records)],
        "Date and Time": [fake.date_time_this_year() for _ in range(num_records)],
        "Channel": [random.choice(["Phone", "Email", "Online Chat"]) for _ in range(num_records)],
        "Query Type": [random.choice(["Account Inquiry", "Transaction Issue", "Loan Service", "General Question"]) for _ in range(num_records)],
        "Response Time (min)": np.random.randint(1, 60, num_records),
        "Resolution Status": [random.choice(["Resolved", "Escalated", "Pending"]) for _ in range(num_records)],
        "Agent ID": [random.randint(100, 999) for _ in range(num_records)]
    }

    df = pd.DataFrame(data)
    # Adding metadata about the owner
    df.attrs['Owner'] = owner

    return df

