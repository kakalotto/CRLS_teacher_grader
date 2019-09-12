# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.lossy_compression import docs_feedback_lossy_compression

fulltext_search = 'lossless_compression'


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'_lab', r' - Rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B5', 'B7', 'B9', 'B11', 'B13', 'B15', 'F4', 'F6', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['C17', 'C18', 'C19']

#match_cells = ['H7', 'H9', 'I6']
master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
              scorer=docs_feedback_lossy_compression,
              rubric_extra_fulltext="not fullText contains 'Lossless_compression'",
              match_cells=match_cells)

