import pandas as pd

import datetime

DATE_FORMATS = ["%Y-%m-%d", "%d.%m.%Y", "%d.%m.%y", "%d-%m-%Y", "%d/%m/%Y", "%m/%d/%Y"]

def get_date_format(dates):
    # Gets a Pandas Series of dates as strings and attempts to convert each string to a DateTime object
    # Conversion is attempted with every format in 'DATE_FORMATS' list
    # Returns a date format that works for all date strings
    for date_format in DATE_FORMATS:
        reject_format = False
        i = 0
        while not reject_format:
            try:
                datetime.datetime.strptime(dates[i], date_format)
                if (i + 1) == len(dates):
                    return date_format
            except ValueError:
                reject_format = True
            i += 1
    raise Exception('An error occurred: no valid date format found.')
    
def clean_data(file_name):
    
    date_format = get_date_format(file_name['date'])
    file_name['date'] = pd.to_datetime(file_name["date"],format=date_format)
    file_name['date'] = file_name['date'].dt.date
    
    file_name['cases'] = file_name ['cases'].str.replace(' ','')
    file_name['cases'] = file_name ['cases'].str.replace('.','')
    file_name['cases'] = file_name ['cases'].str.replace(',','')
    file_name['cases'] = pd.to_numeric(file_name["cases"],errors ='coerce', downcast='integer')
    return file_name

# ask the user for the names of the three TSV files


def main():
    
    file_list = []
    dfs = []
    name_list = ['date']   
    while len(file_list) < 3:
        file_name = input("Enter the name of file #"+ str(len(file_list)+1) +":\n")
        if file_name not in file_list: 
            file_list.append(file_name)
            name_list.append(file_name.split('.')[0])
            try:
                df = clean_data(pd.read_csv(file_name, sep="\t", dtype = str))
                dfs.append(df)
            except:
                print('Error in reading file ' + file_name + '. Closing program.')
                return -1
        else: 
            print('File ' + file_name + 'is already included in this analysis. Please choose a different file.')
    
   
    
    merged_dataframe = pd.merge(dfs[0], dfs[1], how='outer', on='date')
    merged_dataframe = pd.merge(merged_dataframe, dfs[2], how='outer', on='date')
    column_names = [name_list[0], 'cases_'+ name_list[1].split('\\')[-1].lower(), 'cases_'+name_list[2].split('\\')[-1].lower(),'cases_'+ name_list[3].split('\\')[-1].lower()]
    merged_dataframe.columns = column_names

    # Print summary statistics and the first five rows
    print("\nPrinting summary statistics:")
    print(merged_dataframe.describe())
    print("\nPrinting first five rows:")
    print(merged_dataframe.head())
    
main()
