#include <stdio.h>
#include <stdlib.h>
void selectionsort(int *arr, int n) {
	for (int d = 0; d<n-1; d++){
		int key = arr[d];
		int ind = d;
		for(int j =d+1; j<n; j++){
			if (arr[j]>key){
			key = arr[j];
            ind = j;	  }  }
		if (d != ind){
		int t = arr[d];
		arr[d] = arr[ind];
		arr[ind] = t; }
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
    selectionsort(arr, n);

    for (int i = 0; i < n; i++)
        printf("%d%c", arr[i], i + 1 < n ? ' ' : '\n');

    free(arr);
    return 0;
}
