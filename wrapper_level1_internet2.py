# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.level1_internet2 import docs_feedback_level1_internet_2


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'Internet_2_lab', r'internet2_rubric', p_rubric_name)
    return p_rubric_name


fulltext_search = 'tracert'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]

value_cells = ['B4', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B16', 'B17']
rubric_sheet_name = 'Sheet1'

match_cells = ['D5', 'D15', 'D18']
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_level1_internet_2, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_level1_internet_2, person=person, match_cells=match_cells)

