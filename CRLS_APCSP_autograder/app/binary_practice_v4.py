def docs_feedback_binary_practice_v4(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)
    test1a = exact_answer('question 1a', [r'1a .+? tabledata \s* 0011 .+ tabledata \s*? 3 [^a-z] '], text, points=2)
    test1b = exact_answer('question 1b', [r'1b .+? tabledata \s* 0100 .+ tabledata \s*?  4 [^a-z]'], text, points=2)
    test1c = exact_answer('question 1c', [r'1c .+? tabledata \s* 0101 .+ tabledata \s*? 5 [^a-z]'], text, points=2)
    test1d = exact_answer('question 1d', [r'1d .+? tabledata \s* 0110 .+ tabledata \s*? 6 [^a-z]'], text, points=2)
    test1e = exact_answer('question 1e', [r'1e .+? tabledata \s* 0111 .+ tabledata \s*?  7 [^a-z]'], text, points=2)
    test1f = exact_answer('question 1f', [r'1f .+? tabledata \s* 1000 .+ tabledata \s*?  8 [^a-z]'], text, points=2)
    test1g = exact_answer('question 1g', [r'1g .+? tabledata \s* 1001 .+ tabledata \s*?  9 [^a-z]'], text, points=2)
    test1h = exact_answer('question 1h', [r'1h .+? tabledata \s* 1010 .+ tabledata \s*?  10 [^a-z]'], text, points=2)
    test1i = exact_answer('question 1i', [r'1i .+? tabledata \s* 1011 .+ tabledata \s*?  11 [^a-z]'], text, points=2)
    test1j = exact_answer('question 1j', [r'1j .+? tabledata \s* 1100 .+ tabledata \s*?  12 [^a-z]'], text, points=2)
    test1k = exact_answer('question 1k', [r'1k .+? tabledata \s* 1101 .+ tabledata \s*?  13 [^a-z]'], text, points=2)
    test1l = exact_answer('question 1l', [r'1l .+? tabledata \s* 1110 .+ tabledata \s*?  14 [^a-z]'], text, points=2)
    test1m = exact_answer('question 1m', [r'1m .+? tabledata \s* 1111 .+ tabledata \s*?  15 [^a-z]'], text, points=2)
    test2a = exact_answer('question 2a', [r'2a. .+? tabledata \s* 0000 \s 0100 .+ tabledata \s* 4'], text, points=2)
    test2b = exact_answer('question 2b', [r'2b. .+? tabledata \s* 0000 \s 1000 .+ tabledata \s* 8'], text, points=2)
    test2c = exact_answer('question 2c', [r'2c. .+? tabledata \s* 0001 \s 0000 .+ tabledata \s* 16'], text, points=2)
    test2d = exact_answer('question 2d', [r'2d. .+? tabledata \s* 0010 \s 0000 .+ tabledata \s* 32'], text, points=2)
    test2e = exact_answer('question 2e', [r'2e. .+? tabledata \s* 0100 \s 0000 .+ tabledata \s* 64'], text, points=2)
    test2f = exact_answer('question 2f',
                          [r'2f. .+? tabledata \s* 1000 \s 0000 .+? tabledata \s* 128 .+? conversion \s practice'],
                          text, points=2)
    test3a = exact_answer('question 3a', [r'3a. .+? tabledata \s* 100 .+ tabledata \s* 4 .+? 3h'], text, points=2)
    test3b = exact_answer('question 3b', [r'3b. .+? tabledata \s* 111 .+ tabledata \s* 7 .+? 3i'], text, points=2)
    test3c = exact_answer('question 3c', [r'3c. .+? tabledata \s* 1101 .+ tabledata \s* 13 .+? 3j'], text, points=2)
    test3d = exact_answer('question 3d', [r'3d. .+? tabledata \s* 0011\s1111 .+ tabledata \s* 63 .+? 3k'],
                          text, points=2)
    test3e = exact_answer('question 3e', [r'3e. .+? tabledata \s* 0100 \s 0000 .+ tabledata \s* 64 '],
                          text, points=2)
    test3f = exact_answer('question 3f', [r'3f. .+? tabledata \s* 1010 \s 1010 .+ tabledata \s* 170'], text, points=2)
    test3g = exact_answer('question 3g', [r'3g. .+? tabledata \s* 1111 \s 1111 .+ tabledata \s* 255'], text, points=2)
    test3h = exact_answer('question 3h', [r'3h. .+? tabledata \s* 0*? 101 .+ tabledata \s* 5 .+? 3b'], text, points=2)
    test3i = exact_answer('question 3i', [r'3i. .+? tabledata \s* 0*? 1\s* 0001.+ tabledata \s* 17'], text, points=2)
    test3j = exact_answer('question 3j', [r'3j. .+? tabledata \s* 0*? 11\s*1111 .+ tabledata \s* 63'], text, points=2)
    test3k = exact_answer('question 3k', [r'3k. .+? tabledata \s* 0*? 100 \s* 0000 .+ tabledata \s* 64'], text, points=2)
    test3l = exact_answer('question 3l', [r'3l. .+? tabledata \s* 0*? 111 \s* 1111 .+ tabledata \s* 127'], text, points=2)
    test3m = exact_answer('question 3m', [r'3m. .+? tabledata \s* 0*? 1 \s* 0000 \s* 0000.+ tabledata \s* 256'],
                          text, points=2)
    test3n = exact_answer('question 3n', [r'3n. .+? tabledata \s* 0*? 10 \s* 0000 \s* 0010 .+ tabledata \s* 514'],
                          text, points=2)
    test4 = keyword_and_length('question 4', [r'[a-zA-Z]+'], text,
                               search_string=r'4. \s there .+? tabledata (.+) 5. .+? many', min_length=10, points=1)
    test5 = keyword_and_length('question 5', [r'[0-9]+'], text,
                               search_string=r'5. \s how .+? tabledata (.+) 6. .+? cartoon', min_length=7, points=1)
    test6 = keyword_and_length('question 6', [r'[0-9]+'], text,
                               search_string=r'6. \s most .+? tabledata (.+) .+? cartoon', min_length=7, points=1)
    tests.extend([test1a, test1b, test1c, test1d, test1e, test1f, test1g, test1h, test1i, test1j, test1k, test1l,
                  test1m, test2a, test2b, test2c, test2d, test2e, test2f, test3a, test3b, test3c, test3d, test3e,
                  test3f, test3g, test3h, test3i, test3j, test3k, test3l, test3m, test3n, test4, test5, test6])

    return tests
