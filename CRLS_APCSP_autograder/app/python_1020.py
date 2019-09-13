def docs_feedback_python_1020(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)

    test1a = exact_answer('question 1 expected', [r'\s1a\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 1b\.\n'],
                          text, points=0.5)
    test1b = exact_answer('question 1 actual', [r'\s1b\. \n+ tabledata \s 9 .+ tabledata \s 1c\.\n'],
                          text, points=0.5)
    test1c = exact_answer('question 1 difference',
                          [r'\s1c\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s print .+ 2a\.'],
                          text, points=0.5)
    test2a = exact_answer('question 2 expected', [r'\s2a\. \n+ tabledata \s [\.a-zA-Z0-9] .+ tabledata \s 2b\.\n'],
                          text, points=0.5)
    test2b = exact_answer('question 2 actual', [r'\s2b\. \n+ tabledata \s 0*\.6+ .+ tabledata \s 2c\.\n'],
                          text, points=0.5)
    test2c = exact_answer('question 2 difference',
                          [r'\s2c\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s print .+ 3a\.'],
                          text, points=0.5)
    test3a = exact_answer('question 3 expected', [r'\s3a\. \n+ tabledata \s [\.a-zA-Z0-9] .+ tabledata \s 3b\.\n'],
                          text, points=0.5)
    test3b = exact_answer('question 3 actual', [r'\s3b\. \n+ tabledata \s 3\.0 .+ tabledata \s 3c\.\n'],
                          text, points=0.5)
    test3c = exact_answer('question 3 difference',
                          [r'\s3c\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s print .+ 4a\.'],
                          text, points=0.5)
    test4a = exact_answer('question 4 expected', [r'\s4a\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 4b\.\n'],
                          text, points=0.5)
    test4b = exact_answer('question 4 actual', [r'\s4b\. \n+ tabledata \s 50 .+ tabledata \s 4c\.\n'],
                          text, points=0.5)
    test4c = exact_answer('question 4 difference',
                          [r'\s4c\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s print .+ 5a\.'],
                          text, points=0.5)
    test5a = exact_answer('question 5 expected', [r'\s5a\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 5b\.\n'],
                          text, points=0.5)
    test5b = exact_answer('question 5 actual', [r'\s5b\. \n+ tabledata \s 2\.0 .+ tabledata \s 5c\.\n'],
                          text, points=0.5)
    test5c = exact_answer('question 5 difference',
                          [r'\s5c\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s print .+ 6a\.'],
                          text, points=0.5)
    test6a = exact_answer('question 6 expected', [r'\s6a\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 6b\.\n'],
                          text, points=0.5)
    test6b = exact_answer('question 6 actual', [r'\s6b\. \n+ tabledata \s 1\.0 .+ tabledata \s 6c\.\n'],
                          text, points=0.5)
    test6c = exact_answer('question 6 difference',
                          [r'\s6c\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s print .+ section'],
                          text, points=0.5)
    test7a = exact_answer('question 7 expected', [r'\s7a\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 7b\.\n'],
                          text, points=0.5)
    test7b = exact_answer('question 7 actual', [r'\s7b\. \n+ tabledata \s error .+ tabledata \s 7c\.\n'],
                          text, points=0.5)
    test7c = exact_answer('question 7 difference',
                          [r'\s7c\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s print .+ 8a\.'],
                          text, points=0.5)
    test8a = exact_answer('question 8 expected', [r'\s8a\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 8b\.\n'],
                          text, points=0.5)
    test8b = exact_answer('question 8 actual', [r'\s8b\. \n+ tabledata \s a .+ tabledata \s 8c\.\n'],
                          text, points=0.5)
    test8c = exact_answer('question 8 difference',
                          [r'\s8c\. \n+ tabledata \s [a-zA-Z0-9] .+? section'],
                          text, points=0.5)
    test9a = exact_answer('question 9 expected', [r'\s9a\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 9b\.\n'],
                          text, points=0.5)
    test9b = exact_answer('question 9 actual', [r'\s9b\. \n+ tabledata \s a \s* \+ \s* b .+ tabledata \s 9c\.\n'],
                          text, points=0.5)
    test9c = exact_answer('question 9 difference',
                          [r'\s9c\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s print .+ 10a\.\n'],
                          text, points=0.5)
    test10a = exact_answer('question 10 expected', [r'\s10a\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 10b\.\n'],
                          text, points=0.5)
    test10b = exact_answer('question 10 actual', [r'\s10b\. \n+ tabledata \s ab .+ tabledata \s 10c\.\n'],
                          text, points=0.5)
    test10c = exact_answer('question 10 difference', [r'\s10c\. \n+ tabledata \s [a-zA-Z0-9] .+ section'],
                          text, points=0.5)
    test11a = exact_answer('question 11 expected', [r'\s11a\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 11b\.\n'],
                           text, points=0.5)
    test11b = exact_answer('question 11 actual', [r'\s11b\. \n+ tabledata \s error .+ tabledata \s 11c\.\n'],
                           text, points=0.5)
    test11c = exact_answer('question 11 difference',
                           [r'\s11c\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s print .+ 12a\.\n'],
                           text, points=0.5)
    test12a = exact_answer('question 12 expected', [r'\s12a\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 12b\.\n'],
                           text, points=0.5)
    test12b = exact_answer('question 12 actual', [r'\s12b\. \n+ tabledata \s aa .+ tabledata \s 12c\.\n'],
                           text, points=0.5)
    test12c = exact_answer('question 12 difference',
                           [r'\s12c\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s .+ part'],
                           text, points=0.5)
    test13a = exact_answer('question 13 expected datatype',
                           [r'\s13a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 13b\.\n'],
                           text, points=0.5)
    test14a = exact_answer('question 14 expected datatype',
                           [r'\s14a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 14b\.\n'],
                           text, points=0.5)
    test15a = exact_answer('question 15 expected datatype',
                           [r'\s15a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 15b\.\n'],
                           text, points=0.5)
    test16a = exact_answer('question 16 expected datatype',
                           [r'\s16a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 16b\.\n'],
                           text, points=0.5)
    test17a = exact_answer('question 17 expected datatype',
                           [r'\s17a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 17b\.\n'],
                           text, points=0.5)
    test18a = exact_answer('question 18 expected datatype',
                           [r'\s18a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 18b\.\n'],
                           text, points=0.5)
    test19a = exact_answer('question 19 expected datatype',
                           [r'\s19a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 19b\.\n'],
                           text, points=0.5)
    test20a = exact_answer('question 20 expected datatype',
                           [r'\s20a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 20b\.\n'],
                           text, points=0.5)
    test21a = exact_answer('question 21 expected datatype',
                           [r'\s21a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 21b\.\n'],
                           text, points=0.5)
    test22a = exact_answer('question 22 expected datatype',
                           [r'\s22a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 22b\.\n'],
                           text, points=0.5)
    test23a = exact_answer('question 23 expected datatype',
                           [r'\s23a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 23b\.\n'],
                           text, points=0.5)
    test24a = exact_answer('question 24 expected datatype',
                           [r'\s24a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 24b\.\n'],
                           text, points=0.5)
    test25a = exact_answer('question 25 expected datatype',
                           [r'\s25a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 25b\.\n'],
                           text, points=0.5)
    test26a = exact_answer('question 26 expected datatype',
                           [r'\s26a\. \n+ tabledata \s (integer|float|string|error) .+? tabledata \s 26b\.\n'],
                           text, points=0.5)
    test13b = exact_answer('question 13 expected', [r'\s13b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 13c\.\n'],
                           text, points=0.5)
    test14b = exact_answer('question 14 expected', [r'\s14b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 14c\.\n'],
                           text, points=0.5)
    test15b = exact_answer('question 15 expected', [r'\s15b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 15c\.\n'],
                           text, points=0.5)
    test16b = exact_answer('question 16 expected', [r'\s16b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 16c\.\n'],
                           text, points=0.5)
    test17b = exact_answer('question 17 expected', [r'\s17b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 17c\.\n'],
                           text, points=0.5)
    test18b = exact_answer('question 18 expected', [r'\s18b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 18c\.\n'],
                           text, points=0.5)
    test19b = exact_answer('question 19 expected', [r'\s19b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 19c\.\n'],
                           text, points=0.5)
    test20b = exact_answer('question 20 expected', [r'\s20b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 20c\.\n'],
                           text, points=0.5)
    test21b = exact_answer('question 21 expected', [r'\s21b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 21c\.\n'],
                           text, points=0.5)
    test22b = exact_answer('question 22 expected', [r'\s22b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 22c\.\n'],
                           text, points=0.5)
    test23b = exact_answer('question 23 expected', [r'\s23b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 23c\.\n'],
                           text, points=0.5)
    test24b = exact_answer('question 24 expected', [r'\s24b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 24c\.\n'],
                           text, points=0.5)
    test25b = exact_answer('question 25 expected', [r'\s25b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 25c\.\n'],
                           text, points=0.5)
    test26b = exact_answer('question 26 expected', [r'\s26b\. \n+ tabledata \s [a-zA-Z0-9] .+ tabledata \s 26c\.\n'],
                           text, points=0.5)
    test13c = exact_answer('question 13 actual',
                           [r'\s13c\. \n+ tabledata \s  5\.0 .+? tabledata \s 14a\.\n'],
                           text, points=0.5)
    test14c = exact_answer('question 14 actual',
                           [r'\s14c\. \n+ tabledata \s  0 .+? tabledata \s 15a\.\n'],
                           text, points=0.5)
    test15c = exact_answer('question 15 actual',
                           [r'\s15c\. \n+ tabledata \s  8 .+? tabledata \s 16a\.\n'],
                           text, points=0.5)
    test16c = exact_answer('question 16 actual',
                           [r'\s16c\. \n+ tabledata \s  21 .+? tabledata \s 17a\.\n'],
                           text, points=0.5)
    test17c = exact_answer('question 17 actual',
                           [r'\s17c\. \n+ tabledata \s  17 .+? tabledata \s 18a\.\n'],
                           text, points=0.5)
    test18c = exact_answer('question 18 actual',
                           [r'\s18c\. \n+ tabledata \s  ab123 .+? tabledata \s 19a\.\n'],
                           text, points=0.5)
    test19c = exact_answer('question 19 actual',
                           [r'\s19c\. \n+ tabledata \s  error .+? tabledata \s 20a\.\n'],
                           text, points=0.5)
    test20c = exact_answer('question 20 actual',
                           [r'\s20c\. \n+ tabledata \s  abcd .+? tabledata \s 21a\.\n'],
                           text, points=0.5)
    test21c = exact_answer('question 21 actual',
                           [r'\s21c\. \n+ tabledata \s  abcabc .+? tabledata \s 22a\.\n'],
                           text, points=0.5)
    test22c = exact_answer('question 22 actual',
                           [r'\s22c\. \n+ tabledata \s 11222 .+? tabledata \s 23a\.\n'],
                           text, points=0.5)
    test23c = exact_answer('question 23 actual',
                           [r'\s23c\. \n+ tabledata \s error .+? tabledata \s 24a\.\n'],
                           text, points=0.5)
    test24c = exact_answer('question 24 actual',
                           [r'\s24c\. \n+ tabledata \s error .+? tabledata \s 25a\.\n'],
                           text, points=0.5)
    test25c = exact_answer('question 25 actual',
                           [r'\s25c\. \n+ tabledata \s error .+? tabledata \s 26a\.\n'],
                           text, points=0.5)
    test26c = exact_answer('question 26 actual',
                           [r'\s26c\. \n+ tabledata \s error .+? $'],
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
