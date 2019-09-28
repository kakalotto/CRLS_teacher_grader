# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.ip_addressing_dns import docs_feedback_ip_addressing_dns

fulltext_search = 'IP address'
lab_extra_fulltext = 'Cerf'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab', r'lab - Rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B6', 'B8', 'B9', 'B10', 'F3', 'F5', 'F7', 'F9']
rubric_sheet_name = 'Sheet1'

match_cells = ['A15', 'D5', 'D7', 'A15', 'A15', 'D11', 'H4', 'H6', 'H8', 'H10']
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_ip_addressing_dns, match_cells=match_cells,
                  lab_extra_fulltext=lab_extra_fulltext)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_ip_addressing_dns, person=person, match_cells=match_cells,
                  lab_extra_fulltext=lab_extra_fulltext)

