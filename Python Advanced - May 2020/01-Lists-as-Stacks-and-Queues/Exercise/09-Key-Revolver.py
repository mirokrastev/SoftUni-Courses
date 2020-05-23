from collections import deque


def shoot(bullet, lock):
    if bullet <= lock:
        return 'Bang!'
    locks.appendleft(lock)
    return 'Ping!'


def end_game(bullets, fired):
    if not locks:
        earned_money = intelligence - (fired * price_bullet)
        return f'{len(bullets)} bullets left. Earned ${earned_money}'
    elif locks:
        return f'Couldn\'t get through. Locks left: {len(locks)}'

price_bullet = int(input())
gun_barrel = int(input())
bullets = [int(i) for i in input().split()]
locks = deque(int(i) for i in input().split())
intelligence = int(input())
initial_bullets = 0
fired = 0

while True:
    if initial_bullets == gun_barrel and bullets:
        print('Reloading!')
        initial_bullets = 0
    if not locks or not bullets:
        print(end_game(bullets, fired))
        break
    bullet = bullets.pop()
    fired += 1
    initial_bullets += 1
    lock = locks.popleft()
    print(shoot(bullet, lock))