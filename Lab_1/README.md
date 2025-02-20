# Fibonacci Algorithm Analysis
### Alexandru Rudoi, FAF-231, Technical University of Moldova

This repository contains an in-depth analysis of various Fibonacci computation methods, focusing on their **time complexity, execution performance, and scalability**. The laboratory work involved benchmarking different algorithms and visualizing their performance to understand their efficiency.

## 📜 Report
For a detailed analysis, refer to the full LaTeX report:
👉 **[Fibonacci Performance Analysis Report](https://github.com/AlexandruRudoi/AA_Course/blob/Lab_1/Lab_1/REPORT.pdf)**

## 📌 Implemented Methods
The following Fibonacci computation methods have been implemented and analyzed:
1. **Recursive Method** (\( O(2^n) \)) – Naïve recursion, highly inefficient.
2. **Memoization (Top-Down DP)** (\( O(n) \)) – Recursion with caching.
3. **Bottom-Up DP** (\( O(n) \)) – Iterative dynamic programming approach.
4. **Space-Optimized DP** (\( O(n) \)) – Reduced memory usage.
5. **Matrix Exponentiation** (\( O(\log n) \)) – Uses matrix power computation.
6. **Fast Doubling** (\( O(\log n) \)) – Most efficient approach for large \( n \).
7. **Binet’s Formula** (\( O(1) \)) – Direct formula, but imprecise for \( n > 70 \).

## 📊 Performance Benchmarking
To compare the execution time of different methods, a benchmarking script was developed, generating **performance graphs** based on real execution times.

### **Running the Benchmark**
To run the benchmark and visualize the performance comparison:

```bash
git clone https://github.com/AlexandruRudoi/AA_Course.git
cd AA_Course
python main_benchmark.py
