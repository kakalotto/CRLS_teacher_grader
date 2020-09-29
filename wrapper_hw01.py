# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.hw01 import route_docs_hw01

fulltext_search = 'HW 01'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]

def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'_lab', r'_rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B5',]
rubric_sheet_name = 'Sheet1'
match_cells = ['D3', 'D4',]

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=route_docs_hw01, match_cells=match_cells)
else:
     master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                   scorer=route_docs_hw01, person=person, match_cells=match_cells)
