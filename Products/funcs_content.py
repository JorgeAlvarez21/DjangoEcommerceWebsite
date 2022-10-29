categories_names = {501: 'All Categories',
                   502: 'Antiques',
                   503: 'Art',
                   504: 'Baby',
                   505: 'Books',
                   506: 'Business; Industrial',
                   507: 'Cameras; Photo',
                   508: 'Cell Phones; Accessories',
                   509: 'Clothing, Shoes; Accessories',
                   510: 'Coins; Paper Money',
                   511: 'Collectibles',
                   512: 'Computers/Tablets; Networking',
                   513: 'Consumer Electronics',
                   514: 'Crafts',
                   515: 'Dolls; Bears',
                   516: 'DVDs; Movies',
                   517: 'Motors',
                   518: 'Entertainment Memorabilia',
                   519: 'Gift Cards; Coupons',
                   520: 'Health; Beauty',
                   521: 'Home; Garden',
                   522: 'Jewelry; Watches',
                   523: 'Music',
                   524: 'Musical Instruments; Gear',
                   525: 'Pet Supplies',
                   526: 'Pottery; Glass',
                   527: 'Real Estate',
                   528: 'Specialty Services',
                   529: 'Sporting Goods',
                   530: 'Sports Mem, Cards; Fan Shop',
                   531: 'Stamps',
                   532: 'Tickets; Experiences',
                   533: 'Toys; Hobbies',
                   534: 'Travel',
                   535: 'Video Games; Consoles',
                   536: 'Everything Else'}



def search_text(text, products):
    text = text.split(' ')
    dictProds = {product.id: product.name.split(' ') for product in products}
    equality = {}
    matching_products = []
    for k, v in dictProds.items():
        v = [val.lower() for val in v]
        dictProds[k] = v

    for i, w2 in dictProds.items():
        count = 0
        for w1 in text:
            if w1.lower() in w2:
                count += 1
        if count > 0:
            equality[i] = count

    if equality:
       equality = {k: v for k, v in sorted(equality.items(), key=lambda item: item[1], reverse=True)}
       for index in equality.keys():
            p = products.get(pk=index)
            matching_products.append(p)
       return matching_products
    return list()
    # returns a list of objects that match the search, to be rendered

