def route_docs_passwords_revisited(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score

    [user, tests, score_info] = initialize_scoring(username='IT2 Scholar', score_max=36, score_manual=27)
    text = get_text(link)

    help_offlineonline = 'https://docs.google.com/presentation/d/1HHVV0CnDuQGp524E1LWaMNQYF5GeaYjHXCw5-LkjLCA/' \
                         'edit#slide=id.g1d2fb27d6a_0_11'
    help_md5 = 'https://www.md5hashgenerator.com/'
    help_hash = 'https://docs.google.com/presentation/d/1HHVV0CnDuQGp524E1LWaMNQYF5GeaYjHXCw5-LkjLCA/' \
                'edit#slide=id.g1d2fb27d6a_0_21'
    help_hash_speeds = 'https://blog.codinghorror.com/speed-hashing/'
    tests.append(check_answer('1a', 'Offline vs. Online?', text,
                              {'min_words': 10, 'help_link': help_offlineonline}, points=1))
    tests.append(check_answer('1b', 'Offline defenses?', text,
                              {'answers': ['network', 'internet', 'lock', 'firewall'], 'min_matches': 2,
                               'help_link': help_offlineonline}, points=5))
    tests.append(check_answer('1c', 'Steal HD?', text,  {'answers': 'off', 'wrong_answers': ['on'], }, points=2))
    tests.append(check_answer('1d', 'howsecureismypassword', text,
                              {'answers': 'off', 'wrong_answers': ['on'], }, points=2))
    tests.append(check_answer('1e', 'Movie hacking', text, {'answers': 'on', 'wrong_answers': ['off'], }, points=2))
    tests.append(check_answer('1f', 'Guessing wifi', text,  {'answers': 'on', 'wrong_answers': ['off'], }, points=2))
    tests.append(check_answer('1g', 'Guessing wifi iphone', text, {'answers': 'on', 'wrong_answers': ['off'], },
                              points=2))
    tests.append(check_answer('2a', 'CRLSisthebest123$ md5 hash', text,
                              {'answers': 'fc272262d626a4b839472de0782c1604', 'help_link': help_md5}, points=5))
    tests.append(check_answer('2b', '3 more hashes', text,
                              {'min_words': 3, 'help_link': help_md5}, points=5))
    tests.append(check_answer('2c', 'How hashes alike and different', text,
                              {'min_words': 7, 'help_link': help_md5}, points=1))
    tests.append(check_answer('3a', 'What is hash?', text,
                              {'min_words': 5, 'help_link': help_hash}, points=1))
    tests.append(check_answer('3b', 'How are users authenticated?', text,
                              {'min_words': 10, 'help_link': help_hash}, points=1))
    tests.append(check_answer('3c', 'Why do I need a hash?', text, {'min_words': 5, 'help_link': help_hash}, points=1))
    tests.append(check_answer('4a', 'Speed rank?', text,
                              {'answers': r'wpa .*? des .*? sha .*? 512 .*?  sha .*? 256 .*? sha .*? 1 .*? m'
                                          r'd5 .*? ntlm',
                               'help_link': help_hash_speeds}, points=5))
    tests.append(check_answer('4b', 'Explain', text, {'min_words': 7, 'help_link': help_hash}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
