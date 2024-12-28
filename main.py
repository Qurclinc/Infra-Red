import requests
from Services.NicknameSearcher import NicknameSearcher

def main():
    searcher = NicknameSearcher()
    searcher.do_search("illidown")
    searcher.do_search("qurclinc")
    # searcher.do_search("byshbasfbvksdbfskhvahbhfhjz")

if __name__ == "__main__":
    main()