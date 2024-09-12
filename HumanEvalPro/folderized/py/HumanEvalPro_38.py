def encode_cyclic(s: str) -> str:
    """
    Returns encoded string by cycling groups of three characters.
    """
    # split string to groups. Each of length 3.
    groups = [s[(3 * i):min((3 * i + 3), len(s))]
              for i in range((len(s) + 2) // 3)]
    # cycle elements in each group. Unless group has fewer elements than 3.
    groups = [(group[1:] + group[0]) if len(group)
              == 3 else group for group in groups]
    return "".join(groups)


def decode_cyclic(s: str) -> str:
    """
    Takes as input string encoded with encode_cyclic function. Returns decoded string.
    """
    return encode_cyclic(encode_cyclic(s))


def check(candidate):
    assert candidate("[Z*uqK1`_ZGX<: C*[8vFn)-SpO") == "*[ZKuq_1`XZG <:[C*F8v-n)OSp"
    assert candidate("bo(") == "(bo"
    assert candidate("fH:*B=]1a@A*W2C~7i95~!(.1") == ":fH=*Ba]1*@ACW2i~7~95.!(1"
    assert candidate("uWiFq6U+hJ|f") == "iuW6FqhU+fJ|"
    assert candidate("NT)OBVt; yxb") == ")NTVOB t;byx"
    assert candidate(":1jP") == "j:1P"
    assert candidate("d`u*@T8bg7=8Z~QX7`EA>") == "ud`T*@g8b87=QZ~`X7>EA"
    assert candidate("rv(^7ohNnS*C>d$<* ") == "(rvo^7nhNCS*$>d <*"
    assert candidate("V2)zogf4>Jd9") == ")V2gzo>f49Jd"
    assert candidate("|69swyOVH") == "9|6yswHOV"
    assert candidate("oc2I,P]l") == "2ocPI,]l"
    assert candidate("pnSWY:07_,u") == "Spn:WY_07,u"
    assert candidate("O|g^qkMB~D") == "gO|k^q~MBD"
    assert candidate("P~xcK") == "xP~cK"
    assert candidate("Xb<oGVq=AQqsc0dEo(V@w~FXtly>o9hn<jk1Wxd") == "<XbVoGAq=sQqdc0(EowV@X~Fytl9>o<hn1jkdWx"
    assert candidate("Oc@oSpm") == "@OcpoSm"
    assert candidate("~Mf;!6M^7<7TG") == "f~M6;!7M^T<7G"
    assert candidate("ldAx1Z^(AMz~ ") == "AldZx1A^(~Mz "
    assert candidate(":^q~NRU2mRxj_") == "q:^R~NmU2jRx_"
    assert candidate("T=7y07<Iy+r[E5]~*|rQ6:!FE@-EKa") == "7T=7y0y<I[+r]E5|~*6rQF:!-E@aEK"
    assert candidate(".gbdd_xDi!ROrzB;;~Xl") == "b.g_ddixDO!RBrz~;;Xl"
    assert candidate("N*oVXtMyR2sGppvf)b") == "oN*tVXRMyG2svppbf)"
    assert candidate("su~J*lp>[uRvHx;[pTj^epUU") == "~sulJ*[p>vuR;HxT[pej^UpU"
    assert candidate("S[u.pIg[>[zOEux+Y`C1q,b~T6<2d5$@5:") == "uS[I.p>g[O[zxEu`+YqC1~,b<T652d5$@:"
    assert candidate("JxO0Ya]]v[aLFZUe:h<[n:[^,`p;") == "OJxa0Yv]]L[aUFZhe:n<[^:[p,`;"
    assert candidate("qU0ANNM1X8-G") == "0qUNANXM1G8-"
    assert candidate("x,QQX)6]rua_YP_v^WRo+kK") == "Qx,)QXr6]_ua_YPWv^+RokK"
    assert candidate("z32|5d(0S>`t2q^l9)CNI_<_T@sIhcRzdHc]-)y_ucE`> ") == "2z3d|5S(0t>`^2q)l9ICN__<sT@cIhdRz]Hcy-)c_u>E` "
    assert candidate("3|1`") == "13|`"
    assert candidate("KanO") == "nKaO"
    assert candidate("heimb") == "ihemb"
    assert candidate("qfibu cmxegegciwzmaduxiaa susovxwisdonq") == "iqf buxcmeegigcmwzuadaxisa ouswvxdisqon"
    assert candidate("szyvadbjbjleqrsqjbuvosx") == "yszdvabbjejlsqrbqjouvsx"
    assert candidate("jb cfrrcgcmonjxlobb") == " jbrcfgrcocmxnjblob"
    assert candidate("uocmtaeq mr") == "cuoamt eqmr"
    assert candidate("ghfljgobksxusanmpdvpperqvxtqp") == "fghgljkobusxnsadmppvpqertvxqp"
    assert candidate("bpmnxhlzzamiwqizipopetbech emteindvjbrhg") == "mbphnxzlziamiwqpzieopetb chtemneijdvhbrg"
    assert candidate("bdvic") == "vbdic"
    assert candidate("ibmjbcbcjnvcgvscoeg") == "mibcjbjbccnvsgvecog"
    assert candidate("gwxryttrhi tlwrjwyefcgxepsnmeyqtqhx") == "xgwtryhtrti rlwyjwcefegxnpsymeqqthx"
    assert candidate("nfymwszcxwcccwylyjytmqvqso pv") == "ynfsmwxzccwcycwjlymytqqv sopv"
    assert candidate("egaabytmvbz xiqa oqb") == "aegyabvtm bzqxioa qb"
    assert candidate("ewynhdnvljieuaxektqskltt") == "yewdnhlnvejixuatekkqstlt"
    assert candidate("ypfmupbdd ohq") == "fyppmudbdh oq"
    assert candidate("drpnajnrflgrnjugrjdsfdmraj") == "pdrjnafnrrlgunjjgrfdsrdmaj"
    assert candidate("gkjrwlxp") == "jgklrwxp"
    assert candidate("kj vugaum") == " kjgvumau"
    assert candidate("vwyqcwujjfticzoysigkjiumaunlpgw") == "yvwwqcjujiftocziysjgkmiunauglpw"
    assert candidate("mpynnkmiaqkaohvxoursrehm") == "ympknnamiaqkvohuxorrsmeh"
    assert candidate("q") == "q"
    assert candidate("bclmldsxgqriyoyrcyblszckpgxqaebiadxrlfuv") == "lbcdmlgsxiqryyoyrcsblkzcxpgeqaabirdxulfv"
    assert candidate("cidsbuzjnkxuanzyspgn kparqbwzztupn") == "dciusbnzjukxzanpys gnakpbrqzwzptun"
    assert candidate("zlxlbzvo qnrzfqvgbngyc") == "xzlzlb vorqnqzfbvgyngc"
    assert candidate("el  mbxlqnuo rudrwcokb") == " elb mqxlonuu rwdrkcob"
    assert candidate("q deettwgkpsidjcbgralsikjddre") == "dq teegtwskpjidgcblraksidjdre"
    assert candidate("gbelmhvyzqzu  rpdkvdpxfidfgtnreuubyvt ") == "egbhlmzvyuqzr  kpdpvdixfgdfrtnueuvbyt "
    assert candidate(" isreqtkqgkobbimiqzmjfksiyehmn ") == "s iqreqtkogkibbqmijzmsfkeiynhm "
    assert candidate("g ") == "g "
    assert candidate("xpvkaf n jbcw afoxnboajbzuyvfdqpnqbdpvzuq") == "vxpfka  ncjbaw xfoonbbajyzudvfnqpdqbzpvuq"
    assert candidate("pfhfvsozndyo kuzepqgu rpmbkanytmsgpgrg") == "hpfsfvnozodyu kpzeuqgp rkmbyanstmggprg"
    assert candidate("ZDRSYXOBOMALUN ZCYYYPKIR") == "RZDXSYOOBLMA UNYZCPYYRKI"
    assert candidate("WLSINWMWFPTSXKRJWPCDZ") == "SWLWINFMWSPTRXKPJWZCD"
    assert candidate("SSJDBFCDUULCSGVJIMZBGLNEPBRZHBKBFDWEULXIWD") == "JSSFDBUCDCULVSGMJIGZBELNRPBBZHFKBEDWXULDIW"
    assert candidate("QVPMXE") == "PQVEMX"
    assert candidate("BH") == "BH"
    assert candidate("TUAJJVWVY") == "ATUVJJYWV"
    assert candidate("JNWFXLB KBQRXC") == "WJNLFXKB RBQXC"
    assert candidate("ENLOEIFFFCILES YJ") == "LENIOEFFFLCI ESYJ"
    assert candidate("CVIMNEFHDPBIFANJWEGUMMY") == "ICVEMNDFHIPBNFAEJWMGUMY"
    assert candidate("WDGOWMPI IWLRCKH") == "GWDMOW PILIWKRCH"
    assert candidate("924323635 ") == "492332563 "
    assert candidate("2809062 2 019931337070552002679175") == "02869022 1 03993137705050207267915"
    assert candidate("147598611217926611") == "714859161721692161"
    assert candidate("42328620705549939952046639383020844702 259 6") == "342628720505949939052646339083820744 02925 6"
    assert candidate("69901834705129305412 9 5821110") == "969801734105329405 1259 182011"
    assert candidate("2637336882934846888329102 82881239355990421058") == "32637386832944886828309182 8283125939592045108"
    assert candidate("03369777707918") == "30376977790718"
    assert candidate("04 8519431409 34807 88 217 5382705320211408579") == " 0418539401439 04887 28  178530272531020147859"
    assert candidate("1418233943831768674 5935 746945 ") == "11438243933861778654 5934 74695 "
    assert candidate("864038267 44 72003") == "4868037264 42 7300"
    assert candidate(">,| |+!` ;]].|]!;$](*-)$=*_>+_ .)") == "|>,+ | !`];]].|$!;*]($-)_=*_>+) ."
    assert candidate("^.|,[!-]<:).,)$>!):*~-") == "|^.!,[<-].:)$,))>!~:*-"
    assert candidate("@*:=:|~* )@>;,;@") == ":@*|=: ~*>)@;;,@"
    assert candidate(".!;;.$[:|)].!`;`$.@~~=;^*^(@[>:] ") == ";.!$;.|[:.)];!`.`$~@~^=;(*^>@[ :]"
    assert candidate(" =*~=:<;<*$|~") == "* =:~=<<;|*$~"
    assert candidate(">$>^`_| >;[>+[<:+^!]@@<^^~)") == ">>$_^`>| >;[<+[^:+@!]^@<)^~"
    assert candidate("@_,;:.^=[.. ~~)!`^ ]<.>-=`~_@``^|<]<`@") == ",@_.;:[^= ..)~~^!`< ]-.>~=``_@|`^<<]`@"
    assert candidate(",|(|:^]. (|+!_>:*`],=~$@_-)]]~ -!@|") == "(,|^|: ].+(|>!_`:*=],@~$)_-~]]! -@|"
    assert candidate("+:>@!]*<") == ">+:]@!*<"
    assert candidate(":_=~[|") == "=:_|~["
    assert candidate("rEeqCcUavwORTDTmFWOXddgBqkitxnfSkaDtIpChpAXDc") == "erEcqCvUaRwOTTDWmFdOXBdgiqkntxkfStaDCIpAhpcXD"
    assert candidate("flxoMdzfZxVA") == "xfldoMZzfAxV"
    assert candidate("mU yEnFJsifwJsmvcSOdTTAGxeKgObPl") == " mUnyEsFJwifmJsSvcTOdGTAKxebgOPl"
    assert candidate("tVheQQUNSyGakNQcLMSQcMpCzdO") == "htVQeQSUNayGQkNMcLcSQCMpOzd"
    assert candidate("uMquPzZWjr") == "quMzuPjZWr"
    assert candidate("bBltBTzOScecczYhih") == "lbBTtBSzOcceYczhhi"
    assert candidate("IEFoshrFqALZVMJmZNKCMXiQEsEfdTbEYVVlRhxvBEK") == "FIEhosqrFZALJVMNmZMKCQXiEEsTfdYbElVVxRhEvBK"
    assert candidate("NAE") == "ENA"
    assert candidate("yMlRjHu") == "lyMHRju"
    assert candidate("eGxkspuFOTCEPzUfYdJGvZvQqobCqm") == "xeGpksOuFETCUPzdfYvJGQZvbqomCq"
    assert candidate("") == ""


def test_check():
    check(decode_cyclic)