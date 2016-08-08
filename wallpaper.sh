#提取壁纸图片URL
url=$(expr "$(curl https://unsplash.com/new |grep hprichbg)" : ".*g_img={url: \"\(.*\)\",id.*")
echo url=${url}
#提取图片名称
filename=$(expr "$url" : ".*/\(.*\)")
echo filename=${filename}
#本地图片地址-当前用户下缺省图片目录
localpath="/Users/$USER/Pictures/$filename"
echo localpath=${localpath}
#下载图片至本地
curl -o $localpath  $url
#调用Finder应用切换桌面壁纸
osascript -e "tell application \"Finder\" to set desktop picture to POSIX file \"$localpath\""






# http://unsplash.com/photos/aYP1uRDI_vI/download
