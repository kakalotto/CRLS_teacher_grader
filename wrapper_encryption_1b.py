# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.encryption_1b import docs_feedback_encryption_1b

fulltext_search = 'simple_encryption'
person=''
if len(sys.argv) > 1:
    person = sys.argv[1]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab', r'rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B6', 'B8', 'B9', 'B11', 'B13', 'F3', 'F5', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['D5', 'D7', 'D10','D12', 'D14', 'H4', 'H6',]

#match_cells = ['H7', 'H9', 'I6']
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_encryption_1b,
                  match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_encryption_1b,
                  match_cells=match_cells, person=person)
