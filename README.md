# AI Tools Lab

A comprehensive Python repository featuring common algorithmic implementations and practical text/data utility functions, created as part of the **Artificial Intelligence Tools and Applications Lab (AGCS 25308)** at **Amritsar Group of Colleges**[cite: 2].

---

## 📌 Project Description

`AI Tools Lab` is a modular Python collection demonstrating fundamental computer science concepts alongside modern AI-assisted software development workflows (using tools like Git, GitHub Copilot, and Claude)[cite: 2]. 

The module provides core functionality split into two main modules:
1. **Sorting Algorithms** (`sorting.py`): Implementations of fundamental sorting routines for performance analysis and algorithmic study[cite: 2].
2. **Utility Functions** (`utils.py`): General-purpose helper utilities for string manipulation and unit conversions[cite: 2].

---

## ⚙️ Installation Instructions

### Prerequisites
* Python 3.8 or higher
* Git

### Steps

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/YOUR_GITHUB_USERNAME/ai-tools-lab.git](https://github.com/YOUR_GITHUB_USERNAME/ai-tools-lab.git)
   cd ai-tools-lab
   ```

2. **Verify installation:**
   Run a quick command to ensure Python is configured properly:
   ```bash
   python3 --version
   ```

---

## 🚀 Usage Examples

### 1. Sorting Algorithms (`sorting.py`)

```python
from sorting import bubble_sort

# Example: Sorting an unsorted list
numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort(numbers)

print("Original List:", numbers)
print("Sorted List:  ", sorted_numbers)
```

### 2. Utility Functions (`utils.py`)

```python
from utils import is_palindrome, count_words, celsius_to_fahrenheit

# Palindrome Check
print(is_palindrome("radar"))  # Output: True

# Word Count
text = "Artificial Intelligence Tools and Applications Lab"
print(count_words(text))  # Output: 6

# Temperature Conversion
celsius = 25
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")  # Output: 25°C is equal to 77.0°F
```

---

## 👥 Contributors

* **Savleen Kaur** – Student, B.Tech CSE, Amritsar Group of Colleges
* **Er. jaspreet singh** – Associate Professor, Department of CSE 

---

