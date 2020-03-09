# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.visualization_exploring_trends import docs_feedback_visualization_exploring_trends


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab', r'rubric', p_rubric_name)
    return p_rubric_name


fulltext_search = 'Visualization_exploring_trends'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]


value_cells = ['B3', 'B5', 'B7', 'B9', 'B11', 'F3', 'F4', 'F6', 'F8', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['D4', 'D6', 'D8', 'D10', 'D12', 'H5', 'H7', 'H9']
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_visualization_exploring_trends, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_visualization_exploring_trends, person=person, match_cells=match_cells)


