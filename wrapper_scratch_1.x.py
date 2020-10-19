# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.scratch_1x import route_scratch_1_x as power
import sys

fulltext_search = ''
person= ''
if len(sys.argv) > 1:
    person = sys.argv[1]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'capstone My Family Migration Story - RSTA',
                           r'Family migration story - rubric - RSTA', p_rubric_name)
    return p_rubric_name


value_cells = ['B9', 'B14', 'F4', 'F5', 'B10', 'B11', 'B12', 'B13', 'F6', 'B4']
rubric_sheet_name = 'Sheet1'


if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power, scratch_file=True, scratch_lab_num='1.x',
                  scratch_rubric_suffix=' - Lab_1.x_My_Family_Migration_Story_Story_of_self_rubric')
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,\
                  scorer=power, scratch_file=True, scratch_lab_num='1.x',
                  scratch_rubric_suffix=' - Lab_1.x_My_Family_Migration_Story_Story_of_self_rubric', person=person)
