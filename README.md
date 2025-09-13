# DAA Codes: Divide and Conquer, Greedy, and Dynamic Programming Algorithms

This repository contains Python implementations of classic algorithms for Design and Analysis of Algorithms (DAA) coursework. The codes cover a variety of problems solved using Divide and Conquer, Greedy, and Dynamic Programming approaches.

## Contents

- `Sorting.py`  
  - **Merge Sort** (Divide and Conquer)
  - **Quick Sort** (Divide and Conquer)
- `kasturba.py`  
  - **Karatsuba Algorithm** for Large Integer Multiplication (Divide and Conquer)
- `knapsack.py`  
  - **0/1 Knapsack Problem** (Greedy approach, for demonstration)
  - **Fractional Knapsack Problem** (Greedy approach, optimal)
- `greedy.py`  
  - **Job Scheduling Problem** (Greedy)
  - **Activity Selection Problem** (Greedy)
- `subsequence.py`  
  - **Longest Common Subsequence (LCS)** (Dynamic Programming)
- `knapsack_dynamic.py`  
  - **0/1 Knapsack Problem** (Dynamic Programming)
- `matrixChain.py`  
  - **Matrix Chain Multiplication** (Dynamic Programming)

## How to Run

Each file is self-contained and can be run directly with Python 3. Example usage and sample input/output are provided in each file.

```bash
python Sorting.py
python kasturba.py
python knapsack.py
python greedy.py
python subsequence.py
python knapsack_dynamic.py
python matrixChain.py
```

## Algorithm Summaries

### Divide and Conquer
- **Merge Sort**: Efficiently sorts an array by recursively dividing and merging.
- **Quick Sort**: Sorts an array by partitioning and recursively sorting subarrays.
- **Karatsuba Algorithm**: Multiplies large integers faster than the traditional method.

### Greedy Algorithms
- **0/1 Knapsack (Greedy)**: Selects items based on value/weight ratio (not always optimal).
- **Fractional Knapsack**: Selects fractions of items for maximum value (optimal).
- **Job Scheduling**: Schedules jobs to maximize profit within deadlines.
- **Activity Selection**: Selects the maximum number of non-overlapping activities.

### Dynamic Programming
- **Longest Common Subsequence (LCS)**: Finds the longest subsequence common to two sequences.
- **0/1 Knapsack (DP)**: Selects items to maximize value without exceeding capacity.
- **Matrix Chain Multiplication**: Finds the most efficient way to multiply a chain of matrices.

## License

This repository is for educational purposes.

---

Feel free to use, modify, and learn from these codes!
