# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.lossy_compression_v2 import route_docs_lossy_compression_v2

fulltext_search = 'Lossy compression presentation'
person=''
if len(sys.argv) > 1:
    person = sys.argv[1]



def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
#    p_rubric_name = re.sub(r'_lab', r' - Rubric', p_rubric_name)
    p_rubric_name = re.sub(r'_lab_v2', r'_v2_rubric', p_rubric_name)

    return p_rubric_name


value_cells = ['B3', 'B5', 'B6', 'B7', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'F3', 'F4', 'F5', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['D4', 'D6', 'D8', 'D9', 'D11']

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=route_docs_lossy_compression_v2,
                  match_cells=match_cells)
else:    
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=route_docs_lossy_compression_v2,
                  match_cells=match_cells, person=person)
