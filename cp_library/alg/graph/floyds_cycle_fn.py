import cp_library.alg.graph.__header__

def floyds_cycle(F, root):
    slow = fast = root
    while F[fast] != -1 and F[F[fast]] != -1:
        slow, fast = F[slow], F[F[fast]]
        if slow == fast:
            cyc = [slow]
            while F[slow] != cyc[0]:
                slow = F[slow]
                cyc.append(slow)
            return cyc
    return None
