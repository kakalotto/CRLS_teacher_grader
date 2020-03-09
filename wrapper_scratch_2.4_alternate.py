# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.scratch_24 import scratch_feedback_24_alternate
import sys

fulltext_search = ''
person= ''
if len(sys.argv) > 1:
    person = sys.argv[1]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'Yellow Brick Road - RSTA Scratch',
                           r'Lab 2.4 alternate variables - rubric - RSTA', p_rubric_name)
    return p_rubric_name


value_cells = ['F5', 'B9', 'F4', 'F6', 'F7', 'F8', 'B11', 'F9', 'F10', 'F11', 'F12', 'B10', 'B4']
rubric_sheet_name = 'Sheet1'


if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=scratch_feedback_24_alternate, scratch_file=True, scratch_lab_num='2.4',
                  scratch_rubric_suffix=' - Lab 2.4 alternate variables - rubric - RSTA')
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,\
                  scorer=scratch_feedback_24_alternate, scratch_file=True, scratch_lab_num='2.4',
                  scratch_rubric_suffix=' - Lab 2.4 alternate variables - rubric - RSTA', person=person)
