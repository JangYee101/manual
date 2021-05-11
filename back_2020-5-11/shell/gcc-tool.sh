#!/bin/bash
old_ifs=$IFS
IFS=".";
arr=($1);
app=app-${arr[0]};
IFS=$old_ifs
echo $1
echo ${app};
gcc $1 -o ${app};
