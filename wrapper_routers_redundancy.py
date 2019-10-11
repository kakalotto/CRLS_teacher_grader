# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.routers_and_redundancy import docs_feedback_routers_and_redundancy

fulltext_search = 'redundancy'
person=''
if len(sys.argv) > 1:
    person = sys.argv[1]

def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab', r'- Rubric', p_rubric_name)
#    p_rubric_name = re.sub(r'lab', r'rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B5', 'B7', 'B9', 'B11', 'B13', 'F3', 'F5', 'F7', 'F9', 'F11', ]
rubric_sheet_name = 'Sheet1'

#match_cells = ['D4', 'D6', 'D8', 'D10', 'D12', 'D14', 'H4', 'H6', 'H8', 'H10', 'H12']
match_cells = ['D4', 'D6', 'D8', 'D10', 'D12', 'D14', 'G4', 'G6', 'G8', 'G10', 'G12']

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_routers_and_redundancy, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_routers_and_redundancy, person=person, match_cells=match_cells)

