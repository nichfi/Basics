
import pandas as pd

def main():
    while True:
        # ask user for filename
        print("Enter the name of the file to be read:")
        filename = input()
        try:
            # check the file extension using pandas
            file_extension = filename.split(".")[-1].lower()
            
            if file_extension == "csv":
                df = pd.read_csv(filename)
            elif file_extension == "xls" or file_extension == "xlsx":
                df = pd.read_excel(filename)
            elif file_extension == "json":
                df = pd.read_json(filename)
            else:
                print("File extension {} is not supported. Please try again.".format(file_extension))
                continue
            
            # print summary statistics
            print("File read successfully.")
            print()
            print("Printing summary statistics:")
            print(df.describe())
            break
        except FileNotFoundError:
             print("Error in reading the file {} Please try again.".format(filename))
        except PermissionError:
             print("Error in reading the file {} Please try again.".format(filename))
        except Exception:
             print("Error in reading the file {} Please try again.".format(filename))
        continue # continue to next iteration of the loop if any other error occurs

main()


