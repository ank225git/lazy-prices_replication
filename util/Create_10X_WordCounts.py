"""
Sample program to tabulate word counts in 10X files using Document Dictionary file

ND-SRAF / McDonald : 201606 | Last update: 202504
https://sraf.nd.edu 
"""

import sys
import datetime as dt
import MOD_Load_MasterDictionary_v2023 as md
import MOD_Read_DocDict as rd

IN_MASTER = r'G:\My Drive\SRAF\LM_Master_Dictionary\Loughran-McDonald_MasterDictionary_1993-2024.csv'
IN_DD = r'G:\My Drive\SRAF\EDGAR_Data\Loughran-McDonald_10X_DocumentDictionaries_1993-2024.txt'
OUT_FILE = 'D:\Temp\word_counts'
TARGETS = ["AND", "LIABILITIES", "DEPRECIATION", "ACCRUALS", "GOVERNANCE", "ETHICS"]
N_LIMIT = 20

def main():

    # Load master dictionary
    master_dictionary = md.load_masterdictionary(IN_MASTER, print_flag=True, get_other=False)
    lookup = rd.create_lookup_dictionary(master_dictionary)
    with open(IN_DD) as f_in:
        for count, line in enumerate(f_in):
            header, docdict = rd.read_docdict(line, lookup)
            print(f'\nWord counts for: {header.company_name} : Form {header.form_type} :', \
                  f'Total words = {header.total_words:,}')
            for word in TARGETS:
                if word in docdict:
                    print(f'  {word:15} = {docdict[word]:,}')
            if count == N_LIMIT: break


if __name__ == '__main__':
    start = dt.datetime.now()
    print(f'\n\n{start.strftime("%c")}\nPROGRAM NAME: {sys.argv[0]}\n')
    main()
    print(f'\n\nRuntime: {(dt.datetime.now()-start)}')
    print(f'\nNormal termination.\n{dt.datetime.now().strftime("%c")}\n')