# Lazy Prices Replication

## Overview

This project replicates and extends the “Lazy Prices” paper, which investigates whether textual repetition in firms’ 10-K filings predicts future stock returns. The hypothesis is that repetitive disclosures signal investor inattention, leading to underreaction and predictable excess returns. Our pipeline builds cosine similarity scores between consecutive 10-K filings and constructs long-short portfolios based on these scores to evaluate return predictability.

We compare the performance of our similarity-based trading strategy to standard return anomalies from the Open Asset Pricing (OAP) dataset. Our main analysis is in [`returns-analysis.ipynb`](code/returns-analysis.ipynb), where we visualize cumulative and log cumulative returns, monthly returns, and moving averages.

---

## Repository Structure

```
lazy-prices_replication/
│
├── code/
│   ├── build_code/                         # Notebooks for intermediate analysis
│   ├── temp/                               # Temporary output files
│   ├── compute_similarity.py               # Script to compute cosine similarity scores
│   ├── create_csv_dictionary.py            # Parser for LM dictionaries into structured CSV
│   ├── load_stock_data*.ipynb              # Stock return loading and merging logic
│   ├── portfolio_construction*.ipynb       # Portfolio strategies (winsorized, propagated, raw)
│   ├── returns-analysis.ipynb              # Main notebook for return analysis and visualizations
│   └── score_distribution.ipynb            # Distribution and study of similarity scores
│
├── data/
│   ├── build_data/                         # Small-sample files for initial development
│   ├── processed/                          # Datasets used in intrmediate and final analyses
│   ├── raw/
│   │   ├── crsp_data/                      # Raw stock return files from WRDS
│   │   ├── lm_dictionaries/                # Loughran-McDonald dictionary of 10-Ks
│   │   └── lm_summaries/                   # LM preprocessed summary files
│
├── output/
│   ├── figs/                               # Exported figures from analysis
│   ├── proposal.md                         # Original proposal
│   └── report.ipynb                        # Final Report
│
├── util/                                   # Utility scripts and data scrapers
├── .gitignore
├── README.md                               # You are here
├── requirements.txt                        # File for batch-installing required packages
```

---

## Quick Start

1. Clone the repository
2. Ensure required packages are installed:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the full analysis from:
   - [`returns-analysis.ipynb`](code/returns-analysis.ipynb)

---

## Datasets Used

| Dataset Name                         | Source |
|--------------------------------------|--------|
| SEC EDGAR 10-K Filings              | [SEC](https://www.sec.gov) |
| CRSP Monthly Stock Returns          | [WRDS](https://wrds-www.wharton.upenn.edu/) |
| Loughran-McDonald 10-K Dictionaries | [LM Dataset](https://sraf.nd.edu) |
| Open Asset Pricing Signals (OAP)    | [Global-Q](https://www.openassetpricing.com) |
| CIK–Ticker Mapping                  | [SEC](https://www.sec.gov) |
| Compustat/CRSP Class File           | WRDS Compustat-CRSP Merged |

---

## Notes

- **Similarity scores** are computed using cosine similarity of word frequency vectors across firm filings.
- **Portfolio construction** is performed using quintile sorting and both exact-match and forward-propagated signals.
- **Benchmarking** is done against OAP signals such as Book-to-Market (BM) and 12-month momentum (Mom12m).

