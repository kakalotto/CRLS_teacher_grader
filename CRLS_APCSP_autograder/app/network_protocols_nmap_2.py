def docs_feedback_network_protocols_nmap(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, exact_answer, keyword_and_length

    tests = list()

    text = get_text(link)

    test1a = exact_answer('1a. SSH protocol', [r'1a\. .+? tabledata \s* tcp \s*  tabledata \s* 1b\.'], text, points=2)
    test1b = exact_answer('1b. SSH port', [r'1b\. .+? tabledata \s* 22\s*  tabledata .+? 2a'], text, points=2)
    test2a = exact_answer('2a. http protocol', [r'2a\. .+? tabledata \s* tcp \s*  tabledata \s* 2b\.'], text, points=2)
    test2b = exact_answer('2b. http port', [r'2b\. .+? tabledata \s* 80\s*  tabledata .+? 3a'], text, points=2)
    test3a = exact_answer('3a. https protocol', [r'3a\. .+? tabledata \s* tcp \s*  tabledata \s* 3b\.'], text, points=2)
    test3b = exact_answer('3b. https port', [r'3b\. .+? tabledata \s* 443 \s*  tabledata .+? 4a'], text, points=2)
    test4a = exact_answer('4a. ping protocol', [r'4a\. .+? tabledata \s* icmp \s*  tabledata \s* 4b\.'], text, points=2)
    test4b = exact_answer('4b. ping port', [r'4b\. .+? tabledata \s* none \s*  tabledata .+? 5a\.'], text, points=2)
    test5a = exact_answer('5a. DNS protocol', [r'5a\. .+? tabledata \s* (both\s*|tcp\/udp) \s*  tabledata \s* 5b\.'], text, points=2)
    test5b = exact_answer('5b. DNS port', [r'5b\. .+? tabledata \s* 53 \s*  tabledata .+? 6a\.'], text, points=2)
    test6a = exact_answer('6a. DHCP protocol', [r'6a\. .+? tabledata \s* udp\s*  tabledata \s* 6b\.'], text, points=2)
    test6b = exact_answer('6b. DHCP port', [r'6b\. .+? tabledata .+? 68 .+? tabledata .+? 7a\. ',
                                            r'6b\. .+? tabledata .+? 67 .+? tabledata .+? 7a\.'], text, points=2,
                          required=2)
    test7a = exact_answer('7a. remote desktop protocol',
                          [r'7a\. .+? tabledata \s* (both\s*|tcp\/udp) \s*  tabledata \s* 7b\.'], text, points=2)
    test7b = exact_answer('7b. remote desktop port', [r'7b\. .+? tabledata \s* 3389 \s*  tabledata \s* '], text,
                          points=2)
    test8a = exact_answer('8a. Screenshot Nmap is running',
                          [r'8a\. .+? tabledata \s* aaa \s* inlineobject .+?  scan \s an \s internal'], text, points=1)
    test9a = exact_answer('9a. CPSD scan',
                          [r'9a\. .+? tabledata .*? starting \s nmap .*? 9b\.',
                           r'9a\. .+? tabledata .*? host \s is \s up .*? 9b\.',
                           r'9a\. .+? tabledata .*? nmap \s done.*? 9b\.'], text, points=5, required=3)
    test9b = exact_answer('9b. CPSD scan, ports',
                          [r'9a\. .+? tabledata .*? [0-9]+.*? 9b\.',
                           ], text, points=5)
    test9c = exact_answer('9c. TCP/UDP?',
                          [r'9c\. .+? tabledata  .+? tcp .+? 9d\.'], text, points=1)
    test9d = keyword_and_length('9d. Describe services', [r'[a-zA-Z]+'], text,
                                search_string=r'9d\. .+? tabledata (.+)  to \s discover', min_length=10,
                                points=1)
    test10a = exact_answer('10a. OS detection scan of 1311a Windows computer',
                           [r'10a\. .+? tabledata .*? starting \s nmap .*? 10b\.',
                            r'10a\. .+? tabledata .*? host \s is \s up .*? 10b\.',
                            r'10a\. .+? tabledata .*? nmap \s done .*? 10b\.',
                            r'10a\. .+? tabledata .*? os \s detection .*? 10b\.',
                            r'10a\. .+? tabledata .*? cpe:/o:microsoft .*? 10b\.'
                            ], text, points=10, required=5)
    test10b = exact_answer('10b. OS detection scan of 1311b Mac computer',
                           [r'10b\. .+? tabledata .*? starting \s nmap .*? 11a\.',
                            r'10b\. .+? tabledata .*? host \s is \s up .*? 11a\.',
                            r'10b\. .+? tabledata .*? os \s detection .*? 11a\.',
                            r'10b\. .+? tabledata .*? no \s exact \s os \s matches .*? 11a\.',
                            r'10b\. .+? tabledata .*? apple .*? 11a\.'
                            ], text, points=10, required=4)
    test11a = exact_answer('11a. UDP scan of public DNS server',
                           [r'11a\. .+? tabledata .*? starting \s nmap .*? use \s nmap',
                            r'11a\. .+? tabledata .*? host \s is \s up .*? use \s nmap',
                            r'11a\. .+? tabledata .*? nmap \s done .*? use \s nmap',
                            r'11a\. .+? tabledata .*? 53/udp .*? use \s nmap'
                            ], text, points=10, required=4)
    test12a = exact_answer('12a. Public machine scan scan',
                          [r'12a\. .+? tabledata .*? starting \s nmap .*? 12b\.',
                           r'12a\. .+? tabledata .*? host \s is \s up .*? 12b\.',
                           r'12a\. .+? tabledata .*? nmap \s done.*? 12b\.'], text, points=5, required=3)
    test12b = keyword_and_length('12b. Public machine, ports, TCP/UDP, and what they do', [r'[0-9]+', r'(udp|tcp)',
                                                                                           r'[a-zA-Z]+'], text,
                                 search_string=r'12b\. .+? tabledata (.+) autograder', min_length=10, points=1,
                                 min_matches=3)

    tests.extend([test1a, test1b, test2a, test2b, test3a, test3b, test4a, test4b, test5a, test5b, test6a, test6b,
                  test7a, test7b, test8a, test9a, test9b, test9c, test9d, test10a, test10b, test11a, test12a, test12b])
    return tests

