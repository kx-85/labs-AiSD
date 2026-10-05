#include <stdio.h>
#include <stdlib.h>
void insertionsort(int *arr, int n) {
	for (int d = 1; d<n; d++){
		int key = arr[d];
		int j = d;
    	while ((j>=1)&&(arr[j-1]>key)){
    		arr[j] = arr[j-1];
    		j -=1;  }
        arr[j] = key;
	}
}

int main(void) {
int *arr = NULL;
	int n=0, cap = 0,x;
	
	 while (scanf("%d", &x) == 1) {          
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
    insertionsort(arr, n);

    for (int i = 0; i < n; i++)
        printf("%d%c", arr[i], i + 1 < n ? ' ' : '\n');

    free(arr);
    return 0;
}
