import pandas as pd

if __name__ == '__main__':
    products_ranking = pd.read_csv('products ranking.csv')

    products_number = len(products_ranking)

    noIndex_products = products_ranking[products_ranking['rank'] == 0]
    top10_products = products_ranking[(products_ranking['rank'] <= 10) & products_ranking['rank'] > 0]
    top20_products = products_ranking[(products_ranking['rank'] <= 20) & (products_ranking['rank'] > 10)]
    top30_products = products_ranking[(products_ranking['rank'] <= 30) & (products_ranking['rank'] > 20)]
    out30_products = products_ranking[products_ranking['rank'] > 30]

    noIndex = len(noIndex_products)
    top10 = len(top10_products)
    top20 = len(top20_products)
    top30 = len(top30_products)
    out30 = len(out30_products)

    print(products_number)
    print(noIndex)
    print(top10)
    print(top20)
    print(top30)
    print(out30)

    noIndex_percentage = noIndex / products_number * 100
    top10_percentage = top10 / products_number * 100
    top20_percentage = top20 / products_number * 100
    top30_percentage = top30 / products_number * 100
    out30_percentage = out30 / products_number * 100

    print(noIndex_percentage)
    print(top10_percentage)
    print(top20_percentage)
    print(top30_percentage)
    print(out30_percentage)
