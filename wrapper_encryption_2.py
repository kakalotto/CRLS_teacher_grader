# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.encryption_2 import docs_feedback_encryption_2

fulltext_search = 'symmetric_key_encryption'
person=''
if len(sys.argv) > 1:
    person = sys.argv[1]



def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'widget', r'widget - Rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B10', 'F3', 'F5', 'F6', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['A17', 'A17', 'A17', 'A17', 'A17', 'C17', 'C18', 'C19', 'A17', 'C20', ]

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_encryption_2,
                  match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_encryption_2,
                  match_cells=match_cells, person=person)
