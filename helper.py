import math

def isprime(x,lst):
    for i in lst:
        if (i > math.sqrt(x)) : break
        if (x % i == 0): return False
    return True

def mulist(lst):
    n = 1
    for i in lst:
        n *= i
    return n

def strnum () :
    return "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

def grid () :
    a=[]
    a.append([ 8, 2,22,97,38,15, 0,40, 0,75, 4, 5, 7,78,52,12,50,77,91, 8])
    a.append([49,49,99,40,17,81,18,57,60,87,17,40,98,43,69,48, 4,56,62, 0])
    a.append([81,49,31,73,55,79,14,29,93,71,40,67,53,88,30, 3,49,13,36,65])
    a.append([52,70,95,23, 4,60,11,42,69,24,68,56, 1,32,56,71,37, 2,36,91])
    a.append([22,31,16,71,51,67,63,89,41,92,36,54,22,40,40,28,66,33,13,80])
    a.append([24,47,32,60,99, 3,45, 2,44,75,33,53,78,36,84,20,35,17,12,50])
    a.append([32,98,81,28,64,23,67,10,26,38,40,67,59,54,70,66,18,38,64,70])
    a.append([67,26,20,68, 2,62,12,20,95,63,94,39,63, 8,40,91,66,49,94,21])
    a.append([24,55,58, 5,66,73,99,26,97,17,78,78,96,83,14,88,34,89,63,72])
    a.append([21,36,23, 9,75, 0,76,44,20,45,35,14, 0,61,33,97,34,31,33,95])
    a.append([78,17,53,28,22,75,31,67,15,94, 3,80, 4,62,16,14, 9,53,56,92])
    a.append([16,39, 5,42,96,35,31,47,55,58,88,24, 0,17,54,24,36,29,85,57])
    a.append([86,56, 0,48,35,71,89, 7, 5,44,44,37,44,60,21,58,51,54,17,58])
    a.append([19,80,81,68, 5,94,47,69,28,73,92,13,86,52,17,77, 4,89,55,40])
    a.append([ 4,52, 8,83,97,35,99,16, 7,97,57,32,16,26,26,79,33,27,98,66])
    a.append([88,36,68,87,57,62,20,72, 3,46,33,67,46,55,12,32,63,93,53,69])
    a.append([ 4,42,16,73,38,25,39,11,24,94,72,18, 8,46,29,32,40,62,76,36])
    a.append([20,69,36,41,72,30,23,88,34,62,99,69,82,67,59,85,74, 4,36,16])
    a.append([20,73,35,29,78,31,90, 1,74,31,49,71,48,86,81,16,23,57, 5,54])
    a.append([ 1,70,54,71,83,51,54,69,16,92,33,48,61,43,52, 1,89,19,67,48])

