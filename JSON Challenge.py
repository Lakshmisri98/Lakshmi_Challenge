import json
import datetime

def transform_string(value):
    value = value.strip()
    if value:
        try:
            timestamp = datetime.datetime.fromisoformat(value.replace("Z", "+00:00")).timestamp()
            return int(timestamp)
        except ValueError:
            return value
    return None

def transform_number(value):
    value = value.strip()
    try:
        if '.' in value:
            return float(value)
        else:
            return int(value)
    except ValueError:
        return None

def transform_boolean(value):
    value = value.strip().lower()
    if value in ['1', 't', 'true', 'true', 't', 'yes', 'y']:
        return True
    elif value in ['0', 'f', 'false', 'false', 'f', 'no', 'n']:
        return False
    return None

def transform_null(value):
    value = value.strip().lower()
    if value in ['1', 't', 'true', 'true', 't', 'yes', 'y']:
        return None
    return None

def transform_list(value):
    transformed_list = []
    for item in value:
        transformed_item = transform_data(item)
        if transformed_item is not None:
            transformed_list.append(transformed_item)
    return transformed_list if transformed_list else None

def transform_data(value):
    if 'S' in value:
        return transform_string(value['S'])
    elif 'N' in value:
        return transform_number(value['N'])
    elif 'BOOL' in value:
        return transform_boolean(value['BOOL'])
    elif 'NULL' in value:
        return transform_null(value['NULL'])
    elif 'L' in value:
        return transform_list(value['L'])
    elif 'M' in value:
        return transform_map(value['M'])
    return None

def transform_map(value):
    transformed_map = {}
    for key, val in sorted(value.items()):
        transformed_key = key.strip()
        transformed_value = transform_data(val)
        if transformed_value is not None:
            transformed_map[transformed_key] = transformed_value
    return transformed_map if transformed_map else None

def transform_input(input_data):
    transformed_output = []
    transformed_item = {}
    
    for key, value in input_data.items():
        if key.strip() == "":
            continue
        transformed_key = key.strip()
        transformed_value = transform_data(value)
        if transformed_value is not None:
            transformed_item[transformed_key] = transformed_value

    if transformed_item:
        transformed_output.append(transformed_item)

    return transformed_output

input_json = """
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
"""

input_data = json.loads(input_json)
output_data = transform_input(input_data)

print(json.dumps(output_data, indent=2))
