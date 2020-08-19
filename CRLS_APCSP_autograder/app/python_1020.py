def route_docs_python_1020(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=39, score_manual=10)
    text = get_text(link)
    expected = 'https://docs.google.com/presentation/d/12hooQ6UZPh7P2TgoLw-Rj_UJaFrP0q4Qe88lIyLHHL0/' \
               'edit#slide=id.g5304dafeb6_0_0'
    difference = 'https://docs.google.com/presentation/d/12hooQ6UZPh7P2TgoLw-Rj_UJaFrP0q4Qe88lIyLHHL0/' \
                 'edit#slide=id.g5304dafeb6_0_13'
    datatype = 'https://docs.google.com/presentation/d/12hooQ6UZPh7P2TgoLw-Rj_UJaFrP0q4Qe88lIyLHHL0/' \
               'edit#slide=id.g5304dafeb6_0_5'
    pemdas = 'https://docs.google.com/presentation/d/1WM9dqehCsNLaOKVI7XkMqHymR1R6Lijx0ZvJC4NKjPE/' \
             'edit#slide=id.g1ccdc42220236e58_37'
    math = 'https://docs.google.com/presentation/d/1WM9dqehCsNLaOKVI7XkMqHymR1R6Lijx0ZvJC4NKjPE/' \
           'edit#slide=id.g1ccdc42220236e58_80'
    no_defined = 'https://docs.google.com/presentation/d/1WM9dqehCsNLaOKVI7XkMqHymR1R6Lijx0ZvJC4NKjPE/' \
                 'edit#slide=id.g1ccdc42220236e58_19'
    defined = 'https://docs.google.com/presentation/d/1WM9dqehCsNLaOKVI7XkMqHymR1R6Lijx0ZvJC4NKjPE/' \
              'edit#slide=id.g1ccdc42220236e58_28'
    cat = 'https://docs.google.com/presentation/d/1WM9dqehCsNLaOKVI7XkMqHymR1R6Lijx0ZvJC4NKjPE/' \
          'edit#slide=id.g1ccdc42220236e58_46'
    math_and_strings = 'https://docs.google.com/presentation/d/1WM9dqehCsNLaOKVI7XkMqHymR1R6Lijx0ZvJC4NKjPE/' \
                       'edit#slide=id.g1ccdc42220236e58_89'
    more_math_strings = 'https://docs.google.com/presentation/d/1WM9dqehCsNLaOKVI7XkMqHymR1R6Lijx0ZvJC4NKjPE/' \
                        'edit#slide=id.g1ccdc42220236e58_109'
    tests.append(check_answer('1a', 'question 1 expected', text, {'answers': r'[a-zA-Z0-9]+', 'help_link': expected},
                              points=0.5))
    tests.append(check_answer('1b', 'question 1 actual', text, {'answers': r'9', 'help_link': pemdas},
                              points=0.5))
    tests.append(check_answer('1c', 'question 1 difference', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': difference}, points=0.5))
    tests.append(check_answer('2a', 'question 2 expected', text,
                              {'answers': r'[a-zA-Za-zA-Z0-9]+', 'help_link': expected}, points=0.5))
    tests.append(check_answer('2b', 'question 2 actual', text, {'answers': r'0*\.6+', 'help_link': pemdas},
                              points=0.5))
    tests.append(check_answer('2c', 'question 2 difference', text,
                              {'answers': r'[a-zA-Za-zA-Z0-9]+', 'help_link': difference}, points=0.5))
    tests.append(check_answer('3a', 'question 3 expected', text,
                              {'answers': r'[a-zA-Za-zA-Z0-9]+', 'help_link': expected}, points=0.5))
    tests.append(check_answer('3b', 'question 3 actual', text, {'answers': r'3.0', 'help_link': pemdas},
                              points=0.5))
    tests.append(check_answer('3c', 'question 3 difference', text, {'answers': r'[a-zA-Z]+', 'help_link': difference},
                              points=0.5))
    tests.append(check_answer('4a', 'question 4 expected', text,
                              {'answers': r'[a-zA-Za-zA-Z0-9]+', 'help_link': expected}, points=0.5))
    tests.append(check_answer('4b', 'question 4 actual', text, {'answers': r'50', 'help_link': pemdas},
                              points=0.5))
    tests.append(check_answer('4c', 'question 4 difference', text, {'answers': r'[a-zA-Z]+', 'help_link': difference},
                              points=0.5))
    tests.append(check_answer('5a', 'question 5 expected', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': expected}, points=0.5))
    tests.append(check_answer('5b', 'question 5 actual', text, {'answers': r'2\.0', 'help_link': math},
                              points=0.5))
    tests.append(check_answer('5c', 'question 5 difference', text, {'answers': r'[a-zA-Z]+', 'help_link': difference},
                              points=0.5))
    tests.append(check_answer('6a', 'question 6 expected', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': expected}, points=0.5))
    tests.append(check_answer('6b', 'question 6 actual', text, {'answers': r'1\.0', 'help_link': math},
                              points=0.5))
    tests.append(check_answer('6c', 'question 6 difference', text, {'answers': r'[a-zA-Z]+', 'help_link': difference},
                              points=0.5))
    tests.append(check_answer('7a', 'question 7 expected', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': expected}, points=0.5))
    tests.append(check_answer('7b', 'question 7 actual', text, {'answers': r'error', 'help_link': no_defined},
                              points=0.5))
    tests.append(check_answer('7c', 'question 7 difference', text, {'answers': r'[a-zA-Z]+', 'help_link': difference},
                              points=0.5))
    tests.append(check_answer('8a', 'question 8 expected', text, {'answers': r'[a-zA-Z]+', 'help_link': expected},
                              points=0.5))
    tests.append(check_answer('8b', 'question 8 actual', text, {'answers': r'a', 'help_link': defined}, points=0.5))
    tests.append(check_answer('8c', 'question 8 difference', text, {'answers': r'[a-zA-Z]+', 'help_link': difference},
                              points=0.5))
    tests.append(check_answer('9a', 'question 9 expected', text, {'answers': r'[a-zA-Z]+', 'help_link': expected},
                              points=0.5))
    tests.append(check_answer('9b', 'question 9 actual', text, {'answers': r'a \s* \+ \s* b', 'help_link': defined},
                              points=0.5))
    tests.append(check_answer('9c', 'question 9 difference', text, {'answers': r'[a-zA-Z]+', 'help_link': difference},
                              points=0.5))
    tests.append(check_answer('10a', 'question 10 expected', text, {'answers': r'[a-zA-Z]+', 'help_link': expected},
                              points=0.5))
    tests.append(check_answer('10b', 'question 10 actual', text, {'answers': r'ab', 'help_link': cat},
                              points=0.5))
    tests.append(check_answer('10c', 'question 10 difference', text, {'answers': r'[a-zA-Z]+', 'help_link': difference},
                              points=0.5))
    tests.append(check_answer('11a', 'question 11 expected', text, {'answers': r'[a-zA-Z]+', 'help_link': expected},
                              points=0.5))
    tests.append(check_answer('11b', 'question 11 actual', text, {'answers': r'error', 'help_link': math_and_strings},
                              points=0.5))
    tests.append(check_answer('11c', 'question 11 difference', text, {'answers': r'[a-zA-Z]+', 'help_link': difference},
                              points=0.5))
    tests.append(check_answer('12a', 'question 12 expected', text, {'answers': r'[a-zA-Z]+', 'help_link': expected},
                              points=0.5))
    tests.append(check_answer('12b', 'question 12 actual', text, {'answers': r'aa', 'help_link': math_and_strings},
                              points=0.5))
    tests.append(check_answer('12c', 'question 12 difference', text, {'answers': r'[a-zA-Z]+', 'help_link': difference},
                              points=0.5))
    tests.append(check_answer('13a', 'question 13 expected datatype', text,
                              {'answers': r'(integer|float|string|error)', 'help_link': datatype}, points=0.5))
    tests.append(check_answer('13b', 'question 13 expected', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': expected}, points=0.5))
    tests.append(check_answer('13c', 'question 13 actual', text,
                              {'answers': r'5\.0', 'help_link': pemdas}, points=0.5))
    tests.append(check_answer('14a', 'question 14 expected datatype', text,
                              {'answers': r'(integer|float|string|error)', 'help_link': datatype}, points=0.5))
    tests.append(check_answer('14b', 'question 14 expected', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': expected}, points=0.5))
    tests.append(check_answer('14c', 'question 14 actual', text,
                              {'answers': r'0', 'help_link': math}, points=0.5))
    tests.append(check_answer('15a', 'question 15 expected datatype', text,
                              {'answers': r'(integer|float|string|error)', 'help_link': datatype}, points=0.5))
    tests.append(check_answer('15b', 'question 15 expected', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': expected}, points=0.5))
    tests.append(check_answer('15c', 'question 15 actual', text,
                              {'answers': r'8', 'help_link': math}, points=0.5))
    tests.append(check_answer('16a', 'question 16 expected datatype', text,
                              {'answers': r'(integer|float|string|error)', 'help_link': datatype}, points=0.5))
    tests.append(check_answer('16b', 'question 16 expected', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': expected}, points=0.5))
    tests.append(check_answer('16c', 'question 16 actual', text,
                              {'answers': r'21', 'help_link': pemdas}, points=0.5))
    tests.append(check_answer('17a', 'question 17 expected datatype', text,
                              {'answers': r'(integer|float|string|error)', 'help_link': datatype}, points=0.5))
    tests.append(check_answer('17b', 'question 17 expected', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': expected}, points=0.5))
    tests.append(check_answer('17c', 'question 17 actual', text,
                              {'answers': r'17', 'help_link': pemdas}, points=0.5))
    tests.append(check_answer('18a', 'question 18 expected datatype', text,
                              {'answers': r'(integer|float|string|error)', 'help_link': datatype}, points=0.5))
    tests.append(check_answer('18b', 'question 18 expected', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': expected}, points=0.5))
    tests.append(check_answer('18c', 'question 18 actual', text,
                              {'answers': r'ab123', 'help_link': cat}, points=0.5))
    tests.append(check_answer('19a', 'question 19 expected datatype', text,
                              {'answers': r'(integer|float|string|error)', 'help_link': datatype}, points=0.5))
    tests.append(check_answer('19b', 'question 19 expected', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': expected}, points=0.5))
    tests.append(check_answer('19c', 'question 19 actual', text,
                              {'answers': r'error', 'help_link': no_defined}, points=0.5))
    tests.append(check_answer('20a', 'question 20 expected datatype', text,
                              {'answers': r'(integer|float|string|error)', 'help_link': datatype}, points=0.5))
    tests.append(check_answer('20b', 'question 20 expected', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': expected}, points=0.5))
    tests.append(check_answer('20c', 'question 20 actual', text,
                              {'answers': r'abcd', 'help_link': cat}, points=0.5))
    tests.append(check_answer('21a', 'question 21 expected datatype', text,
                              {'answers': r'(integer|float|string|error)', 'help_link': datatype}, points=0.5))
    tests.append(check_answer('21b', 'question 21 expected', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': expected}, points=0.5))
    tests.append(check_answer('21c', 'question 21 actual', text,
                              {'answers': r'abcabc', 'help_link': math_and_strings}, points=0.5))
    tests.append(check_answer('22a', 'question 22 expected datatype', text,
                              {'answers': r'(integer|float|string|error)', 'help_link': datatype}, points=0.5))
    tests.append(check_answer('22b', 'question 22 expected', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': expected}, points=0.5))
    tests.append(check_answer('22c', 'question 22 actual', text,
                              {'answers': r'11222', 'help_link': math_and_strings}, points=0.5))
    tests.append(check_answer('23a', 'question 23 expected datatype', text,
                              {'answers': r'(integer|float|string|error)', 'help_link': datatype}, points=0.5))
    tests.append(check_answer('23b', 'question 23 expected', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': expected}, points=0.5))
    tests.append(check_answer('23c', 'question 23 actual', text,
                              {'answers': r'error', 'help_link': math_and_strings}, points=0.5))
    tests.append(check_answer('24a', 'question 24 expected datatype', text,
                              {'answers': r'(integer|float|string|error)', 'help_link': datatype}, points=0.5))
    tests.append(check_answer('24b', 'question 24 expected', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': expected}, points=0.5))
    tests.append(check_answer('24c', 'question 24 actual', text,
                              {'answers': r'error', 'help_link': more_math_strings}, points=0.5))
    tests.append(check_answer('25a', 'question 25 expected datatype', text,
                              {'answers': r'(integer|float|string|error)', 'help_link': datatype}, points=0.5))
    tests.append(check_answer('25b', 'question 25 expected', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': expected}, points=0.5))
    tests.append(check_answer('25c', 'question 25 actual', text,
                              {'answers': r'error', 'help_link': more_math_strings}, points=0.5))
    tests.append(check_answer('26a', 'question 26 expected datatype', text,
                              {'answers': r'(integer|float|string|error)', 'help_link': datatype}, points=0.5))
    tests.append(check_answer('26b', 'question 26 expected', text,
                              {'answers': r'[a-zA-Z0-9]+', 'help_link': expected}, points=0.5))
    tests.append(check_answer('26c', 'question 26 actual', text,
                              {'answers': r'error', 'help_link': more_math_strings}, points=0.5))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]