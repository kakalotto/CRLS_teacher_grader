def route_docs_binary_practice_v5(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='CRLS AP CSP Scholar', score_max=78, score_manual=33)
    text = get_text(link)
    part1_link = 'https://docs.google.com/presentation/d/1YQRhCBrkp9AIzpL52NNXKeAPw_AYtekOhcRUt5B2pXI/' \
                 'edit#slide=id.g81feb4b5cd_0_0'
    part2_link = 'https://docs.google.com/presentation/d/1YQRhCBrkp9AIzpL52NNXKeAPw_AYtekOhcRUt5B2pXI/' \
                 'edit#slide=id.g81feb4b5cd_0_7'
    even_odd_link = 'https://docs.google.com/presentation/d/1YQRhCBrkp9AIzpL52NNXKeAPw' \
                    'AYtekOhcRUt5B2pXI/edit#slide=id.g81feb4b5d2_1_0'
    bits_link = 'https://docs.google.com/presentation/d/1YQRhCBrkp9AIzpL52NNXKeAPw_AYtekOhcRUt5B2pXI/' \
                'edit#slide=id.g81feb4b5cd_0_13'

    tests.append(check_answer('1a', '3', text, {'answers': '0011', 'help_link': part1_link}, points=2))
    tests.append(check_answer('1b', '4', text, {'answers': '0100', 'help_link': part1_link}, points=2))
    tests.append(check_answer('1c', '5', text, {'answers': '0101', 'help_link': part1_link}, points=2))
    tests.append(check_answer('1d', '6', text, {'answers': '0110', 'help_link': part1_link}, points=2))
    tests.append(check_answer('1e', '7', text, {'answers': '0111', 'help_link': part1_link}, points=2))
    tests.append(check_answer('1f', '8', text, {'answers': '1000', 'help_link': part1_link}, points=2))
    tests.append(check_answer('1g', '9', text, {'answers': '1001', 'help_link': part1_link}, points=2))
    tests.append(check_answer('1h', '10', text, {'answers': '1010', 'help_link': part1_link}, points=2))
    tests.append(check_answer('1i', '11', text, {'answers': '1011', 'help_link': part1_link}, points=2))
    tests.append(check_answer('1j', '12', text, {'answers': '1100', 'help_link': part1_link}, points=2))
    tests.append(check_answer('1k', '13', text, {'answers': '1101', 'help_link': part1_link}, points=2))
    tests.append(check_answer('1l', '14', text, {'answers': '1110', 'help_link': part1_link}, points=2))
    tests.append(check_answer('1m', '15', text, {'answers': '1111', 'help_link': part1_link}, points=2))
    tests.append(check_answer('2a', '0000 0100', text, {'answers': '4', 'help_link': part2_link}, points=2))
    tests.append(check_answer('2b', '0000 1000', text, {'answers': '8', 'help_link': part2_link}, points=2))
    tests.append(check_answer('2c', '0001 0000', text, {'answers': '16', 'help_link': part2_link}, points=2))
    tests.append(check_answer('2d', '0010 0000', text, {'answers': '32', 'help_link': part2_link}, points=2))
    tests.append(check_answer('2e', '0100 0000', text, {'answers': '64', 'help_link': part2_link}, points=2))
    tests.append(check_answer('2f', '1000 0000', text, {'answers': '128', 'help_link': part2_link}, points=2))
    tests.append(check_answer('3a', '100', text, {'answers': '4', 'help_link': part2_link}, points=2))
    tests.append(check_answer('3b', '111', text, {'answers': '7', 'help_link': part2_link}, points=2))
    tests.append(check_answer('3c', '1101', text, {'answers': '13', 'help_link': part2_link}, points=2))
    tests.append(check_answer('3d', '0001 1111', text, {'answers': '31', 'help_link': part2_link}, points=2))
    tests.append(check_answer('3e', '0100 0000', text, {'answers': '32', 'help_link': part2_link}, points=2))
    tests.append(check_answer('3f', '1010 1010', text, {'answers': '170', 'help_link': part2_link}, points=2))
    tests.append(check_answer('3g', '1111 1111', text, {'answers': '25', 'help_link': part2_link}, points=2))
    tests.append(check_answer('3h', '5', text, {'answers': '101', 'help_link': part1_link}, points=2))
    tests.append(check_answer('3i', '17', text, {'answers': r'1 \s* 0001', 'help_link': part1_link}, points=2))
    tests.append(check_answer('3j', '63', text, {'answers': r'11 \s* 1111', 'help_link': part1_link}, points=2))
    tests.append(check_answer('3k', '64', text, {'answers': r'100 \s* 0000', 'help_link': part1_link}, points=2))
    tests.append(check_answer('3l', '127', text, {'answers': r'111 \s* 1111', 'help_link': part1_link}, points=2))
    tests.append(check_answer('3m', '256', text, {'answers': r'1 \s* 0000 \s* 0000', 'help_link': part1_link},
                              points=2))
    tests.append(check_answer('3n', '513', text, {'answers': r'10 \s* 0000 \s* 0001',
                                                  'help_link': part1_link}, points=2))
    tests.append(check_answer('4a', 'How to tell if odd', text,
                              {'min_words': 10, 'help_link': even_odd_link}, points=1))
    tests.append(check_answer('5a', 'How many bits to count to 1000', text,
                              {'answers': '10', 'help_link': bits_link}, points=1))
    tests.append(check_answer('5b', 'Explain 5a', text,
                              {'min_words': 7, 'help_link': bits_link}, points=1))
    tests.append(check_answer('6a', 'Same or different', text,
                              {'answers': 'same', 'help_link': bits_link}, points=1))
    tests.append(check_answer('6b', 'Explain 6a', text, {'min_words': 5, 'help_link': bits_link}, points=1))
    tests.append(check_answer('7a', '2 bits enough for vowels?', text,
                              {'answers': 'no', 'help_link': bits_link}, points=1))
    tests.append(check_answer('7b', 'Explain 7a', text, {'min_words': 5, 'help_link': bits_link}, points=1))
    tests.append(check_answer('8a', 'add a 0, result?', text, {'answers': ['2', 'two'], 'help_link': part1_link},
                              points=5))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]