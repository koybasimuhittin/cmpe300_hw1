# CmpeAlgorithm Benchmarking Tool

## Authors
- Muhittin Köybaşı - 2021400162
- Osman Yusuf Tosun - 2021400261

## Overview

The **CmpeAlgorithm Benchmarking Tool** is a Python script designed to evaluate the performance of the `CmpeAlgorithm` function across different input scenarios. It systematically measures execution times for various input sizes and case types, providing insights into the algorithm's efficiency and behavior under different conditions.

## Features

- **Multiple Case Types:** Evaluate the algorithm under Best, Worst, and Average case scenarios.
- **Diverse Input Sizes:** Test the algorithm with a wide range of input sizes to observe scalability.
- **Reproducible Results:** Utilize a fixed seed for random input generation to ensure consistent results across runs.
- **Customizable Attempts:** Specify the number of attempts for Average cases to gather comprehensive performance data.


## Requirements

- **Python Version:** Python 3.6 or higher
- **Standard Libraries:** 
  - `random`
  - `sys`
  - `time`

No external libraries are required.

## Usage

The script is executed via the command line and accepts up to four arguments to customize the benchmarking process.

### Command-Line Arguments

The script can be run with the following optional command-line arguments in the specified order:

1. **Case Type:** (`Best`, `Worst`, `Average`)
2. **Input Size:** An integer representing the size of the input array.
3. **Attempt Count:** An integer specifying the number of attempts (only applicable for the `Average` case).
4. **Seed Value:** An integer to set the random seed for reproducibility.

**Note:** If no arguments are provided, the script uses default values for all parameters.

**Argument Positions:**

| Position | Argument       | Description                                                  |
|----------|----------------|--------------------------------------------------------------|
| 1        | Case Type      | Type of case to test (`Best`, `Worst`, `Average`).           |
| 2        | Input Size     | Size of the input array (integer).                           |
| 3        | Attempt Count  | Number of attempts for the `Average` case (integer).         |
| 4        | Seed Value     | Seed for random number generator (integer).                  |

### Running the Script

Navigate to the directory containing the script and execute it using Python:

```bash
python <student_number>.py [Case_Type] [Input_Size] [Attempt_Count] [Seed_Value]
```

### Examples

1. **Run with Default Settings:**
   ```bash
   python <student_number>.py
   ```
   *Uses all default values for case types, input sizes, attempt count, and seed.*

2. **Run a Specific Case (`Best`):**
   ```bash
   python <student_number>.py Best
   ```
   *Benchmarks only the Best case across all predefined input sizes.*

3. **Run a Specific Case with a Specific Input Size (`Worst` case, size 50):**
   ```bash
   python <student_number>.py Worst 50
   ```
   *Benchmarks the Worst case with an input size of 50.*

4. **Run the `Average` Case with Specific Input Size and Attempt Count:**
   ```bash
   python <student_number>.py Average 100 30
   ```
   *Benchmarks the Average case with an input size of 100 over 30 attempts.*

5. **Run with All Arguments Specified:**
   ```bash
   python <student_number>.py Average 100 30 456
   ```
   *Benchmarks the Average case with an input size of 100, 30 attempts, and a random seed of 456.*


### Output Structure

```
Case: <Case_Type> Size: <Input_Size> Elapsed Time (s): <Average_Time>
	Attempt 1 Elapsed Time (s): <Time1>
	Attempt 2 Elapsed Time (s): <Time2>
	...
```

- **Case:** The type of case being benchmarked (`Best`, `Worst`, `Average`).
- **Size:** The size of the input array.
- **Elapsed Time (s):** The average execution time over all attempts.
- **Attempt Details:** For the `Average` case, each individual attempt's execution time is listed.


## Reproducibility

To ensure that the random input generation is consistent across multiple runs, the script uses a seed value. By default, the seed is set to `123`, but it can be customized via command-line arguments.

**Setting the Seed:**

```bash
python benchmark.py Average 100 30 456
```

In the above command, `456` is the seed value. Using the same seed will generate identical random input arrays, allowing for reproducible benchmarking results.

## Notes

- **Default Values:**
  - **Case Types:** `['Best', 'Worst', 'Average']`
  - **Input Sizes:** `[1, 5, 10, 20, 30, 40, 50, 60, 70, 90, 100, 120, 130, 140, 150, 160, 170]`
  - **Seed:** `123`
  - **Attempt Count:** `20` (applicable only for the `Average` case)
