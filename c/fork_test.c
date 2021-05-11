/*================================================================
*   Copyright (C) 2021 LuoYe. All rights reserved.
*   
*   文件名称：fork_test.c
*   创 建 者：JangYee
*   创建日期：2021年05月11日
*   描    述：使用fork创建多进程
*
================================================================*/

#include <stdio.h>
#include <sys/types.h>
#include <unistd.h>

void mainFunc(int son_pid) {
    printf("I am main, my son pid is %d!\n", son_pid);
}

void sonFunc() {
    printf("I am son, my pid is %d!\n", getpid());
}


int main() {
    //On success, the PID of the child process is returned in the parent, and 0 is returned in the child.
    //On failure, -1 is returned in the parent, no child process is created,
    //and errno is set appropriately
    int pid = fork();
    if(pid == 0) {
        sonFunc();
    }
    else {
        mainFunc(pid);
    }
    return 0;

}

