# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.stealing_password_from_unsecured_system \
    import route_docs_stealing_passwords_from_unsecured_systems as power


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab', r'rubric', p_rubric_name)
    return p_rubric_name


fulltext_search = 'You should never  save passwords on a public machine!'
person = ''
people = []
if len(sys.argv) == 2:
    person = sys.argv[1]
elif len(sys.argv) >= 3:
    people = sys.argv[1:]

value_cells = ['B3', 'B4', 'B5', 'B6', 'B7', 'B8']
rubric_sheet_name = 'Sheet1'

match_cells = ['D3', 'D4', 'D5', 'D6', 'D7', 'D8']
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

