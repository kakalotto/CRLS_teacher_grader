# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.scratch_35 import route_scratch_3_5 as power
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


#             spaces hero  flag score  score  lft    rt, wlk ,jump,  scenery,lyr, mv, spd, roloer
value_cells = ['B23', 'B23', 'B9','B10', 'B11', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'F11' , 'F12',
               'F13', 'F14', 'F15', 'F16', 'F17', 'F18', 'F19', 'F20', 'F21', 'F22', 'F23', 'B4']
rubric_sheet_name = 'Sheet1'


if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power, scratch_file=True, scratch_lab_num='3.5',
                  scratch_rubric_suffix=' - Lab_3.5_Platform_game_rubric')
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,\
                  scorer=power, scratch_file=True, scratch_lab_num='3.5',
                  scratch_rubric_suffix=' - Lab_3.5_Platform_game_rubric', person=person)
# - Lab_3.5_Platform_game_rubric