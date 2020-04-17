from collections import deque

price_bullet = int(input())
shoot_before_reload = int(input())
bullets = deque(int(i) for i in input().split())
initial_bullets = len(bullets)
locks = deque(int(i) for i in input().split())
intelligence = int(input())

while bullets:
    if not locks:
        bullets_used = initial_bullets - len(bullets)
        bullets_cost = bullets_used * price_bullet
        print(f'{len(bullets)} bullets left. Earned ${intelligence - bullets_cost}')
        exit()
    for i in range(shoot_before_reload):
        if bullets:
            if locks:
                current_bullet = bullets.pop()
                if current_bullet <= locks[0]:
                    print('Bang!')
                    locks.popleft()
                else:
                    print('Ping!')
            else:
                bullets_used = initial_bullets - len(bullets)
                bullets_cost = bullets_used * price_bullet
                print(f'{len(bullets)} bullets left. Earned ${intelligence - bullets_cost}')
                exit()
        else:
            break
    if not bullets and not locks:
        bullets_cost = initial_bullets * price_bullet
        print(f'0 bullets left. Earned ${intelligence - bullets_cost}')
        exit()
    if not bullets:
        print(f'Couldn\'t get through. Locks left: {len(locks)}')
        exit()
    print('Reloading!')