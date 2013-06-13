clc;
clear all;

% le arquivo
fid = fopen('matrix.txt', 'r');
A = fscanf(fid, '%f');
fclose(fid);

% cria a matriz
X = zeros(A(1), A(2));

A = A(3:size(A));
for i = 1 : size(X,1)
    for j = 1 : size(X,2)
        X(i, j) = A((i-1) * size(X, 2) + j);
    end
end

[U, S, V] = svds(X, 2);

fid = fopen('u.txt','wt');
for i = 1 : size(U, 1)
    fprintf(fid,'%20.18f ', U(i, :));
    fprintf(fid,'\n');
end
fclose(fid);

fid = fopen('s.txt','wt');
for i = 1 : size(S, 1)
    fprintf(fid,'%20.18f ', S(i, :));
    fprintf(fid,'\n');
end
fclose(fid);

fid = fopen('v.txt','wt');
for i = 1 : size(V, 1)
    fprintf(fid,'%20.18f ', V(i, :));
    fprintf(fid,'\n');
end
fclose(fid);