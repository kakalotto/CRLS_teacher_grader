def docs_feedback_hardware_cpus(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)

    test1a = keyword_and_length('1a. Computer core?', [r'process', r'comput', r'calcul', r'brain'], text,
                                search_string=r'1a. .+? tabledata (.+) 1b.', min_length=7, points=1)
    test1b = keyword_and_length('1b. CPU cache?', [r'memory'], text,
                                search_string=r'1b. .+? tabledata (.+) 1c.', min_length=7, points=1)
    test1c = keyword_and_length('1c. Why cache good?', [r'perform', r'speed', r'process'], text,
                                 search_string=r'1c. .+? tabledata (.+) buying', min_length=9, points=1)
    test2a = exact_answer('2a. model of computer?', [r'2a\. .+? tabledata .*? ell .+? 2b',
                                                     r'2a\. .+? tabledata .*? [0-9] .+? 2b'], text, points=1, required=2)
    test2b = exact_answer('2b. model of chip?', [r'2b\. .+? tabledata .*? (amd|intel) .+? 2c',
                                                 r'2b\. .+? tabledata .*? [0-9] .+? 2c'], text, points=1, required=2)
    test2c = exact_answer('2b. Cache L1, L2, L3?', [r'2c\. .+? tabledata .*? L1 .+? through',
                                                    r'2c\. .+? tabledata .*? L2 .+? through',
                                                    r'2c\. .+? tabledata .*? L3 .+? through',
                                                    r'2c\. .+? tabledata .*? M .+? through',
                                                    r'2c\. .+? tabledata .*? K .+? through',],
                          text, points=1, required=5)
    test3a = exact_answer('3a. Type of CPU', [r'3a\. .+? tabledata .*? (intel|amd) .*?  3b\.',
                                              r'3a\. .+? tabledata .*?  i7 .*?  3b\.', ], text, points=8, required=2)
    test3b = exact_answer('3b. How many cores?', [r'3b\. .+? tabledata .*? 4 .*? installation',
                                                 ], text, points=7)
    test4a = keyword_and_length('4a. Heat sink?', [r'[a-zA-Z]'], text,
                                search_string=r'4a. .+? tabledata (.+) emove', min_length=10, points=1)
  
    tests.extend([test1a, test1b, test1c, test2a, test2b, test2c, test3a, test3b, test4a ])
    return tests


