/*
 *局部变量不释放，还可以读写
 * */
#include <stdio.h>

void rev(char **P){
	char fp[4];
	int i;
	for(i=0;i<3;i++) fp[i] = 'x';
	fp[3] = 0;
	printf("rev fp at :%p\t%s\n", fp, fp);
	*P = fp;
    return ;
}

int main(){
    int i;
	char *p = "haodemaodddddddd"; //注释改行结果不同
	char **P;
    int is;
	rev(P);
	printf("%p\t%s\n", *P, *P);
	**P = 'a';
	printf("%p\t%s\n", *P, *P);
	return 0;
}

int main_(){
    //t();
    return 0;
}
