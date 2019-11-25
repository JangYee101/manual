/*
 *符号位是有作用的，char ==> int，符号位会复制，并且缺位补成符号位。但是int ==> char 符号位却不会复制。
 * */
#include <stdio.h>
#include <string.h>


void writeBite(char *file_name, char *buf){
    FILE *fd = fopen(file_name, "w");
    fwrite(buf, 1, strlen(buf), fd);
    fclose(fd);
}

void readBite(char *file_name, char *buf){
    FILE *fd = fopen(file_name, "r");
    fread(buf, 1, 100, fd);
    fclose(fd);
}

void fgetBite(char *file_name, char *buf){
    FILE *fd = fopen(file_name, "r");
    int i=0;
    char ch;
    while((ch = fgetc(fd)) != EOF){
        buf[i] = ch;
        printf("%d\t%x\n",i, buf[i]);
        i++;
    }
    printf("%d\t%x\n",i, ch);
    fclose(fd);

}

void fgetBiteInt(char *file_name, char *buf){
    FILE *fd = fopen(file_name, "r");
    int i=0;
    int ch;
    while((ch = fgetc(fd)) != EOF){
        printf("ch is %d\t%x\n", ch, ch);
        buf[i] = ch;
        printf("%d\t%x\n",i, buf[i]);
        i++;
    }
    printf("ch is %d\t%x\n",ch, ch);
    if(buf[2] == ch){
        printf("yes\n");
    }
    fclose(fd);

}

int main(){
    char buf[100];
    memset(buf, 0, 100);
    buf[0] = 0x41;
    buf[1] = 0x42;
    buf[2] = 0xff;
    buf[3] = 0x41;
    buf[4] = 0x42;
    printf("%s\n", buf);
    printf("--------------\n");
    char *file_name = "txt";
    writeBite(file_name, buf);
    memset(buf, 0, 100);
    readBite(file_name, buf);
    printf("%s\n", buf);
    printf("--------------\n");
    memset(buf, 0, 100);
    fgetBite(file_name, buf);
    printf("%s\n", buf);
    printf("--------------\n");
    memset(buf, 0, 100);
    fgetBiteInt(file_name, buf);
    printf("%s\n", buf);
    printf("\n\n--------------\n");
    char cc=0xff;
    int aaa = -1;
    if(cc == aaa){
        printf("%d\t%d\n", sizeof(cc), sizeof(aaa));
        printf("ooooooo\n");
    }
    printf("\n\n--------------\n");
    char cccc[3];
    memset(cccc, 0, 3);
    printf("%p\t%x\n%p\t%x\n", cccc,*cccc, cccc+2, *(cccc+2));
    char *ccc = cccc+1;
    int ddd;
    printf("ccc at %p\n", ccc);
    *ccc = 128;
    printf("%p\t%x\n%p\t%x\n", cccc,*cccc, cccc+2, *(cccc+2));
    printf("ccc at %p\n", ccc);
    aaa = *ccc;
    printf("%d\t%d\t%x\n", sizeof(*ccc), *ccc, *ccc);
    printf("%d\t%d\t%x\n", sizeof(aaa), aaa, aaa);
    ddd = (int)((*ccc)&0xff);
    printf("ddd is %d\t%d\t%x\n", sizeof(ddd), ddd, ddd);
    *ccc = 127;
    printf("%p\t%x\n%p\t%x\n", cccc,*cccc, cccc+2, *(cccc+2));
    aaa = *ccc;
    printf("%d\t%d\t%x\n", sizeof(*ccc), *ccc, *ccc);
    printf("%d\t%d\t%x\n", sizeof(aaa), aaa, aaa);
    aaa = 0xffffffff;
    printf("%d\t%d\t%x\n", sizeof(aaa), aaa, aaa);
    if(0xff == 0x000000ff)
        printf("yes\n");
    printf("%d\t%d\n",sizeof(0xff), sizeof(0xfffffffff));
    unsigned char ii = 255;
    char oo = 255;
    int ll = ii;
    printf("%d\n", ll);
    ll = oo;
    printf("%d\n", ll);
    
    ii = 0xabcd;
    printf("%x\n", ii);
    ll = 0xfffff081;
    printf("ll is %x\n", ll);
    cc = ll;
    printf("ii is %x\n", cc);


    return 0;
}
