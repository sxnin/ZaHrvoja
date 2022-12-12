
def uvecanje_potencijom(osnovni_broj, potencija):
    result = 1
    for broj in range(potencija):
        result = result * osnovni_broj
    return result

print(uvecanje_potencijom(5,8))


