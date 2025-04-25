This file provides a tabulated dictionary of all words from the LM dictionary for each filing, which means that you can work with word counts without parsing the underlying documents.

[Loughran-McDonald_10X_DocumentDictionaries_1993-2024.txt (15.8 GB)](https://drive.google.com/file/d/1zFN2u4JjNKBCopgTH-P8-PFnA1Gexau9/view?usp=sharing)

 

This file contains header information and word counts for all 10X filings. 

The header data is pipe-delimited from the word counts.
The word counts appear as word-sequence-number:word-count.
A [Python function to decode the records](https://drive.google.com/file/d/17ipMssklHhSadNtK3fnIcotTzwUOfk9V/view). File named `MOD_Read_DocDict.py `
A [sample program to produce word counts using the function](https://drive.google.com/file/d/17mjU-AIPuHfnxVaf_8d2Z09LsA4UF2Lm/view). File named `Create_10X_WordCounts.py `.
 

Here is a truncated line containing Google's first 10-Q filing:


1288776,20040816,0001193125-04-141838,20040630,10-Q,Google Inc.|101:42,126:16,184:17,186:10,213:1,248:1, ...

The first six fields before the pipe are: (1) cik, (2) filing_date, (3) accession_number, (4) conformed_period_report, (5) form_type, and (6) company_name.

The subsequent fields contain the word sequence number in the master dictionary followed by the count for that word. The first field (101:42), indicates that the word "ability "occurred 42 times in the filing.