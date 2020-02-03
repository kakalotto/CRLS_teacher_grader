# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.bytes_and_filesizes_v3 import docs_feedback_bytes_and_file_sizes_v3

fulltext_search = 'A salesperson is trying to sell you a used phone '

person=''
if len(sys.argv) > 1:
    person = sys.argv[1]



def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab', r'rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13','B14', 'B15', 'B16',
               'B17', 'B18', 'F3', 'F4', 'F6', 'F7', 'F9', 'F10', 'F12','F13', 'F15', 'F16', ]
rubric_sheet_name = 'Sheet1'
match_cells = ['D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18', 'H5', 'H8', 'H11', 'H14', 'H17', 'H18', 'H19']

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_bytes_and_file_sizes_v3, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_bytes_and_file_sizes_v3, match_cells=match_cells, person=person)
