% Octave: run as octave -qf main.m
% Matlab: delete last line ("main") and run

function scaleOfKrylovSpace

  % nn = 100;
  % npd_AA = sprand(nn,nn,7.0/nn); % npd_AA is not positive definite
  % AA = npd_AA'*npd_AA; % AA is positive definite
  % bb = rand(nn,1);

  % fd = fopen('AA.txt','r')
  % fscanf(fd,'%f')
  % fclose(fd)


  fprintf('Loading AA matrix\n');
  load AA.dat
  fprintf('Converting AA matrix\n');
  AA = spconvert(AA);
  fprintf('AA Matrix ready\n');

  fd = fopen('bb.dat','r')
  bb = fscanf(fd,'%f');
  fclose(fd);

  xx = zeros(size(bb,1),1);
  MM = speye(size(bb,1));
  rr = 20;
  mit = 10000;
  toller = 1.0e-4;

  display(size(AA))
  display(size(xx))
  display(size(bb))

  fprintf('Building Krylov space\n');

  MM = inv(diag(diag(AA)));

  %display (MM)

  x = krylovSpaceNorms( AA, xx, bb, MM, 12);

end

function [x] = krylovSpaceNorms ( A, x, b, M, n )

      t = M*x;

%      display(t)

    k{1} = b - A*t;


    fprintf ( '%d, %e\n',1,norm(k{1}));
    for i = 2:n,
        t = M*k{i-1};

        k{i} = A*t;
        fprintf( '%d, %e\n',i,norm(k{i}));
    end

    display('Building dot product matrix\n');

    for i = 1:n,
        for j = 1:n,
            N(i,j) = dot(k{i},k{j});
        end
    end

    display (N)

    display ('Det(N):')
    display (det(N))

    invN = inv(N)


end

scaleOfKrylovSpace
