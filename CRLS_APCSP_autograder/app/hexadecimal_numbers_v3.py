def docs_feedback_hexadecimal_numbers_v3(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)
    test1a = exact_answer('1a. A', [r'1a\. .+? tabledata \s* 1010 \s* tabledata \s 2a\.'], text, points=3)
    test2a = exact_answer('2a. 2E', [r'2a\. .+? tabledata \s* 0* 10 \s* 1110 \s* tabledata \s 3a\.'], text, points=3)
    test3a = exact_answer('3a. D6', [r'3a\. .+? tabledata \s* 1101 \s* 0110 \s* tabledata \s 4a\.'], text, points=3)
    test4a = exact_answer('4a. DD1', [r'4a\. .+? tabledata \s* 1101 \s* 1101 \s* 0001 \s* tabledata \s 5a\.'], text,
                          points=3)
    test5a = exact_answer('5a. DEF9', [r'5a\. .+? tabledata \s* 1101 \s* 1110 \s* 1111 \s* 1001 \s* .+? exam'],
                          text, points=3)
    test6a = exact_answer('6a. 0100', [r'6a\. .+? tabledata \s* 4 \s* .+? 7a\.'], text, points=3)
    test7a = exact_answer('7a. 1111', [r'7a\. .+? tabledata \s* f \s* .+? 8a\.'], text, points=3)
    test8a = exact_answer('8a. 0111 1001', [r'8a\. .+? tabledata \s* 7 \s* 9 \s* .+? 9a\.'], text, points=3)
    test9a = exact_answer('9a. 1110 0111', [r'9a\. .+? tabledata \s* e \s* 7 \s* .+? 10a\.'], text, points=3)
    test10a = exact_answer('10a. 010101011111', [r'10a\. .+? tabledata \s* 5 \s* 5 \s* f \s* .+? 11a\.'], text, points=3)
    test11a = exact_answer('11a. 101101111110', [r'11a\. .+? tabledata \s* b \s* 7 \s* e \s* .+? $'], text, points=3)
    tests.extend([test1a, test2a, test3a, test4a, test5a, test6a, test7a, test8a, test9a, test10a, test11a, ])
    return tests