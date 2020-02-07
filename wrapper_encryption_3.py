# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.encryption_3 import docs_feedback_encryption_3

fulltext_search = 'asymmetric'
person=''
if len(sys.argv) > 1:
    person = sys.argv[1]

def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'Encryption_3_asymetric_key_encryption_lab', r'Encryption_3_asymmetric_encryption - Rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B5', 'B7', 'B9', 'B11', 'B12', 'F3', 'F5', 'F7' ]
rubric_sheet_name = 'Sheet1'

match_cells = ['D4', 'D6', 'D8', 'D10', 'B16', 'D13', 'H4', 'H6', 'H8']
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_encryption_3, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_encryption_3, person=person, match_cells=match_cells)

