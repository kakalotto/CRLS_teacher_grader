# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.lossless_compression_v2 import route_docs_lossless_compression_v2 as magic

fulltext_search = 'Lossless compression presentation'

person=''
if len(sys.argv) > 1:
    person = sys.argv[1]

def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'_lab', r'_rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B6', 'B8', 'B10', 'B12', 'B14',
               'F3', 'F5', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['D3', 'D5', 'D7', 'D9', 'D11', 'D12', 'D14']

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=magic,
                  match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=magic,
                  match_cells=match_cells, person=person)
