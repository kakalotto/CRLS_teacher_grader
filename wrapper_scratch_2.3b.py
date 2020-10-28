# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.scratch_23b import route_scratch_2_3b as power
import sys

fulltext_search = ''
person = ''
people = []
if len(sys.argv) == 2:
    person = sys.argv[1]
elif len(sys.argv) > 3:
    people = sys.argv[1:]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'Yellow Brick Road - RSTA Scratch',
                           r'Lab 2.4 alternate variables - rubric - RSTA', p_rubric_name)
    return p_rubric_name


value_cells = ['B7', 'F5', 'F6', 'F7', 'F8', 'F9', 'F10', 'B3']
rubric_sheet_name = 'Sheet1'


if not person and not people:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power, scratch_file=True, scratch_lab_num='2.3b',
                  scratch_rubric_suffix=' - Lab_2.3b_conditionals_rubric')
else:
    if person:
        master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,\
                      scorer=power, scratch_file=True, scratch_lab_num='2.3b',
                      scratch_rubric_suffix=' - Lab_2.3b_conditionals_rubric', person=person)
    elif people:
        for scholar in people:
            master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name, \
                          scorer=power, scratch_file=True, scratch_lab_num='2.3b',
                          scratch_rubric_suffix=' - Lab_2.3b_conditionals_rubric', person=scholar)