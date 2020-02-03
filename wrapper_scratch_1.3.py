# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.scratch_13 import scratch_feedback_13
import sys

fulltext_search = ''
person= ''
if len(sys.argv) > 1:
    person = sys.argv[1]



def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab', r'rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B9', 'F4', 'F5', 'F6', 'F7', 'B4', ]
rubric_sheet_name = 'Sheet1'


if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,\
              scorer=scratch_feedback_13, scratch_file=True, scratch_lab_num='1.3',
              scratch_rubric_suffix='- Lab_1.3_Squares_and_triangles_and_stars_Oh_My_rubric')
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,\
                  scorer=scratch_feedback_13, scratch_file=True, scratch_lab_num='1.3',
                  scratch_rubric_suffix='- Lab_1.3_Squares_and_triangles_and_stars_Oh_My_rubric', person=person)
