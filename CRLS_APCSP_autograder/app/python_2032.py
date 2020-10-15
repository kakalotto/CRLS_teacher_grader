
# noinspection SpellCheckingInspection
def route_docs_python_2032(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=12, score_manual=0)
    text = get_text(link)
    tf = 'https://docs.google.com/presentation/d/10zEU08zpSXwkTaMFIsUTLydJtZbP7tM869NRBIL0v1o/' \
         'edit#slide=id.g8c389caccd_3_0'
    table = 'https://docs.google.com/presentation/d/10zEU08zpSXwkTaMFIsUTLydJtZbP7tM869NRBIL0v1o/edit#' \
            'slide=id.g8c7451539a_0_0'
    tests.append(check_answer('1a', 'expected', text, {'answers': r'(true|false)', 'help_link': tf}, points=0.5))
    tests.append(check_answer('1b', 'Actual', text, {'answers': r'true', 'help_link': tf}, points=0.5))
    tests.append(check_answer('2a', 'expected', text, {'answers': r'(true|false)', 'help_link': tf}, points=0.5))
    tests.append(check_answer('2b', 'Actual', text, {'answers': r'false', 'help_link': tf}, points=0.5))
    tests.append(check_answer('3a', 'expected', text, {'answers': r'(true|false)', 'help_link': tf}, points=0.5))
    tests.append(check_answer('3b', 'Actual', text, {'answers': r'true', 'help_link': tf}, points=0.5))
    tests.append(check_answer('4a', 'expected', text, {'answers': r'(true|false)', 'help_link': tf}, points=0.5))
    tests.append(check_answer('4b', 'Actual', text, {'answers': r'false', 'help_link': tf}, points=0.5))
    tests.append(check_answer('5a', 'result', text, {'answers': r'false', 'help_link': table}, points=0.5))
    tests.append(check_answer('6a', 'result', text, {'answers': r'false', 'help_link': table}, points=0.5))
    tests.append(check_answer('7a', 'result', text, {'answers': r'true', 'help_link': table}, points=0.5))
    tests.append(check_answer('8a', 'result', text, {'answers': r'false', 'help_link': table}, points=0.5))
    tests.append(check_answer('9a', 'result', text, {'answers': r'false', 'help_link': table}, points=0.5))
    tests.append(check_answer('10a', 'result', text, {'answers': r'false', 'help_link': table}, points=0.5))
    tests.append(check_answer('11a', 'result', text, {'answers': r'false', 'help_link': table}, points=0.5))
    tests.append(check_answer('12a', 'result', text, {'answers': r'false', 'help_link': table}, points=0.5))
    tests.append(check_answer('13a', 'stomach', text, {'answers': r'[0-9]', 'help_link': table}, points=0.1))
    tests.append(check_answer('13b', 'money', text, {'answers': r'[0-9]', 'help_link': table}, points=0.1))
    tests.append(check_answer('13c', 'T/F', text, {'answers': r'(true|false)', 'help_link': table}, points=0.3))
    tests.append(check_answer('14a', 'stomach', text, {'answers': r'[0-9]', 'help_link': table}, points=0.1))
    tests.append(check_answer('14b', 'money', text, {'answers': r'[0-9]', 'help_link': table}, points=0.1))
    tests.append(check_answer('14c', 'T/F', text, {'answers': r'(true|false)', 'help_link': table}, points=0.3))
    tests.append(check_answer('15a', 'stomach', text, {'answers': r'[0-9]', 'help_link': table}, points=0.1))
    tests.append(check_answer('15b', 'money', text, {'answers': r'[0-9]', 'help_link': table}, points=0.1))
    tests.append(check_answer('15c', 'T/F', text, {'answers': r'(true|false)', 'help_link': table}, points=0.3))
    tests.append(check_answer('16a', 'stomach', text, {'answers': r'[0-9]', 'help_link': table}, points=0.1))
    tests.append(check_answer('16b', 'money', text, {'answers': r'[0-9]', 'help_link': table}, points=0.1))
    tests.append(check_answer('16c', 'T/F', text, {'answers': r'(true|false)', 'help_link': table}, points=0.3))
    tests.append(check_answer('17a', 'stomach', text, {'answers': r'[0-9]', 'help_link': table}, points=0.1))
    tests.append(check_answer('17b', 'money', text, {'answers': r'[0-9]', 'help_link': table}, points=0.1))
    tests.append(check_answer('17c', 'T/F', text, {'answers': r'(true|false)', 'help_link': table}, points=0.3))
    tests.append(check_answer('18a', 'stomach', text, {'answers': r'[0-9]', 'help_link': table}, points=0.1))
    tests.append(check_answer('18b', 'money', text, {'answers': r'[0-9]', 'help_link': table}, points=0.1))
    tests.append(check_answer('18c', 'T/F', text, {'answers': r'(true|false)', 'help_link': table}, points=0.3))
    tests.append(check_answer('19a', 'stomach', text, {'answers': r'[0-9]', 'help_link': table}, points=0.1))
    tests.append(check_answer('19b', 'money', text, {'answers': r'[0-9]', 'help_link': table}, points=0.1))
    tests.append(check_answer('19c', 'T/F', text, {'answers': r'(true|false)', 'help_link': table}, points=0.3))
    tests.append(check_answer('20a', 'stomach', text, {'answers': r'[0-9]', 'help_link': table}, points=0.1))
    tests.append(check_answer('20b', 'money', text, {'answers': r'[0-9]', 'help_link': table}, points=0.1))
    tests.append(check_answer('20c', 'T/F', text, {'answers': r'(true|false)', 'help_link': table}, points=0.3))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]