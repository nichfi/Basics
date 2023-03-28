import pandas as pd
from pathlib import Path

def main():
    while True:
        # ask user for filename
        filename = input("Enter the filename: ")

        try:
            # check the file extension 
            file_extension = Path(filename).suffix.lower()

            if file_extension == ".csv":
                df = pd.read_csv(filename)
            elif file_extension == ".xls" or file_extension == ".xlsx":
                df = pd.read_excel(filename)
            elif file_extension == ".json":
                df = pd.read_json(filename)
            else:
                print("File extension {} is not supported. Please try again.".format(file_extension))
                continue # continue to next iteration of the loop if file extension is not supported
            
            # print summary statistics
            print(df.describe())
            break # exit the loop if file is read successfully

        except FileNotFoundError:
            print("Error in reading the file {} Please try again.".format(filename))
        except PermissionError:
            print("Error in reading the file {} Please try again.".format(filename))
        except Exception:
            print("Error in reading the file {} Please try again.".format(filename))
            break # continue to next iteration of the loop if any other error occurs

main()
