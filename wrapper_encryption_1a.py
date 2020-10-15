# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.encryption_1a import route_docs_encryption_1a as power

fulltext_search = 'simple_encryption'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'Symmetric_Encryption_lab', r'Simple_Encryption_rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B6', 'B8', 'B9', 'B11', 'B13', 'F3', 'F5', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['D3', 'D5', 'D7', 'D8', 'D10', 'D12', 'D14', 'H4', 'H6']

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power,
                  match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power,
                  match_cells=match_cells, person=person)
