function recsave
    clear all;
    k=1;
    rdata=cell(1,1);
    audio=cell(1,1);
            Path = 'wavlib\';                   % �������ݴ�ŵ��ļ���·��
            File = dir(fullfile(Path,'*.wav'));  % ��ʾ�ļ��������з��Ϻ�׺��Ϊ.txt�ļ���������Ϣ
            FileNames = {File.name}';            % ��ȡ���Ϻ�׺��Ϊ.txt�������ļ����ļ�����ת��Ϊn��1��
    for i=1:1
        for j=1:1
            filename=['wavlib\',FileNames{k,1}];
            k=k+1;
            x=readwav('testwav4.wav');
            audio{1,j}=x;
            rdata{1,i}=audio;
        end
    end
    fprintf('Finish!\n');

    clear k;
    save rec_data.mat rdata;