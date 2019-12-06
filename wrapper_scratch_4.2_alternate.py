# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.scratch_42_alternate import scratch_feedback_42_alternate
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


value_cells = ['B12', 'B8', 'B9', 'B10', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11', 'B4']
rubric_sheet_name = 'Sheet1'


if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=scratch_feedback_42_alternate, scratch_file=True, scratch_lab_num='4.2',
                  scratch_rubric_suffix=' - Lab 4.2 Mr. Kanns ice cream shop - rubric')
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,\
                  scorer=scratch_feedback_42_alternate, scratch_file=True, scratch_lab_num='4.2',
                  scratch_rubric_suffix=' - Lab 4.2 Mr. Kanns ice cream shop - rubric', person=person)
