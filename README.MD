# DevX RUN SEAL JSON Transformer

This project implements a JSON transformer that converts a schema-less input JSON into a structured output based on specified transformation rules. The transformation handles various data types such as strings, numbers, booleans, nulls, and lists, and it ensures proper data sanitization and conversion.

## Requirements

- **Python 3.x**  
- No third-party libraries are required, as the solution uses Python's built-in libraries for JSON handling and data type conversion.

## Features

- Converts JSON fields with different types (`S`, `N`, `BOOL`, `NULL`, `L`, `M`) into appropriate Python data types.
- Handles RFC3339 formatted strings and converts them to Unix Epoch time.
- Strips leading and trailing whitespace from values.
- Removes empty keys, invalid fields, and unsupported data types.

## Transformation Rules

The input JSON follows a specific format where each field contains metadata about its type. The solution follows these transformation criteria:

1. **S**: String — Transforms the value into a sanitized string.
2. **N**: Number — Converts the value into a numeric type, stripping leading zeros.
3. **BOOL**: Boolean — Converts truthy values (like `true`, `1`, `t`, etc.) to `True` and falsy values (like `false`, `0`, `f`, etc.) to `False`.
4. **NULL**: Null — Converts values like `true`, `1`, `t`, etc., to `None` (null in Python).
5. **L**: List — Converts lists while filtering out empty strings and invalid types.
6. **M**: Map — Handles nested maps and converts them recursively according to the above rules.

## Local Execution Instructions
   
1. (Optional) Install any necessary dependencies (there are none by default):
   ```bash
   pip install -r requirements.txt
   ```

2. Run the transformer script:
   ```bash
   python transformer.py
   ```

The script will print the transformed output to `stdout`.

## Replit Setup Instructions

1. Import the repository into Replit using the “Import from GitHub” option.

2. After importing, you should see the `transformer.py` script in the Replit file explorer.

3. Press the **Run** button to execute the script. The output will be displayed in the Replit console.

## Processing Time

The time taken to execute the transformation is printed after the script runs. Example:

Processing Time: 0.0025 seconds

## Example

### Input JSON:
{
  "number_1": {
    "N": "1.50"
  },
  "string_1": {
    "S": "784498 "
  },
  "string_2": {
    "S": "2014-07-16T20:55:46Z"
  },
  "map_1": {
    "M": {
      "bool_1": {
        "BOOL": "truthy"
      },
      "null_1": {
        "NULL ": "true"
      },
      "list_1": {
        "L": [
          {
            "S": ""
          },
          {
            "N": "011"
          },
          {
            "N": "5215s"
          },
          {
            "BOOL": "f"
          },
          {
            "NULL": "0"
          }
        ]
      }
    }
  },
  "list_2": {
    "L": "noop"
  },
  "list_3": {
    "L": [
      "noop"
    ]
  },
  "": {
    "S": "noop"
  }
}

### Output JSON:
[
  {
    "number_1": 1.5,
    "string_1": "784498",
    "string_2": 1405544146,
    "map_1": {
      "list_1": [
        11,
        false
      ]
    }
  }
]
