def docs_feedback_python_1030(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)

    test1a = exact_answer('question 1a expected',
                         [r'\s1a\. \n+ tabledata \s* [a-zA-Z\.0-9] .+? tabledata \s 1b\.\n'],
                         text, points=0.5)
    test2a = exact_answer('question 2a expected',
                         [r'\s2a\. \n+ tabledata \s* [a-zA-Z\.0-9] .+? tabledata \s 2b\.\n'],
                         text, points=0.5)
    test3a = exact_answer('question 3a expected',
                         [r'\s3a\. \n+ tabledata \s* [a-zA-Z\.0-9] .+? tabledata \s 3b\.\n'],
                         text, points=0.5)
    test4a = exact_answer('question 4a expected',
                         [r'\s4a\. \n+ tabledata \s* [a-zA-Z\.0-9] .+? tabledata \s 4b\.\n'],
                         text, points=0.5)
    test5a = exact_answer('question 5a expected',
                         [r'\s5a\. \n+ tabledata \s* [a-zA-Z\.0-9] .+? tabledata \s 5b\.\n'],
                         text, points=0.5)
    test1b = exact_answer('question 1b actual', [r'\s1b\. \n+ tabledata \s  1 .+? tabledata \s 1c\.\n'],
                          text, points=0.5)
    test2b = exact_answer('question 2b actual', [r'\s2b\. \n+ tabledata \s  1 .+? tabledata \s 2c\.\n'],
                          text, points=0.5)
    test3b = exact_answer('question 3b actual', [r'\s3b\. \n+ tabledata \s  3 .+? tabledata \s 3c\.\n'],
                          text, points=0.5)
    test4b = exact_answer('question 4b actual', [r'\s4b\. \n+ tabledata \s  12 .+? tabledata \s 4c\.\n'],
                          text, points=0.5)
    test5b = exact_answer('question 5b actual',
                          [r'\s5b\. \n+ tabledata \s  this \s is \s a \s sentence\. .+? tabledata \s 5c\.\n'],
                          text, points=0.5)
    test1c = exact_answer('question 1c different', [r'\s1c\. \n+ tabledata \s [a-zA-Z0-9\.] .+? tabledata \s 2a\.\n'],
                          text, points=0.5)
    test2c = exact_answer('question 2c different', [r'\s2c\. \n+ tabledata \s [a-zA-Z0-9\.] .+? tabledata \s 3a\.\n'],
                          text, points=0.5)
    test3c = exact_answer('question 3c different', [r'\s3c\. \n+ tabledata \s [a-zA-Z0-9\.] .+? tabledata \s 4a\.\n'],
                          text, points=0.5)
    test4c = exact_answer('question 4c different', [r'\s4c\. \n+ tabledata \s [a-zA-Z0-9\.] .+? tabledata \s 5a\.\n'],
                          text, points=0.5)
    test5c = exact_answer('question 5c different', [r'\s5c\. \n+ tabledata \s [a-zA-Z0-9\.] .+? part'],
                          text, points=0.5)
    test6a = exact_answer('question 6a', [r'\s6a\. .+? \n+ tabledata \s dogs \s are \s really \s cool .+? 6b\.'],
                          text, points=5)
    test7a = exact_answer('question 7a', [r'\s7a\. .+? \n+ tabledata \s error .+? 7b\.'],
                          text, points=5)
    test6b = keyword_and_length('question 6b', [r'[a-zA-Z]+'], text,
                                search_string=r'6b\. .+? tabledata (.+?) type', min_length=3, points=1)
    test7b = keyword_and_length('question 7b', [r'[a-zA-Z]+'], text,
                                search_string=r'7b\. .+? tabledata (.+?) [Ww]rite', min_length=5, points=1)
    test8a = exact_answer('question 8a', [r'8\. .+? tabledata .+? number \s* = \s* 100 .+? Create\sa\svariable'],
                          text, points=2.5)
    test8b = exact_answer('question 8b', [r'8\. .+? tabledata .+? print \s* \(number\) .+? Create\sa\svariable'],
                          text, points=2.5)
    test8c = exact_answer('question 8c', [r'8\. .+? tabledata .+? number2 .+? 100 .+? Create\sa\svariable'],
                          text, points=2.5)
    test8d = exact_answer('question 8d', [r'8\. .+? tabledata .+? print \s* \(number2\) .+? Create\sa\svariable'],
                          text, points=2.5)
    # test8a = keyword_and_length('question 8a', [r'number \s* = \s* 100'], text,
    #                             search_string=r'\s8\. .+? tabledata (.+?) Create\sa\svariable', min_length=5, points=2.5)
    # test8b = keyword_and_length('question 8b', [r'print \s* \(number\)'], text,
    #                             search_string=r'\s8\. .+? tabledata (.+?) Create\sa\svariable', min_length=5, points=2.5)
    # test8c = keyword_and_length('question 8c', [r'number2 .+? 100'], text,
    #                             search_string=r'\s8\. .+? tabledata (.+?) Create\sa\svariable', min_length=5, points=2.5)
    # test8d = keyword_and_length('question 8d', [r'print \s* \(number2\)'], text,
    #                             search_string=r'\s8\. .+? tabledata (.+?) Create\sa\svariable', min_length=5, points=2.5)


    tests.extend([test1a, test1b, test1c, test2a, test2b, test2c, test3a, test3b, test3c, test4a, test4b, test4c,
                  test5a, test5b, test5c, test6a, test6b, test7a, test7b, test8a, test8b, test8c, test8d])
    return tests