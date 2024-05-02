
import openai
import pandas as pd
import os

# Initialize OpenAI API key
openai.api_key = "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"

def generate_dataset_description(metadata):
    """
    Generate a dataset description, attributes, their definitions, and the owner using GPT-3.

    Parameters:
    - metadata (dict): A dictionary with metadata about the dataset.

    Returns:
    - description (str): A generated description of the dataset, attributes, and owner.
    """
    prompt = (f"Write a detailed description for a dataset named '{{metadata['name']}}' "
              f"with the following attributes: {{metadata['attributes']}}. "
              f"The dataset is owned by {{metadata['owner']}}. "
              f"Provide a definition for each attribute.")

    try:
        response = openai.Completion.create(
            model="gpt-3.5-turbo-instruct",
            prompt=prompt,
            temperature=0.7,
            max_tokens=200
        )
        description = response.choices[0].text.strip()
        return description
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def catalog_datasets(datasets):
    """
    Catalogs datasets by generating descriptions and organizing metadata.

    Parameters:
    - datasets (dict): A dictionary where keys are dataset names and values are DataFrames.

    Returns:
    - catalog (dict): A dictionary where keys are dataset names and values are their descriptions.
    """
    catalog = {}

    for dataset_name, dataset_df in datasets.items():
        # Extract metadata from the dataset
        metadata = {
            'name': dataset_name,
            'attributes': list(dataset_df.columns),
            'owner': dataset_df.attrs.get('Owner', 'Unknown')
        }

        # Generate a description for the dataset
        description = generate_dataset_description(metadata)
        if description:
            catalog[dataset_name] = description

    return catalog
