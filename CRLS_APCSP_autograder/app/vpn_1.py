def route_docs_vpn_1(link):
    from CRLS_APCSP_autograder.app.docs_labs.docs import get_text, check_answer
    from CRLS_APCSP_autograder.app.routes import initialize_scoring, sum_score
    [user, tests, score_info] = initialize_scoring(username='CRLS Scholar', score_max=54, score_manual=46)
    text = get_text(link)
    help_1 = 'https://docs.google.com/presentation/d/1w3pDVZSmVye2opN37hazg8Y47F3eP9izPubm_JkEqj4/' \
             'edit#slide=id.g25e4261d2d_0_6'
    help_1e = 'https://docs.google.com/presentation/d/1w3pDVZSmVye2opN37hazg8Y47F3eP9izPubm_JkEqj4/' \
              'edit#slide=id.g112518ebc7_0_17'
    help_1f = 'https://docs.google.com/presentation/d/1w3pDVZSmVye2opN37hazg8Y47F3eP9izPubm_JkEqj4/' \
              'edit#slide=id.g25e4261d2d_0_6'
    help_2a = 'https://what-is-what.com/what_is/protocol.html'
    help_2b = 'https://duckduckgo.com/?q=l2tp+ports&ia=web'
    help_2k = 'https://duckduckgo.com/?q=open+vpn+ports&ia=web'
    help_3a = 'https://duckduckgo.com/?q=drawbacks+of+free+vpns&ia=web'
    help_3b = 'https://duckduckgo.com/?q=how+to+pick+a+vpn&ia=web'
    tests.append(check_answer('1a', 'CRLS to VPN?', text, {'answers': 'encrypted', 'help_link': help_1}, points=5))
    tests.append(check_answer('1b', 'VPN to youtube', text, {'answers': 'unencrypted', 'help_link': help_1}, points=5))
    tests.append(check_answer('1c', 'Youtube to VPN', text, {'answers': 'unencrypted', 'help_link': help_1}, points=5))
    tests.append(check_answer('1d', 'VPN to CRLS', text, {'answers': 'encrypted', 'help_link': help_1}, points=5))
    tests.append(check_answer('1e', 'How VPN like proxy', text, {'min_words': 10, 'help_link': help_1e}, points=1))
    tests.append(check_answer('1f', 'How VPN unlike proxy', text, {'min_words': 10, 'help_link': help_1f}, points=1))
    tests.append(check_answer('1g', 'Download stuff while connected to VPN', text,
                              {'min_words': 10, 'help_link': help_1f}, points=1))
    tests.append(check_answer('2a', 'What is protocol', text,
                              {'answers': '(standard|rule)', 'help_link': help_2a}, points=5))
    tests.append(check_answer('2b', 'L2TP-IPSEC port 1', text, {'answers': '500', 'help_link': help_2b}, points=2))
    tests.append(check_answer('2c', 'L2TP-IPSEC UDP/TCP 1', text, {'answers': 'udp', 'help_link': help_2b}, points=2))
    tests.append(check_answer('2d', 'L2TP-IPSEC inbound/outbound 1', text,
                              {'answers': 'outbound', 'help_link': help_2b}, points=2))
    tests.append(check_answer('2e', 'L2TP-IPSEC port 2', text, {'answers': '1701', 'help_link': help_2b}, points=2))
    tests.append(check_answer('2f', 'L2TP-IPSEC UDP/TCP 2', text, {'answers': 'udp', 'help_link': help_2b}, points=2))
    tests.append(check_answer('2g', 'L2TP-IPSEC inbound/outbound 2', text,
                              {'answers': 'outbound', 'help_link': help_2b}, points=2))
    tests.append(check_answer('2h', 'L2TP-IPSEC port 3', text, {'answers': '4500', 'help_link': help_2b}, points=2))
    tests.append(check_answer('2i', 'L2TP-IPSEC UDP/TCP 3', text, {'answers': 'udp', 'help_link': help_2b}, points=2))
    tests.append(check_answer('2j', 'L2TP-IPSEC inbound/outbound 3', text,
                              {'answers': 'outbound', 'help_link': help_2b}, points=2))
    tests.append(check_answer('2k', 'OpenVPN port 1', text, {'answers': '1194', 'help_link': help_2k}, points=2))
    tests.append(check_answer('2l', 'OpenVPN UDP/TCP 1', text, {'answers': 'tcp', 'help_link': help_2k}, points=2))
    tests.append(check_answer('2m', 'OpenVPN inbound/outbound 1', text,
                              {'answers': 'outbound', 'help_link': help_2k}, points=2))
    tests.append(check_answer('3a', 'Drawbacks of free VPNs', text, {'min_words': 100, 'help_link': help_3a}, points=1))
    tests.append(check_answer('3b', 'Pick a free VPN', text, {'min_words': 100, 'help_link': help_3b}, points=1))
    score_info = sum_score(tests, score_info)
    return [user, tests, score_info]
