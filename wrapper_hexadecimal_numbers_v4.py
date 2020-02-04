# Pass these in as parameters
from master_grader import master_grader
from CRLS_APCSP_autograder.app.hexadecimal_numbers_v4 import docs_feedback_hexadecimal_numbers_v4
import sys

#fulltext_search = 'hexadecimal_numbers_v4_lab'
#fulltext_search = 'Hexadecimal_numbers_v4'
fulltext_search = 'a number system comprised of the familiar ten arabic'

person=''
if len(sys.argv) > 1:
    person = sys.argv[1]


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'_lab', r'_rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9', 'B10', 'B11','B12','B13', ]
rubric_sheet_name = 'Sheet1'

if not person:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
              scorer=docs_feedback_hexadecimal_numbers_v4)
else:
    master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name=rubric_sheet_name,
                  scorer=docs_feedback_hexadecimal_numbers_v4, person=person)
    
