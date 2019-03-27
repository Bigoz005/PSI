function [w1,w2,f] = perceptron1()
e1=[5,5,5,5,5,5,5,5,5,5];
p=[-8 20;2 20;4 25;-6 -5;-9 -10;-6 -25;-2 -10;1 -10;4 -16; 5,9];
p=p';
t=[0,0,0,0,0,1,1,1,1,1];
w1=rand;
w2=rand;
b=rand;
i=1;
while(1~=0)
    a=(w1*p(1,i)+w2*p(2,i)+b);
    if a>0
        p(2,i)=1;
    else
        p(2,i)=0;
    end
    e1(i)=t(i)-p(2,i);
    if e1==0
        break;
    end
    w1=w1+e1(i)*p(1,i)+e1(i)*p(2,i);
    w2=w2+e1(i)*p(1,i)+e1(i)*p(2,i);
    b=b+e1;
    
    i=i+1;
end  

end


