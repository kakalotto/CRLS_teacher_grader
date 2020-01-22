# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.binary_practice_v4 import docs_feedback_binary_practice_v4

fulltext_search = 'Binary_practice'
person=''
if len(sys.argv) > 1:
    person = sys.argv[1]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'_lab', r' - Rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18',
               'B19', 'B20', 'B21', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15',
               'F16', 'F17', 'F19','F20', 'F22', 'F23', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['H18', 'H21', 'H24']

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_binary_practice_v4,
                  match_cells=match_cells)
else:
        master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                      scorer=docs_feedback_binary_practice_v4,
                      match_cells=match_cells, person=person)
