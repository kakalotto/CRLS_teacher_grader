# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.scratch_15 import scratch_feedback_15
import sys

fulltext_search = ''
person= ''
if len(sys.argv) > 1:
    person = sys.argv[1]



def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'Lab 1.4/1.5 Knock_Knock - RSTA Scratch',
                           r'Lab 1.4/1.5 Knock knock joke - rubric - RSTA', p_rubric_name)
    return p_rubric_name


value_cells = ['B9', 'F4', 'F5', 'B10', 'B11', 'B12', 'B13', 'B4']
rubric_sheet_name = 'Sheet1'


if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=scratch_feedback_15, scratch_file=True, scratch_lab_num='1.5',
                  scratch_rubric_suffix=' - Lab_1.5_Animated_Knock_Knock_Joke_rubric')
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,\
                  scorer=scratch_feedback_15, scratch_file=True, scratch_lab_num='1.5',
                  scratch_rubric_suffix=' - Lab_1.5_Animated_Knock_Knock_Joke_rubric', person=person)
