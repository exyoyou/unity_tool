#!/bin/bash
#
#site: www.jquerycn.cn
function ergodic(){
  for file in `ls $1`
  do
    # echo $1"/"$file
    local path=$1"/"$file 
    chmod 777 $path
    if [ -d $1"/"$file ]
    then
      ergodic $1"/"$file
      # chmod 777 $1
      # chmod 777 $file
      # echo $1"/"$file
    # else
    #   local path=$1"/"$file 
    #   # local name=$file      
    #   # local size=`du --max-depth=1 $path|awk '{print $1}'` 
    #   # echo $name  $size $path 
    #   chmod 777 $path
    fi
  done
}
IFS=$'\n' #这个必须要，否则会在文件名中有空格时出错
INIT_PATH=".";
ergodic $INIT_PATH
echo "获取所有权限完毕！！！"
