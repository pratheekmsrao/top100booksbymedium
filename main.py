import time
import webScrapping


def main():
    start = time.time()
    url="https://medium.com/world-literature/creating-the-ultimate-list-100-books-to-read-before-you-die-45f1b722b2e5"
    webScrapping.scrapingFunction(url,"strong","id ke")


    end = time.time()
    print("time taken by program is:" + str(end - start))


if __name__ == '__main__':
    main()
