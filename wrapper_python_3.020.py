# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.python_3020 import route_python_3_020 as power


person = ''
people = []
if len(sys.argv) == 2:
    person = sys.argv[1]
elif len(sys.argv) > 3:
    people = sys.argv[1:]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab',
                           r'rubric',
                           p_rubric_name)
    return p_rubric_name

fulltext_search = '.py'
value_cells = ['F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'B9', 'B4', ]
rubric_sheet_name = ''

if not person and not people:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power, python_lab_num='3.020',
                  python_rubric_suffix=' - Python_3.020_Birthday_Song_and_Random_Cards_TEALS_rubric')
else:
    if person:
        master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                      scorer=power, python_lab_num='3.020',
                      python_rubric_suffix=' - Python_3.020_Birthday_Song_and_Random_Cards_TEALS_rubric', person=person)
    elif people:
        for scholar in people:
            master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                          scorer=power, python_lab_num='3.020',
                          python_rubric_suffix=' - Python_3.020_Birthday_Song_and_Random_Cards_TEALS_rubric',
                          person=scholar)
