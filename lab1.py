# Skrypt generujacy odleglosci dla podanej liczby miast
import random
import array as arr
l_miast = 1;
a=random.random()
print(a)
M= arr.array("d",[])
M = [[0 for x in range(l_miast)] for y in range(3)]
#M = [[]*2 for i in range(l_miast)]
for i in range(l_miast):
    # r = rand(5) Generate  a 5x5 matrix of uniformly distributed random numbers between 0 and 1. rand(1) generate a 1x1 matrix so just use random(1)
    M[i, 1] = i;
    M[i, 2] = 10 * random.random();
    M[i, 3] = 10 * random.random();
    print(M[i, 1])
    print(M[i, 2])
    print(M[i, 3])



figure;
plot(M(:, 2), M(:, 3), 'o');

w = perms([1:l_miast]);
[lw, lk] = size(w);

subplot(2, 1, 1);
plot(M(w, 2), M(w, 3), 'o-');
axis([0 12 0 12]);

for i=1:l_miast
text(M(i, 2), M(i, 3) + 1, num2str(i));
end;
%
%
koszt = 0;
koszt_c = zeros(lw, 1);

for i=1:lw
for j=1:lk - 1
koszt = koszt + sqrt((M(w(i, j), 2) - M(w(i, j + 1), 2)). ^ 2 + (M(w(i, j), 3) - M(w(i, j + 1), 3)). ^ 2);
end;
koszt_c(i) = koszt + sqrt((M(w(i, end), 2) - M(w(i, 1), 2)). ^ 2 + (M(w(i, end), 3) - M(w(i, 1), 3)). ^ 2);
if i == 1
    koszt_min = koszt_c(i);
else
    if koszt < koszt_min
        koszt_min = koszt;
        pozycja = i;
    end;
end;

koszt = 0;
end;

subplot(2, 1, 2);

plot(M(w(pozycja,:), 2), M(w(pozycja,:), 3), 'ro-');




hold
on;
line([M(w(pozycja, 1), 2), M(w(pozycja, end), 2)], [M(w(pozycja, 1), 3), M(w(pozycja, end), 3)], 'Color', 'r');
axis([0 12 0 12]);

for i=1:l_miast
text(M(i, 2), M(i, 3) + 1, num2str(i));
end;

koszt_Min = min(koszt_c)
koszt_Max = max(koszt_c)
rand(1)

clear

% figure;
% bar(koszt_c);
