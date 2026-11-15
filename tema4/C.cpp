#include <iostream>
#include <vector>
#include <string>
using namespace std;

class MinHeap {
private:
    vector<int> heap;

    void siftUp(int i) {
        while (i > 0 && heap[i] < heap[(i - 1) / 2]) {
            swap(heap[i], heap[(i - 1) / 2]);
            i = (i - 1) / 2;
        }
    }

    void siftDown(int i) {
        int n = heap.size();
        while (2 * i + 1 < n) {
            int left = 2 * i + 1;
            int right = 2 * i + 2;
            int smallest = left;

            if (right < n && heap[right] < heap[left]) {
                smallest = right;
            }

            if (heap[i] > heap[smallest]) {
                swap(heap[i], heap[smallest]);
                i = smallest;
            } else {
                break;
            }
        }
    }

public:
    void clear() {
        heap.clear();
    }

    void add(int value) {
        heap.push_back(value);
        siftUp(heap.size() - 1);
    }

    bool isEmpty() const {
        return heap.empty();
    }

    int extract() {
        int min_val = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        if (!heap.empty()) {
            siftDown(0);
        }
        return min_val;
    }
};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    MinHeap heap;
    string command;

    while (cin >> command) {
        if (command == "CLEAR") {
            heap.clear();
        } else if (command == "ADD") {
            int n;
            cin >> n;
            heap.add(n);
        } else if (command == "EXTRACT") {
            if (heap.isEmpty()) {
                cout << "CANNOT" << "\n";
            } else {
                cout << heap.extract() << "\n";
            }
        }
    }

    return 0;
}