def num50 () :
    b=[]
    b.append(37107287533902102798797998220837590246510135740250)
    b.append(46376937677490009712648124896970078050417018260538)
    b.append(74324986199524741059474233309513058123726617309629)
    b.append(91942213363574161572522430563301811072406154908250)
    b.append(23067588207539346171171980310421047513778063246676)
    b.append(89261670696623633820136378418383684178734361726757)
    b.append(28112879812849979408065481931592621691275889832738)
    b.append(44274228917432520321923589422876796487670272189318)
    b.append(47451445736001306439091167216856844588711603153276)
    b.append(70386486105843025439939619828917593665686757934951)
    b.append(62176457141856560629502157223196586755079324193331)
    b.append(64906352462741904929101432445813822663347944758178)
    b.append(92575867718337217661963751590579239728245598838407)
    b.append(58203565325359399008402633568948830189458628227828)
    b.append(80181199384826282014278194139940567587151170094390)
    b.append(35398664372827112653829987240784473053190104293586)
    b.append(86515506006295864861532075273371959191420517255829)
    b.append(71693888707715466499115593487603532921714970056938)
    b.append(54370070576826684624621495650076471787294438377604)
    b.append(53282654108756828443191190634694037855217779295145)
    b.append(36123272525000296071075082563815656710885258350721)
    b.append(45876576172410976447339110607218265236877223636045)
    b.append(17423706905851860660448207621209813287860733969412)
    b.append(81142660418086830619328460811191061556940512689692)
    b.append(51934325451728388641918047049293215058642563049483)
    b.append(62467221648435076201727918039944693004732956340691)
    b.append(15732444386908125794514089057706229429197107928209)
    b.append(55037687525678773091862540744969844508330393682126)
    b.append(18336384825330154686196124348767681297534375946515)
    b.append(80386287592878490201521685554828717201219257766954)
    b.append(78182833757993103614740356856449095527097864797581)
    b.append(16726320100436897842553539920931837441497806860984)
    b.append(48403098129077791799088218795327364475675590848030)
    b.append(87086987551392711854517078544161852424320693150332)
    b.append(59959406895756536782107074926966537676326235447210)
    b.append(69793950679652694742597709739166693763042633987085)
    b.append(41052684708299085211399427365734116182760315001271)
    b.append(65378607361501080857009149939512557028198746004375)
    b.append(35829035317434717326932123578154982629742552737307)
    b.append(94953759765105305946966067683156574377167401875275)
    b.append(88902802571733229619176668713819931811048770190271)
    b.append(25267680276078003013678680992525463401061632866526)
    b.append(36270218540497705585629946580636237993140746255962)
    b.append(24074486908231174977792365466257246923322810917141)
    b.append(91430288197103288597806669760892938638285025333403)
    b.append(34413065578016127815921815005561868836468420090470)
    b.append(23053081172816430487623791969842487255036638784583)
    b.append(11487696932154902810424020138335124462181441773470)
    b.append(63783299490636259666498587618221225225512486764533)
    b.append(67720186971698544312419572409913959008952310058822)
    b.append(95548255300263520781532296796249481641953868218774)
    b.append(76085327132285723110424803456124867697064507995236)
    b.append(37774242535411291684276865538926205024910326572967)
    b.append(23701913275725675285653248258265463092207058596522)
    b.append(29798860272258331913126375147341994889534765745501)
    b.append(18495701454879288984856827726077713721403798879715)
    b.append(38298203783031473527721580348144513491373226651381)
    b.append(34829543829199918180278916522431027392251122869539)
    b.append(40957953066405232632538044100059654939159879593635)
    b.append(29746152185502371307642255121183693803580388584903)
    b.append(41698116222072977186158236678424689157993532961922)
    b.append(62467957194401269043877107275048102390895523597457)
    b.append(23189706772547915061505504953922979530901129967519)
    b.append(86188088225875314529584099251203829009407770775672)
    b.append(11306739708304724483816533873502340845647058077308)
    b.append(82959174767140363198008187129011875491310547126581)
    b.append(97623331044818386269515456334926366572897563400500)
    b.append(42846280183517070527831839425882145521227251250327)
    b.append(55121603546981200581762165212827652751691296897789)
    b.append(32238195734329339946437501907836945765883352399886)
    b.append(75506164965184775180738168837861091527357929701337)
    b.append(62177842752192623401942399639168044983993173312731)
    b.append(32924185707147349566916674687634660915035914677504)
    b.append(99518671430235219628894890102423325116913619626622)
    b.append(73267460800591547471830798392868535206946944540724)
    b.append(76841822524674417161514036427982273348055556214818)
    b.append(97142617910342598647204516893989422179826088076852)
    b.append(87783646182799346313767754307809363333018982642090)
    b.append(10848802521674670883215120185883543223812876952786)
    b.append(71329612474782464538636993009049310363619763878039)
    b.append(62184073572399794223406235393808339651327408011116)
    b.append(66627891981488087797941876876144230030984490851411)
    b.append(60661826293682836764744779239180335110989069790714)
    b.append(85786944089552990653640447425576083659976645795096)
    b.append(66024396409905389607120198219976047599490197230297)
    b.append(64913982680032973156037120041377903785566085089252)
    b.append(16730939319872750275468906903707539413042652315011)
    b.append(94809377245048795150954100921645863754710598436791)
    b.append(78639167021187492431995700641917969777599028300699)
    b.append(15368713711936614952811305876380278410754449733078)
    b.append(40789923115535562561142322423255033685442488917353)
    b.append(44889911501440648020369068063960672322193204149535)
    b.append(41503128880339536053299340368006977710650566631954)
    b.append(81234880673210146739058568557934581403627822703280)
    b.append(82616570773948327592232845941706525094512325230608)
    b.append(22918802058777319719839450180888072429661980811197)
    b.append(77158542502016545090413245809786882778948721859617)
    b.append(72107838435069186155435662884062257473692284509516)
    b.append(20849603980134001723930671666823555245252804609722)
    b.append(53503534226472524250874054075591789781264330331690)
    return b

def sumdigits (num) :
    result = 0
    while (num>0):
        result += num%10
        num /= 10
    return result

def triangle () :
    c=[]
    c.append([75])
    c.append([95,64])
    c.append([17,47,82])
    c.append([18,35,87,10])
    c.append([20, 4,82,47,65])
    c.append([19, 1,23,75, 3,34])
    c.append([88, 2,77,73, 7,63,67])
    c.append([99,65, 4,28, 6,16,70,92])
    c.append([41,41,26,56,83,40,80,70,33])
    c.append([41,48,72,33,47,32,37,16,94,29])
    c.append([53,71,44,65,25,43,91,52,97,51,14])
    c.append([70,11,33,28,77,73,17,78,39,68,17,57])
    c.append([91,71,52,38,17,14,91,43,58,50,27,29,48])
    c.append([63,66, 4,68,89,53,67,30,73,16,69,87,40,31])
    c.append([ 4,62,98,27,23, 9,70,98,73,93,38,53,60, 4,23])
    return c

def days_in (m,y) :
    if (m==2):
        if (y%4==0 and y%100!=0 or y%400==0): return 29
        else: return 28
    elif (m==4 or m==6 or m==9 or m==11): return 30
    else: return 31

def isqrt (n) :
    x = n
    y = (x + n / x) / 2
    while y < x:
        x = y
        y = (x + n / x) / 2
    return x

def sum_divisors (n) :
    sum = 1
    for i in range (2,isqrt(n)+1) :
        if (n % i == 0) : sum += i + n/i
    return sum

def alphaval (s) :
    sum = 0
    for i in s : sum += ord(i)-64
    return sum