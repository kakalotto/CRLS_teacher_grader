# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.python_4012 import feedback_4012

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
value_cells = [ 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'B4', 'B9', ]
rubric_sheet_name = ''

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=feedback_4012, python_lab_num='4.012',
                  python_rubric_suffix=' - Python 4.012_Samuel_L_Jackson_Algorithm - Rubric')
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=feedback_4012, python_lab_num='4.012',
                  python_rubric_suffix=' - Python 4.012_Samuel_L_Jackson_Algorithm - Rubric', person=person)

fulltext_search = 'Sorting'

#value_cells = ['F4', ]
#rubric_sheet_name = ''

#if not person:
#    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
#                  scorer=docs_feedback_python_2051)
#else:
#    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
#                  scorer=docs_feedback_python_2051, person=person)#
#
#print("oooo" )
