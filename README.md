# SAS to CSV Converter

This project contains a Python script that converts a `.sas7bdat` file to a `.csv` file using the `pandas` and `sas7bdat` libraries.

## Requirements

Before running the script, ensure you have the necessary Python packages installed. You can install them using `pip`:

```sh
pip install pandas sas7bdat
```

## Script Overview

The script performs the following tasks:

1. Reads a `.sas7bdat` file using the `sas7bdat` library.
2. Converts the data to a `pandas` DataFrame.
3. Saves the DataFrame as a `.csv` file with UTF-8 encoding.

## Usage

1. Define the input `.sas7bdat` file path and the output `.csv` file path in the script:
    ```python
    input_file = 'qpm0rlb61x6ixroi7.sas7bdat'
    output_file = 'qpm0rlb61x6ixroi7.csv'
    ```

2. Run the script:
    ```sh
    python convert_sas_to_csv.py
    ```

3. The script will read the specified `.sas7bdat` file, convert it to a `.csv` file, and save it to the specified output path. If successful, a message will be printed to the console:
    ```
    文件已成功转换并保存为 qpm0rlb61x6ixroi7.csv
    ```

## Example

Here's an example of how the script can be used:

```python
import pandas as pd
from sas7bdat import SAS7BDAT

# Define the input .sas7bdat file path and the output .csv file path
input_file = 'qpm0rlb61x6ixroi7.sas7bdat'
output_file = 'qpm0rlb61x6ixroi7.csv'

# Read the .sas7bdat file using SAS7BDAT
with SAS7BDAT(input_file) as reader:
    df = reader.to_data_frame()

# Save the DataFrame as a .csv file with UTF-8 encoding
df.to_csv(output_file, index=False, encoding='utf-8')

print(f'文件已成功转换并保存为 {output_file}')
```

## Notes

- Ensure that the input file path and output file path are correctly specified.
- The script saves the `.csv` file with UTF-8 encoding to prevent any character encoding issues.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
