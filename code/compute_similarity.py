# compute_similarity_chunked.py

import os
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Paths
input_path = "../data/processed/full_docdict.csv"
output_path = "../data/processed/full_similarity_scores.csv"

os.makedirs("../data/processed", exist_ok=True)

# Settings
chunk_size = 10000
word_cols_prefix = "word_"

# Helper function to compute cosine similarity between two rows
def compute_cosine_similarity(vec1, vec2):
    vec1 = np.array(vec1).reshape(1, -1)
    vec2 = np.array(vec2).reshape(1, -1)
    return cosine_similarity(vec1, vec2)[0][0]

# Main processing
def compute_similarity():
    print("start")
    reader = pd.read_csv(input_path, chunksize=chunk_size, low_memory=False)
    header_written = False
    total_rows = 0

    for chunk_idx, chunk in enumerate(reader):
        print(f"Processing chunk {chunk_idx+1}...")

        # Keep needed columns
        word_cols = [col for col in chunk.columns if col.startswith(word_cols_prefix)]
        use_cols = ['cik', 'filing_date'] + word_cols
        chunk = chunk[use_cols]

        # OPTIMIZATION: force 'cik' to int for faster groupby and less memory
        chunk['cik'] = chunk['cik'].astype(int)

        # Fill missing word counts with 0
        chunk[word_cols] = chunk[word_cols].fillna(0)

        # Convert filing_date
        chunk['filing_date'] = pd.to_datetime(chunk['filing_date'], format='%Y%m%d')

        # Sort properly
        chunk = chunk.sort_values(['cik', 'filing_date']).reset_index(drop=True)

        output_rows = []

        # Compute similarities within each CIK group
        for cik, group in chunk.groupby('cik'):
            group = group.sort_values('filing_date')
            previous_vector = None

            for idx, row in group.iterrows():
                if previous_vector is not None:
                    similarity = compute_cosine_similarity(previous_vector, row[word_cols])
                else:
                    similarity = np.nan  # First filing

                output_rows.append({
                    "cik": row['cik'],
                    "filing_date": row['filing_date'],
                    "similarity": similarity
                })

                previous_vector = row[word_cols]

        # Write this batch to file
        df_similarity = pd.DataFrame(output_rows)

        if not header_written:
            df_similarity.to_csv(output_path, index=False, mode='w')
            header_written = True
        else:
            df_similarity.to_csv(output_path, index=False, mode='a', header=False)

        total_rows += chunk.shape[0]
        print(f"Chunk {chunk_idx+1} written. Total filings processed so far: {total_rows}")

    print(f"\nDone. Similarity scores saved to {output_path}.")

if __name__ == "__main__":
    compute_similarity()
