# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.python_2050 import docs_feedback_python_2050

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



#fulltext_search = '.py'
#value_cells = ['F4', 'F5', 'F6', 'F7', 'B10', 'B4', ]
#rubric_sheet_name = ''

#if not person:
#    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
#                  scorer=feedback_2040, python_lab_num='2.051a',
#                  python_rubric_suffix=' -  Python_2.051_Game_show_2_CRLS_voter_rubric')
#else:
#    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
#                  scorer=feedback_2040, python_lab_num='2.051a',
#                  python_rubric_suffix='  Python_2.051_Game_show_2_CRLS_voter_rubric', person=person)

fulltext_search = 'CRLS_voter'

value_cells = ['F4', ]
rubric_sheet_name = ''

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_python_2050)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_python_2050, person=person)

print("oooo" )
