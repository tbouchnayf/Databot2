Data Generation and Analysis Tools

This repository contains a collection of Python scripts designed to generate synthetic datasets for various types of banking transactions and customer interactions, extract data catalog fom these datasets using OpenAI's GPT-3 model, use this catalogs as base knowledge to interact through a Gradio-based interface to interact with the datasets descriptions dynamically.

Features

Synthetic Data Generation: Generates realistic datasets for customer transactions, loan applications, customer accounts, credit card transactions, and customer support interactions.
Dataset Description: Utilizes OpenAI's GPT-3.5-turbo-instruct model to generate rich descriptions of each dataset including attributes, their definitions, and ownership details.
Interactive Web Interface: Gradio interface that allows users to query and receive explanations about datasets and their contents.
Getting Started

Prerequisites
Before you can run these scripts, you'll need to install several Python libraries. Ensure you have Python installed on your system, then run:

bash
Copy code
pip install pandas numpy Faker gradio openai
Installation
Clone this repository to your local machine to get started:

bash
Copy code
git clone https://github.com/yourusername/yourrepository](https://github.com/tbouchnayf/Databot2.git
Usage
Run the main script to generate datasets and launch the Gradio interface:

python
Copy code
python main_script.py
This will start a local web server typically accessible via http://127.0.0.1:7860, where you can interact with the dataset descriptions.

Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request
License

This project is licensed under the MIT License - see the LICENSE.md file for details.

Authors

Tarik Bouchnayaf

