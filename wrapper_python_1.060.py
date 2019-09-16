# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.python_1060 import feedback_1060

fulltext_search = '.py'


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'1.030_Variables_TEALS',
                           r'Python 1.030 Variables - Rubric',
                           p_rubric_name)
#    return p_rubric_name
    return None


value_cells = ['F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'B9', 'B4', ]
rubric_sheet_name = ''

master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
              scorer=feedback_1060, python_lab_num='1.060', python_rubric_suffix=' - Python 1.060 Mad Libs - Rubric')

