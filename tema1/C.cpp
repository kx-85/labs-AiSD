#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
void bubblesort(int *arr, int n) {
    for (int d = 0; d < n - 1; d++) {
        bool flag = false;
        for (int i = 0; i < n - d - 1; i++) {
            if (arr[i] < arr[i + 1]) {
                int t = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = t;
                flag = true;
            }
        }
        if (!flag) break;
    }
}

int main(void) {
	int *arr = NULL;
	int n=0, cap = 0,x;
	
	 while (scanf("%d", &x) == 1) {          // читаем числа до конца ввода
        if (n == cap) {
            cap = cap ? cap * 2 : 8;
            int *a = (int*)realloc(arr, cap * sizeof(int));
			if (!a) {
			    free(arr);          
				return 1;   }
			arr = a;
        }
        arr[n++] = x;
    }
    bubblesort(arr, n);

    for (int i = 0; i < n; i++)
        printf("%d%c", arr[i], i + 1 < n ? ' ' : '\n');

    free(arr);
    return 0;
}
