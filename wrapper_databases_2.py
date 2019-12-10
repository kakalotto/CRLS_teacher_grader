# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.databases_2_002 import docs_feedback_databases_2002

def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'- Databases_2.002_lab', r'- Databases2 - Rubric', p_rubric_name)
    return p_rubric_name


fulltext_search = 'Databases 2.002'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]


value_cells = ['B3', 'B5', 'B7', 'B8', 'B10', 'B11', 'B13', 'F3', 'F4', 'F5', 'F6']
rubric_sheet_name = 'Sheet1'

match_cells = ['D4', 'D6', 'D8', 'D10', 'D12',]
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_databases_2002, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_databases_2002, person=person, match_cells=match_cells)


