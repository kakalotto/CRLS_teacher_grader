# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.hw06 import route_docs_hw06

fulltext_search = 'HW 6, Booleans'
person = ''
name_search = 'HW06'

if len(sys.argv) > 1:
    person = sys.argv[1]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'_lab', r'_rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B5', 'B6', 'B7', 'B8']
rubric_sheet_name = 'Sheet1'
match_cells = ['D3', 'D4', 'D5', 'D6', 'D7', 'D8']

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=route_docs_hw06, match_cells=match_cells, lab_name=name_search)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=route_docs_hw06, person=person, match_cells=match_cells, lab_name=name_search)
