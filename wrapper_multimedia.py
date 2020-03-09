# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.multimedia import docs_feedback_multimedia


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'_lab', r' - rubric', p_rubric_name)
    return p_rubric_name


fulltext_search = 'Multimedia lab'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]


value_cells = ['B3', 'B5', 'B6', 'B8', 'B10', 'B12', 'B14']
rubric_sheet_name = 'Sheet1'

match_cells = ['D4', 'D10']
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_multimedia, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_multimedia, person=person, match_cells=match_cells)

