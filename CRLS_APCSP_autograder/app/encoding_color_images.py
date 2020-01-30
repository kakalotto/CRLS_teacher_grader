def docs_feedback_encoding_color_images(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()

    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. Two other colors?', [r'1a\. .*? tabledata .*? \s* 011 \s* .*?  2a\.',
                                                    r'1a\. .*? tabledata .*? \s* 110 \s* .*?  2a\.'], text, points=5, required=2)
    test2a = exact_answer('2a. 4 other colors?', [r'2a\. .*? tabledata .*? [01][01][01][01][01][01] \s* [01][01][01][01][01][01] \s*'
                                                  '[01][01][01][01][01][01] \s* [01][01][01][01][01][01]  .*?  3a\.'], text, points=5)
    test3a = exact_answer('3a. Fill out 16 colors', [r'3a\. .+? tabledata \s* \d .+? questions'], text, points=1)
    test4a = exact_answer('4a. Arrange numbers', [r'4a\. .*? tabledata .*?  0000 \s* 0010 .*? \n  0000 \s* 0010 .*? \n'
                                                  r' .*? 0000 \s*0011 .*? \n .*?'
                                          '010 \s* 010 .*? \n .*? 101 \s* 010 .*?'], text, points=5)
    test4b = keyword_and_length('4b. Explain arrangement', [r'[a-z]+'], text,
                                search_string=r'4b\. .*? tabledata (.+?) 5a\.', min_length=7, points=1)
    test5a = exact_answer('5a. How many times more colors?', [r'5a\. .*? tabledata .*? 64 .*? 5b\.'], text, points=5)
    test5b = keyword_and_length('Explain 5a', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'5b\. .*? tabledata (.+?)  6a\.', min_length=3, points=1)
    test6a = keyword_and_length('6a. Change 6 bits/pixel to 12?', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'6a\. .*? tabledata (.+?)  7a\.', min_length=7, points=1)
    test7a = keyword_and_length('7a. Need a color more green than #79B', [r'[a-zA-Z0-9]+'], text,
                               search_string=r'7a\. .*? tabledata (.+?)  check \s your \s work', min_length=10, points=1)
    tests.extend([test1a, test2a, test3a, test4a, test4b, test5a, test5b, test6a, test7a])
    return tests

