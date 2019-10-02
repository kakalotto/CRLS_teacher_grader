# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.hardware_cpus import docs_feedback_hardware_cpus

fulltext_search = 'cpu'
person=''
if len(sys.argv) > 1:
    person = sys.argv[1]

def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'_lab', r'_rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B5', 'B7', 'B9', 'B10', 'B11', 'B13', 'B14', 'F3', 'F4', 'F5', 'F6', 'F7']
rubric_sheet_name = 'Sheet1'

match_cells = ['D4', 'D6', 'D8', 'D12', 'F4']
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_hardware_cpus, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_hardware_cpus, person=person, match_cells=match_cells)

