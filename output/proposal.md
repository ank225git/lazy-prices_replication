# **Research Proposal: Lazy Prices**
By Chris Luo and Anastasiia Kozlova

**Does academic research destroy stock return predictability**  
https://onlinelibrary.wiley.com/doi/abs/10.1111/jofi.12365

---

## **Research Objectives and Question**

**The “bigger” question:**  
Does publishing academic research reduce or eliminate the ability to predict stock returns — contributing to market efficiency by helping investors learn about pricing anomalies?

**The specific research question we are trying to answer:**  
How does the performance of the Lazy Prices signal change across in-sample, out-of-sample, and post-publication periods — and what does this tell us about overfitting and investor learning?

Our goal is to replicate the **Lazy Prices signal** as described in the paper by Cohen, Malloy, and Nguyen, and apply the methodology from *Does Academic Research Destroy Stock Return Predictability* (McLean & Pontiff, 2016) to evaluate return performance over time.

We will:
- Measure the Lazy Prices signal using **cosine similarity** between a firm’s 10-K/10-Q filings (all filings available, sorted in chronological order) and its previous reports.
- Trade on this signal monthly by sorting firms and forming long-short portfolios of the top and bottom quintiles.
- Evaluate returns across in-sample, out-of-sample, and post-publication periods.
- Recompute and report portfolio-level statistics and regression-based return decay.

---

## **Hypotheses**

Our project tests how **return predictability evolves over time**, specifically when the Lazy Prices signal becomes public knowledge.  
_Return predictability_ is the ability of a signal to forecast future stock returns.

- **H1 (In-sample):**  
  The Lazy Prices signal generates strong and statistically significant long-short returns in the in-sample period (1994–2003), when the signal is first developed.  
  This period is used to discover and optimize the signal. The high performance may partly come from overfitting or data mining.

- **H2 (Out-of-sample):**  
  The signal’s return decreases in the out-of-sample period (2004–2007), but still remains statistically significant.  
  This tests if the signal works on new data that was not used during signal construction. If performance drops, it suggests that the original results were possibly too optimistic.

- **H3 (Investor learning):**  
  In the post-publication period (2008–2014), the signal’s return decreases even more, and may become statistically insignificant.  
  This may happen because investors read the published paper and start trading based on the strategy, reducing its profit. This would support the idea of semi-strong market efficiency, where public information is quickly priced in.

- **H4 (Stronger decay after publication):**  
  The return drop from the out-of-sample period to the post-publication period is larger than the drop from the in-sample to out-of-sample period.  
  This would suggest that the publication itself has a meaningful effect on return decay, beyond just statistical overfitting. It provides evidence that market participants react to academic research once it becomes public.

---

### **Time Period Definitions and Portfolio Construction**

We adopt the time-period structure from McLean & Pontiff (2016) and apply it to the Lazy Prices signal. The Lazy Prices signal is based on **cosine similarity** between a firm’s current 10-K/10-Q and its previous one. We sort firms monthly and form long-short portfolios using this signal.

---

#### **In-Sample Period (1994–2003):**

This is the period during which the Lazy Prices signal is developed and optimized. Since researchers have access to the full data during this phase, strong performance may reflect overfitting or data mining.

To apply the signal:
1. For each firm, compute the cosine similarity between the current filing and the most recent prior filing (10-K/Q).
2. Rank firms by their similarity scores.
3. Form a long-short portfolio:  
   - **Long** the top 20% (highest similarity — market may underreact)  
   - **Short** the bottom 20% (lowest similarity — market may react faster)
4. Track monthly portfolio returns using historical data.


#### **Out-of-Sample Period (2004–2007):**

This period begins after the in-sample study window ends but before the Lazy Prices paper is officially published. The goal is to test whether the signal generalizes to new data not used in the model design.

We apply the same trading strategy:
1. Use only information available up to each point in time to calculate similarity scores.
2. Rank firms by similarity.
3. Form long-short portfolios using the top and bottom 20%.
4. Track monthly portfolio performance during this window.

A drop in returns relative to the in-sample period would indicate possible overfitting in the original construction.


#### **Post-Publication Period (2008–2014):**

