# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.python_4021 import route_python_4_021 as power

person = ''
people = []
if len(sys.argv) == 2:
    person = sys.argv[1]
elif len(sys.argv) >= 3:
    people = sys.argv[1:]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab',
                           r'rubric',
                           p_rubric_name)
    return p_rubric_name

fulltext_search = '.py'
value_cells = ['F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'B10', 'B4', ]
rubric_sheet_name = ''

if not person and not people:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power, python_lab_num='4.021',
                  python_rubric_suffix=' - Python_4.021_The_Rock_says_rubric')
else:
    if person:
        master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                      scorer=power, python_lab_num='4.021',
                      python_rubric_suffix=' - Python_4.021_The_Rock_says_rubric', person=person)
    elif people:
        for scholar in people:
            master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                          scorer=power, python_lab_num='4.021',
                          python_rubric_suffix=' - Python_4.021_The_Rock_says_rubric', person=person)
