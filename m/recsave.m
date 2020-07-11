function recsave
    clear all;
    k=1;
    rdata=cell(1,1);
    audio=cell(1,1);
            Path = 'wavlib\';                   % 设置数据存放的文件夹路径
            File = dir(fullfile(Path,'*.wav'));  % 显示文件夹下所有符合后缀名为.txt文件的完整信息
            FileNames = {File.name}';            % 提取符合后缀名为.txt的所有文件的文件名，转换为n行1列
    for i=1:1
        for j=1:1
            filename=['wavlib\',FileNames{k,1}];
            k=k+1;
            x=readwav('temp.wav');
            audio{1,j}=x;
            rdata{1,i}=audio;
        end
    end
%     fprintf('Finish!\n');

    clear k;
    save rec_data.mat rdata;