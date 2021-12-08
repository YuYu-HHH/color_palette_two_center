# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.




# Press the green button in the gutter to run the script.
import os

from Get_Palette_by_Two_center.Get_Palette_by_Two_center import Get_Palette_by_Two_center

if __name__ == '__main__':
    filename_Path = "E:\gwu-chahua.jpg";
    filename = "gwu-chahua"
    # filename_Path = "E:\BingWallpaper.jpg";
    # filename = "BingWallpaper";
    save_Path1 = "E:\Save_Path"



    save_Path = os.path.join(save_Path1,filename)

    if not os.path.exists(save_Path1):
        print("文件夹不存在,正在新建中");
        os.mkdir(save_Path1);
    if not os.path.exists(save_Path):
        print("文件夹不存在,正在新建中");
        os.mkdir(save_Path);

    Get_Palette_by_Two_center(filename_Path, save_Path);

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
