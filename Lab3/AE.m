clear
clc

n=10;
%n=100;
pk=0.8;
pm=0.2;
%pm = 0.1;

for i=1:n
	chd(i) = randi(127);
end

disp('wylosowano liczby [d]: ');
chd

disp('wylosowano liczby [b]: ');
disp('wcisnij dowolny klawisz');
chb = dec2bin(chd,7)
    pause;
for z = 1:5000
    
end
fp=2.*(chd.^3+1);   
sfp = sum(fp);
    
fp = 100.*fp/sfp;

chdn=[];

for i=1:n
    licznik=rand(1).*100;
    s=fp(1);
    j=1;
    
    while licznik>a
        j=j+1;
        s=s+fp(j);
    end;
    chdn(i)=chd(j);
end

pary=randperm(n);
for i=1:2:round(n./2)
    if(rand(1)<pk)
        m_k=randi(6);
        t1=chn(pary(i),l:m_k);
        t2=chbn(pary(i),m_k+1:end);
        t3=chbn(pary(i+j),1:m_k);
        t4=chbn(pary(i+j),m_k+1:end);
        
if(rand(1)
end

