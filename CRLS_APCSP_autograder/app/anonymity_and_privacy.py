def route_docs_anonymity_and_privacy(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=27, score_manual=94)
    text = get_text(link)
    one_link = 'https://docs.google.com/presentation/d/1dqbJrVIupobNjG66aYA_5JQz67RlV-RY0F1huypw3j4/' \
               'edit#slide=id.g273aa89b73_0_0'
    two_link = 'https://docs.google.com/presentation/d/1dqbJrVIupobNjG66aYA_5JQz67RlV-RY0F1huypw3j4/' \
               'edit#slide=id.g27452ea861_0_6'
    three_link = 'https://docs.google.com/presentation/d/1dqbJrVIupobNjG66aYA_5JQz67RlV-RY0F1huypw3j4/' \
                 'edit#slide=id.g271bbcd014_0_0'
    tests.append(check_answer('1a', 'roll ppl online?', text,
                              {'answers': 'anonymity', 'help_link': one_link}, points=5))
    tests.append(check_answer('1b', 'Keep password secret', text,
                              {'answers': 'privacy', 'help_link': one_link}, points=5))
    tests.append(check_answer('1c', 'CC on the internet', text,
                              {'answers': 'privacy', 'help_link': one_link}, points=5))
    tests.append(check_answer('1d', 'MAC address forging', text,
                              {'answers': 'anonymity ', 'help_link': one_link}, points=5))
    tests.append(check_answer('2a', 'Google somebody?', text, {'min_words': 20}, points=1))
    tests.append(check_answer('2b', 'What to worry against doxxer?', text,
                              {'min_words': 10, 'help_link': two_link}, points=1))
    tests.append(check_answer('3a', 'Pros and cons, fake FB name?', text,
                              {'min_words': 7, 'help_link': three_link}, points=1))
    tests.append(check_answer('3b', 'What do you do?', text,
                              {'min_words': 7, 'help_link': three_link}, points=1))
    tests.append(check_answer('4a', 'Your settings?', text, {'min_words': 7}, points=1))
    tests.append(check_answer('4b', 'Recommended settings?', text, {'min_words': 7}, points=1))
    tests.append(check_answer('4c', 'Changes to settings?', text, {'min_words': 7}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]