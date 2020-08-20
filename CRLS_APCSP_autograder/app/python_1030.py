def route_docs_python_1030(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=29.5, score_manual=8)
    text = get_text(link)
    expected = 'https://docs.google.com/presentation/d/12hooQ6UZPh7P2TgoLw-Rj_UJaFrP0q4Qe88lIyLHHL0/' \
               'edit#slide=id.g5304dafeb6_0_0'
    print_string = 'https://docs.google.com/presentation/d/1WM9dqehCsNLaOKVI7XkMqHymR1R6Lijx0ZvJC4NKjPE/' \
                   'edit#slide=id.g1ccdc42220236e58_10'
    print_ints = 'https://docs.google.com/presentation/d/1WM9dqehCsNLaOKVI7XkMqHymR1R6Lijx0ZvJC4NKjPE/' \
                 'edit#slide=id.g1ccdc42220236e58_37'
    cat = 'https://docs.google.com/presentation/d/1WM9dqehCsNLaOKVI7XkMqHymR1R6Lijx0ZvJC4NKjPE/' \
          'edit#slide=id.g1ccdc42220236e58_46'
    cat2 = 'https://docs.google.com/presentation/d/1R1jJfHfXgtZAjrYpC8lKL7uG4VW5Ujy8h3TawLWab3A/' \
           'edit#slide=id.g3fba4a5ac1_1_63'
    q_8 = 'https://docs.google.com/presentation/d/12hooQ6UZPh7P2TgoLw-Rj_UJaFrP0q4Qe88lIyLHHL0/' \
          'edit#slide=id.g8c389c728e_2_0'
    no_defined = 'https://docs.google.com/presentation/d/1WM9dqehCsNLaOKVI7XkMqHymR1R6Lijx0ZvJC4NKjPE/' \
                 'edit#slide=id.g1ccdc42220236e58_19'
    tests.append(check_answer('1a', 'question 1a expected', text, {'answers': r'[a-zA-Z0-9]+', 'help_link': expected},
                              points=0.5))
    tests.append(check_answer('1b', 'question 2b actual', text,
                              {'answers': r'1', 'help_link': print_string}, points=0.5))
    tests.append(check_answer('1c', 'question 1c different', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': print_string}, points=0.5))
    tests.append(check_answer('2a', 'question 2a expected', text, {'answers': r'[a-zA-Z0-9]+', 'help_link': expected},
                              points=0.5))
    tests.append(check_answer('2b', 'question 2b actual', text,
                              {'answers': r'1', 'help_link': print_ints}, points=0.5))
    tests.append(check_answer('2c', 'question 2c different', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': print_ints}, points=0.5))
    tests.append(check_answer('3a', 'question 3a expected', text, {'answers': r'[a-zA-Z0-9]+', 'help_link': expected},
                              points=0.5))
    tests.append(check_answer('3b', 'question 3b actual', text,
                              {'answers': r'3', 'help_link': print_ints}, points=0.5))
    tests.append(check_answer('3c', 'question 3c different', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': print_ints}, points=0.5))
    tests.append(check_answer('4a', 'question 4a expected', text, {'answers': r'[a-zA-Z0-9]+', 'help_link': expected},
                              points=0.5))
    tests.append(check_answer('4b', 'question 4b actual', text,
                              {'answers': r'12', 'help_link': cat}, points=0.5))
    tests.append(check_answer('4c', 'question 4c different', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': cat}, points=0.5))
    tests.append(check_answer('5a', 'question 5a expected', text, {'answers': r'[a-zA-Z0-9]+', 'help_link': expected},
                              points=0.5))
    tests.append(check_answer('5b', 'question 5b actual', text,
                              {'answers': r'this \s is \s a \s sentence\.', 'help_link': cat2}, points=0.5))
    tests.append(check_answer('5c', 'question 5c different', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': text}, points=0.5))
    tests.append(check_answer('6a', 'What does this print', text,
                              {'answers': r'dogs \s are \s really \s cool', 'help_link': print_string}, points=5))
    tests.append(check_answer('6b', 'Why?', text, {'min_words': 5}, points=1))
    tests.append(check_answer('7a', 'What does this print', text,
                              {'answers': r'error', 'help_link': print_string}, points=5))
    tests.append(check_answer('7b', 'Why?', text, {'min_words': 5, 'help_link': no_defined}, points=1))
    tests.append(check_answer('8a', 'Create variable "number" equal to 100', text,
                              {'answers': r'number \s* = \s* 100', 'help_link': q_8}, points=2.5))
    tests.append(check_answer('8a', 'print number', text,
                              {'answers': r'print \s* \(number\)', 'help_link': q_8}, points=2.5))
    tests.append(check_answer('8a', 'Create variable "number2" equal to "number" + 100', text,
                              {'answers': r'number2  .+? 100', 'help_link': q_8}, points=2.5))
    tests.append(check_answer('8a', 'print number2', text,
                              {'answers': r'print \s* \(number2\)', 'help_link': q_8}, points=2.5))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
