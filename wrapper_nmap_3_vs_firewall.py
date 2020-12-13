# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.nmap_3_vs_firewall import route_docs_nmap_3_vs_firewall as power


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab', r'rubric', p_rubric_name)
    return p_rubric_name


fulltext_search = 'On machine #1,  scan yourself with Nmap'
person = ''
people = []
if len(sys.argv) == 2:
    person = sys.argv[1]
elif len(sys.argv) >= 3:
    people = sys.argv[1:]

value_cells = ['B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10',
               'B11', 'B12', 'B13', 'B16', 'B17', 'B18',
               'B19', 'B20', 'B21', 'B22', 'B23' ,'B31',]
rubric_sheet_name = 'Sheet1'


match_cells = ['D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11',  'D12', 'D13', 'D16', 'D17',
               'D18', 'D19', 'D20', 'D21', 'D22', 'D23', 'D30',]
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

