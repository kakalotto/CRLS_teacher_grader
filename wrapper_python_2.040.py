# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.python_2040 import feedback_2040
from CRLS_APCSP_autograder.app.python_2040_doc import docs_feedback_python_2040

person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'2.040_Game_Show_TEALS',
                           r'Python 2.040 Game Show - Rubric',
                           p_rubric_name)
    return p_rubric_name



fulltext_search = '.py'
value_cells = ['F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'B9', 'B4', ]
rubric_sheet_name = ''

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=feedback_2040, python_lab_num='2.040',
                  python_rubric_suffix=' - Python_2.040_Game_Show_rubric')
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=feedback_2040, python_lab_num='2.040',
                  python_rubric_suffix=' - Python_2.040_Game_Show_rubric', person=person)

fulltext_search = 'Game_Show'

value_cells = ['F4', 'F5', 'F6', ]
rubric_sheet_name = ''

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_python_2040)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_python_2040, person=person)

print("oooo" )
