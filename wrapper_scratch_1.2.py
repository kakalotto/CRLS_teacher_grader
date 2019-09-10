# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.scratch_12 import docs_feedback_scratch_12

fulltext_search = 'Scavenger'

def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'Scavenger',r'Scratch Scavenger ', p_rubric_name)
    p_rubric_name = re.sub(r'Hunt', r'Hunt - rubric ', p_rubric_name)
    return p_rubric_name


value_cells = ['B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15',
               'B16', 'B17', 'B18', 'B19', 'B20', 'B21', 'B22', 'B23', 'B24', 'B25', 'F4',
	       'F5', 'F6', 'F7']
rubric_sheet_name = 'Sheet1'

master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name, scorer=docs_feedback_scratch_12)
