# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.lossless_compression import docs_feedback_lossless_compression

fulltext_search = 'develop a heuristic'

person=''
if len(sys.argv) > 1:
    person = sys.argv[1]

def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'_lab', r' - Rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B6', 'B8', 'B10', 'B12', 'B14',
               'F3', 'F5', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['C18', 'C19', 'C20', 'C21', 'C22', 'C23', 'C24', 'C25', 'C26', 'C27']

#match_cells = ['A18', 'A18', 'A18', 'A18', 'H11', 'H13', 'H15', 'H16', 'H17']
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_lossless_compression,
                  match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_lossless_compression,
                  match_cells=match_cells, person=person)
