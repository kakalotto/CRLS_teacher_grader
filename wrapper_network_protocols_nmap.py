# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.passwords_offline_crack_1 import docs_feedback_passwords_offline_crack_1


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab', r'rubric', p_rubric_name)
    return p_rubric_name


fulltext_search = 'crunch_win'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]


value_cells = ['B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17',
               'B18', 'B19', 'B20', 'B21', 'F3', 'F4', 'F5', 'F6', 'F7']
rubric_sheet_name = 'Sheet1'

match_cells = ['D22', 'H22']
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_passwords_offline_crack_1, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_passwords_offline_crack_1, person=person, match_cells=match_cells)

