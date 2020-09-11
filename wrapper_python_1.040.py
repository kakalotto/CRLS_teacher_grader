# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.python_1040 import route_python_1_040
import sys

fulltext_search = '.py'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'1.030_Variables_TEALS',
                           r'Python 1.030 Variables - Rubric',
                           p_rubric_name)
    return p_rubric_name


value_cells = ['F4', 'F5', 'F6', 'F7', 'F8', 'B9', 'B4', ]
rubric_sheet_name = ''

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=route_python_1_040, python_lab_num='1.040',
                  python_rubric_suffix=' - Python_1.040_Magic_Genie_TEALS_rubric')
else:
     master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                   scorer=route_python_1_040, python_lab_num='1.040',
                   python_rubric_suffix=' - Python_1.040_Magic_Genie_TEALS_rubric',
                   person=person)
