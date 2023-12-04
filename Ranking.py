import csv
import random
import time

import googlesearch


class Ranking:
    def __int__(self):
        pass

    def top_n_serp(self, keyword: str, num_results=30):
        serp = []
        for i in googlesearch.search(term=keyword, num_results=num_results, sleep_interval=5):
            serp.append(i)

        return serp

    def locate_target(self, serp: list, target: str):
        position = 1
        for result in serp:
            if target.lower() in result:
                return position
            else:
                position += 1
        return 0

    def add_to_finished(self, product):
        finished_file = open('finished.txt', 'a')
        finished_file.write(product + '\n')

    def read_finished(self):
        try:
            return open('finished.txt', 'r').read().split('\n')
        except:
            open('finished.txt', 'w')
            return open('finished.txt', 'r').read().split('\n')

    def save_results(self, position: list):
        results_file = open('products ranking.csv', 'a', encoding='utf-8', newline='')
        writer = csv.writer(results_file)
        writer.writerow(position)

    def rank(self, num_results=30):
        target = input('Enter the keyword you want to know its rank: ')
        keywords_list = open('focus key phrases.txt', 'r').read().split('\n')

        pages_number = len(keywords_list)
        while len(keywords_list):
            page = keywords_list[len(keywords_list) - 1]
            if page in self.read_finished():
                keywords_list.remove(page)
                continue

            j = 0
            while j <= 5:
                try:
                    SERP = self.top_n_serp(page, num_results)
                    if type(SERP) is list:
                        break
                except Exception as e:
                    print(
                        f'error while getting serp for product number {len(keywords_list) - 1}, named {page}, {e}, {time.ctime()}')
                    j += 1
                    if j > 5:
                        exit()
                    time.sleep(random.randint(1, 60))

            product_position = self.locate_target(SERP, target)

            self.save_results([page, product_position])
            self.add_to_finished(page)

            keywords_list.remove(page)

            print(f'Done: {pages_number - len(keywords_list)} out of {pages_number}, '
                  f'remaining pages: {len(keywords_list)}')
