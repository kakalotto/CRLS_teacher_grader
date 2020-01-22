# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.hex_minilab_v2 import docs_feedback_hex_minilab_v2

fulltext_search = '- Hex_mini_lab'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]

    # NEED TO FIX HIS S2 2019/2020 2n entry b19 is a dummy.


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'minilab_lab', r'minilab_rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', ]
rubric_sheet_name = 'Sheet1'

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_hex_minilab_v2)
else:
     master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                   scorer=docs_feedback_hex_minilab_v2, person=person)
