import os
import pandas as pd


def count_stars(text):
    return text.count("⭐")


def sort_csv_by_stars(file_path):
    try:
        data = pd.read_csv(file_path)
        if "ranking" in data.columns:
            data["star_count"] = data["ranking"].apply(count_stars)
            sorted_data = data.sort_values(by="star_count", ascending=False)
            # Remove the 'star_count' column before saving
            sorted_data = sorted_data.drop(columns=["star_count"])
            return sorted_data
        else:
            print(f"No 'ranking' column in {file_path}. Skipping.")
            return None
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None


def process_folder(folder_path):
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            file_path = os.path.join(folder_path, file)
            sorted_data = sort_csv_by_stars(file_path)
            if sorted_data is not None:
                sorted_file_path = os.path.join(folder_path, f"sorted_{file}")
                sorted_data.to_csv(sorted_file_path, index=False)
                print(f"Processed and saved sorted data to {sorted_file_path}")


# Replace 'your_folder_path' with the path to your folder containing the CSV files
folder_path = input("Folder path: ")
process_folder(folder_path)
