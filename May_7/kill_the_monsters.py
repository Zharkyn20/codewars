def kill_monsters(health, monsters, damage):
    counter = 0
    hits = 0
    if monsters % 3 == 0:
        hits -= 1
    for i in range(monsters):
        counter += 1
        if counter % 3 == 0:
            counter = 0
            hits += 1
    health -= damage * hits
    if health <= 0:
        return 'hero died'

    return 'hits: {}, damage: {}, health: {}'\
        .format(hits, damage*hits, health)

# BEST SOLUTION
# def kill_monsters(health, monsters, damage):
#     hits = (monsters - 1) // 3
#     damage *= hits
#     health -= damage
#     return f'hits: {hits}, damage: {damage}, health:
#     {health}' if health > 0 else 'hero died'