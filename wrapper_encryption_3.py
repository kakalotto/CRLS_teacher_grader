# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.encryption_3 import route_docs_encryption_3 as power

fulltext_search = 'asymmetric'
person=''
if len(sys.argv) > 1:
    person = sys.argv[1]

def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'_lab', r'_rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B5', 'B7', 'B9', 'B11', 'B12', 'F3', 'F5',  'F8', 'F9', 'F10',]
rubric_sheet_name = 'Sheet1'

match_cells = [ 'D6', 'D8', 'D10', 'D11', 'D13', 'H4', 'H6', 'H8', 'H9', 'H10', 'H11', ]
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power, person=person, match_cells=match_cells)

