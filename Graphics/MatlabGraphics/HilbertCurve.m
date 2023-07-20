% 4 empty matrices with 0 rows and 2 columns
A = zeros(0,2);
B = zeros(0,2);
C = zeros(0,2);
D = zeros(0,2);

% up and down is positive and negative along y-axis
% left and right are positive and negative along y axis
up = [ 0  1];
right  = [ 1  0];
down = [ 0 -1];
left  = [-1  0];

% set order
order = 1;

% loop draws the curve by dividing the square into smaller squares and
% building the curve in each sub-square
for n = 1:order

  %semi colons concat the matricies
  % each element is a segment of the Hilbert Curve


  AA = [B ; up ; A ; right ; A ; down ; C];
  BB = [A ; right ; B ; up ; B ; left ; D];
  CC = [D ; left ; C ; down ; C ; right ; A];
  DD = [C ; down ; D ; left ; D ; up ; B];
  
  % updating the curve segments for the next iteration
  A = AA;
  B = BB;
  C = CC;
  D = DD;
end
  % temporary matrices: formed by concatenating 

A = [0 0; cumsum(A)];

plot(A(:,1), A(:,2), 'clipping', 'off', 'color', 'red', LineWidth=2)
axis equal, axis off