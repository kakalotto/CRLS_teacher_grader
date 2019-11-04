def docs_feedback_hardware_RAID(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()

    text = get_text(link)

    test1a = exact_answer('1a. RAID0 (include units)', [r'1a\. .+? tabledata .*? 10 \s* TB .*? 1b\.'], text, points=5)
    test1b = exact_answer('1b. RAID1 (include units)', [r'1b\. .+? tabledata .*? 1 \s* TB .*? 1c\.'], text, points=5)
    test1c = exact_answer('1c. RAID5 (include units)', [r'1c\. .+? tabledata .*? 9 \s* TB .*? 1d\.'], text, points=5)
    test1d = exact_answer('1d. RAID10 (include units)', [r'1d\. .+? tabledata .*? 5 \s* TB .*? 1e\.'], text, points=5)
    test1e = exact_answer('1e. RAID6 (include units)', [r'1e\. .+? tabledata .*? 8 \s* TB .*? 1f\.'], text, points=5)
    test1f = exact_answer('1f. RAID60 (include units)', [r'1f\. .+? tabledata .*? 6 \s* TB .*? understanding'], text, points=5)
    test2a = exact_answer('2a. checkoff', [r'2a\. .+? tabledata .*? [a-zA-Z] .*? hich'], text, points=1)
    test3a = exact_answer('3a. fast RAID?', [r'3a\. .+? tabledata .*? [^156]0 .*? 3b\.'], text, points=2, )
    test3b = keyword_and_length('3b. Why checkoff ?', [r'[a-zA-Z]+'], text,
                                search_string=r'3b. .+? tabledata (.+?) 3c\.', min_length=5, points=1)
    test3c = exact_answer('3c. safe RAID?', [r'3c\. .+? tabledata .*? 10 .*? 3d\.'],
                          text, points=2, )
    test3d = keyword_and_length('3d. Why checkoff ?', [r'[a-zA-Z]+'], text,
                                search_string=r'3d. .+? tabledata (.+?) 3e\.', min_length=5, points=1)
    test3e = exact_answer('3e. fast and safe RAID?', [r'3e\. .+? tabledata .*? 10 .*? 3f\.'], text, points=2, )
    test3f = keyword_and_length('3f. Why checkoff ?', [r'[a-zA-Z]+'], text,
                                search_string=r'3f. .+? tabledata (.+?) 3g\.', min_length=5, points=1)
    test3g = exact_answer('3g. large and safe RAID?', [r'3g\. .+? tabledata .*? 5[^0] .*? 3h\.',
                                                       r'3g\. .+? tabledata .*? 6[^0] .*? 3h\.'], text, points=2, )
    test3h = keyword_and_length('3h. Why checkoff ?', [r'[a-zA-Z]+'], text,
                                search_string=r'3h. .+? tabledata (.+?) 3i\.', min_length=5, points=1)
    test3i = exact_answer('3i. 48 drive RAID?', [r'3i\. .+? tabledata .*? 50 .*? 3j\.',
                                                 r'3i\. .+? tabledata .*? 60 .*? 3j\.'], text, points=2, )
    test3j = keyword_and_length('3j. Why checkoff ?', [r'[a-zA-Z]+'], text,
                                search_string=r'3j. .+? tabledata (.+?) hands', min_length=7, points=1)
    tests.extend(
        [test1a, test1b, test1c, test1d, test1e, test1f, test2a, test3a, test3b, test3c, test3d, test3e, test3f,
         test3g, test3h, test3i, test3j])

    return tests
