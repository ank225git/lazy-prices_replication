###**10X Summaries**
[Loughran-McDonald_10X_Summaries_1993-2024.csv (188MB)](https://drive.google.com/file/d/16XQDG15-wSdqZrHTnv8ooMtqA95f3ifH/view?usp=sharing)

Using the [cleaned files from the stage one parsing process](https://drive.google.com/drive/folders/1tZP9A0hrAj8ptNP3VE9weYZ3WDn9jHic?usp=sharing), a dataset is created containing summary data for each filing. A [Python class for this module is available](https://drive.google.com/file/d/1qTRr7-Zfr9kORK2fLs6qUgEAOIGnEnzR/view?usp=sharing). **This class transforms a row from the LM 10X summaries CSV file into a Python object with fields that you can use to compute textual metrics for each 10-K/10-Q filing.**
The file contains a header record with labels and is comma-delimited. Each record reports:

Header info
1. CIK – the SEC Central Index Key.

2. FILING_DATE – the filing date (YYYYMMDD) for the form.

3. ACC_NUM – the EDGAR-assigned identifier unique to each submission. Format: (10-Char CIK)+"-"+YY+"-"+(6-Char sequence #).

4. CPR - Conformed Period of Report. End date of the reporting period of filing. Note, per the SEC, this is optional.

5. FORM_TYPE – the specific form type (e.g., 10-K, 10-K/A, 10-Q405, etc.).

6. CoName – Company Conformed Name.

7. SIC – the four-digit SIC reported in the header of the filing. If this number does not appear in the header, then the primary web page for all filings from that firm at EDGAR is parsed in an attempt to identify the SIC number. If all of these methods fail, an SIC of -99 is assigned.

Fama-French Industry
8. FFInd – the Fama-French 48 industry classification based on the SIC number. All missing SIC numbers are assigned to the Miscellaneous category.

Word counts
9. N_Words – the count of all words, where a word is any token appearing in the Master Dictionary.

10. N_Unique_Words  – the number of words occurring at least once in the document.

11-17. A sequence of sentiment counts – negative, positive, uncertainty, litigious, strong modal, weak modal, constraining.

18. Complexity - counts for the LM measure of complexity.

19. N_Negation—a count of cases where negation occurs within four or fewer words from a word identified as positive. Negation words are (“no, not, none, neither, never, nobody”, see Gunnel Totie, 1991, Negation in Speech and Writing). Thus, the net positive word count should be calculated as the Positive word count minus the count for Negation. Although the technique seems reasonable, most important cases of negation are sufficiently subtle that most algorithms will not pick them up.

Statistics from Stage 1 Parse
20. GrossFileSize – the total number of characters in the original filing.

21. NetFileSize – the total number of characters in the filing after the Stage One Parse which eliminates HTML, ASCII-encoded materials, etc.

22. NonTextDocTypeChars – the total number of ASCII Encoded characters (e.g., &amp;)

23. HTMLChars – the total number of characters attributable to HTML encoding.

24. XBRLChars – the total number of characters attributable to XBRL encoding.

25. XMLChars – the total number of characters attributable to XML encoding.

26. N_Exhibits – number of exhibits in the filing.