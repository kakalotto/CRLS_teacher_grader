# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.encoding_text_v1 import route_docs_encoding_text

fulltext_search = 'Activity Guide - Encoding Text'
name_search = 'Encoding_text_v1'
person=''
if len(sys.argv) > 1:
    person = sys.argv[1]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'_lab', r'_rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B5', 'B7', 'B8', 'B10', 'B11', 'F3', 'F4', 'F6', 'F7']
rubric_sheet_name = 'Sheet1'

match_cells = ['D4', 'D6', 'D7', 'D9', 'D10', 'D12', 'H3', 'H5', 'H6', 'H8']

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=route_docs_encoding_text,
                  match_cells=match_cells, lab_name=name_search)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=route_docs_encoding_text,
                  match_cells=match_cells, person=person, lab_name=name_search)
