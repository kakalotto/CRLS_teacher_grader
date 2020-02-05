# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.python_2021 import feedback_2021


fulltext_search = '.py'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab',
                           r'rubric',
                           p_rubric_name)
    return p_rubric_name




fulltext_search = '.py'
value_cells = ['F18', 'F19', 'F20', 'F21', 'F22', 'F23', 'B9', 'B4', ]
rubric_sheet_name = ''

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=feedback_2021, python_lab_num='2.021',
                  python_rubric_suffix='- Python_2.021_Casting_TEALS_rubric')
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=feedback_2021, python_lab_num='2.021',
                  python_rubric_suffix=' - Python_2.021_Casting_TEALS_rubric',
                  person=person)



#value_cells = ['F4','F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17',]
#fulltext_search = 'Casting'


