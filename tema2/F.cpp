#include <iostream>
#include <algorithm>

using namespace std;

bool good(long cnt, long q, long s, long t) {
    return (t / q + t / s) >= cnt;
}

int main() {
    long n, quick, slow;
    cin >> n >> quick >> slow;

    if (quick > slow) {
        swap(quick, slow);
    }

    long l = 0;
    long r = (n - 1) * slow;

    while (r - l > 1) {
        long m = (l + r) / 2;
        if (!good(n - 1, quick, slow, m)) {
            l = m;
        } else {
            r = m;
        }
    }

    cout << r + quick << endl;

    return 0;
}
