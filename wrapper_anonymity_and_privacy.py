# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.anonymity_and_privacy import route_docs_anonymity_and_privacy
fulltext_search = 'Presentation of anonymity and privacy'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'_lab_1', r'_rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B5', 'B6', 'B7', 'B9',  'B11', 'B12', 'B13', 'B15', 'B17',]
rubric_sheet_name = 'Sheet1'

match_cells = ['D3', 'D4', 'D5', 'D6', 'D8', 'D10', 'D11', 'D12', 'D14', 'D16', 'D18',]

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=route_docs_anonymity_and_privacy,
                  match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=route_docs_anonymity_and_privacy,
                  match_cells=match_cells, person=person)
