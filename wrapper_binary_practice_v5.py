# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.binary_practice_v5 import route_docs_binary_practice_v5

fulltext_search = 'Binary_practice'
person=''
if len(sys.argv) > 1:
    person = sys.argv[1]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'_lab', r'_rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18',
               'B19', 'B20', 'B21', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'F12', 'F13', 'F14', 'F15',
               'F16', 'F17', 'F19', 'F20', 'F22', 'F23', 'F25', 'F26', 'F28', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17',
               'D18', 'D19', 'D20', 'D21', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10', 'H11', 'H12', 'H13', 'H14',
               'H15', 'H16', 'H18', 'H19', 'H21', 'H22', 'H24', 'H25', 'H26', 'H27']

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=route_docs_binary_practice_v5,
                  match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=route_docs_binary_practice_v5,
                  match_cells=match_cells, person=person)
