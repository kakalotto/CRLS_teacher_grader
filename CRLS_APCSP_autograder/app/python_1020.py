def docs_feedback_python_1020(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)

    test1a = exact_answer('question 1 expected', [r'1a\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s 1b\.'],
                          text, points=0.5)
    test1b = exact_answer('question 1 actual', [r'1b\. .*? tabledata \s 9 .*? tabledata \s 1c\.'],
                          text, points=0.5)
    test1c = exact_answer('question 1 difference',
                          [r'1c\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s print .*? 2a\.'],
                          text, points=0.5)
    test2a = exact_answer('question 2 expected', [r'2a\. .*? tabledata .*? [\.a-zA-Z0-9] .*? tabledata \s 2b\.'],
                          text, points=0.5)
    test2b = exact_answer('question 2 actual', [r'2b\. .*? tabledata .*? 0*\.6+ .*? tabledata \s 2c\.'],
                          text, points=0.5)
    test2c = exact_answer('question 2 difference',
                          [r'2c\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s print .*? 3a\.'],
                          text, points=0.5)
    test3a = exact_answer('question 3 expected', [r'3a\. .*? tabledata \s [\.a-zA-Z0-9] .*? tabledata \s 3b\.'],
                          text, points=0.5)
    test3b = exact_answer('question 3 actual', [r'3b\. .*? tabledata \s 3\.0 .*? tabledata \s 3c\.'],
                          text, points=0.5)
    test3c = exact_answer('question 3 difference',
                          [r'3c\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s print .*? 4a\.'],
                          text, points=0.5)
    test4a = exact_answer('question 4 expected', [r'4a\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s 4b\.'],
                          text, points=0.5)
    test4b = exact_answer('question 4 actual', [r'4b\. .*? tabledata \s 50 .*? tabledata \s 4c\.'],
                          text, points=0.5)
    test4c = exact_answer('question 4 difference',
                          [r'4c\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s print .*? 5a\.'],
                          text, points=0.5)
    test5a = exact_answer('question 5 expected', [r'5a\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s 5b\.'],
                          text, points=0.5)
    test5b = exact_answer('question 5 actual', [r'5b\. .*? tabledata \s 2\.0 .*? tabledata \s 5c\.'],
                          text, points=0.5)
    test5c = exact_answer('question 5 difference',
                          [r'5c\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s print .*? 6a\.'],
                          text, points=0.5)
    test6a = exact_answer('question 6 expected', [r'6a\. .*? tabledata .*? [a-zA-Z0-9] .*? tabledata \s 6b\.'],
                          text, points=0.5)
    test6b = exact_answer('question 6 actual', [r'6b\. .*? tabledata .*? 1\.0 .*? tabledata \s 6c\.'],
                          text, points=0.5)
    test6c = exact_answer('question 6 difference',
                          [r'6c\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s print .*? section'],
                          text, points=0.5)
    test7a = exact_answer('question 7 expected', [r'7a\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s 7b\.'],
                          text, points=0.5)
    test7b = exact_answer('question 7 actual', [r'7b\. .*? tabledata \s error .*? tabledata \s 7c\.'],
                          text, points=0.5)
    test7c = exact_answer('question 7 difference',
                          [r'7c\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s print .*? 8a\.'],
                          text, points=0.5)
    test8a = exact_answer('question 8 expected', [r'8a\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s 8b\.'],
                          text, points=0.5)
    test8b = exact_answer('question 8 actual', [r'8b\. .*? tabledata \s a .*? tabledata \s 8c\.'],
                          text, points=0.5)
    test8c = exact_answer('question 8 difference',
                          [r'8c\. .*? tabledata \s [a-zA-Z0-9] .*? section'],
                          text, points=0.5)
    test9a = exact_answer('question 9 expected', [r'9a\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s 9b\.'],
                          text, points=0.5)
    test9b = exact_answer('question 9 actual', [r'9b\. .*? tabledata \s a \s* \+ \s* b .*? tabledata \s 9c\.'],
                          text, points=0.5)
    test9c = exact_answer('question 9 difference',
                          [r'9c\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s print .*? 10a\.'],
                          text, points=0.5)
    test10a = exact_answer('question 10 expected', [r'10a\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s 10b\.'],
                          text, points=0.5)
    test10b = exact_answer('question 10 actual', [r'10b\. .*? tabledata \s ab .*? tabledata \s 10c\.'],
                          text, points=0.5)
    test10c = exact_answer('question 10 difference', [r'10c\. .*? tabledata \s [a-zA-Z0-9] .*? section'],
                          text, points=0.5)
    test11a = exact_answer('question 11 expected', [r'11a\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s 11b\.'],
                           text, points=0.5)
    test11b = exact_answer('question 11 actual', [r'11b\. .*? tabledata \s error .*? tabledata \s 11c\.'],
                           text, points=0.5)
    test11c = exact_answer('question 11 difference',
                           [r'11c\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s print .*? 12a\.'],
                           text, points=0.5)
    test12a = exact_answer('question 12 expected', [r'12a\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s 12b\.'],
                           text, points=0.5)
    test12b = exact_answer('question 12 actual', [r'12b\. .*? tabledata \s aa .*? tabledata \s 12c\.'],
                           text, points=0.5)
    test12c = exact_answer('question 12 difference',
                           [r'12c\. .*? tabledata \s [a-zA-Z0-9] .*? tabledata \s .*? part'],
                           text, points=0.5)
    test13a = exact_answer('question 13 expected datatype',
                           [r'13a\. .*? tabledata .*? (integer|float|string|error) .*? tabledata \s 13b\.'],
                           text, points=0.5)
    test14a = exact_answer('question 14 expected datatype',
                           [r'14a\. .*? tabledata .*? (integer|float|string|error) .*? tabledata \s 14b\.'],
                           text, points=0.5)
    test15a = exact_answer('question 15 expected datatype',
                           [r'15a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 15b\.'],
                           text, points=0.5)
    test16a = exact_answer('question 16 expected datatype',
                           [r'16a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 16b\.'],
                           text, points=0.5)
    test17a = exact_answer('question 17 expected datatype',
                           [r'17a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 17b\.'],
                           text, points=0.5)
    test18a = exact_answer('question 18 expected datatype',
                           [r'18a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 18b\.'],
                           text, points=0.5)
    test19a = exact_answer('question 19 expected datatype',
                           [r'19a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 19b\.'],
                           text, points=0.5)
    test20a = exact_answer('question 20 expected datatype',
                           [r'20a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 20b\.'],
                           text, points=0.5)
    test21a = exact_answer('question 21 expected datatype',
                           [r'21a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 21b\.'],
                           text, points=0.5)
    test22a = exact_answer('question 22 expected datatype',
                           [r'22a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 22b\.'],
                           text, points=0.5)
    test23a = exact_answer('question 23 expected datatype',
                           [r'23a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 23b\.'],
                           text, points=0.5)
    test24a = exact_answer('question 24 expected datatype',
                           [r'24a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 24b\.'],
                           text, points=0.5)
    test25a = exact_answer('question 25 expected datatype',
                           [r'25a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 25b\.'],
                           text, points=0.5)
    test26a = exact_answer('question 26 expected datatype',
                           [r'26a\. .*? tabledata \s (integer|float|string|error) .*? tabledata \s 26b\.'],
                           text, points=0.5)
    test13b = exact_answer('question 13 expected', [r'13b\. .*? tabledata .*? [a-zA-Z0-9] .+ tabledata \s 13c\.'],
                           text, points=0.5)
    test14b = exact_answer('question 14 expected', [r'14b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 14c\.'],
                           text, points=0.5)
    test15b = exact_answer('question 15 expected', [r'15b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 15c\.'],
                           text, points=0.5)
    test16b = exact_answer('question 16 expected', [r'16b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 16c\.'],
                           text, points=0.5)
    test17b = exact_answer('question 17 expected', [r'17b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 17c\.'],
                           text, points=0.5)
    test18b = exact_answer('question 18 expected', [r'18b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 18c\.'],
                           text, points=0.5)
    test19b = exact_answer('question 19 expected', [r'19b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 19c\.'],
                           text, points=0.5)
    test20b = exact_answer('question 20 expected', [r'20b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 20c\.'],
                           text, points=0.5)
    test21b = exact_answer('question 21 expected', [r'21b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 21c\.'],
                           text, points=0.5)
    test22b = exact_answer('question 22 expected', [r'22b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 22c\.'],
                           text, points=0.5)
    test23b = exact_answer('question 23 expected', [r'23b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 23c\.'],
                           text, points=0.5)
    test24b = exact_answer('question 24 expected', [r'24b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 24c\.'],
                           text, points=0.5)
    test25b = exact_answer('question 25 expected', [r'25b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 25c\.'],
                           text, points=0.5)
    test26b = exact_answer('question 26 expected', [r'26b\. .*? tabledata \s [a-zA-Z0-9] .+ tabledata \s 26c\.'],
                           text, points=0.5)
    test13c = exact_answer('question 13 actual',
                           [r'13c\. .*? tabledata .*?  5\.0 .*? tabledata \s 14a\.'],
                           text, points=0.5)
    test14c = exact_answer('question 14 actual',
                           [r'14c\. .*? tabledata \s  0 .*? tabledata \s 15a\.'],
                           text, points=0.5)
    test15c = exact_answer('question 15 actual',
                           [r'15c\. .*? tabledata \s  8 .*? tabledata \s 16a\.'],
                           text, points=0.5)
    test16c = exact_answer('question 16 actual',
                           [r'16c\. .*? tabledata \s  21 .*? tabledata \s 17a\.'],
                           text, points=0.5)
    test17c = exact_answer('question 17 actual',
                           [r'17c\. .*? tabledata \s  17 .*? tabledata \s 18a\.'],
                           text, points=0.5)
    test18c = exact_answer('question 18 actual',
                           [r'18c\. .*? tabledata \s  ab123 .*? tabledata \s 19a\.'],
                           text, points=0.5)
    test19c = exact_answer('question 19 actual',
                           [r'19c\. .*? tabledata .*?  error .*? tabledata \s 20a\.'],
                           text, points=0.5)
    test20c = exact_answer('question 20 actual',
                           [r'20c\. .*? tabledata \s  abcd .*? tabledata \s 21a\.'],
                           text, points=0.5)
    test21c = exact_answer('question 21 actual',
                           [r'21c\. .*? tabledata \s  abcabc .*? tabledata \s 22a\.'],
                           text, points=0.5)
    test22c = exact_answer('question 22 actual',
                           [r'22c\. .*? tabledata \s 11222 .*? tabledata \s 23a\.'],
                           text, points=0.5)
    test23c = exact_answer('question 23 actual',
                           [r'23c\. .*? tabledata \s error .*? tabledata \s 24a\.'],
                           text, points=0.5)
    test24c = exact_answer('question 24 actual',
                           [r'24c\. .*? tabledata \s error .*? tabledata \s 25a\.'],
                           text, points=0.5)
    test25c = exact_answer('question 25 actual',
                           [r'25c\. .*? tabledata \s error .*? tabledata \s 26a\.'],
                           text, points=0.5)
    test26c = exact_answer('question 26 actual',
                           [r'26c\. .*? tabledata \s error .*? $'],
                           text, points=0.5)

    tests.extend([test1a, test1b, test1c, test2a, test2b, test2c, test3a, test3b, test3c, test4a, test4b, test4c,
                  test5a, test5b, test5c, test6a, test6b, test6c, test7a, test7b, test7c, test8a, test8b, test8c,
                  test9a, test9b, test9c, test10a, test10b, test10c, test11a, test11b, test11c,
                  test12a, test12b, test12c, test13a, test13b, test13c, test14a, test14b, test14c, test15a, test15b,
                  test15c, test16a, test16b, test16c, test17a, test17b, test17c, test18a, test18b, test18c, test19a,
                  test19b, test19c, test20a, test20b, test20c, test21a, test21b, test21c, test22a, test22b, test22c,
                  test23a, test23b, test23c, test24a, test24b, test24c, test25a,
                  test25b, test25c, test26a, test26b, test26c, ])

    return tests
