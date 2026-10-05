#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>
void bubblesort(int *arr, int n, int *k) {
    for (int d = 0; d < n - 1; d++) {
        bool flag = false;
        for (int i = 0; i < n - d - 1; i++) {
            if (arr[i] > arr[i + 1]) {
            	*k+=1;
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
	int *arr;
	int k = 0, n;
	scanf("%d", &n);
	if (n<1||n>1000){
	return 1;}	
	arr = (int *)malloc(n * sizeof(int *));
    if (arr == NULL) {
        return 1;}
	for (int i = 0; i<n; i++){
		scanf("%d", &arr[i]);
		if (arr[i]>pow(10,9)||arr[i]<-pow(10,9)){
		return 1;}
	}
	
    bubblesort(arr, n, &k);

//    for (int i = 0; i < n; i++){
//        printf("%d%c", arr[i], i + 1 < n ? ' ' : '\n');}
        
	printf("%d",k);
    free(arr);
    return 0;
}
