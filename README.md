# Design and Analysis of Algorithms

A comprehensive collection of algorithm implementations in both **C++** and **Python**, covering fundamental concepts from sorting and searching to dynamic programming and greedy algorithms.

## 📚 Table of Contents

- [Overview](#overview)
- [Experiments](#experiments)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
- [Running the Programs](#running-the-programs)
- [Algorithm Complexity](#algorithm-complexity)
- [Project Structure](#project-structure)
- [Contributing](#contributing)

## 🎯 Overview

This repository contains implementations of classic algorithms and data structure problems, organized as practical experiments. Each algorithm is implemented in both C++ and Python, making it accessible for learners familiar with either language.

### Key Features

✨ **Dual Implementation**: Every algorithm available in both C++ and Python  
📖 **Well-Documented**: Clear comments and readable code structure  
🎓 **Educational**: Perfect for learning algorithm design paradigms  
⚡ **Executable**: All programs are ready to compile/run  
🔍 **Comprehensive**: Covers multiple algorithm design techniques

## 🧪 Experiments

### Experiment 1: Sorting Algorithms
Implementation of fundamental sorting techniques with O(n²) complexity.

| Algorithm | Time Complexity | Space Complexity | Stable |
|-----------|----------------|------------------|---------|
| Bubble Sort | O(n²) | O(1) | Yes |
| Insertion Sort | O(n²) | O(1) | Yes |
| Selection Sort | O(n²) | O(1) | No |
| Counting Sort | O(n+k) | O(k) | Yes |

**Files**: `bubble_sort`, `insertion_sort`, `selection_sort`, `counting_sort`

---

### Experiment 2: Searching Algorithms
Classic search techniques for finding elements in arrays.

| Algorithm | Time Complexity | Requirement |
|-----------|----------------|-------------|
| Linear Search | O(n) | None |
| Binary Search | O(log n) | Sorted array |

**Files**: `linear_search`, `binary_search`

---

### Experiment 3: Exponential Function
Multiple approaches to compute x^n with varying time complexities.

- **Iterative Approach**: O(n) - Simple loop-based multiplication
- **Recursive D&C O(n)**: O(n) - Divide and conquer with recursion
- **Optimized D&C O(log n)**: O(log n) - Efficient divide and conquer

**Files**: `exponential`

---

### Experiment 4: Divide & Conquer Sorting
Advanced sorting algorithms using the divide and conquer paradigm.

| Algorithm | Avg. Time | Worst Time | Space | Stable |
|-----------|-----------|------------|-------|---------|
| Merge Sort | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n²) | O(log n) | No |

**Files**: `merge_sort`, `quick_sort`

---

### Experiment 5: Karatsuba Multiplication
Fast multiplication algorithm using divide and conquer approach.

- **Complexity**: O(n^1.585) - Better than traditional O(n²) multiplication
- **Application**: Large number multiplication

**Files**: `karatsuba_multiplication`

---

### Experiment 6: Knapsack Problem (Greedy Approach)
Two variants of the classic knapsack optimization problem.

| Variant | Approach | Optimal Solution |
|---------|----------|------------------|
| 0/1 Knapsack | Greedy (Recursive) | Not guaranteed |
| Fractional Knapsack | Greedy | Yes |

**Files**: `0 by 1 Knapsack`, `Fractional Knapsack`

---

### Experiment 7: Greedy Algorithms Applications
Real-world applications of the greedy approach.

- **Activity Selection**: Select maximum non-overlapping activities - O(n log n)
- **Job Scheduling**: Maximize profit with deadlines - O(n²)

**Files**: `activity_selection`, `job_scheduling`

---

### Experiment 8: Longest Common Subsequence (LCS)
Dynamic programming solution for finding the longest subsequence common to two strings.

- **Complexity**: O(m × n) time, O(m × n) space
- **Application**: DNA sequence alignment, diff algorithms, version control

**Files**: `longest_common_subsequence`

---

### Experiment 9: 0/1 Knapsack (Dynamic Programming)
Optimal solution for the 0/1 knapsack problem using dynamic programming.

- **Complexity**: O(n × W) time, O(n × W) space
- **Guarantee**: Finds optimal solution

**Files**: `0 by 1 Knapsack using dynamic programming`

---

### Experiment 10: Matrix Chain Multiplication
Find the optimal way to multiply a chain of matrices to minimize scalar multiplications.

- **Complexity**: O(n³) time, O(n²) space
- **Output**: Minimum multiplications and optimal parenthesization

**Files**: `chain_matrix_multiplication`

---

## 💻 Technologies

### Languages
- **C++** (C++11 or later recommended)
- **Python** (Python 3.6+)

### Compilers & Interpreters
- **C++**: g++, clang++, MSVC
- **Python**: CPython 3.x

## 🚀 Getting Started

### Prerequisites

**For C++:**
```bash
# Install g++ compiler (Linux/Mac)
sudo apt-get install g++  # Ubuntu/Debian
brew install gcc          # macOS

# Verify installation
g++ --version
```

**For Python:**
```bash
# Python 3 should be pre-installed on most systems
python3 --version

# If not installed (Ubuntu/Debian)
sudo apt-get install python3
```

### Clone the Repository

```bash
git clone https://github.com/Chanevan317/Design-and-Analysis-of-Algorithms.git
cd Design-and-Analysis-of-Algorithms
```

## ▶️ Running the Programs

### Running C++ Programs

```bash
# Navigate to the experiment folder
cd "Exp 1 Sorting Agorithms"

# Compile the program
g++ bubble_sort.cpp -o output/bubble_sort

# Run the compiled program
./output/bubble_sort
```

**One-liner compile and run:**
```bash
g++ bubble_sort.cpp -o output/bubble_sort && ./output/bubble_sort
```

### Running Python Programs

```bash
# Navigate to the experiment folder
cd "Exp 1 Sorting Agorithms"

# Run the Python program
python3 bubble_sort.py
```

### Example Usage

**Bubble Sort Example:**
```bash
cd "Exp 1 Sorting Agorithms"
python3 bubble_sort.py

# Sample Input:
# Enter the size of the array: 5
# Enter the elements of the array
# - Element 1: 64
# - Element 2: 34
# - Element 3: 25
# - Element 4: 12
# - Element 5: 22

# Output:
# Your array: 64 34 25 12 22
# Bubble Sorted array: 12 22 25 34 64
```

## 📊 Algorithm Complexity

### Sorting Algorithms Comparison

```
Algorithm          | Best Time  | Avg Time   | Worst Time | Space   | Stable
-------------------|------------|------------|------------|---------|--------
Bubble Sort        | O(n)       | O(n²)      | O(n²)      | O(1)    | Yes
Insertion Sort     | O(n)       | O(n²)      | O(n²)      | O(1)    | Yes
Selection Sort     | O(n²)      | O(n²)      | O(n²)      | O(1)    | No
Counting Sort      | O(n+k)     | O(n+k)     | O(n+k)     | O(k)    | Yes
Merge Sort         | O(n log n) | O(n log n) | O(n log n) | O(n)    | Yes
Quick Sort         | O(n log n) | O(n log n) | O(n²)      | O(log n)| No
```

### Algorithm Design Paradigms

| Paradigm | Experiments | Key Characteristic |
|----------|-------------|-------------------|
| **Brute Force** | Exp 1, 2 | Try all possibilities |
| **Divide & Conquer** | Exp 3, 4, 5 | Break into subproblems |
| **Greedy** | Exp 6, 7 | Make locally optimal choices |
| **Dynamic Programming** | Exp 8, 9, 10 | Solve overlapping subproblems |

## 📁 Project Structure

```
Design-and-Analysis-of-Algorithms/
│
├── Exp 1 Sorting Agorithms/
│   ├── bubble_sort.cpp
│   ├── bubble_sort.py
│   ├── counting_sort.cpp
│   ├── counting_sort.py
│   ├── insertion_sort.cpp
│   ├── insertion_sort.py
│   ├── selection_sort.cpp
│   ├── selection_sort.py
│   └── output/
│
├── Exp 2 Searching Algorithms/
│   ├── binary_search.cpp
│   ├── binary_search.py
│   ├── linear_search.cpp
│   ├── linear_search.py
│   └── output/
│
├── Exp 3 Exponential Function/
│   ├── exponential.cpp
│   ├── exponential.py
│   └── output/
│
├── Exp 4 Sorting Algorithm using D&C approach/
│   ├── merge_sort.cpp
│   ├── merge_sort.py
│   ├── quick_sort.cpp
│   ├── quick_sort.py
│   └── output/
│
├── Exp 5 Application-based Algorithm using D&C Approach/
│   ├── karatsuba_multiplication.cpp
│   ├── karatsuba_multiplication.py
│   └── output/
│
├── Exp 6 Knapsack Problem using Greedy Approach/
│   ├── 0 by 1 Knapsack.cpp
│   ├── 0 by 1 Knapsack.py
│   ├── Fractional Knapsack.cpp
│   ├── Fractional Knapsack.py
│   └── output/
│
├── Exp 7 Application-based Algorithms using Greedy Approach/
│   ├── activity_selection.cpp
│   ├── activity_selection.py
│   ├── job_scheduling.cpp
│   ├── job_scheduling.py
│   └── output/
│
├── Exp 8 Longest Common Sub-sequence using Dynamic Programming Approach/
│   ├── longest_common_subsequence.cpp
│   ├── longest_common_subsequence.py
│   └── output/
│
├── Exp 9 0_1 Knapsack Problem using Dynamic Programming Approach/
│   ├── 0 by 1 Knapsack using dynamic programming.cpp
│   ├── 0 by 1 Knapsack using dynamic programming.py
│   └── output/
│
├── Exp 10 Matrix Chain Multiplication using Dynamic Programming Approach/
│   ├── chain_matrix_multiplication.cpp
│   ├── chain_matrix_multiplication.py
│   └── output/
│
└── README.md
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a new branch (`git checkout -b feature/improvement`)
3. **Commit** your changes (`git commit -am 'Add new feature'`)
4. **Push** to the branch (`git push origin feature/improvement`)
5. **Open** a Pull Request

### Contribution Ideas
- Add test cases for algorithms
- Implement additional algorithms
- Optimize existing implementations
- Improve documentation
- Add visualization tools
- Create performance benchmarks

## 📝 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- Classic algorithm designs from foundational computer science texts
- Implementations inspired by academic curriculum
- Community contributions and feedback

## 📧 Contact

**Repository Owner**: Ashutosh Kumar Singh
**Email**: ashutoshhjp1067@gmail.com 
---

<div align="center">

### ⭐ Star this repository if you found it helpful!

**Happy Coding! 🚀**

Made with ❤️ for algorithm enthusiasts

</div>
