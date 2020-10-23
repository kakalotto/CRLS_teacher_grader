# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.python_2051a import route_python_2_051a as power

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
value_cells = ['F5', 'F6', 'F7', 'F8', 'B10', 'B4', ]
rubric_sheet_name = ''

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power, python_lab_num='2.051a',
                  python_rubric_suffix=' - Python_2.051_Game_show_2_shortened_rubric')
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power, python_lab_num='2.051a',
                  python_rubric_suffix=' - Python_2.051_Game_show_2_shortened_rubric', person=person)

fulltext_search = 'Game_Show'

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
