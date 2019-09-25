# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.scratch_22 import scratch_feedback_22
import sys

fulltext_search = ''
person= ''
if len(sys.argv) > 1:
    person = sys.argv[1]



def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'Yellow Brick Road - RSTA Scratch',
                           r'Brick Wall - rubric - RSTA', p_rubric_name)
    return p_rubric_name


value_cells = ['B7', 'F3', 'F4', 'F5', 'F6']
rubric_sheet_name = 'Sheet1'


if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=scratch_feedback_22, scratch_file=True, scratch_lab_num='2.2',
                  scratch_rubric_suffix=' - Brick Wall - rubric - RSTA')
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,\
                  scorer=scratch_feedback_22, scratch_file=True, scratch_lab_num='2.2',
                  scratch_rubric_suffix=' - Brick Wall - rubric - RSTA', person=person)
