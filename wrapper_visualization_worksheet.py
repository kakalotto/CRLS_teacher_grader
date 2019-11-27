# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.visualization_worksheet import docs_feedback_visualization_worksheet


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'Visualization_worksheet', r'visualization_worksheet - Rubric', p_rubric_name)
    return p_rubric_name


fulltext_search = 'Visualization_worksheet'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]


value_cells = ['B3', 'B5', 'B6', 'B8', 'B10', 'B12', 'B14', 'B15', 'F3', 'F4', 'F6', 'F7', 'F9', 'F10', 'F12' ]
rubric_sheet_name = 'Sheet1'

match_cells = ['D4', 'D7', 'D9', 'D11', 'D13', 'D16', 'H5', 'H8', 'H11']
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_visualization_worksheet, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_visualization_worksheet, person=person, match_cells=match_cells)

