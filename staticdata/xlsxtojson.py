import pandas as pd
import json

# Define the function to convert Excel to JSON
def excel_to_json(file_path, output_path):
    try:
        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path)
        
        # Ensure the columns "Team" and "UID" exist
        if "Team" not in df.columns or "UID" not in df.columns:
            raise ValueError("The Excel file must contain 'Team' and 'UID' columns.")
        
        # Convert the DataFrame to a list of dictionaries
        json_data = df.to_dict(orient="records")
        
        # Write the JSON data to a file
        with open(output_path, "w", encoding="utf-8") as json_file:
            json.dump(json_data, json_file, ensure_ascii=True)
        
        print(f"JSON data successfully written to {output_path}")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
input_file = "fifamteams.xlsx"   # Path to the Excel file
output_file = "teamsMini.json" # Path to the output JSON file

excel_to_json(input_file, output_file)
