"""
Program to read data created by Build_10XMasterandDictionary Doc_Dict_10X_YYYY.txt file
and build a dictionary for each filing.

Dependencies: Needs master_dictionary, which can be loaded in the calling routine using the 
              MOD_LoadmasterDictionary_v####.py file.

create_lookup_dictionary():
    Arguments:
      master_dictionary - the LM master dictionary preloaded in the calling routine.

    Returns:
      d_lookup - creates a dictionary used to lookup the wordcount for a given word given its
                 sequence number. This should be called once in the main program and then passed
                 in the calls to read_docdict.

read_docdict():
    Arguments:
      line - the current string read from the Document Dicitonary file.
      lookup - the lookup dictionary created in the main routine by calling (once) 
               create_lookup_dictionary().

    Returns:
      header - an object with attributes for the filing (see HeaderClass).
      doc_dict - a dictionary with keys for each unique word in the filing and the corresponding
                 word count for that word.

ND-SRAF / McDonald : 201606 | Last update: 202201
https://sraf.nd.edu 
"""


def create_lookup_dictionary(master_dictionary):

    # Given master dictionary, create dictionary that looks up words based on sequence
    d_lookup = dict()
    for word in master_dictionary.keys():
        d_lookup[master_dictionary[word].sequence_number] = word

    return d_lookup


def read_docdict(line, lookup):

    line = line.replace('\n', '')
    doc_dict = dict()
    doc_wordcount = 0
    cols = line.split('|')
    header = HeaderCls(cols[0])
    parts = cols[1].split(',')

    cnt = 0
    if len(cols[1]) > 0:
        for pair in parts:
            tmp = pair.split(':')
            word = lookup[int(tmp[0])]
            cnt += 1
            count = int(tmp[1])
            doc_wordcount += count
            doc_dict[word] = count
        header.total_words = doc_wordcount
    else:
        header.total_words = 0

    return header, doc_dict


class HeaderCls:

    def __init__(self, line):
        parts = line.split(',')
        self.cik = int(parts[0])
        self.filing_date = int(parts[1])
        self.accession_number = parts[2]
        self.cpr = int(parts[3])
        self.form_type = parts[4]
        self.company_name = parts[5]
        self.total_words = -99
