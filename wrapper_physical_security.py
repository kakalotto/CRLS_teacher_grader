# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.physical_security import route_docs_physical_security as power


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab', r'rubric', p_rubric_name)
    return p_rubric_name


fulltext_search = 'Physical security is security up BEFORE an actual computer'
person = ''
people = []
if len(sys.argv) == 2:
    person = sys.argv[1]
elif len(sys.argv) >= 3:
    people = sys.argv[1:]

value_cells = ['B3', 'B5', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['D4', 'D6',]
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

