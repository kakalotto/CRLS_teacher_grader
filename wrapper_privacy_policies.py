# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.privacy_policies import route_docs_privacy_policies as power


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab', r'rubric', p_rubric_name)
    return p_rubric_name


fulltext_search = 'Privacy Policies'
person = ''
people = []
if len(sys.argv) == 1:
    person = sys.argv[1]
elif len(sys.argv) > 1:
    people = sys.argv[1:]


value_cells = ['B5', 'D15', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15']
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

