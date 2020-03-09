# Pass these in as parameters
import sys
from master_grader import master_grader
from CRLS_APCSP_autograder.app.big_data_sleuth_card import docs_feedback_big_data_sleuth_card


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'sleuth_card', r'sleuthcard_rubric', p_rubric_name)
    return p_rubric_name


fulltext_search = 'Activity Guide - Big Data Sleuth Card'
person = ''
if len(sys.argv) > 1:
    person = sys.argv[1]


value_cells = ['B3', 'B4', 'B6', 'B8', 'B10',]
rubric_sheet_name = 'Sheet1'

match_cells = ['D5', 'D7', 'D9', 'D11']
if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_big_data_sleuth_card, match_cells=match_cells)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_big_data_sleuth_card, person=person, match_cells=match_cells)


