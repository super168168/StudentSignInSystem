speak=cell(1,5);
audio=cell(1,10);
Path = 'wavlib\';                   % 设置数据存放的文件夹路径
File = dir(fullfile(Path,'*.wav'));  % 显示文件夹下所有符合后缀名为.txt文件的完整信息
FileNames = {File.name}'            % 提取符合后缀名为.txt的所有文件的文件名，转换为n行1列
FileNames{1,1}
filename=['wavlib\',FileNames{2,1}]
x=readwav(filename)
audio{1,1}=x
speak{1,1}=audio