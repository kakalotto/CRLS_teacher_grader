# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.network_protocols_revisited import route_docs_network_protocols_revisited as power


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab', r'rubric', p_rubric_name)
    return p_rubric_name


fulltext_search = 'Recon Network protocols revisited'
person = ''
people = []
if len(sys.argv) == 2:
    person = sys.argv[1]
elif len(sys.argv) >= 3:
    people = sys.argv[1:]

value_cells = ['B3', 'B4', 'B5', 'B6', 'B8', 'B10', 'B12', 'F3', 'F4', 'F6', 'F7',  'F9', 'F10', 'F12', 'F13',
               'F15', 'F16', 'F18', 'B19', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['D3', 'D4', 'D5', 'D7', 'D9', 'D11', 'D13', 'H3', 'H5', 'H6', 'H8', 'H9', 'H11', 'H12', 'H14', 'H15',
               'H17', 'H18', 'H20']
if not person and not people:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power, match_cells=match_cells)
else:
    if person:
        master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                      scorer=power, person=person, match_cells=match_cells)
    elif people:
        for scholar in people:
            master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                          scorer=power, person=scholar, match_cells=match_cells)

