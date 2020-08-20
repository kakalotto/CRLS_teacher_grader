# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.python_1030 import route_docs_python_1030
import sys
person = ''
fulltext_search = 'Python 1.030'

if len(sys.argv) > 1:
    person = sys.argv[1]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab',
                           r'rubric',
                           p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', 'B15', 'B16', 'B17', 'B18',
               'B19', 'B21', 'B22', 'F3', 'F4', 'F5', 'F6', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9', 'D10', 'D11', 'D12', 'D13', 'D14', 'D15', 'D16', 'D17', 'D18',
               'D19', 'D21', 'D22', 'H3', 'H4', 'H5', 'H6', ]

# match_cells = ['D20', 'D23']

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=route_docs_python_1030, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=route_docs_python_1030, match_cells=match_cells, person=person)
