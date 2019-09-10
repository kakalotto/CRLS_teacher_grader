# Pass these in as parameters
from master_grader import master_grader

fulltext_search = 'ESD'


def doc_name_to_rubric_name(doc_name):
    import re
    p_rubric_name = doc_name
    p_rubric_name = re.sub(r'Hardware_',r'Hardware - ', p_rubric_name)
    p_rubric_name = re.sub(r'ESD_Expansion_cards_cases_lab', r'ESD_cases_expansion_cards - rubric', p_rubric_name)
    return p_rubric_name


value_cells = ['B3', 'B4', 'B6', 'B7', 'B8', 'B9', 'B10', 'B12', 'B14',  'F3', 'F5', 'F6']
rubric_sheet_name = 'Sheet1'

master_grader(fulltext_search, doc_name_to_rubric_name, value_cells, sheet_name='Sheet1')