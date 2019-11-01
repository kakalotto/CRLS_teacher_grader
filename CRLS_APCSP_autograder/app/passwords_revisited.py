
def docs_feedback_passwords_passwords_revisited(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length


    tests = list()
    text = get_text(link)

    print(text)
    test1a = keyword_and_length('1a. Offline vs. online? ?', [r'[a-zA-Z]+'], text,
                                search_string=r'1a. .+? tabledata (.+?) 1b\.', min_length=7, points=1)
    test1b = exact_answer('1b. offline slower why?', [r'1b\. .+? tabledata .*? network.*? 1c\.',
                                                      r'1b\. .+? tabledata .*? internet .*? 1c\.',
                                                      r'1b\. .+? tabledata .*? lock .*? 1c\.',
                                                      r'1b\. .+? tabledata .*? firewall .*? 1c\.'], text, points=5,
                          required=2)
    test1c = exact_answer('1c. Steal HD?', [r'1c\. .+? tabledata .*? offline .*? 1d\.'], text, points=1)
    test1d = keyword_and_length('1d. Why checkoff ?', [r'[a-zA-Z]+'], text,
                                search_string=r'1d\. .+? tabledata (.+?) 1e\.', min_length=5, points=1)
    test1e = exact_answer('1e. How secure is my pword?', [r'1e\. .+? tabledata .*? offline .*? 1f\.'], text, points=1)
    test1f = keyword_and_length('1f. Why checkoff ?', [r'[a-zA-Z]+'], text,
                                search_string=r'1f\. .+? tabledata (.+?) 1g\.', min_length=5, points=1)
    test1g = exact_answer('1g. movie scene?', [r'1g\. .+? tabledata .*? online .*? 1h\.'], text, points=1)
    test1h = keyword_and_length('1h. Why checkoff ?', [r'[a-zA-Z]+'], text,
                                search_string=r'1h\. .+? tabledata (.+?) demonstra', min_length=5, points=1)
    test2a = exact_answer('2a. paste MD5 hash', [r'2a\. .+? tabledata .{32,35} 2b\.'], text, points=3)
    test2b = exact_answer('2b. paste MD5 hash 3x', [r'2b\. .+? tabledata .{96,102} 2c\.'], text, points=2)
    test2c = keyword_and_length('2c. Why hashes in common?', [r'[a-zA-Z]+'], text,
                                search_string=r'2c\. .+? tabledata (.+?) questions', min_length=7, points=1)
    test3a = keyword_and_length('3a. What is hash and what it contains ?', [r'[a-zA-Z]+'], text,
                                search_string=r'3a\. .+? tabledata (.+?) 3b\.', min_length=7, points=1)
    test3b = keyword_and_length('3b. How users authenticated ?', [r'[a-zA-Z]+'], text,
                                search_string=r'3b\. .+? tabledata (.+?) 3c\.', min_length=10, points=1)
    test3c = keyword_and_length('3c. Why hash needed ?', [r'[a-zA-Z]+'], text,
                                search_string=r'3c\. .+? tabledata (.+?) 3d\.', min_length=7, points=1)
    test3d = exact_answer('3d. Speed ranking?', [r'3d\. .+? tabledata .*?  WPA .*?  SHA -* 256 .*?'
                                                 r' SHA -* 1 .*?'
                                                 r' MD5 .*?  NTLM .*? 3e\.'], text, points=5, )
    test3e = keyword_and_length('3e. Why ?', [r'[a-zA-Z]+'], text,
                                search_string=r'3e\. .+? tabledata (.+?) cracking', min_length=7, points=1)
    test4a = keyword_and_length('4a. Brute force cracking?', [r'[a-zA-Z]+'], text,
                                search_string=r'4a\. .+? tabledata (.+?) 4b\.', min_length=7, points=1)
    test4b = keyword_and_length('4b. Dictionary cracking?', [r'[a-zA-Z]+'], text,
                                search_string=r'4b\. .+? tabledata (.+?) 4c\.', min_length=7, points=1)
    test4c = keyword_and_length('4c. Precopmutation cracking?', [r'[a-zA-Z]+'], text,
                                search_string=r'4c\. .+? tabledata (.+?) 4d\.', min_length=7, points=1)
    test4d = keyword_and_length('4d. Why rainbow tables?', [r'[a-zA-Z]+'], text,
                                search_string=r'4d\. .+? tabledata (.+?) alts', min_length=7, points=1)
    test5a = keyword_and_length('5a. What is password salt?', [r'[a-zA-Z]+'], text,
                                search_string=r'5a\. .+? tabledata (.+?) 5b\.', min_length=7, points=1)
    test5b = keyword_and_length('5b. Salt vs Brute force?', [r'[a-zA-Z]+'], text,
                                search_string=r'5b\. .+? tabledata (.+?) 5c\.', min_length=7, points=1)
    test5c = keyword_and_length('5c. Salt vs precomputation?', [r'[a-zA-Z]+'], text,
                                search_string=r'5c\. .+? tabledata (.+?) kiddies', min_length=7, points=1)

    tests.extend(
        [test1a, test1b, test1c, test1d, test1e, test1f, test1g, test1h, test2a, test2b, test2c, test3a,
         test3b, test3c, test3d, test3e, test4a, test4b, test4c, test4d, test5a, test5b, test5c, ])

    return tests

