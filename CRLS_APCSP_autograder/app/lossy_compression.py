def docs_feedback_lossy_compression(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()
    text = get_text(link)


    test1a = keyword_and_length('1a what is happening', [r'[a-zA-Z]'], text,
                                search_string=r'\s1a\. .+? tabledata (.+) 2a\.', min_length=10, points=1)
    test2a = exact_answer('2a counts?', [r'\s2a\. .+? tabledata \s (y|yes) .+? 2b\.'], text, points=5)
    test2b = keyword_and_length('2b Why counts or not?', [r'[a-zA-Z]'], text,
                                search_string=r'\s2b\. .+? tabledata (.+) 3a', min_length=7, points=1)

    test3a = keyword_and_length('3a Lossy refers to?', [r'[a-zA-Z]'], text,
                                search_string=r'\s3a\. .+? tabledata (.+?) identify', min_length=10, points=1)
    test4a1 = exact_answer('4a-1', [r'\s4a-1\. .+? tabledata \s (audio|video|image) .+? 4b-1\.'], text, points=2)
    test4a2 = exact_answer('4a-2', [r'\s4a-2\. .+? tabledata \s (audio|video|image) .+? 4b-2\.'], text, points=2)
    test4a3 = exact_answer('4a-3', [r'\s4a-3\. .+? tabledata \s (audio|video|image) .+? 4b-3\.'], text, points=2)
    test4b1 = exact_answer('4b-1', [r'\s4b-1\. .+? tabledata \s [\.a-zA-Z] .+? 4c-1\.'], text, points=2)
    test4b2 = exact_answer('4b-2', [r'\s4b-2\. .+? tabledata \s [\.a-zA-Z] .+? 4c-2\.'], text, points=2)
    test4b3 = exact_answer('4b-3', [r'\s4b-3\. .+? tabledata \s [\.a-zA-Z] .+? 4c-3\.'], text, points=2)
    test4c1 = exact_answer('4c-1', [r'\s4c-1\. .+? tabledata \s (uncompressed|lossy|lossless) .+? 4a-2\.'], text, points=2)
    test4c2 = exact_answer('4c-2', [r'\s4c-2\. .+? tabledata \s (uncompressed|lossy|lossless) .+? 4a-3\.'], text, points=2)
    test4c3 = exact_answer('4c-3', [r'\s4c-3\. .+? tabledata \s (uncompressed|lossy|lossless) .+? $'], text, points=2)
    tests.extend([test1a, test2a, test2b, test3a, test4a1, test4b1, test4c1, test4a2, test4b2, test4c2, test4a3, test4b3,
                  test4c3, ])
    return tests
