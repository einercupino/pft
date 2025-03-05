import os
import pandas as pd

# Folder containing CSV files
folder_path = "D:/Portfolio/PFT/cibc_dump"

# Output file name
output_file = "combined_data.csv"

# List to hold DataFrames
df_list = []

# Process each CSV file in the folder
for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        file_path = os.path.join(folder_path, file)
        
        # Read the CSV and extract only the first 4 columns (A to D)
        df = pd.read_csv(file_path, usecols=[0, 1, 2, 3], dtype=str)
        
        # Rename columns for clarity
        df.columns = ["Date", "Transaction Description", "Debit", "Credit"]
        
        # Convert Amount to numeric (if applicable)
        df["Debit"] = pd.to_numeric(df["Debit"], errors="coerce")
        df["Credit"] = pd.to_numeric(df["Credit"], errors="coerce")
        
        # Add a column with the filename
        df["Source File"] = file
        
        # Drop rows where Transaction Description is missing
   #     df.dropna(subset=["Transaction Description"], inplace=True)
        
        # Append to list
        df_list.append(df)

# Combine all DataFrames
if df_list:
    combined_df = pd.concat(df_list, ignore_index=True)
    
    # Save to CSV
    combined_df.to_csv(os.path.join(folder_path, output_file), index=False)
    print(f"✅ Combined data saved to {output_file}")
else:
    print("⚠️ No valid CSV files found in the folder.")