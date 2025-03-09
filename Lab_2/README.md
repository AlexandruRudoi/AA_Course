# Sorting Algorithm Analysis
### Alexandru Rudoi, FAF-231, Technical University of Moldova

This repository contains an in-depth analysis of various **sorting algorithms**, focusing on their **time complexity, execution performance, and scalability**. The laboratory work involved benchmarking different sorting methods and visualizing their performance to determine their efficiency across different input sizes.

## 📜 Report
For a detailed analysis, refer to the full LaTeX report:
👉 **[Sorting Algorithm Performance Analysis Report](https://github.com/AlexandruRudoi/AA_Course/blob/Lab_2/Lab_2/REPORT.pdf)**

## 📌 Implemented Sorting Algorithms
The following sorting algorithms have been implemented and analyzed:

### **Comparison-Based Sorting Algorithms**
1. **QuickSort (Standard)** (\( O(n \log n) \) avg, \( O(n^2) \) worst) – Efficient but degrades with poor pivot selection.
2. **QuickSort (Optimized)** (\( O(n \log n) \)) – Uses median-of-three pivoting for better performance.
3. **MergeSort (Standard)** (\( O(n \log n) \)) – Stable, efficient for large datasets.
4. **MergeSort (Optimized)** (\( O(n \log n) \)) – Uses insertion sort for small partitions to improve speed.
5. **HeapSort (Standard)** (\( O(n \log n) \)) – Reliable but slower due to frequent memory access.
6. **HeapSort (Optimized)** (\( O(n \log n) \)) – Uses Floyd’s heap construction for better efficiency.

### **Non-Comparison-Based Sorting Algorithm**
7. **Radix Sort (Standard)** (\( O(nk) \)) – Best for large integers, but requires extra space.
8. **Radix Sort (Optimized)** (\( O(nk) \)) – Uses MSD-based sorting for improved performance.

## 📊 Performance Benchmarking
To compare the execution time of different sorting algorithms, **empirical benchmarking** was conducted on randomly generated datasets of varying sizes. The results are presented in **performance tables and graphs** in the report.

### **Empirical Execution Time Table (Random Data)**
| Size  | HeapSort (s) | HeapSort Opt (s) | MergeSort (s) | MergeSort Opt (s) | QuickSort (s) | QuickSort Opt (s) | RadixSort (s) | RadixSort Opt (s) |
|-------|-------------|------------------|---------------|--------------------|---------------|--------------------|---------------|--------------------|
| 10    | 0.000033    | 0.000026         | 0.000028      | 0.000020           | 0.000018      | 0.000140           | 0.000035      | 0.000035           |
| 100   | 0.000274    | 0.000043         | 0.000126      | 0.000080           | 0.000094      | 0.000079           | 0.000076      | 0.000048           |
| 300   | 0.001107    | 0.000124         | 0.000450      | 0.000294           | 0.000315      | 0.000254           | 0.000383      | 0.000127           |
| 1000  | 0.004510    | 0.000569         | 0.001726      | 0.001660           | 0.001020      | 0.001079           | 0.000778      | 0.000430           |
| 5000  | 0.043775    | 0.001790         | 0.014607      | 0.008259           | 0.006205      | 0.010795           | 0.004893      | 0.002142           |
| 10000 | 0.035584    | 0.003557         | 0.025414      | 0.018674           | 0.012507      | 0.026124           | 0.009029      | 0.005336           |
| 50000 | 0.178751    | 0.023716         | 0.145296      | 0.113300           | 0.080032      | 0.101214           | 0.054606      | 0.028066           |
| 100000| 0.482278    | 0.041026         | 0.382493      | 0.265694           | 0.119467      | 0.238067           | 0.158375      | 0.062931           |
| 500000| 3.058232    | 0.213585         | 1.887582      | 1.693795           | 1.050868      | 2.692924           | 1.027429      | 0.771614           |
| 1M    | 7.319163    | 0.511856         | 4.428565      | 3.872083           | 2.318186      | 9.301961           | 2.385705      | 1.910860           |

📊 **For detailed visualizations of execution time trends, check the full report!**

## ⚡ Running the Benchmark
To run the benchmark and compare sorting algorithm performance:

```bash
git clone https://github.com/AlexandruRudoi/AA_Course.git
cd AA_Course/Lab_2
python compare_sorts.py
