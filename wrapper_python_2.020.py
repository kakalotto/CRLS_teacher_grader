# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.python_2020 import docs_feedback_python_2020


fulltext_search = 'Casting'


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'2.020_Casting_TEALS',
                           r'Python 2.020 Casting - Rubric',
                           p_rubric_name)
    return p_rubric_name


value_cells = ['F4','F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15', 'F16', 'F17',]

master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, 
              scorer=docs_feedback_python_2020,
              )

