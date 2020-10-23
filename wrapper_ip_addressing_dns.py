# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.ip_addressing_dns import route_docs_ip_addressing_dns as power
fulltext_search = 'IP address'
lab_extra_fulltext = 'Cerf'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab', r'rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B6', 'B8', 'B9', 'B10', 'F3', 'F5', 'F7', 'F9']
rubric_sheet_name = 'Sheet1'

match_cells = ['D9', 'D5', 'D7', 'D9', 'D9', 'D11', 'H4', 'H6', 'H8', 'H10']
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power, match_cells=match_cells,
                  lab_extra_fulltext=lab_extra_fulltext)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power, person=person, match_cells=match_cells,
                  lab_extra_fulltext=lab_extra_fulltext)

