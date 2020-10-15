# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.vpn_1 import route_docs_vpn_1 as power
fulltext_search = 'Your friend who works for Amazon is on the company’s VPN and is connected from your friend’s to Amazon HQ.  She says'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'_lab', r'_rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B5', 'B6', 'B7', 'B9',  'B11', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18', 'B19', 'B20',
               'B21', 'B22', 'F3', 'F4', 'F5', 'F6', 'F8']
rubric_sheet_name = 'Sheet1'
match_cells = ['D3', 'D4', 'D5', 'D6', 'D8', 'D10', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'D19', 'D20',
               'D21', 'D22', 'H3', 'H4', "H5", 'H7', 'H9']

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power,
                  match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power,
                  match_cells=match_cells, person=person)
