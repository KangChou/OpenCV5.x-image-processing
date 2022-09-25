# 参考教程:https://blog.conan.io/2018/12/19/New-OpenCV-release-4-0.html

cd sobel
rm -rf build
mkdir build
cd build
cmake ..
make
./demo

cd ../../

cd sobel-gapi
rm -rf build
mkdir build
cd build
cmake ..
make
./demo