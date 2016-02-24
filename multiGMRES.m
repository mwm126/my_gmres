
function main
  
  printf("Loading AA matrix\n");
 
  load AA.dat
%   fd = fopen('AA.dat','r');
%   [i,j,val] = fscanf(fd,'%d %d %f');
%   fclose(fd);
  

  printf("Converting AA matrix\n");
  AA = spconvert(AA);
  %AA = sparse(i,j,val)
  printf("AA Matrix ready\n");
  
  %display (AA)
  
  fd = fopen('bb.dat','r')
  bb = fscanf(fd,'%f');
  fclose(fd);


  xx = zeros(size(bb,1),1);
  MM = speye(size(bb,1));


  display(size(AA))
  display(size(xx))
  display(size(bb))

  printf("Building Krylov space\n");
  
  MM = inv(diag(diag(AA)));
  
  %display (MM)
  
  krylovSpaceNorms( AA, xx, bb, MM, 10);
  
  %display (xx)
  
  %display (A*xx - b)
  
  %display norm(A*xx - b)

end

function [x] = krylovSpaceNorms ( A, x, b, M, n )

  bNorm = norm(b);
  printf("Initial Residual: %e\n",norm(A*x - b)/bNorm)
  
  
  for it = 1:100
    
    res = b - A*x;
    
    k{1} = res;
    
    %printf ( '%d, %e\n',1,norm(k{1}));
    for i = 2:n+1,
        t = M*k{i-1};
        k{i} = A*t;
        %printf( '%d, %e\n',i,norm(k{i}));
    end
    
    %display("Building dot product matrix\n");
    
    for i = 2:n+1,
        r(i-1) = dot(k{i},res);
        for j = 2:n+1,
            N(i-1,j-1) = dot(k{i},k{j});
        end
    end
    
    %display(det(N))
    %display(N)
    %display(r')
    
    alpha = N \ r';
    
    %display (alpha)
    
    err = N*alpha - r';
    %display (norm(err))

%    dalpha = N \ (err);
%    alpha -= dalpha;
%    err = N*alpha - r';
%    display (norm(err))
    
%    dalpha = N \ (err);
%    alpha -= dalpha;
%    err = N*alpha - r';
%    display (norm(err))   


    y = zeros(size(x));
    for i = 1:n
      y += alpha(i)*k{i};
    end
    x += M*y;
    
    display (norm(A*x-b)/bNorm)
    %display(x)
    
  end

end

main
