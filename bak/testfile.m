speak=cell(1,5);
audio=cell(1,10);
Path = 'wavlib\';                   % �������ݴ�ŵ��ļ���·��
File = dir(fullfile(Path,'*.wav'));  % ��ʾ�ļ��������з��Ϻ�׺��Ϊ.txt�ļ���������Ϣ
FileNames = {File.name}'            % ��ȡ���Ϻ�׺��Ϊ.txt�������ļ����ļ�����ת��Ϊn��1��
FileNames{1,1}
filename=['wavlib\',FileNames{2,1}]
x=readwav(filename)
audio{1,1}=x
speak{1,1}=audio