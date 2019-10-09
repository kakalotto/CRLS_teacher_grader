# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.privacy_policies import docs_feedback_privacy_policies


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'Privacy_policies', r'Privacy_policies - Rubric', p_rubric_name)
    return p_rubric_name


fulltext_search = 'Privacy Policies'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]

    # NEED TO FIX HIS S2 2019/2020 2n entry b19 is a dummy.

value_cells = ['B5', 'B19', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14', ]
rubric_sheet_name = 'Sheet1'

match_cells = []
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_privacy_policies, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_privacy_policies, person=person, match_cells=match_cells)


