# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.two_factor_authentication import docs_feedback_two_factor_authentication

def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'- Two factor authentication', r'- Twofactor authentication - Rubric', p_rubric_name)
    return p_rubric_name


fulltext_search = 'two factor authentication'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]


value_cells = ['B3', 'B5', 'B7', 'B9', 'B11', 'F3', 'F5']
rubric_sheet_name = 'Sheet1'

match_cells = ['D4', 'D6', 'D10', 'D12','H4', 'H6']
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_two_factor_authentication, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_two_factor_authentication, person=person, match_cells=match_cells)


