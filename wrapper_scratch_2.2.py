# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.scratch_22 import route_scratch_2_2 as power
import sys

fulltext_search = ''
person = ''
people = []
if len(sys.argv) == 2:
    person = sys.argv[1]
elif len(sys.argv) >= 3:
    people = sys.argv[1:]

print("people are " + str(people))


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab',
                           r'rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B7', 'F3', 'F4', 'F5', 'F6', 'B3']
rubric_sheet_name = 'Sheet1'


if not person and not people:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power, scratch_file=True, scratch_lab_num='2.2',
                  scratch_rubric_suffix=' - Lab_2.2_Yellow_Brick_Road_rubric')
else:
    if person:
        master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,\
                      scorer=power, scratch_file=True, scratch_lab_num='2.2',
                      scratch_rubric_suffix=' - Lab_2.2_Yellow_Brick_Road_rubric', person=person)
    elif people:
        for scholar in people:
            master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name, \
                          scorer=power, scratch_file=True, scratch_lab_num='2.2',
                          scratch_rubric_suffix=' - Lab_2.2_Yellow_Brick_Road_rubric', person=scholar)
