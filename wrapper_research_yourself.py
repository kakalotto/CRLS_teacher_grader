# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.research_yourself import route_docs_research_yourself as power


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'lab', r'rubric', p_rubric_name)
    return p_rubric_name


fulltext_search = 'Research Yourself'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]

value_cells = ['B4', 'B5', 'B6', 'B7', 'B8', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['D4', 'D5', 'D6', 'D7', 'D8',]
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=power, person=person, match_cells=match_cells)

