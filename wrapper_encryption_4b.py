# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.encryption_4b import docs_feedback_encryption_4b

fulltext_search = 'keys_and_passwords'
person=''
if len(sys.argv) > 1:
    person = sys.argv[1]

def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab', r'rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B5', 'B7', 'B9', 'F3', 'F5' ]
rubric_sheet_name = 'Sheet1'

match_cells = ['D6', 'D8', 'D10', 'H4', 'H6']
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_encryption_4b, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_encryption_4b, person=person, match_cells=match_cells)

