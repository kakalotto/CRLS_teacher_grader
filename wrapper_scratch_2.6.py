# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.scratch_26 import route_scratch_2_6 as power
import sys

fulltext_search = ''
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'Yellow Brick Road - RSTA Scratch',
                           r'Lab 2.4 alternate variables - rubric - RSTA', p_rubric_name)
    return p_rubric_name


value_cells = ['B8', 'F4', 'F5', 'F6', 'F7', 'F8', 'B4']
rubric_sheet_name = 'Sheet1'


if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power, scratch_file=True, scratch_lab_num='2.6',
                  scratch_rubric_suffix=' - Lab_2.6_What_goes_up_rubric')
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,\
                  scorer=power, scratch_file=True, scratch_lab_num='2.6',
                  scratch_rubric_suffix=' - Lab_2.6_What_goes_up_rubric', person=person)
