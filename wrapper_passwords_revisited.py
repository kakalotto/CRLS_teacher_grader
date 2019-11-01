# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.passwords_revisited import docs_feedback_passwords_passwords_revisited


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab', r'rubric', p_rubric_name)
    return p_rubric_name


fulltext_search = 'script kiddies always'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]


value_cells = ['B3', 'B5', 'B6', 'B6', 'B7', 'B9', 'B10', 'B12', 'B13', 'B15', 'B16', 'B17', 'B19', 'B21', 'B23', 'F3',
               'F5', 'F7', 'F9', 'F11', 'F13', 'F15', 'F15', 'F17']
rubric_sheet_name = 'Sheet1'

match_cells = ['C4', 'C8', 'C14', 'C118', 'C20', 'C22', 'C24', 'G4', 'G6', 'G8', 'G10', 'G12', 'G14', 'G16', 'G18', 'G19']
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_passwords_passwords_revisited, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_passwords_passwords_revisited, person=person, match_cells=match_cells)

