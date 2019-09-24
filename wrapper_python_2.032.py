# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.python_2032 import docs_feedback_python_2032
import sys

fulltext_search = '.py'


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'2.032_DC_Superhero_girls_4_Buckets_KFC',
                           r'Python 2.032 DC Superhero girls KFC- Rubric',
                           p_rubric_name)
    return p_rubric_name


value_cells = ['F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F14', 'F15', 'F16', 'F17', 'F18',
               'F19', 'F20', 'F21', 'F24', 'F25', 'F26', 'F27', 'F28', 'F29', 'F30', 'F31', 
               'F32', 'F33', 'F34', 'F35', 'F35', 'F36', 'F37', 'F38', 'F39', 'F40', 'F41',
               'F42', 'F42', 'F43', 'F44', 'F45', 'F46', 'F47',  ]
rubric_sheet_name = ''

master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
              scorer=docs_feedback_python_2032,)

