def route_python_2_032b(filename):
    from CRLS_APCSP_autograder.app.python_labs.find_items import find_if
    from CRLS_APCSP_autograder.app.python_labs.python_2_03x import python_2_032b
    from CRLS_APCSP_autograder.app.python_labs.python import filename_test, helps, pep8, read_file_contents
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=26.5, score_manual=11)
    test_filename = filename_test(filename, '2.032b')
    tests.append(test_filename)
    if test_filename['pass'] is False:
        return [user, tests, score_info]
    else:
        filename_data = read_file_contents(filename)
        no_ifs = 'https://docs.google.com/presentation/d/10zEU08zpSXwkTaMFIsUTLydJtZbP7tM869NRBIL0v1o/' \
                 'edit#slide=id.g8dcab24d0a_1_2'
        test_ifs = find_if(filename_data, 0, 5, minmax='max',
                           description='There should be zero ifs in the code.  See help link for details.',
                           help_link=no_ifs)
        tests.append(test_ifs)
        if test_ifs['name'] is False:
            return [user, tests, score_info]
        else:
            tests.append(python_2_032b(filename, filename_data))
            tests.append(pep8(filename, 7))
            tests.append(helps(filename, 2.5))
            score_info['finished_scoring'] = True
            score_info = sum_score(tests, score_info)
            return [user, tests, score_info]