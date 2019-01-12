def best_stock(data):

    exp = [m for m in data.keys() if data[m] == max([data[m] for m in data.keys()])]


    return exp


if __name__ == '__main__':
    print("Example:")
    print(best_stock({
        'CAC': 10.0,
        'ATX': 390.2,
        'WIG': 1.2
    }))
