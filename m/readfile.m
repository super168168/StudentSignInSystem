function readfile
    clear all;
    k=1;
    Spk_num=4;
    tdata=cell(1,num);
    audio=cell(1,10);
            Path = 'wavlib\';                   % �������ݴ�ŵ��ļ���·��
            File = dir(fullfile(Path,'*.wav'));  % ��ʾ�ļ��������з��Ϻ�׺��Ϊ.txt�ļ���������Ϣ
            FileNames = {File.name}';            % ��ȡ���Ϻ�׺��Ϊ.txt�������ļ����ļ�����ת��Ϊn��1��
    for i=1:num
        for j=1:10
            filename=['wavlib\',FileNames{k,1}];
            k=k+1;
            x=readwav(filename);
            audio{1,j}=x;
            tdata{1,i}=audio;
        end
    end
    fprintf('Finish!\n');

    clear k;
    save tra_data.mat tdata;