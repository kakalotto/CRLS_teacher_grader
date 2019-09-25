# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.python_2051b import feedback_2051b

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
value_cells = [ 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'B11', 'B5', ]
rubric_sheet_name = ''

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=feedback_2051b, python_lab_num='2.051b',
                  python_rubric_suffix=' -  Python_2.051_Game_show_2_CRLS_voter_rubric')
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=feedback_2051b, python_lab_num='2.051b',
                  python_rubric_suffix='  Python_2.051_Game_show_2_CRLS_voter_rubric', person=person)

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
