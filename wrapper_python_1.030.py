# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.python_1030 import docs_feedback_python_1030
import sys

fulltext_search = 'Python 1.030'

if len(sys.argv) > 1:
    person = sys.argv[1]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'1.030_Variables_TEALS',
                           r'Python 1.030 Variables - Rubric',
                           p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18',
               'B19', 'B21', 'B22', 'F3', 'F4', 'F5', 'F6', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['E27', 'E28']

#match_cells = ['H7', 'H9', 'I6']
if not person:

    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_python_1030, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_python_1030, match_cells=match_cells, person=person)
