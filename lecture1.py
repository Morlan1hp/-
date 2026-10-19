import sys
import time

def gcd_euclid(m,n):
    while n != 0:
        r = m % n;
        m = n;
        n = r;
    return m;

def gcd_bruteforce(m,n):
    r  = min(m,n);
    while r != 0:
        if m % r == 0 and n % r == 0:
            return r;
        r = r - 1;
    raise Error("Should never get here");

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("Usage: " + sys.argv[0] + " m n\n");
        sys.exit(1);

    m = int(sys.argv[1]);
    n = int(sys.argv[2]);

    start = time.time()
    g = gcd_euclid(m,n);
    end = time.time()

    print("gcd_euclid: %d. Running time: %fs \n" % (g,end-start));

    start = time.time()
    g = gcd_bruteforce(m,n);
    end = time.time()

    print("gcd_bruteforce: %d. Running time: %fs \n" % (g,end-start));
