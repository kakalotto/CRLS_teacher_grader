# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.scratch_32_alternate import scratch_feedback_32_alternate
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


#             spaces hero  flag score  score  lft    rt, wlk ,jump,  scenery,lyr, mv, spd, roloer
value_cells = ['B20', 'B20', 'B8', 'B9', 'B10', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9']
rubric_sheet_name = 'Sheet1'


if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=scratch_feedback_32_alternate, scratch_file=True, scratch_lab_num='3.2_alternate',
                  scratch_rubric_suffix=' - Lab 3.2 alternate - rubric')
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,\
                  scorer=scratch_feedback_32_alternate, scratch_file=True, scratch_lab_num='3.2_alternate',
                  scratch_rubric_suffix=' - Lab 3.2 alternate - rubric', person=person)
