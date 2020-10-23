# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.python_2032 import route_docs_python_2032 as power
from CRLS_APCSP_autograder.app.python_2032a import route_python_2_032a as power2
from CRLS_APCSP_autograder.app.python_2032b import route_python_2_032b as power3

import sys

fulltext_search = '2.032'

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


value_cells = ['F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F14', 'F15', 'F16', 'F17', 'F18',
               'F19', 'F20', 'F21', 'F24', 'F25', 'F26', 'F27', 'F28', 'F29', 'F30', 'F31', 
               'F32', 'F33', 'F34', 'F35', 'F36', 'F37', 'F38', 'F39', 'F40', 'F41',
               'F42', 'F43', 'F44', 'F45', 'F46', 'F47',  ]
rubric_sheet_name = ''

if not person:

    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power,)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power, person=person)



fulltext_search = '.py'
value_cells = ['F12', 'F13', 'B10', 'B4',]
rubric_sheet_name = ''
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power2, python_lab_num='2.032a',
                  python_rubric_suffix=' - Python_2.032_DC_Superhero_girls_4_Buckets_KFC_rubric')
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power2, python_lab_num='2.032a',
                  python_rubric_suffix=' - Python_2.032_DC_Superhero_girls_4_Buckets_KFC_rubric', person=person)



fulltext_search = '.py'
value_cells = ['F22', 'F23', 'B11', 'B5', ]
rubric_sheet_name = ''
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power3, python_lab_num='2.032b',
                  python_rubric_suffix=' - Python_2.032_DC_Superhero_girls_4_Buckets_KFC_rubric')
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power3, python_lab_num='2.032b',
                  python_rubric_suffix=' - Python_2.032_DC_Superhero_girls_4_Buckets_KFC_rubric', person=person)