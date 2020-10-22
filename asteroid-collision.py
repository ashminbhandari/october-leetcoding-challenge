class Solution(object):
    def asteroidCollision(self, asteroids):
        if len(asteroids) <= 1:
            return asteroids
        i = 0
        while i < len(asteroids) - 1:
            m = asteroids[i]
            a = asteroids[i + 1]
            if m > 0 and a < 0:
                if abs(m) < abs(a):
                    asteroids.pop(i)
                    i -= 1
                    if i < 0:
                        i = 0
                if abs(m) > abs(a):
                    asteroids.pop(i + 1)
                if abs(m) == abs(a):
                    asteroids.pop(i)
                    asteroids.pop(i)
                    i -= 1
                    if i < 0:
                        i = 0
            else:
                i += 1
        return asteroids

