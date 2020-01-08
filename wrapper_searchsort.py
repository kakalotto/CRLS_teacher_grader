# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.search_sort import docs_feedback_search_sort

def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'- Search_and_sort_lab', r'- Search and sort - Rubric', p_rubric_name)
    return p_rubric_name


fulltext_search = 'Sorting and Searching'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]


value_cells = ['F2', 'F4', 'F6', 'F8', 'F9', 'F11', 'F12', 'F13', 'F15', 'F17', 'F19', 'F20', ]
rubric_sheet_name = 'Sheet1'

match_cells = ['H3', 'H5', 'H7', 'H10', 'H14', 'H16', 'H18', ]
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_search_sort, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_search_sort, person=person, match_cells=match_cells)


