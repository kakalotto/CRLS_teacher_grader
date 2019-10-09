# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.research_yourself import docs_feedback_research_yourself


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'yourself', r'yourself - Rubric', p_rubric_name)
    return p_rubric_name


fulltext_search = 'Research Yourself'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]

value_cells = ['F5', 'F6', 'F7', 'F8', 'F9', ]
rubric_sheet_name = 'Sheet1'

match_cells = []
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_research_yourself, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_research_yourself, person=person, match_cells=match_cells)

