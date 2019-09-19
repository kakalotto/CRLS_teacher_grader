# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.bytes_and_filesizes_v3 import docs_feedback_bytes_and_file_sizes_v3

fulltext_search = 'Bytes and file sizes'


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'v3', r'v3 - Rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12','B13',
               'B14', 'B15', 'B16', 'B17', 'B18', 'F3', 'F4', 'F6', 'F8', 'F10', 'F12' ]
rubric_sheet_name = 'Sheet1'
match_cells = ['H5', 'H7', 'H9', 'H11', 'H13']
master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
              scorer=docs_feedback_bytes_and_file_sizes_v3, match_cells=match_cells)
