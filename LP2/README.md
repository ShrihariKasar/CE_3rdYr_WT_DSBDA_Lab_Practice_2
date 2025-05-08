# Computer Engineering 3rd Year Lab Practicals

This repository contains code and practice files for **Web Technologies**, **DSBDA (Data Science and Business Data Analytics)**, and **Lab Practice** in **Python**. These labs are designed for 3rd Year Computer Engineering students. The code and exercises are implemented in different environments like VS Code for Python and Jupyter Notebooks for DSBDA.

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

# 🔍 LP2 Python Programs

This README provides concise explanations for each Python program in the LP2 folder. Each script implements a key algorithm or data structure concept.

---

## ✅ `1stbfs.py` – Breadth-First Search (BFS)

### 🔧 Description:
Implements BFS traversal for a user-defined graph using a queue and recursion.

### 💡 Key Concepts:
- Uses `deque` from `collections` for queue implementation.
- Accepts graph edges and start node from the user.
- Tracks visited nodes to avoid cycles.

---

## ✅ `1stdfs.py` – Depth-First Search (DFS)

### 🔧 Description:
Performs DFS traversal recursively on a user-input graph.

### 💡 Key Concepts:
- User builds the graph via input.
- DFS is implemented using recursion.
- Visited nodes tracked using a set.

---

## ✅ `2nd.py` – Tic-Tac-Toe A* heuristic-based game

---

## ✅ `3rd.py` – Implement Greedy search algorithm for Job Scheduling Problem application



## ✅ `4th.py` – N-Queens Problem (Backtracking)

### 🔧 Description:
Solves the N-Queens problem using backtracking.

### 💡 Key Concepts:
- Places queens row by row ensuring no conflicts (same column/diagonal).
- Recursively attempts valid placements.
- Outputs all possible board configurations.

---

## ✅ `5th.py` – Fractional Knapsack Problem

### 🔧 Description:
Solves the fractional knapsack problem using a greedy approach.

### 💡 Key Concepts:
- Items sorted based on value/weight ratio.
- Takes full or fractional part of the most valuable item until the knapsack is full.
- Maximizes total value.

---

## 📁 Upcoming Scripts in:
- `6th/`, `7th/`, `8th/`, `9th/`: These directories contain Clound Computing Practicals

---


## Contributing

Feel free to fork this repository, make changes, and submit pull requests. If you encounter any issues or have suggestions for improvements, please open an issue in the **Issues** section.

---

## License

This repository is licensed under the MIT License. See the LICENSE file for more information.
