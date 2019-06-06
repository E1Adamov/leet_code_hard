from collections import Counter

class Solution:
    def findSubstring(self, s, words):
        self.counter = Counter(words)

        if not words or not s:
            return []

        substring_len = len(words[0]) * len(words)
        string_len = len(s)

        output = []

        start_index = self.get_start_index(s, words)
        if start_index is None:
            return []

        for i in range(start_index, string_len - substring_len + 1):
            last_index = i+substring_len

            string_window = s[i:last_index]
            if self.all_words_in_string_window(string_window, words):
                output.append(i)

            if last_index >= string_len:
                return output
        return output

    @staticmethod
    def get_start_index(s, words):
        try:
            return min([s.index(word) for word in words])
        except ValueError:
            return None

    def all_words_in_string_window(self, string_window, words):
        # a = string_window
        for word in words:
            if word not in string_window:
                return False
        substrings = [(string_window[i:i+len(words[0])]) for i in range(0, len(string_window), len(words[0]))]
        # print(substrings, words, sorted(substrings) == sorted(words))
        return self.counter == Counter(substrings)




# string_ = "faoucbmnvdujheznbntaszqsxicczlagnqbrsnfptbycfapjnkjflbzilemkpotehwvblcsefqgnsxwgkhnvjpgutuhklcosylvjonqtfyiyyegimtfxilrdiantcdncpiofxgaegjcenkobguyqhsupsjkxnxbehrjgxjlespiiazjiviyeaswuegtrexxnogumrfskwcuwbfgynfdpzzmdfhwletbvbvjtcbfydbxhgdfuiilkhznpjmcnhdkjytecujbykafqdkmovaacbntkbwyjziuaeycyhfytfdllqybnabpbqlmujmdiwxkaxnzeuxzcdknvkqimtzojkcdtoiemhonedokanjcswpnihvvaxlljprdfzjrhzgnfwyfkjhchyssfppfmaqwrjbwjmnslwhqsfverejacbshshohjhdaqgwzsmtfkbycitjzasccvukpcywlhboyjkzdyvjiwhngcwicqkhnercgrzuzcizmuyptvadrhqymmgqeqxrwqwfivzjzjklfkbygbczlszzhfpnxpfwfdbpacazlklqxordrveepedwlvmjktfrwihwkjvvugntweyqzcupgynstzdfskwqsfmcpixlqmenrcfsezjlxzdsyiztswjkdymsgldwxhlqlqjqsudptikuqjpihyslwgderjdqsqhejswbmzqihcczorhvrbiqhouaxxqroxvxrragssozvqajhhgakrqrfltekkvajtzbkzhfsvepnfawoiwzznsgammmykphdoipqrukobzbizxyhuxjjsrjgexgomntbyktphdekchsdfqmbqxkkpvstsyjfleilqbdxgjhkqbnvsbwkzguodmjwkubxaljqomouvxelztjtwhdvqzltlwpxssusffjtrznowtavmlojstgisuefsvclozdteopwnckmwmjkzavstecoyitsewduvjpzzexnjkbhykrympsitwwtfpllnrfiaukzzjoivrrueisqxmysiulpmzazqfkqcwrbfilbzcxfmrwmdwelrsbfrdehjqznmsquabxcfuhtlfhqcmbvgeaxkggvxfilxyfabecgalbnrjdtxhodnqcxwisvpahmyomztqhveljvumotteyhuagskzozbxlclabgslcwylruzhnvnlejnkcxlswnpjrajsjefnadauxzbmwrzaamnclauhplrgocbxggkjmkdllgykzzkamzcxazhpkywycxxlfhuttzfhhfrhedjqfnqfmxwzxuxztxmzgischzjrecajhjbmwrtlqqknmjpgg"
# word_list = ["mntbyktphjheznbntaszqsxicczlagnqbrsnfptbycfapjnkjflbzilemkpotehwvblcsefqgnsxwgkhnvjpgutuhklcosylvjonqtfyiyyegimtfxilrdiantcdncpiofxgaegjcenkobguyqhsupsjkxnxbehrjgxjlespiiazjiviyeaswuegtrexxnogumrfskwcuwbfgynfdpzzmdfhwletbvbvjtcbfydbxhgdfuiilkhznpjmcnhdkjytecujbykafqdkmovaacbntkbwyjziuaeycyhfytfdllqybnabpbqlmujmdiwxkaxnzeuxzcdknvkqimtzojkcdtoiemhonedokanjcswpnihvvaxlljprdfzjrhzgnfwyfkjhchyssfppfmaqwrjbwjmnslwhqsfverejacbshshohjhdaqgwzsmtfkbycitjzasccvukpcywlhboyjkzdyvjiwhngcwicqkhnercgrzuzcizmuyptvadrhqymmgqeqxrwqwfivzjzjklfkbygbczlszzhfpnxpfwfdbpacazlklqxordrveepedwlvmjktfrwihwkjvvugntweyqzcupgynstzdfskwqsfmcpixlqmenrcfsezjlxzdsyiztswjkdymsgldwxhlqlqjqsudptikuqjpihyslwgderjdqsqhejswbmzqihcczorhvrbiqhouaxxqroxvxrragssozvqajhhgakrqrfltekkvajtzbkzhfsvepnfawoiwzznsgammmykphdoipqrukobzbizxyhuxjjsrjgexgomntbyktphdekchsdfqmbqxkkpvstsyjfleilqbdxgjhkqbnvsbwkzguodmjwkubxaljqomouvxelztjtwhdvqzltlwpxssusffjtrznowtavmlojstgisuefsvclozdteopwnckmwmjkzavstecoyitsewduvjpzzexnjkbhykrympsitwwtfpllnrfiaukzzjoivrrueisqxmysiulpmzazqfkqcwrbfilbzcxfmrwmdwelrsbfrdehjqznmsquabxcfuhtlfhqcmbvgeaxkggvxfilxyfabecgalbnrjdtxhodnqcxwisvpahmyomztqhveljvumotteyhuagskzozbxlclabgslcwylruzhnvnlejnkcxlswnpjrajsjefnadauxzbmwrzaamnclauhplrgocbxggkjmkdllgykzzkamzcxazhpkywycxxlfhuttzfhhfrhedjqfnqfmxwzxuxztxmzgischzjrecajhjbmwrtlqqknmjpgg"]
# string_ = "ababaab"
# word_list = ['ab', 'ba', 'ba']
string_ = "wordgoodgoodgoodbestword"
word_list = ["word", "good", "best", "word"]
# string_ = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
# word_list = ["fooo", "barr", "wing", "ding", "wing"]


S = Solution()
print(S.findSubstring(string_, word_list))