This is the period after the Lazy Prices paper becomes public. If returns drop significantly here, it suggests that investors may have adopted the strategy, leading to faster price adjustment and reduced profitability — consistent with semi-strong market efficiency.

We simulate investor behavior as if the strategy is known:
1. Compute similarity using only past data available at each time.
2. Rank firms and form the same long-short portfolios.
3. Track monthly returns and compare them to the out-of-sample period.

If the return decline is greater here than in the out-of-sample period, it supports the hypothesis that publication itself accelerates return decay.




## **Evaluation Metrics and Benchmarks:**

- **Metrics:** Change in monthly long-short portfolio returns across periods  
- **Baseline (from McLean & Pontiff):**
  - ~26% return decay out-of-sample
  - ~58% return decay post-publication
  - Publication effect: ~32% return drop

---

## **Necessary Data**

### **Final Dataset Structure**

A panel dataset of **monthly Lazy Prices long-short portfolio returns**, labeled by period type.

- **Entities:** Lazy Prices signal portfolio  
- **Time:** Monthly data 
- **Variables:** 
  - Month  
  - Portfolio return  
  - Time period label (in-sample / out-of-sample / post-publication)  
  - Signal (similarity score ) 
  - Top/bottom quintile returns  

_Example:_

For each firm:

| month    | avg_ret | period_type       | similarity_sig |
|----------|---------|-------------------|----------------|
| 2001-01  | 0.006   | in_sample         | 0.745          |
| 2005-02  | 0.004   | out_of_sample     | 0.722          |
| 2010-03  | 0.001   | post_publication  | 0.715          |

---

### **Main regression:**

![Main regression](figs/main_formula_revised.png)

---

### **Observation?**  
One month of Lazy Prices long-short portfolio returns.

### **Sample period?**  
In the Lazy Prices paper: January 1994 to December 2014;  
(in-sample: 1994–2003, out-of-sample: 2004–2007, post-publication: 2008–2014)
Project time cutoffs may be adjusted to include more data.

### **Sample conditions?**
- Publicly listed U.S. stocks from CRSP  
- Exclude financials and microcap firms  
- Use only publicly available filings (10-Ks and 10-Qs)  
- Firm must have consecutive filings to compute similarity

---

### **Essential and Supplementary Variables**

**Absolutely necessary:**
- Cosine similarity scores (Lazy Prices signal)
- Monthly firm returns (CRSP)
- Filing dates and CIKs (from 10-Ks / MasterIndex)
- Time range label

**Nice to have:**
- Market cap
- Portfolio rankings and weights
- Short interest
- Analyst forecast revisions
- Dividend flags
- Total assets, net income, cash flow (Compustat)

---

## **Available and Required Data**

**Available:**
- Lazy Prices paper  
- CRSP monthly return data (shared by professor)  
- Access to cleaned 10-K/Q dataset from Notre Dame  
- MasterIndex file to map filings

**Required:**
- Extract firm text data from 10-Ks and 10-Qs  
- Calculate cosine similarity between current and previous reports  
- Merge with CRSP returns using CIK/PERMNO mapping

---

## **Data Collection and Processing Plan**

- Download cleaned 10-Ks from Notre Dame (McDonald’s repository)
- Parse text filings and compute cosine similarity between firm reports at t and t−1
- Use CIKs and dates to match with CRSP monthly returns

---

## **Raw inputs and folder structure**
/data/ 
  /raw/ 
    crsp_monthly.csv 
    master_index.txt 
    /10_x_cleaned/....
  /processed/ 
    lazy_prices_returns.csv 
/code/ 
  compute_similarity.ipynb 
  build_portfolio.ipynb 
  run_regression.ipynb 
/output/ 
  proposal.md 
  summary_results.csv 
  figs/...

  ---

## **Data Transformation Process**

1. Clean and align CRSP returns with 10-K/Q filing dates  
2. Compute signal using cosine similarity for each firm’s filings  
3. Sort firms monthly based on signal strength and construct long-short portfolios (top 20% vs bottom 20%)  
4. Label time periods and calculate monthly returns  
5. Run regression to estimate return decay and test investor learning hypotheses  

## **Potential project expansion**

Compare Lazy Prices statistics to the anomalies presented in the OAP project.
