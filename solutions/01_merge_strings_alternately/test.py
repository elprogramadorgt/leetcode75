import sys
import os

from solution import solution, solutionString   

#Must be declare before import run_performance_test
sys.path.insert(0, os.path.abspath(os.path.join(
    os.path.dirname(__file__), '../../', 'tests_ui')))

from test import test_performance

a = 'ymeilgzqsveeohzomvnntjrmygsyyfwuvmhpkxmzqwyobzoyskqowvajbrsnicnqueyypvwihmnlvbfvotdtaoaionkrzqnsjnhhcmidjdgfakfypcsryfhsnfzkljsbyxkhkpstldfphkqezwwgfqxsejvgikhwbumvpmiwiqmjgsppzxwjyfjtlukpjqiunqtxxupupycxnicapnbsbiiibpxjydkpmkpudyldcgvxvyqonrehrgkwvvdpdjihrtmzkzmwwyalockaihikjuujhkbgaprfqtigxusysoxfuyjjexyekirvxfydoiwdrpgbxjyzmmroihzwyjrfcjkraeoenxaibdceujmkakemzbkxbewheaalyiasrkzkkrntgiyotqdnybedasqixkzbdnjlohyevvkvezxifhwraymmukzelgvjmnisqffctooourmisvbuqrsybuvmuiqzwjcukfdklswaiybywjlvgamjwmjqqhgpcyhpusasuswewrwhkwuwhaanacdcfqpmerhfeadpunnieevhtzgrptepdsslmvvhfhybjludzjngcuxdnmmrfevpurfdlgswsqruegafywuzqcfhhpnculhqjtrmemdgfcnyvvybemzwawnwdnvdwwdoyklfxmfxslbisaysugeshgwemabivmivkdlserdiqifdoktfskdodqraimfqwxmbzywbhzoepndfahwyfscyirkytkeuuzkeohqclmivkshzyeepoxxqethwnnjmzghehitnpyjuynastybqaxbblijfojbwfqyitbnlqyncdcnnvbhrvdbuelomdizbzbqzubqtldfhcxxocxfsbjieiuzjesppnlrqsjuqjbtbtgoeksjrtzvxswlcqsyqotugyvrsmvanbcijhpxizockwsguldpicevitpmnvwqgqrpmeeasyofnzkwdnxqfyeehiqqxteylhgmlmovaeglfulyrisqxfpqeuuuvvfopvxlqfdvjcdqdoiwecdxvnrgzznyrjhsupgorqludtbzncpbqutljsigdygynjzeugolkafrytkgjtqhlcqpmtygiuvlneprptpchgtfijtgkxcgfausytdsnqkeheunoiwmggqvzfeyxdiastdklffshtvtddhrcbahukuqbqbqkcjweqcoivtyotgbrxjrejyaanzxidhnocairgdxzeygrginvqirfeevolmlcwbaemgnuxhikxjgwwuxruvjwyllvpqjnrabnypurrqfbjvphtpdaueiefoypuotffiozykeufvpxdqaijtmxtwswqrnhuraqjhjqcqygbhohyetatzuygwmgojxtvecjtcffrvytddreelotzbwmdtgkydygmhjzhdqtfcdjtfhsvuracqjroyhavgfzvovjauginytgxegwnhqribemfiyykluowhwxklyrkgpcgcrtfwxriskqtjuhlqfeooyfyorxedzfxvoieobsaiacjmuimpddkrgdsbktqxveesewobocephrbexjssblrdsrumidcbexskuvqlvaaqfuwfeozfpgzubrvgzhadkldpowcdxlychshmbjznblbessguelmlvnyqfzfggkunvsqttqggmlzgxtixgpintcyjqxdhjsdstoqtgwkunjrnhtvywrntndxcgqgazzlojgftmfclmbkmyzznnnijyzqxyyoibpmjyxfeksyfvklgildejqjxbbgowblejlzwslsjvokxhrrwgvlodmdlyusyxwgssishrlpjyskddlfianfxajajpaaydsiodlmwwtmhzxphwuytkrawtgftuthlwapxfisvgslqagtbgwsovxttjtnuzakpuxctutcdddgzbnjxxzipulohqxpzqqhxwuhdasjshqvcfuiwqdumdtwklyqehlsdbdwhafsnfihtxyxrvxrwvrsdugnzbbacgvskhjmjefvyiynieyrzqrrajaeydkbklmxfehkiveqzcjwejzdnwvwbiiypeacasxehdubhcepwcgtvnxqmqgxiqmgmvwroeafjvboyodlnhemdhtuaxnhcqmugllcpqmamxqdcobbielaxksxgkjluorlrscmhnstzrbhmkpwpcfwzuigluckxwwxvgxeurgphucohquzjatuoywuakvlkuoojqhiaunfycjxdpgnielokhihshhvjatzltfinvyqzziyhiabkxioyvjgweirztzmtmzcgzpwlggtirruecjgdkwacfsirdesmpbbjwjoqepnuuqianwmwbyfttdpvminzmgqqhukntcscoxfnuunblhewgdkmmqzqsmhzparmtjnuhtutbuieresguvfpllyuggcipwqfmzsocyllpdttnrhywpcjaawucbthzeruagykrpuawclrdrybjnuhccugkxnoljntszjnrilkplyxcbutzvxenymlbbmekbcmozbfspbbawvywpnitmqtzdwczzdzvyjfmacfxinfbaisphnnzgyzcdrdnqyvuhcwupyvyksmkecxmlsvmgwgocwewuuzkigoypahltrhcdvqekydleqynuoptwqcfchtzzrjndbykwyiywegnwbeikopwotyqowdgujqcadkxxtxkqhkiudxljzgdhqtnsiniamziwngoqstvpswahqbktodljwhdvrjfmrqdzpptdtbddzwbnqectymgbgtcpsysadphxjfxhgvqegqxjmmtnckkhbmkicsmdhzezdmekznyqnaipgqzrnfgmnwpujttylhnkrfnitsvjaaaqzrdjcdnwilmnkiywghqluuxbezgeiupclfzvlakxwoqfugyvcptlltkiezrmftksusihgmekuddbvhnydrxfbymrlxyhkxdmbcyfbizlnwfzwsauxdeuoobcvkqanydkerljztxvdrlsflcmmtysthnhhwftedupgbihrgtvbphexpitwpkwdqoqgjjsfttapgudlfcuomojlrtckcsgoyljeosquwnzqsmtgvrlnttsjaaqikvlfydzmaujxsbltciuxcvencsramujroedibbmalfraxwajaccfcwxflobhbqvrqtycnrcbnoczuoqxcxiaeohzizvvhpfmrrikuptdfanzpsgtnxdssqjqurihjdxbnisrtxpvhfpmfjvsruedfgugraftabanqwxglugrzugeiyvflswoaywspfrkersajuyfsnicuoftjftujpwpsmvqmepineryzdgsspwigagdevlkhlkpusjidaydrxrnjcoytodqrzmgkpvkanxfumlflatnjrtphyrleumictpiykvbxkknglxqxqhdeeniksfoolpalsggpmsvqkfmeogtaxuiwjiqwqijdtxufbzjsvtwnzjjhgunhzgdgjdpbomylaypnmljdohyejnurljtycotnndhpmjdywnbwiisxnesjcnfjtfiwkhtwncluztsmphwwwvvlgdhihaqikfyoavmejqzmszoszqiwvrhiskfdlxoaetiwybjbdtrjodzmciomezbmttcklmvjooctvbwztsibtkubrxrwsbksoxlpqtqftytzftdgojzfzgkkywierbxrdoqztaqgixpevgpfpmdrmwudxftgtdmprgzfnkqdzfmjdabjjjbyeukhdfejzsvmtdryfbuospnkjmkeubuxqyglearnbsuenjvquafrqxaodmkvbatnmbfjrsgtaagdtrmznfbyfvevuhjdmybxcgbbarvvazwbhjwrwcrsqkoksqpdgooduzxzeciggdvnkortfuatsioemjcqnnibsiwltfnbrgcdpwjufvpmgsmqplkqrxllvtlwlocagfntqdulenaeplbimhmwlkyeueydvfnlmxguabppwiaopgsbxaxvlwalsszowjmtpoomfkhohdlufqkwhudotldnxkoijzzpyahrfkwqdmhyspjcmhysdhwmqcuvwlrhosazbesmvobtyjpyxzjsxtcfggnjncnpwjykltkwgzivcpwlebmbvicdineilwgtthirltzbdwxkecuqsthlcsogdxqjbekqxvmorfgslqwrkefgccoifycxldkowpwlutfblqjzmrxngzpqhwomqiareikkgiuuvsvkmxqtdwpgnwjsykjkfoxksgxrrwzprhodgelngpnzqlzfyaogakhzqepwstdyznldhlpursbvhyzynmovztxkvymamfjmuofrrljlwedsxiavolibaajuixhtojagiefkrhszpksnbsaiobtptvnjjkmnvntfaxwyxqiffrnlqxprmbrxojnldqupiemiczsekavoudcxbhsxkmjmgtsdxgapeaefewxpekkfexprjemvqkadhewlmytdkttpcczakqlgkpneqozesdzdkjfxilvjdruzsizdlyxfnnvvljxuzgwidwhozswckdzrynoyqgmwabfeuasatkgcwwpxcnkgfmybpneiiwvosozmtzulkuxfosgirktlwasddwxvafczsadfupoawikfabheprgkgbjopnxxometvjcsrmahgtzwcfzajpoaxucnmshpqiemvouchjymkkesttbjhdxczdsbtrurdrrhorzdcprndfdmcfvmdsvjwivndcjmhibtrbcdbztrybdbfjbzvgobxozjsqlvixsiwaxfgceohtvsxjwnmygxaabmevwongenpjnqhyiydqupbvgolvmjcncaktpaydlpbkvtzgywdoesjdcwzpychuosamexunwnaeexajsneekecplcbygzrukwvttkgplbscvprquqfcavajruxdbxegsccxmnraldxkmvbvpcdqnlmuhfdhatypkeustqcruoqwfddcngtcsqolqrrtlpkdyhlapbgwveotbhwsbazwwyejqqmvgdwxrlcistepkujsfmjhhswrovrzsffwzakcuinggquyzgrfjiylbemnotmwpquwwralxlyhkmouypjemwbkiojevzifabvothfpkgpxgyhmjtarmhkjapnkwkbcczbutpiekpwsscdzbgaqmjknazuyzwpvjgxpgzzgqjvxxzsnekamabywlcdgmvunbyypuyypqbpanlcsnxbxzqfickgljswrxdsncmgtmwbmvgsmqwvgdjabiakcxsyrethhcargkluodlqmdmwajeolcdggqcuesaxydqdeexrnhzquucoafdvapnqfmejaspcdzthcituzjxteyseldmyzvargtldfkshfbhbcyeimropbqgytwwmqwrtjycpsfaeuqjtbkwkzwvhomwcokbjqeffnahtetznzkmijnnymgpxyiexxbbxtqeaawklfnrjpofvwkozauyszqcqdvvhdcxlkxptdcitntztxzxxzzrrowfobohmbmqdllrdqdbxtfkqhkacexrxfvyienrquikwwojfjwodveboixjcxoriqjclkteiahhjxnfejsqjphcsxizjqkaiwrbhlyufmicsyxjcbatresjgzxvyokjryejgcmphfjfvawklusbsvrqbezdbxpfnsynnwvgcsapectmiqpgvcbczpapvpbgmtsppqmiofrjxzlqarqfrdjptqxbwgaahtvlbjjeqtaycnhdcykfhpvrfzyonnlnyjujlpyqtrrilaspecrhqazpoumltybxbqpocmslbnhgaiwmxbjscndektjkjsaicntifmjrvumlpkhqczgxzpskzpwtgzzwunldncvdccdvyycnfduoremfluhvoldccaeoanbthefavetcjuyedhnulcoatitosxwkqdeczyqffehdeauvowltzuhzaiklmxezyiebbxhbiwsghtpyhxktzbmhdftfebouxxslfgcwyunqvlgpkpvuxilzkgxornbqrnvgbnvsnlukclsdwofoolznicmlzfyrcnrvuabmchcnpbwgjhxvdjmdlphedgdxokpgaptkvkxhlzhnddsvlvelzaghuifbeuwzvlioxdfzftuxpnaaemnmeloehqecatdtxizggabtdpgtufkqazrlasqvaiwlmrvyysvnsnjklwelliijopmsbdppodzdxedwzjzwwnvsmqfgwecgslsuekodkakymfgqyfquvylbxmwpssycyexeuizcsyqygkbosemvcljyofgjsqepfsypsnnfrmagewqbbqsfolnylzdmbznsfbpjamwhwosyosvjmkvmjsvqrcmvmeajqjkyjkflwhbjwqfckrsxgrqxzhcngzpjtacyugtpcnvryurohsjctqzqqrecoolmjbrwpdmordysxlkcuinpoarhwxsrbjrvdfmvadzavnzcntuvmvqsrxlkyuauwzuazlixepigvoypsenuocvnswrsexasvomzlrasjhxzshiwepgtxehstfdvhpfgmrmsnqwlobymdqtzeyzysdxobpgttwdktmjhhpufuefixyrbdmtzvtiadoxzbgbgxqxzoyzjcbrrwziiajvndbpmqjwthmetwjubzpmwqdktdeyquzwglqxinfzizrlycgblpuuehfprqsravbwzncjfbmjujsekwpkytmxxrangzmeasnsbawnwjfmqyxcnwrxsqldabdbvvwebyfxhtoouebqweqwwhojwoqxxdnkundagtzoxckblktqndyhrgqedkgccfzdtbrdarzihpritjhkvljwatpiwmatlnwexxaoaqcbbefttrnthskptkzldlzbequaerzrecihudrtkytgelomiikejxcosxgwockvkzitkojubtglimyimsjrddocksitxbqleddhvflnlokorvvhnkltglfxeumbqldrowfirloaijixbgqhqhrpsumbqyxnztuxlaiipudxbpaybaasskpssaybwmkhembkrdqjpiuyypsthybpathhbephhmxzmgjyfzvhileqxvyevmscnjidjttlizkujzjaeboaggczghqpbguvjvmamwhzeszbmzlnchbnbgdigzpwfrhedovfwtvxdkjlyuvgxklyfdbkqgxgzgcstmwqprqpbwmptutqsskydsagmxopwtadzsiocgoacvqjcmsathonflfrskxododrktadkqduhgmojhdceqqfaidczdrjgcvouofkdvrorjmuajfvqrucdhytgwcfhnrucfjeglcvoiafhcmyghgkvwgbykwuignnuvzhksfvrqmbjdkrcxvxgajsyuonyunqjepzmidlboegqhbibquqybhvxaomrhrmknnfofimtfatttxsxbotwnkiyxhefgbtlofcyesaocsmpfzbvhfmfnrfoivkhxusoanofldzlddgufrrtlwvrwrpqgzruqlhfxvyxupacbnpmnkifkxmldmkhipbfdjjszheokrtxmtvzembohakmbpgsbebkiozyutjwjqjqjvwmcfqjirrvxxzezrqvzijverrlwgpvwnobthwcgeygtvxmzgfbbfhrwtslroicpfvubufsoxmyxhmhlluoisrhqhwkrbjjasxjwboqkgyvlooevsgcisuneapweuyooprtvhknmywvbtcfwfcfkrtytrrwojrubrckyhtckorqusfhedmoildyiqgijhwpmpvcybxqaxbktegtnkiidldapnyqdyvieoxmymkoqcrpehyhhivggawjwlnrvyxhzbwdvsfhzmsyjvpoqjdnygtmtxdueerpzsnuydppuywqyzcffmfnxouiuicojoixjgpacvoppsmxxulbyyvqrdajjqcclcxvirbbbwradbmqxpxmubdffilhasxlnhtyqdqtohpxjdsoxaotwvdinhmsiyhdbsvpdpzbnvenzbrtyliztcomxijzvrwimwkdhmacaamwczbopstrsclzqgxpjtpmeyempuronmvtuubuxvnxoptgmzhkvbutfbtzzxpnwdnjodhxnllherjugkwrjguejefnitmhsmulbjrzntzscnqaisboyylrrsdcigbkdzvkmlezwzdfpvoofgovoalfsmwkqrapfniwzsspnbuymesqdivnuclxjmhzaukqezzjnatgmenbgroiqtchxngsilqjbmwzasmizqemvptzjrtztxrtrhfalqlyfavsofpaauzwdxfrkswresriqmfcxnoxpzsoojjazscfnnaosvbvhtlztkshtxnsxzajhidrqjblfusqqtkdkmrnplbcgchajvrroktavhbxqzacpisjpqxdahskqvjrmhkwkxsecyrwqpzelhtmdcelpgyfcwjfvrwkqjunoqabiucsvcqeklmgunfbyrtpnzymogvxkoyyhebjncnedxlcjpohhbnxbmnxetnemxwwthvgmtuwdmvojwpljxgubcyretzkjyyepqcgyptmlqmfikojboqnsarrwvuixrgtzkjygzrvzzmaeldhuahnpsauuvhvmblsjwnpamrdeuidkufjemutlicpsxgboimjtoxgnwsbgokqguwexlhzctrzpdjxphbfmorvdvwgifojyljiyewueahyxdssjkkaomaluoclccdxqsukbnlhdohngoltljeexayrkqloohhjrrcwcxxmtckbvpubxadnhyuvgizoayqecgwgfrkkzprpjvrwqhxqtxksiozbggyiavvpakzpdewfgrytcwsqnsuakxpxhtqbvvqhcqvqmvssfkoeydruysnlgyttkvtqiqitoktebkdabovnriltltxuiksmiwejqhvrvjoyoszrdjxabiqtmpebjhidjnhbrpzhpaicxipyzroaumorglynovzpyftocpjkwhoshlcarnejvydzwzzslcrqflbttyflulyzufrujzqoqmcuxwvtbfmcohsamugiokrxfodjwgfjebbzutzngwuetvbdtgzibczcdpzadgfljwuwrzijybxztkoeqbfyjnksyyzfqsqltvpuseitxltxhwjcsviejxbntyjnqzyazyfiyedgreukzuoviaeadfxovnhbnlkfncmmgowtwapbkiyybtylxwzqenjogecknfnkbewakpydpdcyzxhseholnyznshtnfsinqqooewnnbsgfcnvexulhwclxxyqfgvzyuezrnxlmwehotmtdcqypfjyqgonfgxbemiizpzpotbaqozlspwqwkeuaqklehbxxraadpfyceynlmgcwbiagntbzvdhinhkilkgtapkuhxmwmfqukxkyydulfzxwgiovnxmcsxjhgnpjhcepmeslxbitvvkqipsvoblopvbxefgmhcakqvfrlwvxynsyfuikwwskdfjqyolikvfvgrsqgpxveayvcxecqeczndokiuzdmuyweaoaxtnafadxuunjjglpaetzwrygmpnrlasmvheedpoxcyjvcwzzxavumofvvjwdpdpplzvvqekmawfmjhmzsfbeopecaxmptcrvclrnvwamaceyhwbwcekrsgavztsurfcdviybaclbkqtihaatjlxxbvdstivtgwnivtcbnggkpsdbgvrgwwcaomgpjkuvndtjxgnvbpnsbjpefabqntesofocztetegrnjemseppmsuxuzwqzjhzqjooffmnchlfivplidhqbgydiwulaszbyzduujdroyvnrqyylqtbshjzpvupjiiztddrmvlifqcfjqgddgshnpcvxrgywudvyvsnmcbivmgqvocvjhyndmjtybbcjiuqfaxdyiuhxsuzjmjjsyjtzfhyjlhjxaypsvyhyuhsgkpqobolwxhyezscjcegzhsuarokrhgfihkgcnodjnkruxkerdqgnzlacpf'
b = 'noookxbijxonaeyswwllluwadsiwejoxgcsxfkfwlfweblgxwpzshiwjnuioaaahmridkplyotawaivtypfyadufhxxmazeclfnxnachotgulowwixptkfhlzatnvpikezmwpcusrthtifuxufowpadnyodhlpqqhzqkrpaeixmffhsdbqtfqlgewznyjdvsocisiaqxvssyuxypwqgcqtyrjyjdzusbvewvkrqeowtlozxxrjtmzodpsprallsrcpznvawlhgzuogceovbdqhpmvqbxqmsbmkbreaeeqemkpvdorvmdprugxuulurpshzjofmfgoelzawdkpbsjnoawyokkzxffcwdfopxoiqnifkdqtyrfpgrfpwtexfypnokapxltgcalklfhazqgnruhhhvtadgkiafczrvqfvokfeqtrkwirakryhonxktwqrpfwvywmsdyblghkvxmgvvrnukwjjkalxeqsfcabnussckotonhbruxobxdngnwizjxnuckretxthjsaehetecanveioipghflepoxiejennhcxhputronvwliiijchacuthylbhxcocwynyyhnrnhzebufmnihotqkrmxweudvjnlqjmwtdwjdylidqyeyilndgqtessezczjhggcdgxxfuhisizwiqpdwxcjlntouuejjrzpmltvzkiitmvrevxbdzlxxnsffppvguombmbopoxslsenqszhhcwigqfddxaohlbxpsqroeexpooatamerzlmuxklldzjnssczlvvpkbdqennvssioappwdnzvttrxwiwxhctwqqwckdokythycljxtnmwlbiehmitnrzjdttkjvlxopvfivunfylzaxzznbsdqivnfkjytncelenlvqhhemuyhquolthhppmvjjlwzjqsqwmipjhaqigsuwkwilklxjlhfjrjifhywkieaxcsxuuwyiykwfbvgkfisjsrqtfmmxhainnuelnmklhkotsfcphilhbiumpthduoobahhexixyhlzapbkohztabwtinowbknkvicsfohrkskeojwtetcdggkwoguuseizkrkmnhvccvvnbrmhyqjmjragtdkkmokzhqdaessbwkahafsicdvehlrkznqmtekxpnqqekpxotrrnkghjoalunoqsltxpxjcsqxxfpkclxpflpahkkhqufktewqmtavtdrhwuiyodocvkgnxmehfigsmcrwmvgjxfoyfujzvosvfblzugsiyihwihbaqyupmkapfgpyrxkedraoaahuvquphhwllepxdvkwlutvaepnpgmmchelgtdtbclveothnqscviehspsywnnilragxatyksoqdkowaqckhehqxhlektthimcaowfahoumotquabqquanvzargybbpfjyqfofksrlxfovnbhlxcguomopzjxscltonykgxgyibcgnrgriqlgjfxwcxdidnsjfanxyqxnevonzfiwfnmagdimoaovdtltihiuxwxsmhuhhyqwrdsqxcfqxrnbqfkiufnltlelbxllbpvthrynzwixfozceakenhfzncbacqraelmwenuxcoaaxdjvwdiwbcpbfxgsjffuyerbhifqeszajgiqidallukaljqrlpfipjnubglykixrrwakmyhstzuiizhjieeayhveqgwgbdfnrtozhzjmdqmybvyrmkvcqqdroioovxqwrwvukwebarqnvyaiyntvtireqhtyoqxucfyrncfxravrzplamdmakmbyhiehvzwepkyjgarwcfjnhqyfeoybfqxptntzylhsbwzlnupartvwjkgffcynuxkwsagzhywekcuiwhpskmwtsztcukiwrwwyasvvvuatonjmusdwmqpapjyivyftymykalbkbabchepcneizjxnhytsldyhnpeqfokmsnysjufisbnkvffgtbzjxcqdyyxvqttbenavomzclkmimgshkflpirenppbnjfywtoliavmzgnwkgymcfdckzixehcykmexgdmlfewjvuylcllcsaluvmyiwjteylkhtxryvwsqnwrlgnmnfmftszehbjerdeyahbleizpysrnhxdchygjfjbakgycdxazvoqczqxozfypqtplkbzovmibodsmpisohgzgolcpefnjmzcyrnxtoqofqwryxbjzzbdrtbhroulkuzofqvfjydtkkdugvkunuifbfaxxpxlcmnzfabmdmanqcljdhctokvjvogqqhkuabejuarifbmmjxywtztbnzfjtlvinakckuhvcrroebhkwulxzkgsczqziiokloshrqkluilxhfpjeubxwulyejlsfytmvmvbrnczmswvfxqsvzxfnjkyybgeedspfnglouvcuahvyyodfurborqfqcbwrzzwqugtphsiwvvdzuvpfsrrxkhztvahtjmdnfchwrgsfakufdbitlxsjaclbjfvyoznpnfrgjuclahoirzlittxbenoutehzmwyrylugpbfpxddwtyipllzfqndofqbvqlzmjbgmfkadnvgufshjqfxibgpgfjbaplzdycytlcjwwvveyrtvyjibmjwzvkehefxjugekhzvpnyhempuebotbfktfrhgdsmwnmqtcxmbqeyelbjsvidpeglbqujneojffbceakasrmzeeimliujygslxrbujltxbqdlbapqjfsehlnvswrcmnnskkobandtdjhdodwcjfsdeyaoihszzbavydyoawqueulccsxodpecuvqknmzelpipwrqehbpbalgjmcpiljaooxnggiquakutztzexcishxyyyxggpatvzznhrgrnfmwcwpjutynvltwqhsbuthuampuhyleuuwqlhmkdmyvzhsqvgsoarprtyehuoiibzgiekmhaaiktnngpkujkbutfxngjictprbeferbjfubaiztdtueyczfdnxmfbofgrqmdrijtmyjspqluygkqtviohfbouratvuwfqhkcbstvwaxuhspmokjvbokqdxmzpngerxqsriyqlqvkpnkbcpktkycofeextdbcyxsvhgyuwtvzevwuseitowieenjlwsvatvxglgcmijvggsmhxspxljjyuzpsdpoligtxhgwoybfrmkzojavqxtbiaqjpgmeajtoaunnzclamkkchrvskiuwvqzqcuoobkqaxtdwoswgzpgdkodewnljlkqxioloatjskxbgjrpgqvgfsdkxwozzcqibazjugyziwmhrtayurtggsausadyglciqcopbuoavdzxtoguxrhnnoklbkhcmzrfbdttwscmldfnxlszorgxnkbvbutjpgbrzkaaopixqclsaxtzplqyrededvcomynwbfytudvlkrubhrcqqptntnsuznjdzlycdpflsgzblcfwsgsjupurbrmjesaemzjoqdzndnbobnofhquejbqnbfufghuwidtpfaanpnhjuolornsexgplluaqsgjudrcxqfsrglpzlvmrttdyesxpkocbzhnlhvkftggphrgvolzbjcogtabdnflipitvmqrgoedviwdivjrtstfikcdlfxcgxbafxzlxhbpkuxjtodimdxtewamcikrkzrlqrwiaskpqzvstwlkitxyxxnfimbwywpkhqtbzjotswxowlpluwjbiirktkhikweephpbaocjqaruhzgeajkeemxmdjzxwncgjzomylqqekvwycinmnudwiytdiddqestzrpfpktmygsbbattbbcsblilbjpxbbvqlntbxclmdyodjhysmhasehjgdzfrqxskvlgvwmgqxxwslxucrbpkvnrfykvsslekcxkeoentdbrmwnmtqopywaqoatrisjegrhsuuzgzmqxgcyopiwmhwaeaxacmmbltzjaodwxmofavuwpbkqmzxislafduwqzwxuxwrohltgtsxepwiztlvbgomylzdsqdwhksdybgruzhxgjnkotbksmcypovbqljltqjifualvmbvjeqejcbutbtnbqrkudnhydquybazgbnuobxfnkdtssoloregwyupocgweqshwulzqfpvmhtnwtduqqzanevxqyzbjchhcdlvmznkvvwettkidqkuthynassulidyyzvbuihpzbsamhupwlqlbbxmgmczzdwmbwyprnjnblcdnzfwsfphylyqqbjxqzxmnzdaeltraemcssfhnabtofnxpkmzjvvmdyzovuljewbldjxamkdjnfycszluacucmxrgyobqmestlfahsyynketxpevegtwmqwuyetubwoiaohrsyigzjniaxadzwctxubeimhnijlkxisuoinlobvjhhutbrvfozmarpsrqjxzsxkxmvnsgcbzkrxmptfgyapxlqiownpmepqbelanuxtpbquohfmdnrrkvjhuwznmqoanbryquijibmqdttgkcaffjnzhteuueuznsxlyaqcadhqzagommwbnvokciqhsfbqsktzlrkweevijzlvxqtwwlyxeehhxrsjqwlsbqceecfzjufzzejepsfplbggjsuqbgsdvwrmnqsmwjwsgjjtcqbqgubymosfjtqbymbuubsrvkzasqizclrcvptvthlzuxutahajadilfclicfldslrnrjbommmlkuzrgwjeqaoktlvvvwbymtetgrxcnwxmqwykotipvjspfvvjcbpbswetctwnlbbucttpebwtbojesjtrbryccryngxdrktxltqsibfuoaryhobhalnzktduiaischvglttrkiinztiswiiyalsjuxnwirnkudwqdnkajqkjhodmsobhlknkwfmuxbeobrujpotlnsbqombptdlfniwhcttbwsjmmducqukflmytqvrlpjtyzgtnnbivyssmzxlbovcofdqriunrcighuzkznktccsooesmpabafzhluakbzzzhekkfcqtlojmvcabgicejljlnoxhafpfvsybqeywigpidssziffxnnyuprmchscwfieedmqjqxivvhtuhdxocgpwowolnitthvwavuuxmvqcuvxpanalnfbqubxgaiurxkyvksewgtmjtcxvymkjinadyrzvmnmivysqnnyazlkiziritqcdxwmlhecvgduogxgdibqoumoepuxjbwnobyfcdppuyanzwramehwptlsaylkdirmdtiunojeqxmohongzrciqiqjprynxlijtrxnqjxlotuncmfjsxiawchgzwyqvagpcudigwcinbkfzrflgfldpcjcvonzimeedbhusicendndvoubksdkgsmhglbfztmmzqwwkrnpklwampzmrgxrhtfmpiokehnmqcimflntggtdzrbqkuzobjkkxauicjjwikxekaciolokppowrqogcfcplekyrdtfhwjaeylwnrdumcvaydjjxnitmymdrycstwfedkgtmgkejpwrtimebxshxwvjcixtrrtlkfaqdwgybpukmrkmjxrcldwjhobkphbroirabcxkpppoljilnyvylhqfrwktqovbxygbpoqgggleahwuhvffdfydvlgchwcslpibkcgfgbmwdbsfrfloyawjdofolwothbmwcvhjcwacmsoutotzgjkslihzcleqnqrxolnralrckaqqykfvcaavbmmzjlilaoxvlqiihdpayzzddflrfcyrvpwivexnzjzxjrxaisvjmwyittmrxwogubcaztsffozmwcflzilezajbafbaqurfqswxamfbpnflfrwbrnoebskjdywrihitlnspqacvunnvlipmdfdelzfvsdmoebvfuysknoxgyaobhctshjbbiwkmzpbcsmkwzuxezwfjwkrnnlhhzdyhypxtboblimeqelwywbqofdscpsvqjoahgyezxkhyvtcmyrcwlszozgblypyzbgxlafisfmepkouflohoznmgxrnjxftktsjtgzesptprydszjuoxtwvkvpimlbrqveqqthacsraxdmukplzewijycqmveufnlskxnziqhxivplhpgqjizwrgubwjwaausiujtexpegxumqgjcbxdgqumxawbpigdrfkxbcrxzsozxlacudolqmlhnksohrcmqbdhrzxlvkeatmxrjypqoalnxgzymorveoklgetqkxwlsultppvumvjxicigbgoxqlrhjzfemxucrenhlzclkjpekifhiruenuhkrsviprjacmpxlalwhhbfbbkmqeugrsnfhxmhnuemfggufhhqltdiewkmwmbffgkrvjxjqtydrxnutxtuwohkhdogqjuafxmjtocjtefujwxablrekpnovlbiickexvjsgagevteiyyzeuxllmyynabdiostsjusnckpxdduwiklizdcoumehfkstkfxfviphjmlpvfgeyghhqwtnqfkvysptdnkmyczpbdkjtbuywdjvcvzwqoggiwgyaissnauvoawbndyidyuphadzmuqcwofgebbbilzxrvefczydltfzdogvgiuvsgblufudvykzjznhsrujpsxvhqbbgslqlommktmobrtfwavhqgthmkdsdgmydkjxlxpzuiprzndxldzgzrahqkwdzbmbswzjsmuseyuhhamggzwqtzembeycprmjrtyytgjbytubnuybbjjnnnzckwdztuhggnclsobajquptwctzxkyfvzcvvjjxhzzibftgiprmphjbactvdcwukgpskycmjfevznvdjkwnxgvenjggwvjcvrfnbzemqmxqownqjbrjxwjurmbdawxzxlhmqzzvjlgxseejkfkphbuovudclatyvxeenkmywwytgralucaleabeqfgpncuogolnbronciqpjjoreqnymzwyrzzektjperyaqorhxubwxfpvbnshiuyqyskvrtfreqrivopjsgqgrncawelocsuwlrobqvmehfethigmyamhvwmygposizaeccmnulgopnomrltcrbgbdftqcoaxwdgyjptufjavcdotyisdaoczixrvurzugkgbmqpqpoamaiazscdskucjkpzrpfmuxzlxigforuypaftbllebhbijvgznhfrqkifnrupdykzmjoctnojwgzjetwlayamecgosdrpneaxpdbldegbumyeyxpurstutofcedgwgirqymheulbfjfwkplmxppryplxrbdtiqqsoecuakdffcshbsfkmvbpdkharvkvgxfsmnblmfyhzlgciirbmycdemfeulrbvmktllxvcjqlrfwqhwrbxedkvuybxqqrbyukyvghdmyphhocsdkviylzlfplyatbuklijcvwjlfmnronjzdoiehvcezyhvcfitdeqdzhpzoccyvvkqxnzvcjtkeqhazrscvrvujwadstrfvxzvnvmcmxtglmqxrrpesvdauprrkybrefwylvtpliahpemjioewlrfnsfaesgaehqrrutwhxgyodjlbokxtjmowehlxglqdernuwyzxbriletvdgsnxhohuvkwcuvtprngbgevhrikydcsnxbboorzymmfkygbyquacygqvlzchlqhsawcprmteqiaykbobfwugwrbcvlsrwrpelglhxxfwnwozaigmxquvdpjurtobjqbfmmotrgsuculjopxsmsumsepmtpwofxmltueaakxljeueqeggacwjksmgcnazvtatqqdcqioeinlogtumaaohlzcrqyrujyraauyrrsuwjkuzqevfubykkoqpfixbrowzbbjrmwfkpunkchotesgfapjwjicnjvoseooidcfkbifthjigjpnlfjbnjohofolnazbosmtcdbxsqfwqtlsltqbtixdcmgzqzdxqwbwstofymarvsubjnpcgqxshnvyavpabbutzrndrbejeysipzlnueuygmfozxdmlycgisivgwusfbixbnvhxhxlrqfnxfcdjpglcqfuforryssyrhprztfbkmglxjaqteszndyxizwpmwfcofsuncrdjqirxhvtzwzwcixxznqjqgbmtykkpftchhkpmlgfhnuuwaycdkqfxuxkkvvsligckcgvgxvwsjlfhygftprrvderktkozpzxisfnwaowruebsbqgwmzfjacxfwmorhdlwxnlwlxvcydlkztgxkovjfzredsvvsqpkwwyhipslauzostirnlgwyduunvvyifzltiyttwvosrennyhplbsgrpjnepvfimfbwvxncenrkniezgiaowpjsgvrtehrsvotwdlzkhdbnyrqtxxohdrrhqytsyzyeiohfjvfplmkshiiggauhvdpadgptiqrncscsrwmyemtpljlvuajugiqgrfyezlvqkbjkwiitgnnaxtehtcmmtroikoslromymkqudrxhvdmpqolriseyhxotemnyekgrxovhddwrpklakngyrbgfbesyoibtogvachzbhtbvifrephdofaxlfowffzpkzjcfnukzhxpwxadninxgyzwkcpvkrvzwxalwlvmwgowaamimclvkhttfbtqpgomlncuiotewoefuatrxpyfyoefouhzjdpfncckwwlzdlbcfeewyxzgkmiajatifbepgupgbiewnniepvzfpaomlzstqxbbllotuyembqcqmgtegpztdhajvpckkrlbdkpdwnomwehvhfxyxgvbwljcvpofxghuoyuuuoernzxsgthzsylfuhvtvhkbexttkiakohvqbgzzmwsdqukudkxhnezcmsapfrftdsxemniaqkkhawglegfwxhcdfilvkmbtukgiivpvbsoccdwkonnpjmvswroewcbyxvrqxfbhbjpsszyxxcawwjllwmxkiivyvtfmytavtxkumdmtqzduusjdsbheihiowzmgjcvucjfyuvrljwismelsmoljmmwjrexzdkqtknqsflbditervdphhaaelvjvhfhgyadlirnsnyqkttmiybzvgwjcjgumvpxkckpkgzdjmapycxtengdifuvutskuebwlxvmwcbweyftlyjsrdwqdlmggvsrgmvxtqjanplpyvurnouubezxbsazyllzkyhqxolficamczagusawdmseqpicrrehcxwmrrkbtvlifoperiqjpkpqxjmjejeqlvczmgprznsjroguhytmiaqlwwjbgtkiutecmknzobllbvgyenzhxpqgyhpqkyoxxryjbblovsowjimmxyovoiduipqjanlolzlxcidfuvfoptzzkjmufkweqwfbylncbopnafalonjtuyxqtmteqitfsstgkwrjaaoqcguaegbhnuvnlrkvrbdqgckmnhndsiubdyflhxfhunfaoidjvbyodlfvfiljyslaihxytkcuatubeevihzqnrlbqykneltcsbzljxqbmjbnwipvhvonoeukpgxiehptpbidjvvghtasgqfjnjkmhlooegpuriprovlraxzcgbcghtceagjeuhtqvrrdetoucrymobvvlhoktqfdvlzgvadrtnwccrhthwhniwwoxjtnquijdrdvdyfzylrrvdkyquejmoqrzawsfdtbeoujiqtnrmfcqsudxmpazohpnukpunfralxqyfbjlhpoitiyqtymznuadreqbypupgotvfrkryyhkcnkoekhwpasgzskcgwfswhuzvkipzmlebshllooudakbewvfzthtqhgrwkxdgcudofdntdhdxrqgviblzvkhquejnydrnhfslaymwkyqxfqsnlalewrvqogykgkzolfwpzzzfaqwkepxnnzceqomejmsmujrfyydusaafuijkkikquftsnwauadmubytunmpjmjuiqxnsffrructqkmhzkdqdppdepo'


test_performance(solution, a, b)
test_performance(solutionString, a, b)