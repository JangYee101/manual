/*================================================================
*   Copyright (C) 2021 LuoYe. All rights reserved.
*   
*   文件名称：thread_demo.c
*   创 建 者：JangYee
*   创建日期：2021年05月11日
*   描    述：linux pthread多线程demo
*
================================================================*/

#include <stdio.h>
#include <pthread.h>
#include <time.h>
#include <stdlib.h>
#include <unistd.h>

//定义新的结构体变量
typedef struct _Actor {
    char name[20];
    char sex[10];
    int age;
    unsigned char show_time;
} Actor;

//线程函数
void threadFunc(Actor *actor) {
    printf("My name is %s, I will show %d second!\n", actor->name, actor->show_time);
    sleep(actor->show_time);
    printf("%s show end!\n", actor->name);
}

//串行执行，线程1执行完后再执行线程2
void singleShow(Actor actors[], int num) {
    printf("start single show!\n");
    int i, status;
    pthread_t *t = malloc(sizeof(pthread_t)*num);
    for(i=0;i<num;i++) {
        //On success, pthread_create() returns 0; on error, it returns an error number, and the contents of *thread are undefined
        status = pthread_create(t+i, NULL, (void *)threadFunc, (void *) (actors+i));
        if(status != 0) {
            printf("create thread error(%d), exit!\n", status);
            exit(status);
        }
        //On success, pthread_join() returns 0; on error, it returns an error number
        pthread_join(t[i], NULL);
    }
    free(t);
    printf("end single show!\n");
}

//并行执行，线程1和2同时执行
void commonShow(Actor actors[], int num) {
    printf("start common show!\n");
     int i, status;
    pthread_t *t = malloc(sizeof(pthread_t)*num);
    for(i=0;i<num;i++) {
        //On success, pthread_create() returns 0; on error, it returns an error number, and the contents of *thread are undefined
        status = pthread_create(t+i, NULL, (void *)threadFunc, (void *) (actors+i));
        if(status != 0) {
            printf("create thread error(%d), exit!\n", status);
            exit(status);
        }
    }
    for(i=0;i<num;i++)
        pthread_join(t[i], NULL);
    free(t);
    printf("end common show!\n");
}

int main() {
    //结构体复制方式
    Actor actors[2];
    Actor actors1 = {.name="jiangye", .sex="man", .age=24, .show_time=2};
    Actor actors2 = {.name="ping", .sex="woman", .age=24, .show_time=3};
    actors[0] = actors1;
    actors[1] = actors2;
    singleShow(actors, 2);
    commonShow(actors, 2);
    return 0;
}
