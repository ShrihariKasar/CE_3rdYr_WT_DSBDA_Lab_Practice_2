# Computer Engineering 3rd Year Lab Practicals

This repository contains code and practice files for **Web Technologies**, **DSBDA (Data Science and Big Data Analytics)**, and **Lab Practice** in **Python**. These labs are designed for 3rd Year Computer Engineering students. The code and exercises are implemented in different environments like VS Code for Python and Jupyter Notebooks for DSBDA.

## Table of Contents

<!-- - [Web Technologies Lab](#web-technologies-lab) -->

- [DSBDA Lab](#dsbda-lab)
- [Lab Practice (Python)](#lab-practice-python)
- [Creating a New Jupyter Notebook](#creating-a-new-jupyter-notebook)
- [Uploading Files to Jupyter Notebook](#uploading-files-to-jupyter-notebook)
- [Reading a CSV File in Jupyter Notebook](#reading-a-csv-file-in-jupyter-notebook)

---

<!-- ## Web Technologies Lab

This section contains the exercises and code for **Web Technologies**. The code is implemented using **HTML, CSS, JavaScript**, and **Backend Technologies (Node.js, Flask)**.

### How to Run the Web Technologies Code

1. **Install Dependencies**:
   - Make sure you have **Node.js** installed on your system. You can download it from [here](https://nodejs.org/).
   - For Flask-based projects, you need to install **Flask** using pip. Run the following command:
     ```bash
     pip install Flask
     ```
   
2. **Run the Node.js Code (if applicable)**:
   - Navigate to the folder where the project is located and run:
     ```bash
     npm install
     npm start
     ```
   - This will start the backend server, usually on `http://localhost:3000` or a similar port.

3. **Run the Flask Code (if applicable)**:
   - Navigate to the Flask project folder and start the application with the following command:
     ```bash
     flask run
     ```
   - This will start the Flask development server, usually on `http://127.0.0.1:5000`.

4. **Open the Project in the Browser**:
   - After running the above steps, open the browser and navigate to `http://localhost:3000` (for Node.js) or `http://127.0.0.1:5000` (for Flask).

--- -->

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

## Lab Practice (Python)

This section contains Python-based lab practice exercises which are best run in **VS Code**.

### How to Run the Python Code in VS Code

1. **Install Python**:
   - Make sure Python is installed on your system. You can download it from [here](https://www.python.org/downloads/).

2. **Install VS Code**:
   - If you haven't already, install **Visual Studio Code (VS Code)** from [here](https://code.visualstudio.com/Download).

3. **Open the Python Code**:
   - Open **VS Code** and open the folder that contains the Python code files.

4. **Install Dependencies (if any)**:
   - If the project requires additional libraries (like `numpy`, `pandas`, etc.), you can install them using:
     ```bash
     pip install -r requirements.txt
     ```
   - Make sure that the required libraries are mentioned in the `requirements.txt` file.

5. **Run the Python Code**:
   - To run a Python file, open it in **VS Code** and click the **Run** button or use the **Terminal** in VS Code:
     ```bash
     python filename.py
     ```

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

## Contributing

Feel free to fork this repository, make changes, and submit pull requests. If you encounter any issues or have suggestions for improvements, please open an issue in the **Issues** section.

---

## License

This repository is licensed under the MIT License. See the LICENSE file for more information.
