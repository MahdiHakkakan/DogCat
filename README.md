# DOGCAT

DOGCAT is a system designed to classify images of dogs and cats. While the current version has a few known issues, improvements and updates are in progress.

---

## Features

- Image classification for dogs and cats.
- Data stored in a MongoDB database.
- Code implemented in Python with a Jupyter Notebook for step-by-step execution.

---

## Requirements

Before using this system, make sure you have the following installed:

- Python 3.x
- MongoDB
- Required Python libraries (install via `requirements.txt`)

---

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone <repository_url>
   cd DOGCAT
   ```
2. Install the required Python libraries:

   ```bash 
    pip install -r requirements.txt
   ```
3. Ensure that your MongoDB server is running.
4. Populate your MongoDB database with the dataset by running:
   ```bash
    python3 storing_mongo.py
   ```

---

## Usage

The main code is in a Jupyter Notebook file. Open the notebook using the following command:
```bash
jupyter notebook
```
Run each cell step by step to execute the code.

---

## Licence

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
