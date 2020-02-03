# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.lossy_compression import docs_feedback_lossy_compression

fulltext_search = 'what is happening in the app'
person=''
if len(sys.argv) > 1:
    person = sys.argv[1]



def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
#    p_rubric_name = re.sub(r'_lab', r' - Rubric', p_rubric_name)
    p_rubric_name = re.sub(r'_lab', r'_rubric', p_rubric_name)

    return p_rubric_name


value_cells = ['B3', 'B5', 'B6', 'B8', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'F3', 'F4', 'F5', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['D4', 'D7', 'D9']

#match_cells = ['H7', 'H9', 'I6']
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_lossy_compression,
                  match_cells=match_cells)
else:    
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_lossy_compression,
                  match_cells=match_cells, person=person)
