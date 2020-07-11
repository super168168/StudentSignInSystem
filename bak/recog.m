% -- ʶ�� ---
function recname = recog
    clear all;
    load rec_data.mat;  % �����ʶ������
    load speaker.mat;   % ����ѵ���õ�ģ��
    Spk_num=size(speaker,2); %˵���˸���
    Tes_num=1;  %ÿ��˵���˴�ʶ���������Ŀ
    fs=8000; %����Ƶ��
    ncentres=16; %��ϳɷ���Ŀ
    names = {'ganjiahao','liaojunjie','zhangwentao','laijintao','zhuzhenye'};

    % for spk_cyc=1:Spk_num    % ����˵����
    spk_cyc=1;
      for sph_cyc=1:Tes_num  % �������� 
         speech = rdata{spk_cyc}{sph_cyc};

         %---Ԥ����,������ȡ--
         pre_sph=filter([1 -0.97],1,speech);
         win_type='M'; %������
         cof_num=20; %����ϵ������
         frm_len=fs*0.02; %֡����20ms
         fil_num=20; %�˲��������
         frm_off=fs*0.01; %֡�ƣ�10ms
         c=melcepst(pre_sph,fs,win_type,cof_num,fil_num,frm_len,frm_off); %(֡��)*(cof_num)
         cof=c(:,1:end-1); %N*Dάʸ��

         %----ʶ��---
         MLval=zeros(size(cof,1),Spk_num);
         for b=1:Spk_num %˵����ѭ��
             pai=speaker{b}.pai;
             for k=1:ncentres 
               mu=speaker{b}.mu(k,:);
               sigma=speaker{b}.sigma(:,:,k);
               pdf=mvnpdf(cof,mu,sigma);
               MLval(:,b)=MLval(:,b)+pdf*pai(k); %������Ȼֵ
             end
        end
        logMLval=log((MLval)+eps);
        sumlog=sum(logMLval,1);
        [maxsl,idx]=max(sumlog); % �о����������Ȼֵ��Ӧ�����idx��Ϊʶ����
        fprintf('%s\n',names{1,idx});     

      end
  recname = names{1,idx};
% end