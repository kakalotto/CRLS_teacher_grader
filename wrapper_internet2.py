# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.internet_2_v2 import docs_feedback_internet_2_v2

fulltext_search = 'Read the following on internet cookies'
person=''
if len(sys.argv) > 1:
    person = sys.argv[1]

def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
#    p_rubric_name = re.sub(r'lab', r'- Rubric', p_rubric_name)
    p_rubric_name = re.sub(r'lab', r'rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B5', 'B7', 'B9', 'B11', 'B13', 'B15', 'B17',
               'F3', 'F5', 'F7', 'F9', 'F11', 'F13', 'F14' ]
rubric_sheet_name = 'Sheet1'

match_cells = ['D6', 'D8', 'D10', 'D12', 'D14', 'D16', 'D18', 'H4', 'H6', 'H8', 'H10', 'H12']

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_internet_2_v2, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_internet_2_v2, person=person, match_cells=match_cells)

