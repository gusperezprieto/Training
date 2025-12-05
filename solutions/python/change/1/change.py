def find_fewest_coins(coins, target):

    if target == 0:
        return []

    if target < 0:
         raise ValueError("target can't be negative")

    map = {}

    for coin in coins:
        map[coin] = [coin]

    def recursive (coins, target):

        print ("coins, target " + str(coins) + " " + str(target))
        
        if target in map:
            return map[target]

        for coin in coins[::-1]:
            if coin > target:
                continue 
            
            response = []
            response.append(coin)

            print(response)

            if target - coin == 0:
                map[target] = response
                return map[target]

            responseAux = recursive(coins, target - coin)

            if len(responseAux) > 0:
                response.extend(responseAux)
                if not target in map or len(map[target]) > len(response):
                    map[target] = response

        return map.get(target,[])
    

    response = recursive(coins, target)[::-1]

    if len(response) == 0:
        raise ValueError("can't make target with given coins")
    return response
        
    
