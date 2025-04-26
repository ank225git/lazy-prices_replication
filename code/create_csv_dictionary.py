# create_csv_dictionaries.py

import os
import pandas as pd
import gc

# Input and output paths
input_path = "../data/raw/lm_dictionaries/Loughran-McDonald_10X_DocumentDictionaries_1993-2024.txt"
csv_output_path = "../data/processed/full_docdict.csv"

# Ensure output folder exists
os.makedirs("../data/processed", exist_ok=True)

# Line parser
def parse_docdict_line(line):
    header_str, wordcount_str = line.strip().split('|', maxsplit=1)
    header_parts = header_str.split(',')
    word_counts = wordcount_str.split(',')

    header = {
        "cik": header_parts[0],
        "filing_date": header_parts[1],
        "accession_number": header_parts[2],
        "report_date": header_parts[3],
        "form_type": header_parts[4],
        "company_name": header_parts[5]
    }

    word_dict = {}
    for pair in word_counts:
        if ':' in pair:
            idx, count = pair.split(':')
            word_dict[f'word_{int(idx)}'] = int(count)

    return header, word_dict

# Parse and write in batches
batch_size = 10000
records = []
header_written = False
total_rows = 0
line_count = 0

print("start")

with open(input_path, "r", encoding="utf-8") as f_in:
    for line in f_in:
        line_count += 1
        header, word_data = parse_docdict_line(line)
        row = {**header, **word_data}
        records.append(row)

        if len(records) >= batch_size:
            df_batch = pd.DataFrame(records)

            if not header_written:
                df_batch.to_csv(csv_output_path, index=False, mode='w')
                header_written = True
            else:
                df_batch.to_csv(csv_output_path, index=False, mode='a', header=False)

            total_rows += df_batch.shape[0]
            print(f"Wrote batch: {df_batch.shape[0]} rows | Total written: {total_rows}")
            records = []
            gc.collect()

# Write remaining
if records:
    df_batch = pd.DataFrame(records)
    if not header_written:
        df_batch.to_csv(csv_output_path, index=False, mode='w')
    else:
        df_batch.to_csv(csv_output_path, index=False, mode='a', header=False)

    total_rows += df_batch.shape[0]
    print(f"Wrote final batch: {df_batch.shape[0]} rows | Total written: {total_rows}")
    records = []
    gc.collect()

print("Parsing and saving complete.")
