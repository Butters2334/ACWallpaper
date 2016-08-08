
mkdir -p ~/Pictures/copyLrvue

cp ~/Library/Containers/com.leonspok.osx.Irvue/Data/Library/Application\ Support/Irvue/unsplash_* ~/Pictures/copyLrvue

echo "copy - "

sleep 600

echo "递归"

sh ~/Nut/python/demo/ACWallpaper/CopyLrvueImage.sh
