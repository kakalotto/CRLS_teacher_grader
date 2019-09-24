# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.encryption_4 import docs_feedback_encryption_4

fulltext_search = 'keys_and_passwords'
person=''
if len(sys.argv) > 1:
    person = sys.argv[1]

def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'passwords_lab', r'passwords - Rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B5', 'B7', 'B9', 'F3', 'F5' ]
rubric_sheet_name = 'Sheet1'

match_cells = ['A14', 'A14', 'D6', 'D8', 'D10', 'G13', 'G14']
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_encryption_4, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_encryption_4, person=person, match_cells=match_cells)

