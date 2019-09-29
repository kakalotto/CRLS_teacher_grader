# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.hardware_memory import docs_feedback_hardware_memory

fulltext_search = 'Memory'
person=''
if len(sys.argv) > 1:
    person = sys.argv[1]

def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'Hardware_Memory_lab', r'Hardware - Memory - rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B5', 'B7', 'B9', 'B11', 'B13', 'B15', 'B16', 'B18', 'F3', 'F5', 'F7', 'F9', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['H8', 'H10']
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_hardware_memory, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_hardware_memory, person=person, match_cells=match_cells)

