# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.lossy_compression import docs_feedback_lossy_compression

fulltext_search = 'lossy_compression'


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'_lab', r' - Rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B5', 'B6', 'B8', 'B9', 'B10', 'B13', 'F3', 'B11', 'B14', 'F5', 'B12', 'B15', 'F6', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['H4', 'H7', 'I7']
master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
              scorer=docs_feedback_lossy_compression,
              extra_fulltext="not fullText contains 'Lossless_compression'")

