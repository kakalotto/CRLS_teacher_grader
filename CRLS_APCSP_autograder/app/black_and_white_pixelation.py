def docs_feedback_black_and_white_pixelation(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)

    print(text)
    test1a = exact_answer('1a. Bits for A?', [r'1a\. .*? tabledata .*? 0 \s* 0 \s* 0 \s* 0 \s*     0\s* 0\s*1 \s* 1\s*  '
                                              '\s* 0 \s* 0\s*0\s*0  \s* 0\s*1 \s*0\s*1\s*  '
                                              '1\s*0\s*1 \s*'
                                              '0\s*1\s*0 \s*'
                                              '0\s*0\s*0\s*'
                                              '0\s*1\s*0 \s*'
                                              '0\s*1\s*0 .*? 2a\.'], text, points=20)
    test2a = exact_answer('2a. Screenshot of your image', [r'2a\. .*? tabledata .*? aaa \s* inlineobject .*? 2b\.'], text, points=1)
    test2b = exact_answer('2b. Bits of your image', [r'2b\. .*? tabledata .*? [0-9]+ .*? 3a\.'], text, points=5)
    test3a = exact_answer('3a. Maximum dimensions of this widget', [r'3a\. .*? tabledata .*? 255 .*? 255 .*? 3b\.'], text, points=5)
    test3b = keyword_and_length('3b. Explain 3a', [r'[a-z]+'], text,
                                search_string=r'3b\. .*? tabledata (.+?) 3c\.', min_length=7, points=1)
    test3c = exact_answer('3c. Total bits in largest image?', [r'3c\. .*? tabledata .*? 65 .*? 041 .*? 3d\.'], text, points=5)
    test3d = keyword_and_length('3d. Explain 3c', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'3d\. .*? tabledata (.+?) 3e\.', min_length=7, points=1)
    test3e = exact_answer('3e. Bits for smallest image', [r'3e\. .*? tabledata .*? (1(\s\n)|17) .*? 3f\.'], text, points=5)
    test3f = keyword_and_length('3f. Explain 3e.', [r'[a-zA-Z0-9]+'], text,
                                search_string=r'3f\. .*? tabledata (.+?) 4\. \s what', min_length=7, points=1)
    test4a = keyword_and_length('4a. What if we did not include width and height', [r'[a-z]+'], text,
                                search_string=r'4\. \s what  .*? tabledata (.+?) check \s your \s work', min_length=10, points=1)
    tests.extend([test1a, test2a, test2b, test3a, test3b, test3c, test3d, test3e, test3f, test4a])

    return tests
