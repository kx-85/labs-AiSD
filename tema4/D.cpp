#include <iostream>
#include <queue>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    priority_queue<int> heap;
    string command;

    while (cin >> command) {
        if (command == "CLEAR") {
            while (!heap.empty()) {
                heap.pop();
            }
        } else if (command == "ADD") {
            int n;
            cin >> n;
            heap.push(n);
        } else if (command == "EXTRACT") {
            if (heap.empty()) {
                cout << "CANNOT" << "\n";
            } else {
                cout << heap.top() << "\n";
                heap.pop();
            }
        }
    }

    return 0;
}

