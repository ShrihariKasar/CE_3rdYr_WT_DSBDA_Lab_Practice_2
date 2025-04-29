# Computer Engineering 3rd Year Lab Practicals

This repository contains code and practice files for **Web Technologies**, **DSBDA (Data Science and Big Data Analytics)**, and **Lab Practice** in **Python**. These labs are designed for 3rd Year Computer Engineering students. The code and exercises are implemented in different environments like VS Code for Python and Jupyter Notebooks for DSBDA.

## DSBDA Lab (Data Science and Big Data Analytics)

This section contains the **DSBDA** lab exercises implemented in **Jupyter Notebook**.

### How to Run the DSBDA Code

1. **Install Jupyter Notebook**:
   - First, install **Jupyter Notebook** using pip if it's not already installed:
     ```bash
     pip install notebook
     ```

2. **Open the Jupyter Notebook**:
   - Navigate to the folder where the Jupyter Notebook file is located and run the following command:
     ```bash
     jupyter notebook
     ```
   - This will open the Jupyter Notebook interface in your browser, usually at `http://localhost:8888`.

3. **Run the Notebook**:
   - Open the desired `.ipynb` file from the Jupyter interface.
   - Execute the cells step by step using the **Shift + Enter** command.

---
## Creating a New Jupyter Notebook

To create a new Jupyter Notebook:

1. **Launch Jupyter Notebook**:
   - Open a terminal or command prompt and navigate to the directory where you want to create the new notebook.

2. **Create a New Notebook**:
   - Type the following command to launch Jupyter Notebook:
     ```bash
     jupyter notebook
     ```
   - This will open Jupyter in your default web browser.
   - In the Jupyter interface, click on **New** > **Python 3** to create a new notebook.

3. **Save the Notebook**:
   - Once the notebook is open, you can start writing and running Python code. Save your notebook regularly using **File** > **Save and Checkpoint**.

---

## Uploading Files to Jupyter Notebook

To upload a file to Jupyter Notebook:

1. **Open Jupyter Notebook**:
   - Launch Jupyter Notebook in the desired directory (as mentioned above).

2. **Upload a File**:
   - In the Jupyter interface, click on the **Upload** button on the right side of the screen.
   - Select the file you wish to upload from your computer and click **Open**.
   - After the upload is complete, the file will appear in your Jupyter Notebook interface.

---

## Reading a CSV File in Jupyter Notebook

To read a **CSV** file in Jupyter Notebook:

1. **Install Pandas** (if not already installed):
   - If you don’t have **pandas** installed, run the following command:
     ```bash
     pip install pandas
     ```

2. **Import Pandas**:
   - Add the following import statement to your notebook:
     ```python
     import pandas as pd
     ```

3. **Read the CSV File**:
   - Use the `pd.read_csv()` function to read the CSV file:
     ```python
     df = pd.read_csv('path/to/your/file.csv')
     ```

4. **Display the Data**:
   - To view the first few rows of the CSV file, use:
     ```python
     df.head()
     ```

   - Make sure the path you provide to `read_csv()` is correct. If the file is in the same directory as the notebook, simply use `'filename.csv'`. If it’s in a different folder, provide the relative or absolute path, e.g., `'data/myfile.csv'`.

---

## ✅ 1st.ipynb – Iris Dataset EDA

### 📝 Objective
Perform exploratory data analysis (EDA) on the Iris dataset to understand data structure, summary statistics, and feature correlations.

### 🔧 Key Operations
- Load the dataset using `pandas`.
- Display dataset head, check for null values, and describe statistics.
- Clean column names and inspect data types.
- Analyze correlation between numerical features.
- Visualize the distribution of Sepal Length using a histogram.

### 📚 Libraries Used
- `pandas`
- `numpy`
- `seaborn`
- `matplotlib`

### 📈 Output
- Summary of dataset including shape, null values, and data types.
- Value counts for species.
- Correlation matrix.
- Histogram of Sepal Length.

---

## ✅ 2nd.ipynb – Data Cleaning & Normalization

### 📝 Objective
Create a dataset, handle missing data, remove outliers, and normalize scores using StandardScaler and PowerTransformer.

### 🔧 Key Operations
- Created a sample student performance dataset.
- Saved and read it from a CSV.
- Handled missing values using mean imputation.
- Removed outliers using Z-score filtering.
- Normalized the data using:
  - StandardScaler
  - PowerTransformer
- Visualized the normalized Math Scores.

### 📚 Libraries Used
- `pandas`
- `numpy`
- `scipy.stats.zscore`
- `seaborn`
- `sklearn.preprocessing`

### 📈 Output
- Clean and standardized dataset.
- Histogram showing distribution of transformed Math scores.

---
# DO SAME FOR REST

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. If you encounter any issues or have suggestions for improvements, please open an issue in the **Issues** section.

---

## License

This repository is licensed under the MIT License. See the LICENSE file for more information.
