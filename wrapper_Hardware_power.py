# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.hardware_power import docs_feedback_hardware_power


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab', r'rubric', p_rubric_name)
    return p_rubric_name


fulltext_search = 'Power supply connectors'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]

value_cells = ['B3', 'B4', 'B6', 'B7', 'B9', 'B10', 'B12', 'B13', 'F3', 'F5', 'F7', 'F9', 'F11']
rubric_sheet_name = 'Sheet1'

match_cells = ['D5', 'D8', 'D11', 'D14']
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_hardware_power, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_hardware_power, person=person, match_cells=match_cells)

