# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.encoding_color_images import docs_feedback_encoding_color_images

fulltext_search = 'Encoding color images'
person=''
if len(sys.argv) > 1:
    person = sys.argv[1]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'_lab', r'_rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B5', 'B7', 'B8', 'B10', 'B11', 'F3', 'F5', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['D9', 'D12', 'H4', 'H6',]

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_encoding_color_images,
                  match_cells=match_cells)
else:
        master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                      scorer=docs_feedback_encoding_color_images,
                      match_cells=match_cells, person=person)
