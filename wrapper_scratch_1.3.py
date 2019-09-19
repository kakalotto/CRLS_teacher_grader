# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.scratch_13 import scratch_feedback_13

fulltext_search = 'Triangles'


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'Squares and triangles and stars Oh My - RSTA Scratch',
                           r'Drawing Shapes - rubric - RSTA Scratch', p_rubric_name)
    return p_rubric_name


value_cells = ['B9', 'F4', 'F5', 'F6', 'F7', 'B4', ]
rubric_sheet_name = 'Sheet1'

master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
              scorer=scratch_feedback_13, scratch_file=True)
