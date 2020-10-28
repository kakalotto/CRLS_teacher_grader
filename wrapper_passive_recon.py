# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.passive_recon import route_docs_passive_recon as power


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab', r'rubric', p_rubric_name)
    return p_rubric_name


fulltext_search = 'Use the whois tool on 3 sites'
person = ''
people = []
if len(sys.argv) == 2:
    person = sys.argv[1]
elif len(sys.argv) > 3:
    people = sys.argv[1:]

value_cells = ['B3', 'B5', 'B7', 'B9', 'B11', 'B13',  'B15', 'B16', 'B17', 'B19',
               'B20', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['D4', 'D6', 'D8', 'D10', 'D12', 'D14',  'D15', 'D16', 'D18', 'D19', 'D20']
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

