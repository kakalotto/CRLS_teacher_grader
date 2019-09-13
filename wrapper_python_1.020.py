# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.python_1020 import docs_feedback_python_1020

fulltext_search = 'Python 1.020'


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'1.020_Using_the_Interpreter_TEALS', r'Python 1.020 Interpreter - Rubric',
                           p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18',
               'B19','B20', 'B21', 'B22','B23', 'B24', 'B25', 'B26', 'B27', 'B28', 'B29', 'B30', 'B31', 'B32', 'B33',
               'B34', 'B35', 'B36', 'B37', 'B38', 'B39', 'B40', 'B41', 'B42', 'B43', 'B44', 'B45', 'B46', 'B47', 'B48',
               'B49', 'B50', 'B51', 'B52', 'B53', 'B54', 'B55', 'B56', 'B57', 'B58', 'B59', 'B60', 'B61', 'B62', 'B63',
               'B64','B65', 'B66', 'B67', 'B68','B69', 'B70', 'B71', 'B72', 'B73', 'B74', 'B75', 'B76', 'B77', 'B78',
               'B79', 'B80', ]
rubric_sheet_name = 'Sheet1'

match_cells = []

#match_cells = ['H7', 'H9', 'I6']
master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
              scorer=docs_feedback_python_1020)

